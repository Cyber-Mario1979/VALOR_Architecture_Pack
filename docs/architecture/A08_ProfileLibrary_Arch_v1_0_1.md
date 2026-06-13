---
id: VALOR-block-A08-profile-library-architecture
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
  - VALOR-block-A05-task-pool-architecture
  - VALOR-block-A07-calendar-logic-architecture
summary: "Block A08 — Profile Library Architecture: governed duration/lead-time matrices keyed by task semantics and context, using entries map model, enum-aligned task_type, separate profile_task_semantic, and explicit unit policy."
acceptance_criteria:
  - Defines Profile Library as authoritative governed data for durations and lead times, not calendar rules.
  - Defines profile entity schema using canonical entries map.
  - Defines duration key mapping between atomic tasks and profile entries.
  - Separates WP/TP task_type enum from profile_task_semantic.
  - Defines governance/change control and versioning policy for profile updates.
  - Defines error semantics for missing keys, incompatible units, and context conflicts.
---

# Profile Library Architecture (Durations + Lead Times Matrices)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Profile Library (PROF) is a governed, versioned store of planning data:

- default task durations for authoring, review, approval, execution, reporting, and waits;
- vendor wait times;
- procurement cycle assumptions;
- equipment manufacturing lead times;
- logistics lead times;
- FAT preparation, execution, report, and acceptance durations for the declared high-complexity process-equipment baseline.

PROF is authoritative for:

- default duration and lead-time values;
- duration units;
- the dimensional model used to select values;
- profile key definitions;
- deterministic profile value selection.

PROF is not authoritative for:

- WP/task truth values explicitly set by users;
- calendar rules or working-day arithmetic;
- scheduling algorithm choices;
- approvals or release decisions.

Calendar rules are owned by Calendar Logic. A profile may reference compatible calendar assets but must not define the calendar rules itself.

## 2. Canonical v1.0.1 Profile Asset

The declared profile asset for this blocker is:

- `libraries/profile_library/PROF-PE-HIGH_v1.0.1.yaml`
- profile_id: `PROF-PE-HIGH`
- version: `v1.0.1`
- scope: ProcessEquipment / High / Project
- vendor_model: Intercontinental
- compatible calendar: `CAL-WORKWEEK v1.0.1` wrapper around canonical `CAL-WORKWEEK v1`

## 3. Profile Entity Schema

A profile record must include:

- profile_id;
- version;
- revision_date;
- status;
- usage_classification;
- effective_date;
- source_checked_date;
- review_cycle_months;
- next_review_due;
- expiry_date;
- review_required;
- expired_behavior;
- name;
- description;
- applicability;
- calendar_compatibility_ref;
- unit_policy;
- selector_policy;
- entries.

The governed lifecycle metadata is local governed-library metadata only. It does not mean the profile is frozen, final, released, externally approved, or regulated-approved.

## 4. Entries Map Model

The canonical profile structure is an `entries` map:

```yaml
entries:
  URS_AUTHORING_DUR:
    description: URS drafting/authoring duration.
    selection_priority: 0
    value_table:
      - context_selector:
          phase: URS
          task_type: AUTHORING
          profile_task_semantic: AUTHORING
        value: 10
        unit: WORKING_DAYS
```

`keys` is not the canonical v1.0.1 profile structure. If legacy profile files contain `keys`, they must be normalized to `entries` before freeze.

Each entry key is stable. Meaning changes require a profile version change, not silent key redefinition.

## 5. Task Type and Profile Semantics

`task_type` must remain aligned to the WP/TP task_type enum:

- AUTHORING
- REVIEW
- APPROVAL
- EXECUTION
- REPORTING
- VENDOR_WAIT
- PROCUREMENT_WAIT
- LEAD_TIME

Non-enum duration meaning must be carried by a separate semantic field such as `profile_task_semantic`.

Examples:

