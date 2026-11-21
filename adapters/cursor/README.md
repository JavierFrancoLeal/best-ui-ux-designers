# Cursor Adapter (`best-ui-ux-designers`)

Mounts `best-ui-ux-designers` into Cursor using `.cursor/skills/` and a namespaced `.mdc` rule (`.cursor/rules/uiux-director.mdc`) with `alwaysApply: false` and frontend file `globs`.

## Technical Constraints Covered
- Cursor ignores plain `.md` files inside `.cursor/rules/`; this adapter provides native `.mdc` frontmatter (`description`, `globs`, `alwaysApply: false`).
- Strict `uiux-` prefix avoids collisions with sibling SDLC suites installed in the same workspace.

## Installation

```bash
./adapters/install.sh --target cursor --mode director-only --scope workspace --dest /path/to/repo
```
