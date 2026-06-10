# Phase 12 Decisions Pending Decision Log Merge

Status: PENDING_MERGE_TO_DECISION_LOG
Review branch: review-spec-freeze-control
Date: 2026-06-10

Reason: The main decision log is now large and has repeatedly failed direct GitHub updates in recent sessions. This file preserves the Phase 12 decisions in repo memory until they can be merged into `_review_control/DECISION_LOG.md` or consolidated during Phase 13 final freeze review.

## DEC-0122 — Keep addendum layer as candidate UX/output constraint layer

Date: 2026-06-10
Reviewed file/block: Phase 12 — Addendums and UX/Product Surface
Category: Keep
Decision: Keep the addendum layer as a candidate UX/output constraint layer.
Reason: The four addendums provide concrete behavioral rules for record rendering, plan proposal/apply UX, document output cleanliness, and report/export projection behavior.
Impact: The addendums are valuable implementation guidance, but must be cleaned and aligned before freeze.
Follow-up: Consolidate addendum rules into product-neutral architecture language.

## DEC-0123 — Keep planning proposal/apply UX invariants

Date: 2026-06-10
Reviewed file/block: Phase 12 — Planning Invariants & UX addendum
Category: Keep
Decision: Keep the plan proposal versus apply UX invariants.
Reason: The planning addendum correctly requires plan generation to remain non-mutating, apply to require explicit Yes/No confirmation, cancellation to make no truth changes, and successful apply to mark the proposal as APPLIED.
Impact: The product must clearly separate proposed planning from committed WP/task truth.
Follow-up: Align command/action names with Planning and WP contracts.

## DEC-0124 — Keep token-clean and projection-only output rules

Date: 2026-06-10
Reviewed file/block: Phase 12 — Document and Reporting/Export addendums
Category: Keep
Decision: Keep token-clean document output rules and projection-only report/export rules.
Reason: The document addendum prevents template tokens/placeholders and runtime footer text in final documents. The reporting/export addendum prevents reporting/export from changing WP/task truth, plan proposals, stamps, or missing-field state.
Impact: These rules reinforce DOC/RPT boundaries and should survive freeze after terminology cleanup.
Follow-up: Reconcile with DOC/RPT schemas and output validation.

## DEC-0125 — Replace Canvas terminology with product-neutral surface terminology

Date: 2026-06-10
Reviewed file/block: Phase 12 — Addendums
Category: Conflict
Decision: Replace Canvas-specific wording across addendums with product-neutral terms such as record view, artifact view, workspace panel, output artifact, or product surface.
Reason: Addendums repeatedly describe Canvas objects/WP Canvas as the UI surface, while the architecture pack should not depend on a specific ChatGPT Canvas implementation.
Impact: Leaving Canvas terms in the frozen spec would conflict with product portability and the user’s direction to remove Canvas-related logic/text.
Follow-up: Rename the Canvas rendering addendum or absorb it into a product surface specification.

## DEC-0126 — Reclassify UI surfaces as projections, not truth owners

Date: 2026-06-10
Reviewed file/block: Phase 12 — Canvas rendering addendum and architecture carry-forward
Category: Conflict
Decision: Clarify that UI/product surfaces display authoritative subsystem truth but do not own truth.
Reason: The Canvas rendering addendum says Canvas is the truth view for WP/task/doc records, but A04_2, A04_5, and A04_6 assign truth/artifact ownership to WP, DOC, and RPT subsystems. A UI surface may display truth but must not become the authority.
Impact: Product UI can avoid accidental authority drift.
Follow-up: Define surface-to-authority mapping in a product surface spec.

## DEC-0127 — Align addendum command names with contracts and action blocks

Date: 2026-06-10
Reviewed file/block: Phase 12 — Addendums and prior contract findings
Category: Conflict
Decision: Align addendum command/action names with canonical contracts and action blocks.
Reason: Addendums use commands such as `Plan tasks`, `Apply Plan PLAN### to WP###`, `Build Report`, `Use Preset WP <code>`, and `Add Suggested Tasks WP###`, while prior phases found contract/action naming mismatches across WP, Planning, DOC, and RPT.
Impact: Users and implementers may see different action names for the same behavior.
Follow-up: Choose a public command vocabulary and map it to canonical contract action types.

## DEC-0128 — Add dependencies and cross-references to addendums

