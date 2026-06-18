---
id: VALOR-arch-addendum-record-view-layout
version: v1.0.1A
revision_context: Blocker 7A
revision_date: 2026-06-12
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: frozen_controlled
dependencies: []
summary: Product-surface record/output view layout rules for WP truth, task truth, and plan proposals without requiring a specific Canvas UI/runtime implementation.
acceptance_criteria:
  - WP/Task truth uses clear record-view fields without implying a specific UI technology.
  - Missing values are blank after the field marker, never fabricated.
  - Preset staging shows staged descriptions only until explicit commit.
  - Plan proposals remain visibly PROPOSED until applied through WP authority.
---

# Record / Output View Layout Contract

## 1) Global rules

- A record/output/artifact view is a user-facing representation of governed data; it is not the source of truth unless the owning subsystem contract has written that truth.
- This addendum does not require a specific Canvas runtime, screen, widget, or UI implementation.
- Never represent proposed, staged, or generated content as committed truth.
- Missing values render as blank after the field marker. Do not print `No Entry` or invent values.
- Contract/audit/provenance timestamps remain UTC. Optional local display time may be shown only when explicitly labeled as display/local time.

## 2) Work Package (WP) record view

### 2.1 Title

`Work Package WP###`

### 2.2 Header fields

- **Work Package ID** ➡️ WP###
- **Title** ➡️
- **Area** ➡️
- **Scope** ➡️
- **Objective** ➡️
- **Governance** ➡️
- **Status** ➡️

### 2.3 Optional applied-plan display stamp

- **Plan Applied** ➡️ PLAN### [display/local timestamp if shown]

This display stamp does not replace UTC contract/audit metadata.

## 3) Tasks section

### 3.1 Tasks header

`**Tasks**`

- If none: `- No tasks created yet.`

### 3.2 Structured task record

- **Task ID** ➡️ WP###-T###
  - **Description** ➡️
  - **Owner** ➡️
  - **Start Date** ➡️
  - **Finish Date** ➡️
  - **Status** ➡️
  - **Depends On** ➡️

## 4) Preset staging visibility

After staging candidate tasks:

- WP/task truth must still show no committed tasks until `WP_COMMIT_STAGED_TASKS` succeeds.
- Staged items are displayed as staged/not committed, for example:

**STAGED TASKS (NOT COMMITTED) — WP###**
1. <description>
2. <description>

Structured committed task records are created only after explicit commit through WP authority.

## 5) Plan Proposal section

A plan proposal view may be shown when planning occurs:

- `PLAN PROPOSAL (PROPOSED / NOT COMMITTED) — PLAN###`

After successful apply through `WP_APPLY_PLAN_PROPOSAL`, the display may show:

- `PLAN PROPOSAL (APPLIED TO WP TRUTH) — PLAN###`

The authoritative committed dates are the WP task date fields written by WP authority, not the proposal view itself.

---

## CHANGELOG

| Date | Changes | Type / Version |
| ---- | ------- | -------------- |
| 2026-06-12 | Blocker 7A normalized Canvas wording to record/output/artifact view terminology and preserved non-UI product-surface layout rules | Pre-freeze controlled update |
| 2026-01-03 | First Issue | v1.0.1A |
