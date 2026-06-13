# Blocker 8A — Non-K&S Core Schema and Root Test Vector Cleanup

Status: COMPLETED FOR SCOPED NON-K&S CORE SCHEMA AND ROOT TEST VECTOR CLEANUP — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scope

This blocker replaced placeholder/permissive non-K&S core schemas and stale root test vectors with minimum controlled pre-freeze schemas/vectors aligned to current architecture decisions.

## Files edited

Core contract/result schemas:

- `schemas/contracts/staged_task_set.schema.json`
- `schemas/contracts/plan_proposal.schema.json`
- `schemas/contracts/plan_validation_result.schema.json`
- `schemas/contracts/doc_draft_result.schema.json`
- `schemas/contracts/doc_artifact_result.schema.json`

Object schemas:

- `schemas/objects/work_package_schema.json`
- `schemas/objects/task_schema.json`
- `schemas/objects/document_metadata_schema.json`

Root test vectors:

- `test_vectors/seed_wp.json`
- `test_vectors/expected_staged_tasks.json`
- `test_vectors/expected_committed_wp.json`
- `test_vectors/expected_plan_proposal.json`
- `test_vectors/expected_doc_metadata.json`
- `test_vectors/expected_export.json`
- `test_vectors/expected_report_single_wp.json`
- `test_vectors/expected_report_multi_wp.json`

Validation example:

- `validation/examples/render_inputs_min.json`

## Decisions applied

- Replaced empty/permissive active public-action result schemas for staged task set, plan proposal, plan validation result, DOC draft result, and DOC artifact result.
- Added required state/result/provenance fields to the scoped schemas.
- Aligned WP/task schemas to current architecture naming: `wp_id`, `task_id`, `task_type`, `phase`, dependencies, status/state, duration refs, and provenance refs.
- Updated document metadata schema to require DOC source-chain fields, template/bundle/citation refs, provenance stamps, source input completion status, and testing-only status/stamp fields.
- Preserved DCF generation/finalization as inactive unless separately approved.
- Corrected root test vectors from old IDs/versions to current governed IDs:
  - `PS-PE-HIGH`
  - `TP-PE-HIGH`
  - `PROF-PE-HIGH`
  - `CAL-WORKWEEK v1.0.1` with canonical calendar version `v1`
  - `BND-CQV-BASE v1.0.1`
  - `TPL-URS v1.0.1`
  - `TPL-DCF v1.0.1` only where source-capture metadata is relevant
  - `STD-CQV-BASE v1.0.1`
- Aligned test vectors to current action names and states:
  - `WP_STAGE_TASKS`
  - `WP_COMMIT_STAGED_TASKS`
  - `PLAN_GENERATE_PROPOSAL`
  - `DOC_GENERATE_DRAFT`
  - `RPT_GENERATE_STATUS_REPORT`
  - `RPT_GENERATE_WORKBOOK_EXPORT`
  - `RPT_GENERATE_GANTT_CHART`
- Replaced old generic export vector behavior with declared RPT artifact-family baseline: status report, workbook export, and Gantt chart.
- Kept `ALL_WPS` out of scope and used only `SINGLE_WP` or `SELECTED_WP_SET`.
- Updated minimum render input example with current IDs, testing-only stamp, `TPL-URS`, `BND-CQV-BASE`, `STD-CQV-BASE`, and DCF/source input metadata only.

## Explicit non-scope / deferrals

- K&S schemas and K&S vectors were not edited.
- K&S was not promoted to regulated-active use.
- No real regulated CQV/GMP output was approved.
- Manifest was not regenerated.
- Full document render schema redesign was deferred.
- DCF render schemas and DCF artifact test vectors were not created.
- DCF generation/finalization was not activated.
- No artifacts were generated.
- No templates were imported or converted.
- No implementation, delivery planning, clean repo, or ASBP audit was started.
- No new public callable actions were added.
- Broad governance/security/registry schema work was deferred.
- Validator tooling rewrite was deferred.

## Review-only / preserved

- `schemas/contracts/contract_request.schema.json` was not edited.
- `schemas/contracts/contract_response.schema.json` was not edited.
- `schemas/contracts/export_result.schema.json` was not edited.
- `schemas/documents/*.schema.json` and `schemas/documents/index.json` were not edited.
- `validation/validate_render_inputs.py` was not edited.
- RPT request/result schemas and `schemas/objects/rpt_artifact_metadata_schema.json` were mostly preserved; root vectors were aligned to those schemas.

## Remaining blockers

- K&S user/site source metadata acceptance gate for real regulated CQV/GMP use.
- Broader contract/schema validation enforcement after this scoped cleanup.
- Negative and E2E test-vector coverage outside scoped K&S vectors.
- Governance/audit/security/registry schemas/tests.
- Manifest regeneration.
- Final freeze-readiness review.
