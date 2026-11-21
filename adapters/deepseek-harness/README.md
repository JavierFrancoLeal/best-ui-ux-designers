# DeepSeek Harness Adapter (`best-ui-ux-designers`)

Configures `best-ui-ux-designers` for DeepSeek Harness (`dsh`) running DeepSeek V4 Flash / DeepSeek V4 Pro in deterministic text-only audit mode.

## Text-Only Linter Mode (No Vision Required)
Because DeepSeek V4 Flash/Pro runs primarily on text/code without native screenshot rendering, every rule in `skills/<slug>/DESIGN.md` and `committee/auditors/*/rules.yaml` is anchored in static code, AST, DOM, CSS, ARIA, KLM-GOMS, and state-machine predicates (`observable_indicator` and `detection_rule`). Any visual-only check that cannot be inferred from source tokens MUST be marked `UNVERIFIED_TEXT_ONLY`.

## Installation

```bash
# Workspace install (registers skills under .agents/skills/ and upserts AGENTS.md + CLAUDE.md symlink)
./adapters/install.sh --target deepseek --mode director-only --scope workspace --dest /path/to/repo

# Or package/register via dsh plugin manifest
# Manifest path: adapters/deepseek-harness/dsh-plugin.json
```
