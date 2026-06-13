---
id: VALOR-block-A04-6-reporting-export-architecture
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: pre_freeze_controlled
date: 2026-06-12
dependencies:
  - VALOR-block-A00-specs-architecture-pack
  - VALOR-block-A01-sos-context-capability
  - VALOR-block-A02-principles-invariants
  - VALOR-block-A03-subsystems-authority
  - VALOR-block-A04-2-work-package-architecture
summary: "Block A04.6 — Reporting & Export System Architecture: projection layer that generates narrative status reports, technical workbook exports, and separate Gantt artifacts from WP truth without mutating authoritative data."
acceptance_criteria:
  - Defines Reporting/Export as projection-only with no mutation authority.
  - Separates narrative report, workbook export, and Gantt chart artifact types.
  - Defines supported target scopes: SINGLE_WP and SELECTED_WP_SET; ALL_WPS is outside freeze scope.
  - Defines traceability stamping, artifact metadata, list/get behavior, and schema/template references.
  - Defines contract actions, response envelopes, confirmation rules, and error semantics.
  - Defines product-surface behavior for RPT baseline artifacts and refusal of non-baseline CSV/ALL_WPS behavior.
  - Defines reproducibility/determinism requirements for all declared RPT artifacts.
---

# Reporting & Export System Architecture

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

Reporting & Export (RPT) is Valor’s projection and publishing layer for three distinct artifact families:

1. **Narrative status reports** — human-readable report artifacts intended for PDF-style output.
2. **Workbook exports** — structured Excel `.xlsx` technical workbooks for task/status/statistics review.
3. **Gantt chart artifacts** — separate Excel-based visual schedule artifacts with full-cell timeline coloring.

RPT is authoritative for:

- report/export/Gantt artifact content and formatting;
- computed metrics derived from WP truth with declared rules;
- artifact metadata, stamps, and provenance for generated outputs;
- artifact registry/list/get behavior for declared RPT artifacts.

RPT is not authoritative for:

- WP/task truth;
- schedule truth;
- Planning proposal truth;
- standards/templates beyond referencing governed IDs/versions.

RPT must never correct, overwrite, infer, or silently mutate WP/task truth. All RPT outputs are projection-only.

Invariant alignment:

- Projection-only (A02 INV-09)
- Mandatory stamps for regulated outputs (A02 INV-07)
- Proposed-vs-committed separation

---

## 2. Declared Freeze Scope

### 2.1 Supported Target Scopes

Declared freeze scope supports:

- `SINGLE_WP` — one selected work package.
- `SELECTED_WP_SET` — explicitly selected work packages.

Out of freeze scope:

- `ALL_WPS`

`ALL_WPS` must not be treated as normal freeze-ready behavior. If requested, Orchestration must ask the user to select a bounded WP set or refuse in strict mode.

### 2.2 Declared Artifact Types

| Artifact Type | Product Label | Canonical Generation Action | Output Intent |
| --- | --- | --- | --- |
| `WORK_PACKAGE_STATUS_REPORT` | Work Package Status Report | `RPT_GENERATE_STATUS_REPORT` | PDF-style narrative report |
| `WORK_PACKAGE_WORKBOOK_EXPORT` | Work Package Workbook Export | `RPT_GENERATE_WORKBOOK_EXPORT` | Excel `.xlsx` workbook |
| `WORK_PACKAGE_GANTT_CHART` | Work Package Gantt Chart | `RPT_GENERATE_GANTT_CHART` | Excel-based Gantt artifact |

CSV is not the v1.0.1 freeze baseline for RPT/export. Any request for CSV export must be treated as outside the declared baseline unless later enabled by controlled update.

### 2.3 Product Surface Behavior

- RPT outputs are generated artifacts/projections, not WP/task truth.
- RPT must not mutate WP/task truth, plan proposals, owners, dates, statuses, IDs, or source-data state.
- Product surface must present status report, workbook export, and Gantt chart as distinct artifact choices.
- `SINGLE_WP` and `SELECTED_WP_SET` are supported; `ALL_WPS` must be refused or bounded by explicit selected WPs.
- Proposed schedule data must be labeled separately from committed WP date truth.
- Contract/audit/provenance metadata timestamps use UTC. Optional local display time may be shown only when explicitly labeled as display/local time.

---

## 3. Canonical Inputs

RPT consumes only controlled projections of authoritative data:

- WP snapshot(s) from WP contract read behavior;
- task rows, statuses, owners, dates, dependencies, and metadata contained in the snapshot(s);
- optional Planning proposal references when proposed schedule data is displayed;
- session traceability context and stamps;
- template/spec IDs and versions;
- target scope and selected `wp_ids`.

