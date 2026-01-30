---
id: VALOR-arch-addendum-planning-invariants-ux
version: v1.0.1C
date: 2026-01-27
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: released
dependencies: []
summary: Hard invariants and UX contract for single-table planning (Plan tasks writes to Tasks table; Apply Plan changes statuses only).
acceptance_criteria:
  - Plan tasks updates the existing Tasks table directly with computed Start/Finish dates and sets Status to Planned.
  - Plan tasks writes Planned Duration (d) for every planned task and writes sequential Dependencies when missing.
  - No separate "PLAN PROPOSAL" section is rendered anywhere.
  - Apply Plan requires explicit Yes/No confirmation and, on success, changes WP/Task statuses only (no date manipulation).
  - Duration resolution uses the bound Profile Library and Task Pool duration_ref.profile_key; planning MUST refuse if a task has neither Duration Ref nor explicit Planned Duration (d).
---

# Planning Invariants & UX Contract (Single-Table)

## 1) Definitions
- **Plan tasks**: Computes schedule dates and owners and writes them **directly** into the Tasks table. This is a *proposal-in-place* represented by `Status = Planned`.
- **Apply Plan**: Authorizes execution by changing statuses only (WP: Open → In Progress; first not-completed Task: Planned → In Progress; remaining not-completed Tasks stay Planned). Dates/owners are not changed by Apply Plan.

## 2) Hard invariants (non-negotiable)

1. `Plan tasks <Start_Date>` MUST:
   - update Start/Finish dates in the Tasks table for all tasks included in planning,
   - change each planned task Status from `Open` → `Planned`,
   - use working-day arithmetic from the bound Calendar,
   - refuse planning if required bindings are missing (see 2.3).
   - write Dependencies defaults if missing (first task `—`, subsequent tasks depend on the previous task),
   - write Planned Duration (d) for every planned task.



2. `Plan tasks <Start_Date>` MUST NOT:
   - create any separate planning/proposal section or secondary planning table,
   - change WP Status,
   - change task IDs, WP IDs, or document IDs.

3. `Apply Plan` MUST:
   - stop and ask: `Confirm apply plan to WP###? (Yes/No)`
   - on **Yes**:
     - change WP Status `Open` → `In Progress`
     - set **only the first not-completed task** (lowest Task ID) to `In Progress`
     - set all other not-completed tasks to `Planned`
     - leave any already `Completed` tasks as-is
   - on **No**: respond `Cancelled. No changes committed.`

4. `Apply Plan` MUST NOT:
   - change Start/Finish dates or Owners (already set by Plan tasks).

5. `Update <WP###-T###> Status=Completed` MUST:
   - set that task to `Completed`,
   - set the next not-completed task (by Task ID order) to `In Progress`,
   - set all remaining not-completed tasks to `Planned`,
   - if no remaining tasks exist → set WP Status to `Completed`.


### 2.3 Binding gate (critical)
Planning depends on the WP bound context. If any of the below are missing/unbound, ORCH must refuse planning:

- `CAL` (calendar_id + version)
- `PROF` (profile_id + version)

If `PROF` is missing/`UNBOUND`:
- refuse planning and instruct the user to use a WP preset (`Use Preset WP <code>`) or explicitly set the Profile/Type on the WP header and run `Update WP###`.

## 3) Deterministic duration resolution

### 3.1 Duration source precedence (strict)
For each task, resolve **Planned Duration (d)** in this strict order (no guessing):

1) If task has **Planned Duration (d)** → use it (must be integer ≥ 0).

2) Else if task has **Duration Ref**:
   - If it is `COMPOSITE(k1+k2+...)` → resolve each key from the bound Profile Library and sum as **WORKING_DAYS**.
   - Else resolve the single `duration_ref.profile_key` from the bound Profile Library as **WORKING_DAYS**.

3) Else if task has **Atomic Task ID** and the bound Task Pool maps it to a `duration_ref.profile_key`:
   - Use that mapped profile key as the task’s **Duration Ref**, resolve from the bound Profile Library, and write the Duration Ref back into the task row.

4) Else → **REFUSE PLANNING** for the WP.

Refusal (exact):
`DURATION_REF_REQUIRED — add Duration Ref (or Planned Duration (d)) to every task, then re-run: Plan tasks <dd-mm-yyyy>`

### 3.2 Authoritative lookup source
- **Authoritative**: Libraries set (`ARCH_BUNDLE_Libraries_CR_v1_0_2.yaml`for Type: `Cleanroom` , `ARCH_BUNDLE_Libraries_PE_v1_0_2.yaml` for Type: `ProcessEquipment` , `ARCH_BUNDLE_Libraries_UT_v1_0_2.yaml` for Type: `Utilities`) → the bound `profile_id` record → `keys[]`.

### 3.3 Failure-mode diagnostic
If planning fails to resolve durations for one or more tasks:
- treat as a binding or duration_ref failure.
- verify:
  - WP Bound Context contains `PROF=<profile_id>@<version>` and `CAL=<calendar_id>@<version>`,
  - each task row contains either `Planned Duration (d)` or `Duration Ref` (or `Atomic Task ID` that maps to a duration_ref.profile_key in the bound Task Pool),
  - the profile record contains the referenced `profile_key` under `keys[]`.

## 4) Working-day date math

Definitions:
- `WD_ADD(date, n)` = add `n` working days to `date` per bound Calendar (skipping non-working days).
- `WD_NEXT(date)` = the next working day after `date`.

Rules:
- If `Planned Duration (d) = 0` → Finish Date = Start Date.
- If `Planned Duration (d) = 1` → Finish Date = Start Date.
- If `Planned Duration (d) > 1` → Finish Date = WD_ADD(Start Date, Planned Duration (d) - 1)
- Next task Start Date = WD_NEXT(previous Finish Date), unless dependencies push it later.

## 5) Dependency-aware forward pass
- Plan tasks in ascending Task ID order unless explicit dependencies require otherwise.
- Each task start date is the next working day after the maximum of:
  - previous task finish date, and
  - latest predecessor finish date (+ lag days if defined).


