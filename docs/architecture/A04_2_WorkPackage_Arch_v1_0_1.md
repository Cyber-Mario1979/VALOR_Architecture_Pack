---
id: VALOR-block-A04-2-work-package-architecture
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
summary: "Block A04.2 — Work Package System Architecture: authoritative WP/task truth, lifecycle state machine, deterministic ID allocation, dependency integrity, provenance refs to governed libraries, and proposal-to-commit enforcement."
acceptance_criteria:
  - Defines authoritative WP and Task entities, required fields, and mutability rules.
  - Defines lifecycle state machine for WP and tasks.
  - Defines deterministic ID allocation with non-reuse and tombstoning.
  - Defines dependency model and validation.
  - Defines proposal vs commitment boundary with Planning.
  - Defines governed-library provenance references for preset, task pool, profile, calendar, and standards bundle.
  - Defines no-profile exception constraints.
---

# Work Package System Architecture

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Work Package (WP) System is Valor's single source of truth for:

- Work Package objects;
- Task objects;
- task IDs and WP IDs;
- task status and WP lifecycle state;
- committed task dates;
- dependency graph as instantiated into the WP;
- explicit duration overrides where accepted and stamped;
- provenance refs to governed library assets used to stage or plan the WP.

Any plan, report, or document is derived from WP truth. If it is not reflected in WP truth, it is not authoritative.

WP is not authoritative for:

- task-pool atomic task definitions;
- profile default duration values;
- calendar arithmetic rules;
- standards-bundle content;
- planning algorithm choices;
- generated document/report content.

## 2. Core Entities

### 2.1 Work Package

Required fields:

- wp_id;
- title;
- scope;
- wp_type;
- complexity;
- lifecycle_state;
- created_at_utc;
- updated_at_utc;
- owner_function.

Optional but governed refs:

- preset_ref: preset_id and preset_version;
- task_pool_ref: task_pool_id and task_pool_version;
- profile_ref: profile_id and profile_version;
- calendar_logic_ref: calendar_id, calendar_version, and canonical_calendar_version where wrapped;
- standards_bundle_ref: bundle_id, bundle_version, status, and usage classification;
- vendor_id;
- project_id;
- change_control_id.

WP stores these refs as provenance. WP does not own the governed library assets themselves.

### 2.2 Task

Required fields:

- task_id;
- wp_id;
- name;
- task_type;
- phase;
- status;
- dependencies;
- planned_duration_days or explicit duration_ref/override status;
- owner_role;
- created_at_utc;
- updated_at_utc.

Allowed task_type values:

- AUTHORING
- REVIEW
- APPROVAL
- EXECUTION
- REPORTING
- VENDOR_WAIT
- PROCUREMENT_WAIT
- LEAD_TIME

Date fields:

- proposed_start_date and proposed_end_date are advisory;
- committed_start_date and committed_end_date are authoritative once explicitly applied;
- actual_start_date and actual_end_date are execution evidence fields.

Planning may propose dates. WP commits dates only through an explicit apply/commit action with confirmation and provenance stamps.

### 2.3 Dependency Edge

Dependency edge fields:

- predecessor_task_id;
- successor_task_id;
- dependency_type;
- lag_days;
- notes.

Baseline v1.0.1 support is FS only unless later enabled by controlled update.

Dependency graph must be acyclic.

## 3. Lifecycle State Machine

WP states:

- WP_DRAFT;
- WP_STAGED;
- WP_COMMITTED;
- WP_IN_EXECUTION;
- WP_CLOSED.

Task states:

- TASK_STAGED;
- TASK_COMMITTED;
- TASK_IN_PROGRESS;
- TASK_DONE;
- TASK_BLOCKED;
- TASK_CANCELLED.

Allowed transitions must enforce staging before commit and prevent closure with unresolved required tasks unless explicitly cancelled with rationale.

## 4. Deterministic ID Allocation

IDs must be unique, deterministic, and non-reused.

If an item is cancelled or deleted, its ID is tombstoned.

Implementation must maintain an append-only ID ledger or equivalent invariant-preserving mechanism.

## 5. Mutability Rules

WP mutability:

- wp_id immutable;
- lifecycle_state transitions must follow the state machine;
- governed refs may be added or updated while not closed, subject to provenance rules;
- closed WPs restrict mutation.

Task mutability:

- task_id immutable;
- name/type/phase/owner may be edited before execution starts, subject to policy;
- dependencies may be edited before execution starts, subject to cycle validation;
- committed dates may be changed only through an explicit apply/update action and with justification after execution starts.

## 6. Governed Library Provenance

When tasks are staged or dates are applied, WP must retain the relevant governed library refs used:

- preset_id/version;
- task_pool_id/version;
- profile_id/version or explicit override source stamps;
- calendar_id/version and canonical calendar version where wrapped;
- standards_bundle_id/version/status/usage classification where applicable.

Missing required provenance must block the dependent commit/finalization/export path.

## 7. No-Profile Exception

Normal planning uses a governed profile.

A WP may support no-profile planning only when every task has an explicit duration override and every override includes a stamped source/provenance record.

If any task lacks both a governed profile-derived duration and a stamped explicit override, planning must refuse.

No-profile planning is not normal freeze operation.

## 8. Planning Apply Boundary

Planning outputs are `PROPOSED` only.

The apply sequence is:

1. Planning returns a proposed schedule.
2. Orchestration presents it to the user.
3. User confirms apply.
4. WP writes committed_start_date and committed_end_date.
5. WP stores provenance stamps for the applied proposal.

If the WP apply call fails, Orchestration must not claim success.

## 9. FAT Chain Awareness

For high-complexity process equipment WPs staged from `TP-PE-HIGH`, WP must be able to store the full FAT path as normal task instances:

```text
PEH-MFG-LEAD
→ PEH-FAT-SCHED
→ PEH-FAT-PREP
→ PEH-FAT-EXEC
→ PEH-FAT-REPORT
→ PEH-FAT-ACCEPTANCE
→ PEH-LOGISTICS
```

This is task/dependency truth only. It does not create ERP integration, resource loading, execution evidence ingestion, or delivery planning.

## 10. Validation and Error Semantics

WP validation must enforce:

- required fields;
- legal lifecycle transitions;
- acyclic dependency graph;
- supported dependency types;
- non-reused IDs;
- mutability restrictions;
- required provenance refs;
- proposal vs commitment boundary.

Standard codes:

- VALIDATION_ERROR;
- INVARIANT_VIOLATION;
- MODE_VIOLATION;
- NOT_FOUND;
- CONFLICT;
- UNSUPPORTED_OPERATION;
- INTERNAL_ERROR.

WP-specific subcodes:

- STAGING_REQUIRED
- CYCLE_DETECTED
- ILLEGAL_STATE_TRANSITION
- MUTABILITY_RESTRICTED
- DUPLICATE_TASK
- MISSING_REQUIRED_FIELD
- PROVENANCE_STAMP_MISSING
- NO_PROFILE_DURATION_SOURCE_MISSING

## 11. Integration Points

- Orchestration uses WP actions for truth mutations and gating.
- Preset resolution supplies governed refs and rule decisions for staging.
- Task Pool supplies atomic task definitions and default wiring.
- Profile supplies governed duration defaults.
- Calendar supplies date arithmetic.
- Planning returns proposed schedules only.
- Document Factory and Reporting read WP truth and provenance; they do not mutate WP truth.

## 12. Contract Alignment Dependency

WP contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: clarified governed-library provenance refs, planning apply boundary, no-profile exception, FAT-chain task storage, and local pre-freeze status alignment | Pre-freeze controlled update |