All artifact requests must include:

- `artifact_type`;
- `target_scope` (`SINGLE_WP` or `SELECTED_WP_SET`);
- `wp_ids`;
- `source_snapshot_refs` or `source_snapshot_hash`;
- `generated_at_utc`;
- `stamps`;
- `validation_mode` set to `STRICT` for freeze baseline.

---

## 4. Shared Artifact Metadata

Every generated RPT artifact must include an artifact metadata record containing:

- `artifact_id`;
- `artifact_type`;
- `artifact_label`;
- `target_scope`;
- `wp_ids`;
- `source_snapshot_hash`;
- `template_id`;
- `template_version`;
- `contract_id`;
- `contract_version`;
- `action_type`;
- `generated_at_utc`;
- `projection_only` = true;
- `mutates_wp_truth` = false;
- `stamps`;
- `validation_result`;
- `content_ref`.

Artifact metadata is required for list/get behavior even if the generated content is stored or rendered by a later implementation.

---

## 5. Work Package Status Report

`WORK_PACKAGE_STATUS_REPORT` is a narrative report for human review. It is intended to become a PDF-style controlled artifact.

It is not a workbook export.

Template ID:

- `TPL-RPT-WP-STATUS-REPORT-v1.0.1`

Template source:

- `templates/reports/WP_STATUS_REPORT_v1.0.1.md`

Required sections:

1. Cover Page
2. Executive Summary
3. Work Package Overview
4. Task Status Summary
5. Schedule Summary
6. Risks / Issues / Exceptions
7. Traceability and Governance
8. Recommendations / Next Actions
9. Appendix

For `SELECTED_WP_SET`, the report must include a consolidated executive summary, cross-WP summary table, individual WP sections or subsections, consolidated risks/issues/next actions, and per-WP source snapshot references or hashes.

---

## 6. Work Package Workbook Export

`WORK_PACKAGE_WORKBOOK_EXPORT` is a technical structured workbook for review, filtering, analysis, and downstream planning support.

It is not a narrative report.

The declared freeze baseline is Excel `.xlsx`.

Workbook template/spec ID:

- `TPL-RPT-WP-WORKBOOK-EXPORT-v1.0.1`

Workbook template/spec source:

- `templates/export/WP_WORKBOOK_EXPORT_v1.0.1.yaml`

The canonical workbook export contains exactly these required sheets in this order:

1. `Cover`
2. `WP Summary`
3. `Task Table`
4. `Statistics`
5. `Metadata`

The Gantt chart is not a tab in the workbook export freeze baseline. It is a separate artifact.

For `SELECTED_WP_SET`, task-level and metric-level sheets must include `wp_id` and `wp_title` so the source WP remains explicit.

---

## 7. Work Package Gantt Chart Artifact

`WORK_PACKAGE_GANTT_CHART` is a separate visual schedule artifact derived from WP task schedule data.

It is not part of the core workbook export.

The declared freeze baseline is an Excel-based Gantt artifact.

Gantt template/spec ID:

- `TPL-RPT-WP-GANTT-CHART-v1.0.1`

Gantt template/spec source:

- `templates/export/WP_GANTT_CHART_v1.0.1.yaml`

The Gantt artifact contains:

1. `Gantt`
2. `Task Data`
3. `Metadata`

The Gantt timeline must use full-cell coloring across the timeline area.

Character or symbol bars inside cells are not the baseline visual rule.

For `SELECTED_WP_SET`, the Gantt must group rows by WP. If the selected WP set cannot be rendered readably in strict mode, generation must refuse with a validation error rather than produce a misleading chart.

---

## 8. Traceability Stamping

### 8.1 Required Stamp Set

Every declared RPT artifact must include, where applicable:

- architecture_pack_id/version;
- contract_id/version;
- template_id/version;
- preset_id/version if preset-driven;
- profile_id/version if profile-based planning or metrics are used;
- task_pool_id/version if task pool data is represented;
- calendar_id/version or calendar_logic_version if date/schedule metrics are used;
- standards_bundle_id/version if standards are referenced;
- planning_logic_version or plan_proposal_id/version if proposed schedule data is displayed.

If a required stamp is missing for the requested artifact, strict mode must refuse generation with `INVARIANT_VIOLATION / MISSING_TRACEABILITY_STAMPS`.

### 8.2 Proposed-vs-Committed Separation

Reports, workbook exports, and Gantt artifacts must label proposed schedule data separately from committed WP date truth.

