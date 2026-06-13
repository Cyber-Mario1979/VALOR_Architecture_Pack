# Blocker 7A — Product Surface Terminology and Stale Addenda Cleanup

Status: COMPLETED FOR SCOPED ARCHITECTURE / ADDENDA / README WORDING ALIGNMENT — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scope

This blocker aligned product-surface terminology across architecture, addenda, README, and review-control wording only.

## Files edited

- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`
- `docs/architecture/A04_4_Planning_Arch_v1_0_1.md`
- `docs/architecture/A04_5_DocumentFactory_Arch_v1_0_1.md`
- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `docs/architecture/A13_Architecture_Closure_Checklist_Arch_v1_0_1.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Canvas_Rendering_Record_Layout_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Document_Generation_Compliance_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Planning_Invariants_UX_Contract_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Reporting_Export_Projection_Contract_v1.0.1A.md`
- `README.md`

## Decisions applied

- Defined canonical product-surface states:
  - `STAGED`
  - `PROPOSED`
  - `COMMITTED`
  - `DRAFT`
  - `FINAL`
  - `INCOMPLETE`
  - `BLOCKED`
  - `PRODUCT_TESTING_ONLY`
- Removed Canvas as a runtime/truth requirement.
- Normalized wording to record/output/artifact view terminology.
- Preserved useful layout and product-surface behavior rules only where they do not imply UI implementation.
- Normalized timestamp rule:
  - contract/audit/provenance metadata uses UTC;
  - optional local display time must be explicitly labeled;
  - Africa/Cairo does not replace canonical UTC metadata.
- Normalized RPT product surface:
  - status report, workbook export, and Gantt chart are baseline;
  - CSV is not v1.0.1 freeze baseline;
  - ALL_WPS remains out of scope/refused unless bounded;
  - RPT outputs are generated projection artifacts and must not mutate WP/task truth.
- Normalized DOC / DCF / URS product surface:
  - DOC DRAFT / FINAL / INCOMPLETE / BLOCKED behavior;
  - DCF governance exists as PRODUCT_TESTING_ONLY metadata;
  - DCF artifact generation/finalization remains inactive;
  - testing-only document outputs require the visible product-testing stamp;
  - DOC must not invent missing source data.
- Normalized PLAN / WP product surface:
  - `PLAN_GENERATE_PROPOSAL` returns `PROPOSED`;
  - preview behavior is `PLAN_GENERATE_PROPOSAL` with `dry_run=true`;
  - `WP_APPLY_PLAN_PROPOSAL` is required for committed dates;
  - plan/apply in one request stops before apply confirmation;
  - proposed dates must not be presented as committed.
- Fixed A13 stale action names:
  - `PS_RESOLVE_PRESET`
  - `WP_BIND_PRESET_CONTEXT`
  - `WP_STAGE_TASKS`
  - `WP_COMMIT_STAGED_TASKS`
  - `PLAN_GENERATE_PROPOSAL`
  - `WP_APPLY_PLAN_PROPOSAL`
  - `DOC_GENERATE_DRAFT`
  - `RPT_GENERATE_STATUS_REPORT`
  - `RPT_GENERATE_WORKBOOK_EXPORT`
  - `RPT_GENERATE_GANTT_CHART`
- Updated README to state controlled pre-freeze review and NO-FREEZE YET.

## Explicit deferrals

- No contract edits were made.
- No schema/test-vector hardening was performed.
- Manifest was not regenerated.
- No UI wireframes or pixel design were created.
- No implementation, delivery planning, clean repo, or ASBP audit was started.
- No K&S asset was promoted to ACTIVE or regulated-ready use.
- No new public callable actions were added.
- DCF generation/finalization was not activated.
- No DOC/RPT/DCF/URS artifacts were generated.
- No template import or conversion was performed.
- No broad governance rewrite was performed.

## Remaining blockers

- K&S user/site source metadata acceptance gate for real regulated CQV/GMP use.
- Broader contract/schema validation enforcement and non-K&S validation/test-vector cleanup.
- Negative and E2E test vector coverage outside scoped K&S vectors.
- Governance/audit/security/registry schemas/tests.
- Manifest regeneration.
- Final freeze-readiness review.
