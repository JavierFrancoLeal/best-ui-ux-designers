# OpenAI Codex & ChatGPT Adapter (`best-ui-ux-designers`)

Mounts `best-ui-ux-designers` into OpenAI Codex and ChatGPT workspaces under `.agents/skills/` while staying safely within the initial skill-discovery character budget (`< 8,000` characters across all 17 skills, enforced by `validators/check_skill_frontmatter.py`).

## Paths & Triggers
- **Workspace skills:** `<repo>/.agents/skills/<slug>/`
- **Global skills:** `~/.agents/skills/<slug>/`
- **Direct invocation:** `$design-director` (orchestrator), `$dieter-rams`, `$karri-saarinen`, `$luke-wroblewski`, `$auditor-agentic-anti-slop`, etc.

## Multi-Suite Budget Guidance
In `--mode full`, all 17 `best-ui-ux-designers` skills stay under `8,000` total discovery characters (`name + description`, each `description <= 320` chars). When co-installing 2 to 5 SDLC suites in the same workspace, ALWAYS use `--mode director-only` so `best-ui-ux-designers` consumes only 1 catalog entry (`$design-director`, ~260 chars) and resolves experts lazily from `design-director/references/`.

## Installation

```bash
# Single-suite install
./adapters/install.sh --target codex --mode full --scope workspace --dest /path/to/repo

# Multi-suite coexistence (recommended for >= 2 suites)
./adapters/install.sh --target codex --mode director-only --scope workspace --dest /path/to/repo
```