RPT must never present proposed data as committed truth.

---

## 9. Contract Actions

RPT is invoked via `VALOR-contract-orch-rpt`.

### 9.1 Generate Actions

- `RPT_GENERATE_STATUS_REPORT`
- `RPT_GENERATE_WORKBOOK_EXPORT`
- `RPT_GENERATE_GANTT_CHART`

### 9.2 Validate Actions

- `RPT_VALIDATE_REPORT_INPUTS`
- `RPT_VALIDATE_WORKBOOK_EXPORT`
- `RPT_VALIDATE_GANTT_INPUTS`
- `RPT_VALIDATE_STAMPS`

### 9.3 Artifact Registry Actions

- `RPT_LIST_ARTIFACTS`
- `RPT_GET_ARTIFACT`

### 9.4 Confirmation Rules

- Read/list/get/validate actions do not require user confirmation.
- Report generation does not mutate truth and does not require truth-change confirmation.
- Workbook export generation is a generated artifact and requires explicit generation confirmation.
- Gantt chart generation is a generated artifact and requires explicit generation confirmation.
- No RPT action may mutate WP/task truth.

---

## 10. Artifact Registry / Read Behavior

RPT must define list/get behavior for every declared artifact type.

`RPT_LIST_ARTIFACTS` returns artifact metadata records filtered by:

- `artifact_type`;
- `wp_id` / `wp_ids`;
- `target_scope`;
- generation date range;
- action_type.

`RPT_GET_ARTIFACT` returns:

- artifact metadata;
- validation result;
- content reference;
- optional content if requested and available.

List/get behavior must not require artifact regeneration.

---

## 11. Metrics Computation Policy

RPT computes metrics strictly from WP snapshots and declared rules:

- total tasks;
- tasks by status;
- overdue tasks;
- missing owner/date counts;
- earliest start;
- latest finish;
- elapsed/remaining/lateness values where computable;
- proposed-vs-committed schedule variance where both are present.

If calendar-aware working-day calculations are used, the output must record the calendar version. If the calendar is missing in strict mode, RPT must refuse calendar-based metrics rather than silently compute using an unknown basis.

---

## 12. Error Semantics

Standard codes:

- VALIDATION_ERROR
- INVARIANT_VIOLATION
- MODE_VIOLATION
- NOT_FOUND
- CONFLICT
- UNSUPPORTED_OPERATION
- INTERNAL_ERROR

RPT-specific subcodes:

- MISSING_TRACEABILITY_STAMPS
- TARGET_SCOPE_UNSUPPORTED
- WP_SNAPSHOT_MISSING
- SOURCE_SNAPSHOT_HASH_MISSING
- ARTIFACT_NOT_FOUND
- REPORT_TEMPLATE_MISSING
- WORKBOOK_TEMPLATE_MISSING
- GANTT_TEMPLATE_MISSING
- REQUIRED_SHEET_MISSING
- REQUIRED_COLUMN_MISSING
- GANTT_DATES_MISSING
- GANTT_FINISH_BEFORE_START
- GANTT_SELECTED_SET_UNREADABLE
- FORMAT_NOT_SUPPORTED
- ATTEMPTED_TRUTH_MUTATION

---

## 13. Determinism and Reproducibility

Given the same:

- artifact type;
- target scope;
- selected WP snapshot hash(es);
- template/spec version;
- stamps;
- options;

RPT must produce the same artifact structure and metadata.

If any controlled input changes, the artifact metadata must identify a new source snapshot hash and, where applicable, a new artifact identity.

---

## 14. Integration Points

- Orchestration gates RPT artifact generation using target scope, stamps, and confirmation rules.
- WP provides authoritative snapshots.
- Planning may provide plan proposals, but RPT must label proposed data separately.
- K&S may be referenced by ID/version if standards appear in reports.
- Product surface must present report, workbook export, and Gantt as distinct artifact choices.

---

---

## CHANGELOG
| Date       | Changes     | Type / Version |
| ---------- | ----------- | -------------- |
| 2026-06-12 | Blocker 7A RPT product-surface wording: baseline report/workbook/Gantt artifacts, no CSV baseline, ALL_WPS refusal/bounding, and projection-only behavior clarified | Pre-freeze controlled update |
| 2026-06-10 | Pre-freeze RPT/export blocker: separated narrative report, workbook export, and Gantt chart artifact scope; removed CSV as freeze baseline; added target-scope and artifact registry behavior | Arch_v1.0.1-control |
| 2025-12-23 | First Issue | Arch_v1.0.1    |
