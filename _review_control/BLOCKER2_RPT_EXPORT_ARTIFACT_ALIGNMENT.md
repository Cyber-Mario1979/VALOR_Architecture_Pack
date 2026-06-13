# Blocker 2 — RPT / Export / Artifact Registry Alignment

Status: CLOSED FOR DECLARED RPT SCOPE — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-10
Review branch: review-spec-freeze-control

## Approved declared scope

RPT is a public/user-callable projection and publishing layer with three distinct artifact families:

1. `WORK_PACKAGE_STATUS_REPORT`
   - Narrative PDF-style report.
   - Canonical action: `RPT_GENERATE_STATUS_REPORT`.

2. `WORK_PACKAGE_WORKBOOK_EXPORT`
   - Technical Excel `.xlsx` workbook export.
   - Canonical action: `RPT_GENERATE_WORKBOOK_EXPORT`.
   - CSV is not the v1.0.1 freeze baseline.

3. `WORK_PACKAGE_GANTT_CHART`
   - Separate Excel-based Gantt artifact.
   - Canonical action: `RPT_GENERATE_GANTT_CHART`.
   - Gantt is not a workbook export tab in the freeze baseline.
   - Timeline uses full-cell coloring, not character bars inside cells.

Supported target scopes:

- `SINGLE_WP`
- `SELECTED_WP_SET`

Excluded from freeze scope:

- `ALL_WPS`

## Freeze rule applied

No partial or placeholder RPT/export alignment is acceptable. If an artifact remains declared, it must have contract action, request/result schema, artifact metadata, template/spec, target-scope rules, confirmation rule, and list/get behavior.

## Files modified or created in this blocker

Architecture and contracts:

- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Action blocks:

- `action_blocks/RPT_GENERATE_STATUS_REPORT.yaml`
- `action_blocks/RPT_VALIDATE_REPORT_INPUTS.yaml`
- `action_blocks/RPT_GENERATE_WORKBOOK_EXPORT.yaml`
- `action_blocks/RPT_VALIDATE_WORKBOOK_EXPORT.yaml`
- `action_blocks/RPT_GENERATE_GANTT_CHART.yaml`
- `action_blocks/RPT_VALIDATE_GANTT_INPUTS.yaml`
- `action_blocks/RPT_LIST_ARTIFACTS.yaml`
- `action_blocks/RPT_GET_ARTIFACT.yaml`
- `action_blocks/BUILD_REPORT.yaml`

Schemas:

- `schemas/objects/rpt_artifact_metadata_schema.json`
- `schemas/contracts/report_request.schema.json`
- `schemas/contracts/report_result.schema.json`
- `schemas/contracts/workbook_export_request.schema.json`
- `schemas/contracts/workbook_export_result.schema.json`
- `schemas/contracts/gantt_chart_request.schema.json`
- `schemas/contracts/gantt_chart_result.schema.json`
- `schemas/objects/workbook_export_schema.json`
- `schemas/objects/gantt_chart_schema.json`
- `schemas/contracts/export_result.schema.json`
- `schemas/objects/csv_export_schema.json`

Templates/specs:

- `templates/reports/WP_STATUS_REPORT_v1.0.1.md`
- `templates/export/WP_WORKBOOK_EXPORT_v1.0.1.yaml`
- `templates/export/WP_GANTT_CHART_v1.0.1.yaml`

## Decisions recorded

### B2-DEC-001 — Separate report, workbook export, and Gantt artifact

Decision: RPT now has three distinct declared artifact families: status report, workbook export, and Gantt chart.

Reason: User clarified that report is narrative/PDF-style, export is technical Excel workbook, and Gantt should be a separate visual artifact.

Impact: A04.6, RPT contract, registry, action blocks, schemas, and templates now distinguish these artifacts.

### B2-DEC-002 — Remove CSV as freeze baseline

Decision: CSV is not the v1.0.1 freeze baseline.

Reason: User clarified export should be Excel workbook. The uploaded workbook is a reference sample only, not canonical.

Impact: `csv_export_schema.json` is retained as legacy/reference material only and marked outside v1.0.1 freeze scope.

### B2-DEC-003 — Define target scope

Decision: RPT artifacts support `SINGLE_WP` and `SELECTED_WP_SET`; `ALL_WPS` is excluded from freeze scope.

Reason: Work-package artifacts must support one or chosen WPs without allowing uncontrolled all-WP generation.

Impact: Request schemas and architecture define target scope rules.

### B2-DEC-004 — Gantt is separate artifact

Decision: Gantt is not a workbook export tab in the freeze baseline.

Reason: User preferred a better Gantt form and approved separation as its own artifact.

Impact: Workbook export has Cover, WP Summary, Task Table, Statistics, Metadata. Gantt artifact has Gantt, Task Data, Metadata.

### B2-DEC-005 — Artifact registry/list/get behavior active

Decision: `RPT_LIST_ARTIFACTS` and `RPT_GET_ARTIFACT` are active for declared RPT artifact metadata/read behavior.

Reason: Declared artifacts require registry/read behavior before freeze.

Impact: Registry and action blocks now define list/get as read-only actions.

### B2-DEC-006 — BUILD_REPORT is alias only

Decision: `BUILD_REPORT` is retained as an alias/action-block label mapped to `RPT_GENERATE_STATUS_REPORT`.

Reason: Avoids legacy public command drift while preserving usability.

Impact: `BUILD_REPORT` is no longer a canonical action type.

## Known note

`RPT_VALIDATE_STAMPS` is active in `contracts/VALOR-contract-orch-rpt.yaml` and `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`. A separate `action_blocks/RPT_VALIDATE_STAMPS.yaml` file was attempted twice but blocked by the connector safety gate. It was not forced with a misleading workaround. This does not reopen the RPT/export blocker because the action is specified in contract and registry, and the separate stamp action block was not part of the approved mandatory edit list.

## Remaining freeze blockers after Blocker 2

- Full governed K&S standards bundle/content/schema/test coverage.
- Contract/schema validation enforcement, including contract registry schema and semantic catalog validator.
- DOC/DCF/URS source-chain cleanup.
- WP/Planning/governed library cleanup.
- Product surface minimum behavior cleanup.
- Negative and E2E test vector coverage.
- Manifest regeneration and final freeze-readiness check after all content edits.

## Blocker 2 done state

Blocker 2 is closed for the declared RPT/export/Gantt scope.

Freeze remains blocked by other pre-freeze work. No implementation, delivery plan, clean repo creation, or old ASBP audit was performed.
