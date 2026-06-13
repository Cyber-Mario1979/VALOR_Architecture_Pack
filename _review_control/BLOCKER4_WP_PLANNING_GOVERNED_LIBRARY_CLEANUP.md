# Blocker 4 — WP / Planning / Governed Library Cleanup

Status: COMPLETED FOR SCOPED ARCHITECTURE AND GOVERNED-LIBRARY ALIGNMENT — CONTRACT/REGISTRY VALIDATION REMAINS
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Approved scoped task

Align the WP / Planning / Governed Library architecture and governed library records for the declared v1.0.1 high-complexity process-equipment baseline.

## Scope files edited

Architecture:

- `docs/architecture/A04_2_WorkPackage_Arch_v1_0_1.md`
- `docs/architecture/A04_4_Planning_Arch_v1_0_1.md`
- `docs/architecture/A05_TaskPool_Arch_v1_0_1.md`
- `docs/architecture/A06_PresetSystem_Arch_v1_0_1.md`
- `docs/architecture/A07_CalendarLogic_Arch_v1_0_1.md`
- `docs/architecture/A08_ProfileLibrary_Arch_v1_0_1.md`

Governed libraries:

- `libraries/task_pool/TP-PE-HIGH_v1.0.1.yaml`
- `libraries/preset_library/PS-PE-HIGH_v1.0.1.yaml`
- `libraries/profile_library/PROF-PE-HIGH_v1.0.1.yaml`
- `libraries/calendar/CAL-WORKWEEK_v1.0.1.yaml`

Review-control:

- `_review_control/BLOCKER4_WP_PLANNING_GOVERNED_LIBRARY_CLEANUP.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`

## Decisions applied

### Calendar baseline

`libraries/calendar/CAL-WORKWEEK_v1.0.1.yaml` remains the architecture-pack file and now declares itself as a v1.0.1 governed wrapper around canonical `CAL-WORKWEEK v1`.

Applied canonical baseline:

- `calendar_id: CAL-WORKWEEK`
- `canonical_calendar_version: v1`
- `package_asset_version: v1.0.1`
- timezone: `UTC+02:00`
- working week: Sun-Thu
- weekend: Fri-Sat
- start date rule: `IF_NON_WORKING_START_NEXT_WORKING`
- end date rule: `END_INCLUSIVE`
- diff policy: `COUNT_WORKING_DAYS_BETWEEN`

No `libraries/calendar/CAL-WORKWEEK_v1.yaml` file was created.

### Preset identity and schema

`PS-PE-HIGH` remains the canonical preset ID.

`PS-PE-HIGH` now uses primary applicability fields:

- `equipment_domain: ProcessEquipment`
- `complexity: High`
- `scope: Project`

Existing tag/scope hints are retained only as optional matching hints.

### K&S binding in preset

`PS-PE-HIGH` now binds to `BND-CQV-BASE v1.0.1` as `TESTING_ONLY / PRODUCT_TESTING_ONLY`.

The binding does not approve real regulated CQV/GMP use. Regulated output remains blocked until user/site source metadata acceptance is complete.

### Profile model

`PROF-PE-HIGH` was converted from the ambiguous `keys` list model to the A08 `entries` map model.

All existing profile keys, values, units, and descriptions were preserved except for direct FAT-chain additions.

`calendar_policy` was removed from Profile ownership and replaced with `calendar_compatibility_ref` to `CAL-WORKWEEK v1.0.1` wrapper around canonical `v1`.

### Task type vs profile semantics

`task_type` remains aligned to WP/TP enum values:

- AUTHORING
- REVIEW
- APPROVAL
- EXECUTION
- REPORTING
- VENDOR_WAIT
- PROCUREMENT_WAIT
- LEAD_TIME

Non-enum duration meanings are now carried by `profile_task_semantic`.

### FAT chain

The high-complexity process-equipment path now includes the FAT chain:

```text
PEH-MFG-LEAD
→ PEH-FAT-SCHED
→ PEH-FAT-PREP
→ PEH-FAT-EXEC
→ PEH-FAT-REPORT
→ PEH-FAT-ACCEPTANCE
→ PEH-LOGISTICS
```

This addition stays within the existing high-complexity process-equipment path and does not add ERP/procurement integration, resource loading, evidence ingestion, or delivery planning.

### Governed lifecycle metadata

Local governed-library lifecycle/status/review/expiry metadata was added to TP, PS, PROF, and CAL.

This metadata is pre-freeze controlled library metadata only. It does not imply frozen, released, final, externally approved, or regulated-approved status.

### No-profile planning baseline

Planning now requires a governed profile unless every task has an explicit duration override and every override source is stamped.

No-profile planning is not normal freeze operation.

### Contract files

No contract files were edited in this blocker.

Contract/action registry semantic alignment remains a later dependency.

## Connector status

All scoped connector edits completed successfully.

No USER_APPLY_REQUIRED package was needed.

## Remaining dependencies / blockers

- Contract/action registry semantic validation for WP/PLAN/TP/PS/PROF/CAL naming and action catalogs.
- K&S user/site source metadata acceptance gate for real regulated CQV/GMP use.
- DOC/DCF/URS source-chain cleanup.
- Product surface minimum behavior cleanup.
- Negative and E2E test-vector coverage outside the scoped K&S vectors.
- Governance/audit/security/registry schemas/tests.
- Manifest regeneration and final freeze-readiness check after all content edits.

## Non-scope confirmation

No implementation work, delivery plan creation, clean implementation repository creation, old/current ASBP audit, DOC/DCF/URS work, product-surface work, contract edits, unrelated blocker expansion, or broad new governance layer was performed.
