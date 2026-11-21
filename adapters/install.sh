#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

SUITE_ID="ui-ux"
DIRECTOR_SLUG="design-director"
REPO_NAME="best-ui-ux-designers"

TARGET="all"
MODE="director-only"
SCOPE="workspace"
DEST=""
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: install.sh [OPTIONS]

Install best-ui-ux-designers (suite_id: ui-ux) into one or more coding-agent
harnesses without colliding with sibling ECOSYSTEM_CONTRACT v1.1.0 suites.

Options:
  --target <name>   antigravity | deepseek | claude | codex | cursor | windsurf | all (default: all)
  --mode <mode>     director-only | full (default: director-only)
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
  director-only|full) ;;
  *) echo "ERROR: Invalid --mode '${MODE}' (expected director-only or full)" >&2; exit 1 ;;
esac

case "${SCOPE}" in
  workspace|global) ;;
  *) echo "ERROR: Invalid --scope '${SCOPE}' (expected workspace or global)" >&2; exit 1 ;;
esac

if [[ "${SCOPE}" == "workspace" ]]; then
  [[ -n "${DEST}" ]] || DEST="$(pwd)"
else
  [[ -n "${DEST}" ]] || DEST="${HOME}"
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

safe_replace_owned_dir() {
  local src="$1"
  local dst="$2"
  local expected_prefix="$3"
  local base
  base="$(basename "${dst}")"
  if [[ "${base}" != "${expected_prefix}"* && "${base}" != "${DIRECTOR_SLUG}" ]]; then
    echo "ERROR: Refusing to replace unowned directory '${dst}'" >&2
    exit 1
  fi
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "sync dir ${src} -> ${dst}"
  else
    mkdir -p "$(dirname "${dst}")"
    rm -rf "${dst}"
    cp -R "${src}" "${dst}"
  fi
}