| Profile meaning | task_type | profile_task_semantic |
| --- | --- | --- |
| cycle package | AUTHORING | CYCLE |
| finalization | AUTHORING | FINALIZE |
| protocol authoring | AUTHORING | PROTOCOL_AUTHORING |
| vendor scheduling | VENDOR_WAIT | SCHEDULING |
| delivery lead time | LEAD_TIME | DELIVERY |
| manufacturing lead time | LEAD_TIME | MANUFACTURING_LEADTIME |
| report closure | REPORTING | REPORT |
| vendor coordination block | VENDOR_WAIT | VENDOR_COORDINATION_BLOCK |

This prevents profile-specific labels from contaminating the WP/TP task_type enum.

## 6. Duration Key Mapping

Atomic tasks reference profile entries through `duration_ref.profile_key`.

This is the controlled bridge:

- Task Pool defines which tasks exist.
- Profile defines how long they typically take.
- Planning resolves duration values using the profile entry and selection context.

If a task references a profile key that does not exist, Planning must refuse unless the task instance has an explicit, stamped duration override.

## 7. Unit Policy

Units must be explicit.

Allowed units:

- WORKING_DAYS
- CALENDAR_DAYS
- CALENDAR_WEEKS
- CALENDAR_MONTHS
- CALENDAR_YEARS only if explicitly introduced by a later controlled update

Baseline policy:

- internal CQV work uses WORKING_DAYS;
- vendor lead times may use CALENDAR_DAYS, CALENDAR_WEEKS, or CALENDAR_MONTHS;
- no implicit conversion from CALENDAR_MONTHS to WORKING_DAYS is allowed;
- if conversion is required, the conversion rule must be explicitly approved and stamped.

## 8. Profile Value Selection Logic

Given profile_id/version, profile_key, and selection_context:

1. locate the entry by profile_key;
2. filter value_table rows where context_selector matches supplied fields;
3. choose the most specific match;
4. if tied, choose highest selection_priority;
5. if still tied, use stable row order only if deterministic and documented;
6. if no match exists, return `PROFILE_KEY_VALUE_NOT_FOUND`.

No guessing is allowed.

## 9. Explicit Duration Overrides and No-Profile Baseline

Normal freeze operation requires a governed profile.

No-profile planning is allowed only when every task has an explicit duration override and every override has a stamped source/provenance record.

If any task lacks both a resolvable governed profile entry and an explicit stamped override, Planning must refuse.

## 10. FAT Chain Duration Coverage

For high-complexity process equipment, the profile must include duration entries supporting the FAT path:

- FAT scheduling;
- FAT preparation;
- FAT execution;
- FAT report / punch-list summary;
- FAT acceptance / release-to-ship decision;
- logistics / delivery lead time.

This is limited to the existing high-complexity process-equipment path. It does not add ERP/procurement integration, resource loading, evidence ingestion, or delivery planning.

## 11. Governance and Change Control

Profile versions are immutable.

Any value change, selector change, unit change, or meaning change requires a new profile version or controlled pre-freeze update.

Profile updates should include rationale because planning data directly affects CQV schedule proposals and reporting metrics.

## 12. Error Semantics

Standard codes:

- VALIDATION_ERROR: invalid context, invalid key format, missing required selector;
- NOT_FOUND: profile not found, key not found, value not found;
- CONFLICT: ambiguous match, incompatible units, compatibility failure;
- UNSUPPORTED_OPERATION: unsupported unit conversion;
- INTERNAL_ERROR: unexpected.

PROF-specific subcodes:

- PROFILE_KEY_NOT_FOUND
- PROFILE_KEY_VALUE_NOT_FOUND
- MULTIPLE_EQUAL_MATCHES
- UNIT_CONVERSION_NOT_APPROVED
- PROFILE_INCOMPATIBLE_WITH_TASK_POOL
- PROFILE_EXPIRED

## 13. Integration Requirements

- Task Pool atomic tasks reference profile keys.
- Presets bind a profile version.
- Planning resolves durations using PROF and applies CAL only where unit is WORKING_DAYS.
- Reporting stamps profile_id/version and should flag explicit duration overrides where useful.

## 14. Contract Alignment Dependency

Profile contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: made entries map canonical, separated task_type enum from profile_task_semantic, clarified no-profile baseline, removed calendar ownership from profile, and added FAT duration coverage expectations | Pre-freeze controlled update |
