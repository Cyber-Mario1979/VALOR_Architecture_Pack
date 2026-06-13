---
id: VALOR-block-A04-4-planning-architecture
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
  - VALOR-block-A05-task-pool-architecture
  - VALOR-block-A07-calendar-logic-architecture
  - VALOR-block-A08-profile-library-architecture
summary: "Block A04.4 — Planning System Architecture (Advisory): proposal-only schedule generation from WP truth, governed profiles, and governed calendar logic; never commits truth and requires governed provenance stamps."
acceptance_criteria:
  - Defines Planning's advisory-only authority and non-ownership constraints.
  - Defines profile-required baseline and stamped no-profile exception.
  - Defines planning inputs/outputs with governed version stamps.
  - Defines scheduling model using dependency graph, profile units, and calendar logic.
  - Defines proposal vs commitment boundary.
  - Defines product-surface behavior for proposal, preview, and apply-confirmation boundaries.
  - Defines resource assignment as advisory only.
  - Records contract/action registry alignment as later dependency.
---

# Planning System Architecture (Advisory)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Planning System produces proposed schedules for a Work Package by combining:

- WP truth: tasks, statuses, dependencies, constraints, and explicit overrides;
- governed profile data: durations, lead times, and units;
- governed calendar logic: working days, weekends, holidays, arithmetic policy;
- optional resource availability hints.

Planning is advisory:

- it does not mutate WP truth;
- it does not allocate authoritative resource capacity;
- it does not commit dates;
- it produces `PROPOSED` plan outputs only;
- committed dates require explicit apply through WP authority.

This implements proposal vs commitment separation and subsystem authority separation.

## 2. Planning Owns / Does Not Own

Planning is authoritative for:

- schedule computation rules;
- plan proposal object structure;
- scheduling validation results;
- planning provenance stamps.

Planning is not authoritative for:

- WP/task truth;
- committed task dates;
- task-pool definitions;
- profile values;
- calendar rules;
- standards approval state;
- final regulated output state.

## 3. Required Inputs

Planning must be invoked with explicit versioned inputs.

Required inputs:

- wp_id;
- task snapshot from WP truth;
- dependency graph;
- profile_ref unless the no-profile exception is fully satisfied;
- calendar_logic_ref;
- planning policy options;
- provenance stamps from preset/task pool/profile/calendar where applicable.

If any required input is missing, Planning must refuse.

## 4. No-Profile Baseline

Normal freeze operation requires a governed profile.

No-profile planning is allowed only when every task has an explicit duration override and each override includes a stamped source/provenance record.

A valid explicit duration override must include:

- task_id;
- duration value;
- duration unit;
- source type;
- source reference or rationale;
- recorded_by or accepted_by where applicable;
- timestamp/date;
- override status.

If any task lacks both a resolvable profile entry and a valid explicit stamped override, Planning must return `VALIDATION_ERROR / MISSING_DURATION`.

No-profile planning is not normal freeze operation and must be clearly stamped when used.

## 5. Duration Resolution

Duration source precedence:

1. explicit task planned_duration override from WP truth, if present and stamped;
2. governed profile entry resolved from profile_ref, profile_key, and selection_context;
3. otherwise refuse.

Atomic tasks reference profile entries through `duration_ref.profile_key`.

Profile selectors must keep `task_type` aligned to the WP/TP enum. Profile-specific meaning is carried by `profile_task_semantic`.

## 6. Unit Handling

Planning must respect the profile unit policy.

- `WORKING_DAYS` durations use Calendar Logic arithmetic.
- `CALENDAR_DAYS` durations use calendar-day arithmetic and must be labeled as calendar days.
- `CALENDAR_WEEKS` and `CALENDAR_MONTHS` may be used only when explicitly declared in the profile entry.
- No implicit conversion from calendar months to working days is allowed.
- Any conversion rule must be explicitly approved, versioned, and stamped.

If a requested plan requires an unsupported unit conversion, Planning must return `UNSUPPORTED_OPERATION / UNIT_CONVERSION_NOT_APPROVED` or equivalent validation error.

## 7. Calendar Baseline

The v1.0.1 baseline calendar asset is `CAL-WORKWEEK_v1.0.1.yaml`, a governed architecture-pack wrapper around canonical `CAL-WORKWEEK v1`.

The baseline calendar rules are:

- timezone: `UTC+02:00`;
- working week: Sunday through Thursday;
- weekend: Friday and Saturday;
- start_date_rule: `IF_NON_WORKING_START_NEXT_WORKING`;
- end_date_rule: `END_INCLUSIVE`;
- diff_policy: `COUNT_WORKING_DAYS_BETWEEN`.

Planning must not treat `Africa/Cairo` as the canonical timezone unless accepted in a later controlled patch.

## 8. Scheduling Model

Baseline dependency support:

- FS only;
- lag_days >= 0;
- cycles refused;
- unsupported dependency types refused unless later explicitly enabled.

For each successor:

- earliest_start is derived from predecessor finish plus lag;
- non-working starts are deferred according to calendar policy;
- locked dates must satisfy constraints or return `CONFLICT`.

Milestones may be represented as duration-zero tasks or named markers. Milestones must appear in plan outputs where present in the task set.

## 9. FAT Chain Scheduling

For high-complexity process equipment, Planning must support the declared FAT chain from the task pool:

```text
PEH-MFG-LEAD
→ PEH-FAT-SCHED
→ PEH-FAT-PREP
→ PEH-FAT-EXEC
→ PEH-FAT-REPORT
→ PEH-FAT-ACCEPTANCE
→ PEH-LOGISTICS
```

This scheduling support is limited to task sequencing and duration handling. It does not add ERP/procurement integration, resource loading, evidence ingestion, or delivery planning.

## 10. Plan Proposal Object

Planning returns a plan proposal with:

- plan_id;
- wp_id;
- state: `PROPOSED`;
- apply_required: true;
- computed task schedule;
- proposed_start_date and proposed_end_date;
- duration source per task;
- duration unit per task;
- calendar metadata used;
- milestone dates;
- resource hints if provided;
- validation summary;
- provenance stamps.

## 11. Mandatory Provenance Stamps

Planning outputs must include:

- preset_id/version where preset-driven;
- task_pool_id/version where task-pool-driven;
- profile_id/version or explicit no-profile override stamp set;
- calendar_id/version;
- canonical calendar version where wrapped;
- planning_logic_version;
- contract_id/version used for call;
- standards_bundle_id/version/status where relevant to downstream use.

If required stamps are missing, Planning must return `VALIDATION_ERROR / STAMPS_MISSING`.

## 12. Proposal to Commitment Boundary

Planning never writes committed dates.

To make dates authoritative:

1. Planning returns a `PROPOSED` schedule.
2. Orchestration presents proposal to the user.
3. User confirms apply.
4. Orchestration calls WP authority through `WP_APPLY_PLAN_PROPOSAL` to write committed_start_date and committed_end_date.
5. WP stores committed dates and provenance stamps.

If the apply call fails, Orchestration must not claim success.

### 12.1 Product Surface Behavior

- `PLAN_GENERATE_PROPOSAL` always returns a `PROPOSED` schedule.
- Preview behavior is represented by `PLAN_GENERATE_PROPOSAL` with `options.dry_run=true`; no separate `PLAN_PREVIEW` action is active.
- Proposed dates must not be displayed as committed dates.
- A user request to plan and apply in one step must stop before the apply mutation and require explicit confirmation.
- `WP_APPLY_PLAN_PROPOSAL` is the required path for committed dates.
- Contract/audit/provenance timestamps remain UTC. Optional local display time may be shown only when explicitly labeled as display/local time.

## 13. Resource Assignment

Resource assignment is advisory in v1.0.1.

Planning may propose role-level hints, but it does not authoritatively allocate resource capacity.

If resource constraints are provided and infeasible, Planning returns warning or `CONFLICT` depending on strictness policy.

## 14. Error Semantics

Standard codes:

- VALIDATION_ERROR: missing durations, missing stamps, invalid dates, invalid options;
- INVARIANT_VIOLATION: dependency cycles, negative lag, attempt to commit truth;
- MODE_VIOLATION: planning invoked in wrong mode;
- NOT_FOUND: unknown profile/calendar reference;
- CONFLICT: locked date infeasible, ambiguous version, incompatible constraints;
- UNSUPPORTED_OPERATION: unsupported dependency type, unsupported strategy, unsupported unit conversion;
- INTERNAL_ERROR: unexpected.

Planning-specific subcodes:

- MISSING_DURATION
- CALENDAR_LOGIC_MISSING
- CALENDAR_VERSION_UNSUPPORTED
- CYCLE_DETECTED
- LOCKED_DATE_INFEASIBLE
- STAMPS_MISSING
- DEPENDENCY_TYPE_UNSUPPORTED
- UNIT_CONVERSION_NOT_APPROVED
- PROFILE_EXPIRED
- CALENDAR_EXPIRED

## 15. Determinism and Reproducibility

Planning results must be reproducible given:

- same task snapshot;
- same dependency graph;
- same profile/calendar versions;
- same explicit override stamps;
- same planning policy options.

If any input changes, a new plan_id must be generated.

## 16. Contract Alignment Dependency

Planning contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: clarified profile-required baseline, stamped no-profile exception, canonical CAL-WORKWEEK wrapper use, mixed-unit handling, FAT chain scheduling, and proposal-only boundary | Pre-freeze controlled update |
| 2026-06-12 | Blocker 7A product-surface wording: explicit PROPOSED/preview/apply-confirmation behavior and timestamp display boundary | Pre-freeze controlled update |
