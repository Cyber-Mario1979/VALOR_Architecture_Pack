---
id: VALOR-block-A07-calendar-logic-architecture
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: frozen_controlled
date: 2026-06-12
dependencies:
  - VALOR-block-A00-specs-architecture-pack
  - VALOR-block-A01-sos-context-capability
  - VALOR-block-A02-principles-invariants
  - VALOR-block-A03-subsystems-authority
summary: "Block A07 — Calendar Logic Architecture: versioned working-day rules used consistently by Planning and Reporting. The v1.0.1 freeze asset is a governed wrapper around canonical CAL-WORKWEEK v1."
acceptance_criteria:
  - Defines Calendar Logic as a governed, versioned asset referenced by ID/version.
  - Defines the canonical CAL-WORKWEEK v1 baseline as Sun-Thu working week, Fri-Sat weekend, UTC+02:00.
  - Defines the v1.0.1 package file as a wrapper around canonical CAL-WORKWEEK v1.
  - Defines deterministic date arithmetic requirements.
  - Defines compatibility and change-control rules across versions.
  - Defines strict refusal/fallback rules for CQV planning/reporting usage.
---

# Calendar Logic Architecture (Working Days + Weekend Defer + Holidays)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

Calendar Logic (CAL) is a governed, versioned rule set that defines:

- what constitutes a working day;
- which days are weekends;
- which dates are holidays;
- optional working hours and partial-day rules;
- deterministic calendar arithmetic used by Planning and Reporting.

CAL exists because CQV planning and reporting must be consistent:

- Planning uses CAL to compute proposed schedules in working days.
- Reporting uses CAL to compute working-day metrics and deltas.

CAL is authoritative for calendar rules only.

CAL is not authoritative for:

- task durations, which are owned by Profile Library;
- WP/task truth, which is owned by WP;
- scheduling algorithm choices, which are owned by Planning logic;
- approvals or regulated-use decisions.

## 2. Canonical v1.0.1 Calendar Baseline

The v1.0.1 architecture-pack calendar asset is:

- file: `libraries/calendar/CAL-WORKWEEK_v1.0.1.yaml`
- calendar_id: `CAL-WORKWEEK`
- calendar_version: `v1.0.1`
- canonical_calendar_id: `CAL-WORKWEEK`
- canonical_calendar_version: `v1`
- package_asset_version: `v1.0.1`
- canonical_source_path: `libraries/calendar/CAL-WORKWEEK_v1.yaml`
- canonical_source_sha256: `4789d604a5fb8e72587934a8d0e89db1ce4e7a298ddc62ac5c52be5dfda3c386`

The file remains named `CAL-WORKWEEK_v1.0.1.yaml` for architecture-pack versioning, but it must declare itself as a governed v1.0.1 wrapper around canonical `CAL-WORKWEEK v1`.

The canonical baseline is:

- timezone: `UTC+02:00`
- working week: Sunday through Thursday
- weekend: Friday and Saturday
- weekend_handling: `DEFER_TO_NEXT_WORKING_DAY`
- allow_working_weekends: `false`
- holidays: empty baseline set unless explicitly supplied later
- holiday policy: `TREAT_AS_NON_WORKING`
- working_hours: `null`
- duration_unit: `WORKING_DAYS`
- start_date_rule: `IF_NON_WORKING_START_NEXT_WORKING`
- end_date_rule: `END_INCLUSIVE`
- diff_policy: `COUNT_WORKING_DAYS_BETWEEN`

`Africa/Cairo` must not be treated as the canonical timezone for this baseline unless accepted by a later controlled patch.

## 3. Core Entity

A Calendar asset must include:

- calendar_id;
- calendar_version;
- canonical_calendar_id where wrapped;
- canonical_calendar_version where wrapped;
- package_asset_version where wrapped;
- canonical_source_path and source hash where applicable;
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
- timezone;
- weekend_rule;
- holidays;
- working_hours;
- arithmetic_policy.

The governed lifecycle metadata is local governed-library metadata only. It does not mean the asset is frozen, final, released for regulated use, or externally approved.