Date: 2026-06-10
Reviewed file/block: Phase 12 — Addendum front matter
Category: Modify
Decision: Add explicit dependencies/cross-references from each addendum to the relevant architecture blocks and contracts.
Reason: All four addendums currently show empty `dependencies`, even though they depend on WP, Planning, DOC, RPT, K&S, Governance, Security, and Contract Registry rules.
Impact: Addendum authority and conflict resolution remain unclear without dependency links.
Follow-up: Update addendum metadata during approved cleanup.

## DEC-0129 — Standardize timestamp display versus metadata policy

Date: 2026-06-10
Reviewed file/block: Phase 12 — Addendums and prior document/report findings
Category: Modify
Decision: Standardize timestamp policy across product surfaces: UTC for machine/provenance metadata where required, Cairo display time for user-facing artifacts if selected, and no incorrect UTC labels.
Reason: Addendums use `dd-mm-yyyy HH:MM Africa/Cairo`, while schemas/templates and architecture examples often use `generated_at_utc` or UTC timestamps.
Impact: Mixed timestamp labels may undermine audit clarity.
Follow-up: Define timestamp field names and display labels in schema/product surface cleanup.

## DEC-0130 — Add a product surface specification before freeze

Date: 2026-06-10
Reviewed file/block: Phase 12 — UX/Product Surface
Category: Missing
Decision: Add a product surface specification or addendum before final freeze.
Reason: The current addendums define selected output fragments, but there is no full product surface model for Work Package view, task staging, planning, document review, report/export, validation errors, confirmations, advisory chat, and artifact/download states.
Impact: UI/product behavior remains under-specified for implementation and testing.
Follow-up: Create a minimal product surface spec before final freeze, while deferring detailed wireframes.

## DEC-0131 — Add confirmation and review surface requirements

Date: 2026-06-10
Reviewed file/block: Phase 12 — UX/Product Surface and Governance carry-forward
Category: Missing
Decision: Add product surface requirements for confirmation/review gates.
Reason: Governance requires confirmations for commit/apply/finalize/export/close, but the addendums only specify the plan apply prompt in detail.
Impact: Other critical gates may lack clear UI behavior.
Follow-up: Define confirmation surfaces, role context display, scope preview, cancel behavior, and success/failure states.

## DEC-0132 — Add advisory chat/help/follow-up surface contract

Date: 2026-06-10
Reviewed file/block: Phase 12 — UX/Product Surface
Category: Missing
Decision: Add an advisory chat/help/follow-up surface contract.
Reason: The product needs consistent help output, next-command guidance, advisory disclaimers, missing information handling, and conflict remediation behavior, but current addendums focus mostly on record/output rendering.
Impact: Chat guidance may drift across commands and sessions.
Follow-up: Define help/advisory response requirements before freeze or in a dedicated UI addendum.

## DEC-0133 — Add export/download and artifact-state surface requirements

Date: 2026-06-10
Reviewed file/block: Phase 12 — Reporting/Export addendum
Category: Missing
Decision: Add explicit export/download and artifact-state surface requirements.
Reason: The reporting/export addendum says export produces a downloadable file and should not print CSV inline, but it does not define artifact status, availability, failure, retry, strict-refusal display, or download metadata surfaces.
Impact: Export UX may be inconsistent and hard to validate.
Follow-up: Define artifact states for report/export/document outputs.

## DEC-0134 — Add DCF, URS source, K&S citation, and redaction surfaces

Date: 2026-06-10
Reviewed file/block: Phase 12 — UX/Product Surface carry-forward
Category: Missing
Decision: Add product surface requirements for DCF intake, accepted URS source-chain, K&S citations, restricted excerpts, and redaction choices.
Reason: Earlier phases identified DCF intake, accepted URS gating, K&S bundle/citation gaps, excerpt authorization, and redaction enforcement as missing or incomplete, but current addendums do not define their UI/product behavior.
Impact: Critical regulated workflow decisions may be invisible or inconsistent in the product surface.
Follow-up: Include these surfaces in the minimal product surface specification.

## DEC-0135 — Defer detailed wireframes but not minimum surface requirements

Date: 2026-06-10
Reviewed file/block: Phase 12 — UX/Product Surface
Category: Defer
Decision: Defer detailed wireframes, visual design, and pixel-level UI to the delivery plan, but do not defer minimum surface/state requirements.
Reason: The architecture freeze needs enough product surface specification to prevent ambiguity, but detailed UI design can happen after freeze.
Impact: Freeze can proceed after minimum UX requirements are specified without locking final visual design.
Follow-up: Carry detailed wireframes into post-freeze delivery planning.
