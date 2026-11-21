#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

TARGET="all"
MODE="full"
SCOPE="workspace"
DEST=""
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: install.sh [OPTIONS]

Install best-ui-ux-designers into one or more coding-agent harnesses without
colliding with sibling ECOSYSTEM_CONTRACT v1.0.0 suites.

Options:
  --target <name>   antigravity | deepseek | claude | codex | cursor | windsurf | all (default: all)
  --mode <mode>     full | director-only (default: full)
  --scope <scope>   workspace | global (default: workspace)
  --dest <path>     Destination workspace root (required for workspace scope if not PWD)
  --dry-run         Print planned operations without writing files
  -h, --help        Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --scope)
      SCOPE="${2:-}"
      shift 2
      ;;
    --dest)
      DEST="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

case "${TARGET}" in
  antigravity|deepseek|claude|codex|cursor|windsurf|all) ;;
  *) echo "ERROR: Invalid --target '${TARGET}'" >&2; exit 1 ;;
esac

case "${MODE}" in
  full|director-only) ;;
  *) echo "ERROR: Invalid --mode '${MODE}' (expected full or director-only)" >&2; exit 1 ;;
esac

case "${SCOPE}" in
  workspace|global) ;;
  *) echo "ERROR: Invalid --scope '${SCOPE}' (expected workspace or global)" >&2; exit 1 ;;
esac

if [[ "${SCOPE}" == "workspace" ]]; then
  if [[ -z "${DEST}" ]]; then
    DEST="$(pwd)"
  fi
else
  if [[ -z "${DEST}" ]]; then
    DEST="${HOME}"
  fi
fi

log() {
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    printf '[dry-run] %s\n' "$*"
  else
    printf '[install] %s\n' "$*"
  fi
}

run_mkdir() {
  local dir="$1"
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "mkdir -p ${dir}"
  else
    mkdir -p "${dir}"
  fi
}

copy_dir() {
  local src="$1"
  local dst="$2"
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "copy dir ${src} -> ${dst}"
  else
    mkdir -p "$(dirname "${dst}")"
    rm -rf "${dst}"
    cp -R "${src}" "${dst}"
  fi
}

copy_file() {
  local src="$1"
  local dst="$2"
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "copy file ${src} -> ${dst}"
  else
    mkdir -p "$(dirname "${dst}")"
    cp "${src}" "${dst}"
  fi
}

