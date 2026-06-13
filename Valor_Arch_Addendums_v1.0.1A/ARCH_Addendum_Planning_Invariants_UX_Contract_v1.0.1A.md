---
id: VALOR-arch-addendum-planning-invariants-product-surface
version: v1.0.1A
revision_context: Blocker 7A
revision_date: 2026-06-12
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: pre_freeze_controlled
dependencies: []
summary: Product-surface invariants for plan proposal vs apply behavior without requiring a specific UI implementation.
acceptance_criteria:
  - Plan generation produces PROPOSED output only and does not mutate WP/task truth.
  - Apply Plan always requires explicit Yes/No confirmation and writes through WP authority only.
  - Proposal remains visibly proposed until successful apply, then may be displayed as applied-to-WP-truth.
---

# Planning Invariants & Product Surface Contract

## 1) Definitions

- **Plan Proposal**: A computed schedule/assignment recommendation. It is `PROPOSED`, not committed truth.
- **Apply Plan**: The governed path that writes proposed dates into WP/task truth through `WP_APPLY_PLAN_PROPOSAL`.

## 2) Hard invariants

1. `PLAN_GENERATE_PROPOSAL` MUST NOT:
   - write Start/Finish/Owner into WP/task truth;
   - change task IDs, WP IDs, or document IDs;
   - use mutation language such as committed, applied, saved, or updated records.

2. Preview behavior is represented by:
   - `PLAN_GENERATE_PROPOSAL` with `options.dry_run=true`.

3. `WP_APPLY_PLAN_PROPOSAL` MUST:
   - stop and ask for explicit confirmation before mutation;
   - commit only after an explicit **Yes**;
   - write committed dates through WP authority only.

4. If user answers **No**:
   - respond with a cancelled/no-change message;
   - make no truth changes.

5. If the user asks to “plan and apply” in one command:
   - generate/present the plan proposal first;
   - stop before apply;
   - request explicit apply confirmation.

## 3) Required product-surface outputs

### 3.1 On Plan Proposal

Show or return a plan proposal view labeled:

`PLAN PROPOSAL (PROPOSED / NOT COMMITTED) — PLAN###`

Include at minimum:

- Start Date basis;
- Assignment Method if used;
- Status = `PROPOSED`;
- Assumptions, if any;
- Proposal table: `Task ID | Proposed Owner | Proposed Start Date | Proposed Finish Date | Depends On`.

Chat/product-surface wording must clearly say:

`Plan proposal generated. Not committed. Apply requires confirmation through WP_APPLY_PLAN_PROPOSAL.`

### 3.2 On Apply Success

After successful `WP_APPLY_PLAN_PROPOSAL`, the proposal view may be displayed as:

`PLAN PROPOSAL (APPLIED TO WP TRUTH) — PLAN###`

Committed dates must be read from WP/task truth, not inferred from the prior proposal view.

### 3.3 Timestamp rule

- Contract/audit/provenance metadata timestamps use UTC.
- Optional local display time may be shown only when explicitly labeled as display/local time.
- Local display time must not replace UTC metadata.

---

## CHANGELOG

| Date | Changes | Type / Version |
| ---- | ------- | -------------- |
| 2026-06-12 | Blocker 7A aligned planning product-surface wording to PLAN_GENERATE_PROPOSAL and WP_APPLY_PLAN_PROPOSAL behavior | Pre-freeze controlled update |
| 2026-01-03 | First Issue | v1.0.1A |