install_lazy_references() {
  local director_dst="$1"
  run_mkdir "${director_dst}/references/skills"
  run_mkdir "${director_dst}/references/auditors"
  run_mkdir "${director_dst}/tools"

  copy_file "${REPO_ROOT}/suite.yaml" "${director_dst}/references/suite.yaml"
  copy_file "${REPO_ROOT}/tools/uiux_cpu_scanner.py" "${director_dst}/tools/uiux_cpu_scanner.py"

  # Anti-recursive-discovery: rename nested SKILL.md -> PROFILE.md / AUDITOR.md
  # so harnesses scanning **/SKILL.md index strictly 1 skill per suite.
  for d in "${REPO_ROOT}"/skills/*; do
    [[ -d "${d}" ]] || continue
    local slug
    slug="$(basename "${d}")"
    local dst_s="${director_dst}/references/skills/${slug}"
    run_mkdir "${dst_s}"
    [[ -f "${d}/BRIEF.md" ]] && copy_file "${d}/BRIEF.md" "${dst_s}/BRIEF.md"
    [[ -f "${d}/DESIGN.md" ]] && copy_file "${d}/DESIGN.md" "${dst_s}/DESIGN.md"
    [[ -f "${d}/SKILL.md" ]] && copy_file "${d}/SKILL.md" "${dst_s}/PROFILE.md"
  done

  for a in "${REPO_ROOT}"/committee/auditors/*; do
    [[ -d "${a}" ]] || continue
    local aslug
    aslug="$(basename "${a}")"
    local dst_a="${director_dst}/references/auditors/${aslug}"
    run_mkdir "${dst_a}"
    [[ -f "${a}/rules.yaml" ]] && copy_file "${a}/rules.yaml" "${dst_a}/rules.yaml"
    [[ -f "${a}/SKILL.md" ]] && copy_file "${a}/SKILL.md" "${dst_a}/AUDITOR.md"
  done
}

INSTALLED_SKILL_DIRS="|"
install_skills_into() {
  local skills_dir="$1"
  if [[ "${INSTALLED_SKILL_DIRS}" == *"|${skills_dir}|"* ]]; then
    return 0
  fi
  INSTALLED_SKILL_DIRS="${INSTALLED_SKILL_DIRS}${skills_dir}|"

  run_mkdir "${skills_dir}"
  local director_dst="${skills_dir}/${DIRECTOR_SLUG}"

  if [[ "${MODE}" == "director-only" ]]; then
    log "Installing director-only (1 active SKILL.md + non-recursive references/ + CPU scanner) into ${skills_dir}"
    safe_replace_owned_dir "${REPO_ROOT}/committee/${DIRECTOR_SLUG}" "${director_dst}" "${DIRECTOR_SLUG}"
    install_lazy_references "${director_dst}"
  else
    log "Installing full mode (namespaced ${SUITE_ID}-* skills + director + CPU scanner) into ${skills_dir}"
    safe_replace_owned_dir "${REPO_ROOT}/committee/${DIRECTOR_SLUG}" "${director_dst}" "${DIRECTOR_SLUG}"
    install_lazy_references "${director_dst}"
    for d in "${REPO_ROOT}"/skills/*; do
      [[ -d "${d}" ]] || continue
      local slug
      slug="$(basename "${d}")"
      safe_replace_owned_dir "${d}" "${skills_dir}/${SUITE_ID}-${slug}" "${SUITE_ID}-"
    done
    for a in "${REPO_ROOT}"/committee/auditors/*; do
      [[ -d "${a}" ]] || continue
      local aslug
      aslug="$(basename "${a}")"
      safe_replace_owned_dir "${a}" "${skills_dir}/${SUITE_ID}-${aslug}" "${SUITE_ID}-"
    done
  fi
}

upsert_fenced_block() {
  local target_file="$1"
  local begin_marker="<!-- BEGIN ${REPO_NAME} -->"
  local end_marker="<!-- END ${REPO_NAME} -->"
  local block="$2"

  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "upsert fenced block (${begin_marker} .. ${end_marker}) into ${target_file}"
    return 0
  fi

  mkdir -p "$(dirname "${target_file}")"
  if [[ ! -f "${target_file}" ]]; then
    printf '# %s\n\n%s\n' "$(basename "${target_file}")" "${block}" > "${target_file}"
  elif grep -qF "${begin_marker}" "${target_file}"; then
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
    ' "${target_file}" > "${tmp_file}"
    mv "${tmp_file}" "${target_file}"
    rm -f "${block_file}"
  else
    printf '\n%s\n' "${block}" >> "${target_file}"
  fi
}

AGENTS_UPSERTED=0
upsert_agents_md() {
  local workspace_root="$1"
  local skills_rel="${2:-.agents/skills}"
  if [[ "${AGENTS_UPSERTED}" -eq 1 ]]; then
    return 0
  fi
  AGENTS_UPSERTED=1

  local agents_file="${workspace_root}/AGENTS.md"
  local claude_link="${workspace_root}/CLAUDE.md"

  local block
  block="$(cat <<EOF
<!-- BEGIN best-ui-ux-designers -->
## UI/UX Pre-Merge Governance (\`best-ui-ux-designers\`, \`suite_id: ui-ux\`, v1.1.0)
- **Step 0 (CPU Pre-Scanner):** Run \`python3 ${skills_rel}/design-director/tools/uiux_cpu_scanner.py --format json <ui-files...>\` first (\`TOOL_VERIFIED\`).
- **Fast PR Gate (\`build\`/\`verify\`):** Combine CPU scanner output with semantic checks from \`${skills_rel}/design-director/references/auditors/*/rules.yaml\`; escalate to \`design-director\` on \`BLOCKER\`, new AI surface, or regime shift.
- **Architecture Mode (\`plan\`/\`design\`):** Run \`design-director\` (\`SKILL.md\` + compact \`BRIEF.md\` active panel \`<= 25 KB\` + \`Verdict Envelope v1.1.0\`).
<!-- END best-ui-ux-designers -->
EOF
)"

  upsert_fenced_block "${agents_file}" "${block}"

  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "ensure ${claude_link} symlinks to AGENTS.md (or upsert fenced block if regular file exists)"
    return 0
  fi

  if [[ ! -e "${claude_link}" && ! -L "${claude_link}" ]]; then
    (cd "${workspace_root}" && ln -s "AGENTS.md" "CLAUDE.md")
  elif [[ -f "${claude_link}" && ! -L "${claude_link}" ]]; then
    upsert_fenced_block "${claude_link}" "${block}"
  fi
}

install_antigravity() {
  if [[ "${SCOPE}" == "workspace" ]]; then
    install_skills_into "${DEST}/.agents/skills"
    copy_file "${REPO_ROOT}/adapters/antigravity/${SUITE_ID}-bootstrap.md" "${DEST}/.agents/rules/${SUITE_ID}-bootstrap.md"
    upsert_agents_md "${DEST}"
  else
    install_skills_into "${DEST}/.gemini/config/skills"
    copy_file "${REPO_ROOT}/adapters/antigravity/${SUITE_ID}-bootstrap.md" "${DEST}/.gemini/config/rules/${SUITE_ID}-bootstrap.md"
  fi
}

install_deepseek() {
  local skills_dir="${DEST}/.agents/skills"
  install_skills_into "${skills_dir}"
  copy_file "${REPO_ROOT}/adapters/deepseek-harness/dsh-plugin.json" "${skills_dir}/${DIRECTOR_SLUG}/dsh-plugin.json"
  if [[ "${SCOPE}" == "workspace" ]]; then
    upsert_agents_md "${DEST}"
  fi
}

install_claude() {
  install_skills_into "${DEST}/.claude/skills"
  if [[ "${SCOPE}" == "workspace" ]]; then
    upsert_agents_md "${DEST}" ".claude/skills"
  fi
}

install_codex() {
  install_skills_into "${DEST}/.agents/skills"
  if [[ "${SCOPE}" == "workspace" ]]; then
    upsert_agents_md "${DEST}" ".agents/skills"
  fi
}

install_cursor() {
  install_skills_into "${DEST}/.cursor/skills"
  if [[ "${SCOPE}" == "workspace" ]]; then
    copy_file "${REPO_ROOT}/adapters/cursor/${SUITE_ID}-director.mdc" "${DEST}/.cursor/rules/${SUITE_ID}-director.mdc"
    upsert_agents_md "${DEST}" ".cursor/skills"
  fi
}

install_windsurf() {
  install_skills_into "${DEST}/.windsurf/skills"
  if [[ "${SCOPE}" == "workspace" ]]; then
    copy_file "${REPO_ROOT}/adapters/windsurf-devin/${SUITE_ID}-director.md" "${DEST}/.devin/rules/${SUITE_ID}-director.md"
    copy_file "${REPO_ROOT}/adapters/windsurf-devin/${SUITE_ID}-director.md" "${DEST}/.windsurf/rules/${SUITE_ID}-director.md"
    upsert_agents_md "${DEST}" ".windsurf/skills"
  fi
}

log "Starting ${REPO_NAME} installer (target=${TARGET}, mode=${MODE}, scope=${SCOPE}, dest=${DEST})"

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
