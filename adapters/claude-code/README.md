# Claude Code Adapter (`best-ui-ux-designers`)

Mounts `best-ui-ux-designers` into Claude Code using `.claude/skills/` and the relative symlink `CLAUDE.md -> AGENTS.md`.

## Paths & Invocation
- **Workspace skills:** `<repo>/.claude/skills/<slug>/`
- **Global skills:** `~/.claude/skills/<slug>/`
- **Workspace instructions:** `CLAUDE.md` symlinked to `AGENTS.md` (created only if `CLAUDE.md` does not already exist; `AGENTS.md` is updated idempotently via `<!-- BEGIN best-ui-ux-designers -->` markers).

## Explicit Slash Invocation for Auditors (Optional)
Teams that prefer explicit manual execution of the 4 Via Negativa auditors via `/auditor-cognitive-fatigue`, `/auditor-latency-broken-states`, `/auditor-physics-accessibility`, and `/auditor-agentic-anti-slop` can add `disable-model-invocation: true` to the installed auditor `SKILL.md` frontmatter copies inside `.claude/skills/`.

## Installation

```bash
# Standalone install (17 skills)
./adapters/install.sh --target claude --mode full --scope workspace --dest /path/to/repo

# Multi-suite coexistence (only design-director exposed in catalog)
./adapters/install.sh --target claude --mode director-only --scope workspace --dest /path/to/repo
```
