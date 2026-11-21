# Google Antigravity Adapter (`best-ui-ux-designers`)

Mounts the `ui-ux` adversarial judgment suite into Google Antigravity (App, IDE, CLI) using namespaced rule files (`uiux-bootstrap.md`) and `agentskills.io` discovery paths.

## Paths & Hard Limits
- **Workspace skills:** `<repo>/.agents/skills/<slug>/` (fallback: `.agent/skills/`)
- **Global skills:** `~/.gemini/config/skills/<slug>/`
- **Workspace rule:** `<repo>/.agents/rules/uiux-bootstrap.md` (`trigger: model_decision`, strictly `< 24,000` bytes; avoids draining the `20,000`-token `always_on` budget)
- **CLI slash commands:** Every registered skill automatically mounts as `/<slug>` (e.g., `/design-director`).

## Installation

```bash
# Single-suite workspace install (all 17 skills active)
./adapters/install.sh --target antigravity --mode full --scope workspace --dest /path/to/repo

# Multi-suite coexistence (only design-director registered in active catalog;
# 12 designers + 4 auditors mounted under design-director/references/)
./adapters/install.sh --target antigravity --mode director-only --scope workspace --dest /path/to/repo

# Global install
./adapters/install.sh --target antigravity --mode director-only --scope global
```
