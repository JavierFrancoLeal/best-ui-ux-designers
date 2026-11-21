# Windsurf / Devin Desktop Adapter (`best-ui-ux-designers`)

Mounts `best-ui-ux-designers` into Windsurf / Devin Desktop under `.windsurf/skills/` with a namespaced `model_decision` rule (`uiux-director.md`) written to `.devin/rules/uiux-director.md` (preferred) and `.windsurf/rules/uiux-director.md` (fallback).

## Technical Constraints Covered
- Windsurf / Devin Desktop enforces a hard `12,000`-character cap per workspace rule file (`6,000` chars global) with silent truncation. `uiux-director.md` stays compact (`< 2,500` chars, strictly `< 12,000` chars verified in CI) and delegates all deep schemas to `SKILL.md` / `DESIGN.md`.
- Uses `trigger: model_decision` and the `uiux-` filename prefix to avoid colliding with sibling SDLC suites.

## Installation

```bash
./adapters/install.sh --target windsurf --mode director-only --scope workspace --dest /path/to/repo
```
