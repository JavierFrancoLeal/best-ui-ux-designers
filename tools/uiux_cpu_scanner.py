#!/usr/bin/env python3
"""Deterministic CPU pre-scanner for best-ui-ux-designers (ECOSYSTEM_CONTRACT v1.1.0).

Runs fast, zero-variance static checks over HTML/CSS/JS/JSX/TSX/Vue/Svelte artifacts
before invoking semantic LLM review. Outputs machine-readable JSON, SARIF 2.1.0,
or compact Markdown evidence blocks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

SCANNER_VERSION = "1.1.0"
SUITE_ID = "ui-ux"
MODULE_ID = "cpu-scanner"

JS_BUILTINS = {
    # Keywords & control flow
    "if", "else", "for", "while", "do", "switch", "case", "return", "throw",
    "catch", "try", "finally", "new", "delete", "typeof", "void", "await",
    "async", "function", "class", "super", "this", "import", "export", "from",
    "of", "in", "instanceof", "yield", "break", "continue", "debugger",
    # JS & Web API globals
    "Array", "Object", "String", "Number", "Boolean", "Symbol", "BigInt",
    "Math", "Date", "RegExp", "Error", "TypeError", "RangeError", "SyntaxError",
    "Promise", "Map", "Set", "WeakMap", "WeakSet", "JSON", "Intl", "Proxy",
    "Reflect", "ArrayBuffer", "DataView", "Uint8Array", "Int16Array",
    "Float32Array", "URL", "URLSearchParams", "FormData", "Blob", "File",
    "Headers", "Request", "Response", "AbortController", "ReadableStream",
    "TextEncoder", "TextDecoder", "WebSocket", "EventSource", "CustomEvent",
    "Event", "MutationObserver", "IntersectionObserver", "ResizeObserver",
    "SpeechSynthesisUtterance", "AudioContext", "webkitAudioContext",
    "SpeechRecognition", "webkitSpeechRecognition", "Image", "Audio", "Option",
    "Worker", "SharedWorker", "Notification", "BroadcastChannel", "DOMParser",
    # Global functions
    "parseInt", "parseFloat", "isNaN", "isFinite", "encodeURI", "decodeURI",
    "encodeURIComponent", "decodeURIComponent", "btoa", "atob", "fetch",
    "setTimeout", "clearTimeout", "setInterval", "clearInterval",
    "requestAnimationFrame", "cancelAnimationFrame", "queueMicrotask",
    "structuredClone", "alert", "confirm", "prompt", "eval", "require",
    "define", "getComputedStyle", "matchMedia", "scrollTo", "scrollBy",
    # Common DOM/helper globals
    "window", "document", "navigator", "location", "history", "console",
    "localStorage", "sessionStorage", "indexedDB", "performance", "crypto",
    "speechSynthesis", "screen", "self", "globalThis", "process", "module",
    "exports", "React", "ReactDOM", "h", "Fragment", "clsx", "cn",
}


class _HtmlScanner(HTMLParser):
    """Lightweight HTML structure parser tracking line numbers and visibility."""

    def __init__(self, lines: list[str]) -> None:
        super().__init__(convert_charrefs=True)
        self.lines = lines
        self.hidden_stack: list[bool] = []
        self.elements_by_id: dict[str, tuple[str, int, dict[str, str]]] = {}
        self.visible_form_controls: list[tuple[str, int, str]] = []
        self.selects: list[dict[str, Any]] = []
        self._cur_select: dict[str, Any] | None = None
        self.buttons: list[dict[str, Any]] = []
        self._cur_btn: dict[str, Any] | None = None
        self.div_clicks: list[tuple[str, int, dict[str, str]]] = []
        self.input_minlengths: list[tuple[int, int, str]] = []
        self.inline_styles: list[tuple[int, str]] = []
        self.inline_scripts: list[tuple[int, str]] = []
        self.external_scripts: list[str] = []
        self._in_style_line: int | None = None
        self._style_chunks: list[str] = []
        self._in_script_line: int | None = None
        self._script_chunks: list[str] = []

    @staticmethod
    def _is_hidden_attrs(attrs: dict[str, str]) -> bool:
        style = (attrs.get("style") or "").replace(" ", "").lower()
        cls = set((attrs.get("class") or "").split())
        if "display:none" in style or "hidden" in attrs:
            return True
        if cls & {"hidden", "wcons-hide", "sr-only"}:
            return True
        return False

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        line, _ = self.getpos()
        attrs = {k.lower(): (v if v is not None else "") for k, v in attrs_list}
        is_hidden = (self.hidden_stack[-1] if self.hidden_stack else False) or self._is_hidden_attrs(attrs)
        void_tags = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
        if tag not in void_tags:
            self.hidden_stack.append(is_hidden)

        if "id" in attrs and attrs["id"]:
            self.elements_by_id[attrs["id"]] = (tag, line, attrs)

        if tag in ("input", "select", "textarea"):
            itype = attrs.get("type", "").lower()
            if itype != "hidden" and not is_hidden:
                self.visible_form_controls.append((tag, line, attrs.get("id", attrs.get("name", tag))))
            if tag == "input" and attrs.get("minlength", "").isdigit():
                self.input_minlengths.append((line, int(attrs["minlength"]), attrs.get("id", "")))

        if tag == "select":
            self._cur_select = {
                "id": attrs.get("id", ""),
                "line": line,
                "options": 0,
                "has_optgroup": False,
            }
        elif tag == "optgroup" and self._cur_select is not None:
            self._cur_select["has_optgroup"] = True
        elif tag == "option" and self._cur_select is not None:
            self._cur_select["options"] += 1

        if tag == "button":
            self._cur_btn = {
                "id": attrs.get("id", ""),
                "line": line,
                "attrs": attrs,
                "text": "",
                "has_svg": False,
            }
        elif tag == "svg" and self._cur_btn is not None:
            self._cur_btn["has_svg"] = True

        if tag in ("div", "span") and "onclick" in attrs:
            if attrs.get("role") != "button" or "tabindex" not in attrs:
                self.div_clicks.append((tag, line, attrs))

        if tag == "style":
            self._in_style_line = line
            self._style_chunks = []
        elif tag == "script":
            if attrs.get("src"):
                self.external_scripts.append(attrs["src"])
            else:
                self._in_script_line = line
                self._script_chunks = []

    def handle_endtag(self, tag: str) -> None:
        if self.hidden_stack:
            self.hidden_stack.pop()
        if tag == "select" and self._cur_select is not None:
            self.selects.append(self._cur_select)
            self._cur_select = None
        elif tag == "button" and self._cur_btn is not None:
            self.buttons.append(self._cur_btn)
            self._cur_btn = None
        elif tag == "style" and self._in_style_line is not None:
            self.inline_styles.append((self._in_style_line, "".join(self._style_chunks)))
            self._in_style_line = None
        elif tag == "script" and self._in_script_line is not None:
            self.inline_scripts.append((self._in_script_line, "".join(self._script_chunks)))
            self._in_script_line = None

    def handle_data(self, data: str) -> None:
        if self._cur_btn is not None:
            self._cur_btn["text"] += data
        if self._in_style_line is not None:
            self._style_chunks.append(data)
        if self._in_script_line is not None:
            self._script_chunks.append(data)


def _strip_js_comments_and_strings(js: str) -> str:
    """Replace string literals, regex literals, and comments with spaces while preserving newlines."""
    out: list[str] = []
    i = 0
    n = len(js)
    prev_non_ws = ""
    regex_prev_tokens = set("(=,:!&|?;{[+-*~%^<>")
    while i < n:
        ch = js[i]
        nxt = js[i + 1] if i + 1 < n else ""
        if ch == "/" and nxt == "/":
            while i < n and js[i] != "\n":
                out.append(" ")
                i += 1
        elif ch == "/" and nxt == "*":
            out.append("  ")
            i += 2
            while i < n:
                if js[i] == "*" and i + 1 < n and js[i + 1] == "/":
                    out.append("  ")
                    i += 2
                    break
                out.append("\n" if js[i] == "\n" else " ")
                i += 1
        elif ch == "/" and (prev_non_ws == "" or prev_non_ws in regex_prev_tokens):
            # JS regex literal /.../flags (handles escaped \/ and [...] char classes)
            out.append(" ")
            i += 1
            in_class = False
            while i < n:
                c = js[i]
                if c == "\\":
                    out.append(" ")
                    i += 1
                    if i < n:
                        out.append("\n" if js[i] == "\n" else " ")
                        i += 1
                    continue
                if c == "[":
                    in_class = True
                elif c == "]":
                    in_class = False
                elif c == "/" and not in_class:
                    out.append(" ")
                    i += 1
                    while i < n and js[i].isalpha():
                        out.append(" ")
                        i += 1
                    break
                elif c == "\n":
                    out.append("\n")
                    i += 1
                    break
                out.append(" ")
                i += 1
            prev_non_ws = ")"
        elif ch in ("'", '"', "`"):
            quote = ch
            out.append(" ")
            i += 1
            while i < n:
                c = js[i]
                if c == "\\":
                    out.append(" ")
                    i += 1
                    if i < n:
                        out.append("\n" if js[i] == "\n" else " ")
                        i += 1
                    continue
                if c == quote:
                    out.append(" ")
                    i += 1
                    break
                out.append("\n" if c == "\n" else " ")
                i += 1
            prev_non_ws = ")"
        else:
            out.append(ch)
            if not ch.isspace():
                prev_non_ws = ch
            i += 1
    return "".join(out)


def _find_brand_context(target: Path) -> list[str]:
    """Detect declared brand documentation or design token files in the target repo."""
    markers: list[str] = []
    for parent in [target.parent, *list(target.parents)[:4]]:
        for candidate in (
            "DESIGN.md",
            "BRAND.md",
            "docs/BRAND.md",
            "docs/VISUAL-PHILOSOPHY.md",
            "docs/UI-DOCTRINE.md",
            "tailwind.config.js",
            "tailwind.config.ts",
            "tokens.css",
            "tokens.json",
        ):
            p = parent / candidate
            if p.is_file():
                markers.append(str(p))
        if (parent / ".git").exists():
            break
    return sorted(set(markers))


def _has_project_reduced_motion_guard(target: Path) -> bool:
    """Check whether a global stylesheet in the target project already declares prefers-reduced-motion."""
    for parent in [target.parent, *list(target.parents)[:4]]:
        for candidate in (
            "globals.css",
            "global.css",
            "app.css",
            "index.css",
            "styles.css",
            "src/globals.css",
            "src/index.css",
            "src/app/globals.css",
            "styles/globals.css",
        ):
            p = parent / candidate
            if p.is_file():
                try:
                    if "prefers-reduced-motion" in p.read_text(encoding="utf-8", errors="ignore"):
                        return True
                except OSError:
                    pass
        if (parent / ".git").exists():
            break
    return False


def _check_js_block(
    js_raw: str,
    base_line: int,
    rel_file: str,
    html_info: _HtmlScanner | None,
    findings: list[dict[str, Any]],
    allow_node_syntax_check: bool = True,
) -> None:
    """Run deterministic static checks on a JS/script block."""
    js = _strip_js_comments_and_strings(js_raw)

    # 1. Optional node --check syntax check (pure JS/HTML script blocks only; skip JSX/TS/TSX)
    is_es_module = bool(re.search(r"(?:^|\n)\s*(?:import|export)\s", js))
    if allow_node_syntax_check and not is_es_module:
        try:
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tf:
                tf.write(js_raw)
                tmp_path = Path(tf.name)
            proc = subprocess.run(
                ["node", "--check", str(tmp_path)],
                capture_output=True,
                text=True,
                timeout=5,
            )
            tmp_path.unlink(missing_ok=True)
            if proc.returncode != 0:
                err_line = (proc.stderr or proc.stdout).strip().splitlines()[:3]
                findings.append({
                    "rule_id": "CPU-JS-SYNTAX",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-SYNTAX",
                    "severity": "BLOCKER",
                    "category": "runtime_correctness",
                    "file": rel_file,
                    "line": base_line,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": "JavaScript syntax error detected by `node --check`.",
                    "snippet": " | ".join(err_line),
                })
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

    # 2. Undefined function call detection (catches real ReferenceErrors like esc(...))
    declared: set[str] = set(JS_BUILTINS)
    for m in re.finditer(r"\bfunction\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*\(", js):
        declared.add(m.group(1))
    for m in re.finditer(r"\b(?:const|let|var)\s+([^;\n]+)", js):
        # Capture all comma-separated variable names (including destructuring)
        chunk = m.group(1)
        for vm in re.finditer(r"(?:^|,|\{|\[)\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*(?==|,|:|\}|\]|$)", chunk):
            declared.add(vm.group(1))
    for m in re.finditer(r"\bclass\s+([A-Za-z_$][A-Za-z0-9_$]*)", js):
        declared.add(m.group(1))
    # Function parameters
    for m in re.finditer(r"\(([^()\n]{0,120})\)\s*(?:=>|\{)", js):
        for pm in re.finditer(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\b", m.group(1)):
            declared.add(pm.group(1))
    for m in re.finditer(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\s*=>", js):
        declared.add(m.group(1))
    # Imports
    for m in re.finditer(r"\bimport\s+([^;\n]+)\bfrom\b", js):
        for im in re.finditer(r"\b([A-Za-z_$][A-Za-z0-9_$]*)\b", m.group(1)):
            declared.add(im.group(1))

    # Scan external scripts on disk; if any external <script src> cannot be resolved
    # locally (e.g. CDN library like jQuery/Chart.js), skip CPU-JS-UNDEF to prevent false positives.
    has_unresolved_external_script = False
    if html_info and html_info.external_scripts:
        base_dir = Path(rel_file).parent if Path(rel_file).is_absolute() else Path.cwd()
        for src in html_info.external_scripts:
            if re.match(r"^(?:https?:)?//", src):
                has_unresolved_external_script = True
                continue
            ext_path = base_dir / src
            if ext_path.is_file():
                ext_txt = ext_path.read_text(encoding="utf-8", errors="ignore")
                for m in re.finditer(r"\bfunction\s+([A-Za-z_$][A-Za-z0-9_$]*)", ext_txt):
                    declared.add(m.group(1))
                for m in re.finditer(r"\b(?:window|globalThis)\.([A-Za-z_$][A-Za-z0-9_$]*)\s*=", ext_txt):
                    declared.add(m.group(1))
            else:
                has_unresolved_external_script = True

    # Scan bare identifier calls not preceded by '.' or 'function ' or 'new '
    undef_hits: dict[str, list[int]] = {}
    if not has_unresolved_external_script:
        for offset, line_str in enumerate(js.splitlines()):
            for m in re.finditer(r"(?<![.\w$])([A-Za-z_$][A-Za-z0-9_$]*)\s*\(", line_str):
                name = m.group(1)
                prefix = line_str[: m.start()].rstrip()
                if name in declared:
                    continue
                if prefix.endswith(("function", "class", "get", "set", "async", "new", ":", ".")):
                    continue
                # Ignore object method shorthand like `foo(x) {`
                after = line_str[m.end() :]
                if re.match(r"[^()]*\)\s*\{", after) and not prefix.endswith(("=", "(", ",", "?", "&&", "||", "!")):
                    continue
                undef_hits.setdefault(name, []).append(base_line + offset)

    for fn_name, hit_lines in sorted(undef_hits.items()):
        findings.append({
            "rule_id": "CPU-JS-UNDEF",
            "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-UNDEF",
            "severity": "BLOCKER",
            "category": "runtime_correctness",
            "file": rel_file,
            "line": hit_lines[0],
            "evidence_tier": "TOOL_VERIFIED",
            "message": f"Call to undeclared function `{fn_name}(...)` (lines {hit_lines[:5]}) — throws runtime ReferenceError.",
            "snippet": f"{fn_name}(...) called at line(s) {hit_lines[:5]} with no local or imported declaration.",
        })

    # 3. Async click/submit handlers mutating backend without double-submit guard
    raw_lines = js_raw.splitlines()
    for idx, line_str in enumerate(raw_lines):
        if re.search(r"\.onclick\s*=\s*async\s*\(", line_str):
            # Read handler block (~25 lines or until closing `};`)
            block_lines = [line_str]
            depth = line_str.count("{") - line_str.count("}")
            j = idx + 1
            while j < len(raw_lines) and (depth > 0 or j == idx + 1) and j < idx + 35:
                block_lines.append(raw_lines[j])
                depth += raw_lines[j].count("{") - raw_lines[j].count("}")
                j += 1
            block = "\n".join(block_lines)
            if re.search(r'method\s*:\s*["\'](?:POST|PUT|PATCH|DELETE)["\']', block):
                has_lock = bool(re.search(r"\.disabled\s*=\s*true|aria-busy|inFlight|isSubmitting|busy", block))
                if not has_lock:
                    findings.append({
                        "rule_id": "CPU-JS-DOUBLE-SUBMIT",
                        "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-DOUBLE-SUBMIT",
                        "severity": "BLOCKER",
                        "category": "latency_perception",
                        "file": rel_file,
                        "line": base_line + idx,
                        "evidence_tier": "TOOL_VERIFIED",
                        "message": "Async click handler fires POST/PUT/PATCH/DELETE without `disabled` / `aria-busy` / in-flight double-submit guard.",
                        "snippet": line_str.strip()[:140],
                    })
                if "try" not in block and "catch" not in block:
                    findings.append({
                        "rule_id": "CPU-JS-UNHANDLED-MUTATION",
                        "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-UNHANDLED-MUTATION",
                        "severity": "BLOCKER",
                        "category": "latency_perception",
                        "file": rel_file,
                        "line": base_line + idx,
                        "evidence_tier": "TOOL_VERIFIED",
                        "message": "Async mutation click handler lacks `try/catch` error branch (failed request can silently drop user input or hang UI).",
                        "snippet": line_str.strip()[:140],
                    })

    # 4. Disabled button calling fire-and-forget IPC/setup without await
    for idx, line_str in enumerate(raw_lines):
        if re.search(r"\.disabled\s*=\s*true", line_str):
            window_block = "\n".join(raw_lines[idx : min(len(raw_lines), idx + 8)])
            if re.search(r"\.(?:setup|invoke|send)\s*\(", window_block) and "await " not in window_block and ".then(" not in window_block and ".catch(" not in window_block:
                findings.append({
                    "rule_id": "CPU-JS-FIRE-FORGET-DISABLE",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-FIRE-FORGET-DISABLE",
                    "severity": "BLOCKER",
                    "category": "latency_perception",
                    "file": rel_file,
                    "line": base_line + idx,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": "Button disabled before fire-and-forget async/IPC call without `await` or `.catch(...)` — rejected promise leaves control permanently disabled.",
                    "snippet": line_str.strip()[:140],
                })

    # 5. setTimeout restoring same textContent already set right before it
    for idx, line_str in enumerate(raw_lines):
        m = re.search(r"(\$\([^)]+\)|[A-Za-z_$][\w$]*)\.textContent\s*=\s*([^;]+);", line_str)
        if m:
            target_expr, val_expr = m.group(1), m.group(2).strip()
            lookahead = "\n".join(raw_lines[idx + 1 : min(len(raw_lines), idx + 5)])
            if re.search(r"setTimeout\s*\(\s*\(\)\s*=>\s*" + re.escape(target_expr) + r"\.textContent\s*=\s*" + re.escape(val_expr), lookahead):
                findings.append({
                    "rule_id": "CPU-JS-TIMEOUT-NOOP",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-JS-TIMEOUT-NOOP",
                    "severity": "MAJOR",
                    "category": "runtime_correctness",
                    "file": rel_file,
                    "line": base_line + idx,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"`setTimeout` reassigns identical `{val_expr}` instead of restoring the original button label.",
                    "snippet": line_str.strip()[:140],
                })

    # 6. Clickable non-semantic <div> wired in JS without button/tabindex
    if html_info is not None:
        for idx, line_str in enumerate(raw_lines):
            m = re.search(r'getElementById\(\s*["\']([^"\']+)["\']\s*\)\.onclick\s*=', line_str)
            if m:
                el_id = m.group(1)
                if el_id in html_info.elements_by_id:
                    tag, el_line, attrs = html_info.elements_by_id[el_id]
                    if tag in ("div", "span") and (attrs.get("role") != "button" or "tabindex" not in attrs):
                        findings.append({
                            "rule_id": "CPU-A11Y-DIV-CLICK",
                            "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-DIV-CLICK",
                            "severity": "BLOCKER",
                            "category": "interaction_physics",
                            "file": rel_file,
                            "line": el_line,
                            "evidence_tier": "TOOL_VERIFIED",
                            "message": f"Interactive `<{tag} id=\"{el_id}\">` wired with JS `.onclick` (line {base_line + idx}) lacks `role=\"button\"` and `tabindex=\"0\"` (keyboard unreachable).",
                            "snippet": f"<{tag} id=\"{el_id}\"> -> onclick at line {base_line + idx}",
                        })
        # Dynamically created clickable <div> rows without tabindex/role
        for idx, line_str in enumerate(raw_lines):
            m_div = re.search(r"(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*document\.createElement\(\s*['\"]div['\"]\s*\)", line_str)
            if m_div:
                var_name = m_div.group(1)
                blk = "\n".join(raw_lines[idx : min(len(raw_lines), idx + 8)])
                if re.search(rf"\b{re.escape(var_name)}\.onclick\s*=", blk) and "tabIndex" not in blk and "tabindex" not in blk and "role" not in blk:
                    findings.append({
                        "rule_id": "CPU-A11Y-DIV-CLICK",
                        "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-DIV-CLICK",
                        "severity": "BLOCKER",
                        "category": "interaction_physics",
                        "file": rel_file,
                        "line": base_line + idx,
                        "evidence_tier": "TOOL_VERIFIED",
                        "message": f"Dynamically created `<div>` (`{var_name}`) with `.onclick` lacks keyboard accessibility (`<button>` or `tabIndex=0` + `role=\"button\"`).",
                        "snippet": line_str.strip()[:140],
                    })


def _check_css_block(
    css: str,
    base_line: int,
    rel_file: str,
    full_text: str,
    findings: list[dict[str, Any]],
) -> None:
    """Run deterministic CSS checks for motion jank, reduced-motion, focus, and sizing."""
    css_lines = css.splitlines()
    has_motion = False

    for idx, line in enumerate(css_lines):
        lineno = base_line + idx
        if re.search(r"\btransition\s*:\s*all\b|\btransition-all\b", line):
            has_motion = True
            findings.append({
                "rule_id": "CPU-MOTION-JANK",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-MOTION-JANK",
                "severity": "MAJOR",
                "category": "interaction_physics",
                "file": rel_file,
                "line": lineno,
                "evidence_tier": "TOOL_VERIFIED",
                "message": "`transition: all` / `transition-all` animates layout and paint properties.",
                "snippet": line.strip()[:140],
            })
        elif re.search(r"transition\s*:[^;{}]*\b(box-shadow|height|width|top|left)\b", line):
            has_motion = True
            findings.append({
                "rule_id": "CPU-MOTION-JANK",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-MOTION-JANK",
                "severity": "MAJOR",
                "category": "interaction_physics",
                "file": rel_file,
                "line": lineno,
                "evidence_tier": "TOOL_VERIFIED",
                "message": "CSS `transition` animates non-compositor property (`box-shadow`/`height`/`width`/`top`/`left`).",
                "snippet": line.strip()[:140],
            })
        elif re.search(r"@keyframes\b[^{]*\{[^}]*\b(box-shadow|height|width|top|left)\s*:", line):
            has_motion = True
            findings.append({
                "rule_id": "CPU-MOTION-JANK",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-MOTION-JANK",
                "severity": "MAJOR",
                "category": "interaction_physics",
                "file": rel_file,
                "line": lineno,
                "evidence_tier": "TOOL_VERIFIED",
                "message": "`@keyframes` animates non-compositor paint/layout property (`box-shadow`/`height`/`width`/`top`/`left`).",
                "snippet": line.strip()[:140],
            })

        if re.search(r"@keyframes\b|\banimation\s*:|\btransition\s*:", line):
            has_motion = True

        # outline: none check
        if re.search(r"outline\s*:\s*(?:none|0)\b", line):
            low_alpha = re.search(r"rgba\([^)]*,\s*0?\.([0-3]\d|4[0-4])\s*\)", line)
            has_focus_visible = ":focus-visible" in css
            if low_alpha or not has_focus_visible:
                reason = (
                    "replaces outline with low-opacity focus shadow (<0.45 alpha, likely <3:1 WCAG 1.4.11)"
                    if low_alpha
                    else "removes focus outline with zero `:focus-visible` rule in stylesheet"
                )
                findings.append({
                    "rule_id": "CPU-A11Y-FOCUS",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-FOCUS",
                    "severity": "BLOCKER",
                    "category": "interaction_physics",
                    "file": rel_file,
                    "line": lineno,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"`outline: none` {reason}.",
                    "snippet": line.strip()[:140],
                })

        # Input/select font-size < 16px (causes iOS Safari auto-zoom)
        if re.search(r"(?:^|[},])\s*(?:[.#\w-]+\s+)*(?:input|select|textarea)[^{]*\{[^}]*font-size\s*:\s*(\d+(?:\.\d+)?)px", line):
            m_fs = re.search(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", line)
            if m_fs and float(m_fs.group(1)) < 16.0:
                findings.append({
                    "rule_id": "CPU-A11Y-INPUT-FONT",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-INPUT-FONT",
                    "severity": "MAJOR",
                    "category": "interaction_physics",
                    "file": rel_file,
                    "line": lineno,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"Input/select `font-size: {m_fs.group(1)}px` < `16px` triggers forced mobile auto-zoom.",
                    "snippet": line.strip()[:140],
                })

        # Explicit small icon/button touch targets (< 44px)
        m_btn_sz = re.search(r"(\.[A-Za-z0-9_-]*(?:btn|ico|close|icon)[A-Za-z0-9_-]*)\s*\{[^}]*(?:width|height)\s*:\s*(\d+)px", line)
        if m_btn_sz and int(m_btn_sz.group(2)) < 44:
            findings.append({
                "rule_id": "CPU-A11Y-TARGET-SIZE",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-TARGET-SIZE",
                "severity": "MAJOR",
                "category": "interaction_physics",
                "file": rel_file,
                "line": lineno,
                "evidence_tier": "TOOL_VERIFIED",
                "message": f"Interactive control `{m_btn_sz.group(1)}` sized `{m_btn_sz.group(2)}px` < `44px` minimum mobile touch target.",
                "snippet": line.strip()[:140],
            })

    if "requestAnimationFrame" in full_text:
        has_motion = True

    if has_motion and "prefers-reduced-motion" not in full_text and not _has_project_reduced_motion_guard(Path(rel_file)):
        findings.append({
            "rule_id": "CPU-MOTION-REDUCED",
            "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-MOTION-REDUCED",
            "severity": "BLOCKER",
            "category": "interaction_physics",
            "file": rel_file,
            "line": base_line,
            "evidence_tier": "TOOL_VERIFIED",
            "message": "Animations/transitions or `requestAnimationFrame` detected with zero `@media (prefers-reduced-motion: reduce)` or JS reduced-motion guard.",
            "snippet": "0 occurrences of `prefers-reduced-motion` across file or project global stylesheets.",
        })


def scan_file(path: Path) -> dict[str, Any]:
    """Scan a single frontend artifact deterministically."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    rel_file = str(path)
    findings: list[dict[str, Any]] = []
    suffix = path.suffix.lower()

    brand_files = _find_brand_context(path)
    has_root_tokens = bool(re.search(r":root\s*\{[^}]*--[a-zA-Z0-9_-]+", text))

    html_info: _HtmlScanner | None = None
    if suffix in (".html", ".htm", ".vue", ".svelte"):
        html_info = _HtmlScanner(lines)
        try:
            html_info.feed(text)
        except Exception:
            pass

        # Visible form controls count (Baymard <= 14)
        if len(html_info.visible_form_controls) > 14:
            first_line = html_info.visible_form_controls[0][1]
            findings.append({
                "rule_id": "CPU-FORM-BLOAT",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-FORM-BLOAT",
                "severity": "MAJOR",
                "category": "conversion_ergonomics",
                "file": rel_file,
                "line": first_line,
                "evidence_tier": "TOOL_VERIFIED",
                "message": f"{len(html_info.visible_form_controls)} visible form controls rendered by default (exceeds Baymard <= 14 ceiling).",
                "snippet": ", ".join(x[2] for x in html_info.visible_form_controls[:16]),
            })

        # Flat <select> with > 7 options without <optgroup>
        for sel in html_info.selects:
            if sel["options"] > 7 and not sel["has_optgroup"]:
                findings.append({
                    "rule_id": "CPU-FORM-HICK-SELECT",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-FORM-HICK-SELECT",
                    "severity": "MINOR",
                    "category": "cognitive_load",
                    "file": rel_file,
                    "line": sel["line"],
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"`<select id=\"{sel['id']}\">` exposes {sel['options']} flat `<option>` items (> 7) with no `<optgroup>` or search filter.",
                    "snippet": f"select#{sel['id']} ({sel['options']} options)",
                })

        # Icon-only buttons missing aria-label
        for btn in html_info.buttons:
            clean_txt = re.sub(r"\s+", "", btn["text"])
            is_symbol_only = len(clean_txt) == 0 or (len(clean_txt) <= 2 and not any(c.isalnum() for c in clean_txt))
            if is_symbol_only and not (btn["attrs"].get("aria-label") or btn["attrs"].get("aria-labelledby")):
                findings.append({
                    "rule_id": "CPU-A11Y-ICON-BTN",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-ICON-BTN",
                    "severity": "BLOCKER",
                    "category": "visual_semiotics",
                    "file": rel_file,
                    "line": btn["line"],
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"Icon/symbol-only `<button id=\"{btn['id']}\">` lacks `aria-label` or `aria-labelledby` (WCAG 4.1.2).",
                    "snippet": f"<button id=\"{btn['id']}\">{btn['text'].strip()}</button>",
                })

        # Non-semantic inline div/span onclick
        for tag, dline, attrs in html_info.div_clicks:
            findings.append({
                "rule_id": "CPU-A11Y-DIV-CLICK",
                "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-A11Y-DIV-CLICK",
                "severity": "BLOCKER",
                "category": "interaction_physics",
                "file": rel_file,
                "line": dline,
                "evidence_tier": "TOOL_VERIFIED",
                "message": f"Clickable `<{tag}>` lacks `role=\"button\"` and `tabindex=\"0\"`.",
                "snippet": f"<{tag} id=\"{attrs.get('id', '')}\" onclick=...>",
            })

        # HTML minlength vs JS i18n hint mismatch
        for mline, minlen, input_id in html_info.input_minlengths:
            # Look for "min. <other_num>" in strings across the file
            other_mins = set()
            for idx, ln in enumerate(lines, start=1):
                for mm in re.finditer(r"(?:min\.?|mín\.?|mind\.?)\s*(\d+)\s*(?:char|caract|Zeichen|字|자|أحرف)", ln, re.IGNORECASE):
                    val = int(mm.group(1))
                    if val != minlen:
                        other_mins.add((val, idx))
            if other_mins:
                sample_val, sample_line = sorted(other_mins)[0]
                findings.append({
                    "rule_id": "CPU-I18N-MINLEN-DRIFT",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-I18N-MINLEN-DRIFT",
                    "severity": "MAJOR",
                    "category": "cognitive_load",
                    "file": rel_file,
                    "line": sample_line,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": f"Password/input `#{input_id}` enforces `minlength=\"{minlen}\"` (line {mline}) while UI/i18n strings advertise `min. {sample_val}` (line {sample_line}).",
                    "snippet": f"minlength={minlen} (L{mline}) vs copy min={sample_val} (L{sample_line})",
                })

        for s_line, css_text in html_info.inline_styles:
            _check_css_block(css_text, s_line, rel_file, text, findings)
        for js_line, js_text in html_info.inline_scripts:
            _check_js_block(js_text, js_line, rel_file, html_info, findings)

    elif suffix == ".css":
        _check_css_block(text, 1, rel_file, text, findings)
    elif suffix in (".js", ".jsx", ".ts", ".tsx"):
        _check_js_block(text, 1, rel_file, None, findings, allow_node_syntax_check=(suffix == ".js"))
        # Check inline className/style motion jank in JSX/TSX
        for idx, line in enumerate(lines, start=1):
            if "transition-all" in line:
                findings.append({
                    "rule_id": "CPU-MOTION-JANK",
                    "canonical_id": f"{SUITE_ID}:{MODULE_ID}:CPU-MOTION-JANK",
                    "severity": "MAJOR",
                    "category": "interaction_physics",
                    "file": rel_file,
                    "line": idx,
                    "evidence_tier": "TOOL_VERIFIED",
                    "message": "`transition-all` animates layout/paint properties.",
                    "snippet": line.strip()[:140],
                })

    # Single-root-cause deduplication by (rule_id, file, line)
    seen: set[tuple[str, str, int]] = set()
    deduped: list[dict[str, Any]] = []
    for f in findings:
        key = (f["rule_id"], f["file"], f["line"])
        if key not in seen:
            seen.add(key)
            deduped.append(f)

    counts = {
        "blocker": sum(1 for f in deduped if f["severity"] == "BLOCKER"),
        "major": sum(1 for f in deduped if f["severity"] == "MAJOR"),
        "minor": sum(1 for f in deduped if f["severity"] == "MINOR"),
    }
    sha = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:12]

    return {
        "scanner": "uiux_cpu_scanner",
        "scanner_version": SCANNER_VERSION,
        "suite_id": SUITE_ID,
        "file": rel_file,
        "file_sha256_12": sha,
        "line_count": len(lines),
        "brand_exemption": {
            "declared_brand_docs": brand_files,
            "has_root_css_tokens": has_root_tokens,
            "exempt_brand_palette_from_ai_slop": bool(brand_files or has_root_tokens),
        },
        "counts": counts,
        "findings": deduped,
    }