## 4. Weekend Rule

WeekendRule defines which weekdays are non-working.

For `CAL-WORKWEEK v1`, the weekend rule is:

- weekend_days: `[FRI, SAT]`
- weekend_handling: `DEFER_TO_NEXT_WORKING_DAY`
- allow_working_weekends: `false`

## 5. Holiday Set

HolidaySet defines non-working dates.

Fields:

- holiday_dates: array of `YYYY-MM-DD`;
- holiday_name_map: optional map of date to holiday name;
- policy: `TREAT_AS_NON_WORKING` unless a later controlled calendar version defines an override policy.

The v1 baseline has an empty holiday set. This does not mean holidays do not exist in reality; it means no holiday dates are governed in the baseline asset yet.

## 6. Working Hours

Whole-working-day planning is the v1.0.1 baseline.

`working_hours: null` means partial-day scheduling is not in the declared baseline. Requests requiring partial-day scheduling must refuse or be deferred to a later explicitly supported calendar version.

## 7. Arithmetic Policy

Calendar operations must be deterministic for a given calendar version.

The v1 arithmetic policy is:

- duration_unit: `WORKING_DAYS`
- start_date_rule: `IF_NON_WORKING_START_NEXT_WORKING`
- end_date_rule: `END_INCLUSIVE`
- diff_policy: `COUNT_WORKING_DAYS_BETWEEN`

## 8. Canonical Calendar Functions

CAL must support deterministic functions used by Planning and Reporting:

### 8.1 `is_working_day(date) -> bool`

Returns `false` if the date is a weekend day or a governed holiday.

### 8.2 `next_working_day(date) -> date`

If the date is a working day, returns the same date.

If the date is non-working, returns the next date that is a working day.

### 8.3 `add_working_days(start_date, n) -> end_date`

Rules:

1. apply `start_date_rule` first;
2. add `n` working days while skipping governed non-working dates;
3. apply `end_date_rule`.

### 8.4 `working_days_between(date_a, date_b) -> int`

Returns count of working days per `diff_policy`.

## 9. Versioning, Compatibility, and Change Control

`calendar_id + calendar_version` is immutable.

Changes require a new calendar version or a controlled wrapper update.

Major version bump is required when arithmetic semantics change, for example changing `END_INCLUSIVE` to `END_EXCLUSIVE`.

Planning and Reporting must:

- require calendar_id/version in requests;
- stamp calendar_id/version in outputs;
- refuse if the calendar version is missing, expired, unknown, or unsupported;
- refuse if a required holiday set or arithmetic policy is incompatible with the requested operation.

## 10. Strictness Policy

For CQV usage:

- missing calendar version returns `VALIDATION_ERROR`;
- unknown calendar version returns `NOT_FOUND` or `CONFLICT` depending on ambiguity;
- unsupported arithmetic policy returns `CONFLICT` / `ARITHMETIC_POLICY_UNSUPPORTED`;
- partial-day requests return `UNSUPPORTED_OPERATION` unless explicitly supported by a later calendar version.

Relaxed fallback is not normal freeze operation.

## 11. Integration Requirements

### 11.1 Planning Integration

Planning must:

- use `CAL-WORKWEEK_v1.0.1` wrapper for the canonical v1 calendar baseline when that calendar is referenced;
- compute working-day durations using the governed calendar rules;
- stamp calendar_id, calendar_version, canonical_calendar_version, and package_asset_version into plan outputs;
- refuse to plan if required calendar metadata is missing or expired.

### 11.2 Reporting Integration

Reporting must:

- compute working-day metrics using the stamped calendar version;
- refuse to compute working-day metrics if the calendar is missing or unsupported;
- label metrics clearly as working days or calendar days.

## 12. Contract Alignment Dependency

Calendar contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: aligned CAL-WORKWEEK v1.0.1 wrapper to canonical CAL-WORKWEEK v1 Sun-Thu/Fri-Sat/UTC+02:00 baseline and added local governed-library lifecycle expectations | Pre-freeze controlled update |