install_skills_into() {
  local skills_dir="$1"
  run_mkdir "${skills_dir}"

  if [[ "${MODE}" == "full" ]]; then
    log "Installing all 17 skills (mode=full) into ${skills_dir}"
    copy_dir "${REPO_ROOT}/committee/design-director" "${skills_dir}/design-director"
    for d in "${REPO_ROOT}"/skills/*; do
      [[ -d "${d}" ]] || continue
      copy_dir "${d}" "${skills_dir}/$(basename "${d}")"
    done
    for a in "${REPO_ROOT}"/committee/auditors/*; do
      [[ -d "${a}" ]] || continue
      copy_dir "${a}" "${skills_dir}/$(basename "${a}")"
    done
  else
    log "Installing director-only (1 active catalog entry + lazy references/) into ${skills_dir}"
    local director_dst="${skills_dir}/design-director"
    copy_dir "${REPO_ROOT}/committee/design-director" "${director_dst}"
    run_mkdir "${director_dst}/references/skills"
    run_mkdir "${director_dst}/references/auditors"
    copy_file "${REPO_ROOT}/committee/design-director/routing-matrix.yaml" "${director_dst}/references/routing-matrix.yaml"
    copy_file "${REPO_ROOT}/suite.yaml" "${director_dst}/references/suite.yaml"
    for d in "${REPO_ROOT}"/skills/*; do
      [[ -d "${d}" ]] || continue
      copy_dir "${d}" "${director_dst}/references/skills/$(basename "${d}")"
    done
    for a in "${REPO_ROOT}"/committee/auditors/*; do
      [[ -d "${a}" ]] || continue
      copy_dir "${a}" "${director_dst}/references/auditors/$(basename "${a}")"
    done
  fi
}

upsert_agents_md() {
  local workspace_root="$1"
  local agents_file="${workspace_root}/AGENTS.md"
  local claude_link="${workspace_root}/CLAUDE.md"
  local begin_marker="<!-- BEGIN best-ui-ux-designers -->"
  local end_marker="<!-- END best-ui-ux-designers -->"

  local block
  block="$(cat <<'EOF'
<!-- BEGIN best-ui-ux-designers -->
## UI/UX Adversarial Judgment Suite (`best-ui-ux-designers`, `suite_id: ui-ux`)
- **Architecture Mode (`plan`/`design`):** Run `design-director` (Solow Central Dynamo check + 4 active Barbell designers + rebuttal + 4 Via Negativa auditors + `verdict_envelope` v1.0.0).
- **Fast PR Gate Mode (`build`/`test`/`deploy`/`maintain`):** Run the 4 Via Negativa auditors (`auditor-cognitive-fatigue`, `auditor-latency-broken-states`, `auditor-physics-accessibility`, `auditor-agentic-anti-slop`) on UI diffs; escalate to `design-director` on `hard_veto`, new AI surface, or regime shift.
<!-- END best-ui-ux-designers -->
EOF
)"

  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "upsert fenced block (${begin_marker} .. ${end_marker}) into ${agents_file}"
    log "ensure relative symlink ${claude_link} -> AGENTS.md if absent"
    return 0
  fi

  mkdir -p "${workspace_root}"
  if [[ ! -f "${agents_file}" ]]; then
    printf '# AGENTS.md\n\n%s\n' "${block}" > "${agents_file}"
  elif grep -qF "${begin_marker}" "${agents_file}"; then
    local tmp_file block_file
    tmp_file="$(mktemp)"
    block_file="$(mktemp)"
    printf '%s\n' "${block}" > "${block_file}"
    awk -v begin="${begin_marker}" -v end="${end_marker}" -v bfile="${block_file}" '
      $0 == begin {
        while ((getline line < bfile) > 0) print line
        close(bfile)
        skip=1
        next
      }
      $0 == end { skip=0; next }
      !skip { print }
    ' "${agents_file}" > "${tmp_file}"
    mv "${tmp_file}" "${agents_file}"
    rm -f "${block_file}"
  else
    printf '\n%s\n' "${block}" >> "${agents_file}"
  fi

  if [[ ! -e "${claude_link}" && ! -L "${claude_link}" ]]; then
    (cd "${workspace_root}" && ln -s "AGENTS.md" "CLAUDE.md")
  fi
}

install_antigravity() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.agents/skills"
    copy_file "${REPO_ROOT}/adapters/antigravity/uiux-bootstrap.md" "${DEST}/.agents/rules/uiux-bootstrap.md"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.gemini/config/skills"
    copy_file "${REPO_ROOT}/adapters/antigravity/uiux-bootstrap.md" "${DEST}/.gemini/config/rules/uiux-bootstrap.md"
  fi
}

install_deepseek() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.agents/skills"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.agents/skills"
  fi
}

install_claude() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.claude/skills"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.claude/skills"
  fi
}

install_codex() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.agents/skills"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.agents/skills"
  fi
}

install_cursor() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.cursor/skills"
    copy_file "${REPO_ROOT}/adapters/cursor/uiux-director.mdc" "${DEST}/.cursor/rules/uiux-director.mdc"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.cursor/skills"
  fi
}

install_windsurf() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.windsurf/skills"
    copy_file "${REPO_ROOT}/adapters/windsurf-devin/uiux-director.md" "${DEST}/.devin/rules/uiux-director.md"
    copy_file "${REPO_ROOT}/adapters/windsurf-devin/uiux-director.md" "${DEST}/.windsurf/rules/uiux-director.md"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.windsurf/skills"
  fi
}

log "Starting best-ui-ux-designers installer (target=${TARGET}, mode=${MODE}, scope=${SCOPE}, dest=${DEST})"

case "${TARGET}" in
  antigravity) install_antigravity ;;
  deepseek)    install_deepseek ;;
  claude)      install_claude ;;
  codex)       install_codex ;;
  cursor)      install_cursor ;;
  windsurf)    install_windsurf ;;
  all)
    install_antigravity
    install_deepseek
    install_claude
    install_codex
    install_cursor
    install_windsurf
    ;;
esac

log "Completed installation successfully."