def to_sarif(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Convert scanner results into SARIF 2.1.0 format."""
    sev_map = {"BLOCKER": "error", "MAJOR": "warning", "MINOR": "note"}
    sarif_results = []
    rules_seen: dict[str, dict[str, Any]] = {}
    for res in results:
        for f in res["findings"]:
            rid = f["canonical_id"]
            if rid not in rules_seen:
                rules_seen[rid] = {"id": rid, "shortDescription": {"text": f["rule_id"]}}
            sarif_results.append({
                "ruleId": rid,
                "level": sev_map.get(f["severity"], "warning"),
                "message": {"text": f["message"]},
                "locations": [{
                    "physicalLocation": {
                        "artifactLocation": {"uri": f["file"]},
                        "region": {"startLine": max(1, int(f["line"]))},
                    }
                }],
            })
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "uiux_cpu_scanner",
                    "version": SCANNER_VERSION,
                    "rules": list(rules_seen.values()),
                }
            },
            "results": sarif_results,
        }],
    }


def to_markdown(results: list[dict[str, Any]]) -> str:
    """Render concise Markdown summary for LLM ingestion."""
    out: list[str] = []
    for res in results:
        c = res["counts"]
        out.append(f"### CPU Pre-Scan: `{res['file']}` (sha:{res['file_sha256_12']}, {res['line_count']} lines)")
        out.append(
            f"- Counts: **BLOCKER={c['blocker']}**, **MAJOR={c['major']}**, **MINOR={c['minor']}** "
            f"| Brand palette exemption: `{res['brand_exemption']['exempt_brand_palette_from_ai_slop']}`"
        )
        if not res["findings"]:
            out.append("- No deterministic CPU defects detected.")
        else:
            out.append("| Severity | Canonical ID | Line | Finding |")
            out.append("|---|---|---|---|")
            for f in res["findings"]:
                out.append(f"| `{f['severity']}` | `{f['canonical_id']}` | L{f['line']} | {f['message']} |")
        out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic CPU pre-scanner for best-ui-ux-designers")
    parser.add_argument("targets", nargs="+", help="One or more frontend files or directories to scan")
    parser.add_argument("--format", choices=["json", "sarif", "markdown"], default="json")
    parser.add_argument("--fail-on-blocker", action="store_true", help="Exit 2 if any BLOCKER finding exists")
    args = parser.parse_args(argv)

    supported_exts = {".html", ".htm", ".css", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}
    skip_dirs = {".git", "node_modules", ".next", "dist", "build", ".venv", "__pycache__", "coverage"}

    results: list[dict[str, Any]] = []
    for t in args.targets:
        p = Path(t)
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if any(part in skip_dirs for part in child.parts):
                    continue
                if child.is_file() and child.suffix.lower() in supported_exts:
                    results.append(scan_file(child))
        elif p.is_file():
            results.append(scan_file(p))
        else:
            print(f"ERROR: Target path not found: {t}", file=sys.stderr)
            return 1

    total_blockers = sum(r["counts"]["blocker"] for r in results)
    if args.format == "json":
        payload = {"scanner_version": SCANNER_VERSION, "total_blockers": total_blockers, "results": results}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.format == "sarif":
        print(json.dumps(to_sarif(results), indent=2, ensure_ascii=False))
    else:
        print(to_markdown(results))

    if args.fail_on_blocker and total_blockers > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
