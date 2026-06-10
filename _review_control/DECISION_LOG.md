# VALOR Architecture Pack Decision Log

Status: ACTIVE
Review branch: review-spec-freeze-control

## Decision Format

Each decision should use this format:

```text
Decision ID:
Date:
Reviewed file/block:
Category: Keep | Modify | Missing | Conflict | Defer
Decision:
Reason:
Impact:
Follow-up:
```

---

## DEC-0001 — Use VALOR_Architecture_Pack as candidate spec

Date: 2026-06-10
Reviewed file/block: README.md, manifest.yaml, A00 intake
Category: Keep
Decision: Use `VALOR_Architecture_Pack` as the candidate Architecture Pack for review.
Reason: The repository is already structured as a specification pack with architecture docs, contracts, action blocks, templates, governed libraries, schemas, validation tools, test vectors, and manifest discipline.
Impact: The pack becomes the starting point for product specification freeze review.
Follow-up: Continue block-by-block review before freeze.

## DEC-0002 — Do not treat current pack as frozen final spec yet

Date: 2026-06-10
Reviewed file/block: README.md, A00 intake
Category: Modify
Decision: The pack is not frozen yet and must be reviewed before becoming product specification authority.
Reason: Strong claims such as implementation-ready must be verified, and gaps around AI, DCF-to-URS, UI/product surface, and delivery planning must be reviewed.
Impact: No clean implementation repo or delivery plan starts until review completes.
Follow-up: Review A01/A02 next.

## DEC-0003 — Repo is review memory

Date: 2026-06-10
Reviewed file/block: Review process decision
Category: Keep
Decision: Store review memory in `_review_control` inside the repository instead of relying on ChatGPT history or uploaded sources.
Reason: The review will span multiple sessions and needs persistent, inspectable state.
Impact: Each session must read `REVIEW_STATE.md` and `SESSION_HANDOFF.md` before continuing.
Follow-up: Keep `REVIEW_STATE.md` and `SESSION_HANDOFF.md` updated after every session.

## DEC-0004 — No implementation during architecture review

Date: 2026-06-10
Reviewed file/block: Review process decision
Category: Keep
Decision: Do not write implementation code during architecture/specification review.
Reason: The product specification must drive implementation, not the old implementation repo or assumptions.
Impact: Current ASBP implementation/rebuild remains stopped.
Follow-up: After review, create delivery plan and perform old repo asset assessment.

## DEC-0005 — Keep SoS product boundary and human-owned approvals

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 SoS and Invariants
Category: Keep
Decision: Keep the A01/A02 product boundary as a freeze-review baseline: Valor structures CQV work, manages WP/task truth, generates advisory planning proposals, controlled documents, and reports/exports, while QMS execution, procurement execution, physical execution evidence, and final approvals/signatures remain outside Valor or human-owned.
Reason: A01 clearly defines Valor as a governed orchestration/traceability system and explicitly excludes ERP/MES/LIMS/SCADA substitution, autonomous scheduling commitment, uncontrolled knowledge chat, invented durations, and human approval ownership. A02 reinforces that humans decide and Valor assists.
Impact: Downstream architecture and implementation must preserve Valor as a governed assistant/specification-driven system, not an autonomous approval or execution system.
Follow-up: Verify A03/A04 contracts preserve this boundary.

## DEC-0006 — Keep subsystem capability map and authority ownership baseline

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01 SoS capability map
Category: Keep
Decision: Keep the A01 subsystem decomposition and authority highlights as the current baseline for later block review.
Reason: A01 identifies Orchestration, Work Package, Task Pool, Preset, Planning, Knowledge & Standards, Document Factory, Reporting & Export, and Security & Compliance, and assigns data-truth ownership at SoS level.
Impact: Phase 3 and later reviews can use this map to check whether each subsystem, contract, action block, schema, and test vector respects the correct authority boundary.
Follow-up: Review A03 and A04_1 next for subsystem authority and orchestration enforcement.

## DEC-0007 — Keep global invariant spine as hard-stop baseline

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 invariants
Category: Keep
Decision: Keep the A01/A02 invariant spine as the global hard-stop baseline: no silent inference, proposal vs commitment boundary, staging before commit, ID non-reuse, no circular dependencies, calendar-aware date arithmetic, mandatory traceability stamps, non-disclosure, reporting as projection only, and compatibility by major version.
Reason: A02 cleanly distinguishes principles from invariants and gives enforcement location, failure behavior, and implementation checks. This is suitable as the top-level deterministic governance frame for later review.
Impact: Later contracts, schemas, validation scripts, and test vectors must map back to these invariants.
Follow-up: Carry invariant-to-contract/schema/test mapping into Phase 11.

## DEC-0008 — Expand AI role coverage before freeze

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 AI principle coverage
Category: Modify
Decision: A01/A02 should be expanded before freeze to state AI-role boundaries at principle level: advisory chat, DCF extraction, controlled drafting, standards-aware review, candidate-only acceptance, provenance, and human confirmation.
Reason: A01 defines Valor as a deterministic assistant that proposes, validates, and structures; A02 states humans decide and Valor assists. That is directionally correct but not yet explicit enough for the known AI roles needed by the product.
Impact: Without a top-level AI boundary, later document-generation and advisory-chat behavior could drift into uncontrolled generation or implied acceptance.
Follow-up: Do not edit architecture files yet. When the user approves edits, add a concise AI-role principle/invariant either in A01/A02 or through the approved modification batch.

## DEC-0009 — Add DCF-to-URS-to-downstream document flow authority

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 DCF and document-generation coverage
Category: Missing
Decision: A01/A02 are missing an explicit principle-level statement that DCF intake, URS acceptance, and downstream RTM/DQ/IQ/OQ/PQ/VSR generation are source-gated and human-accepted before use as regulated output authority.
Reason: A01 includes Document Factory generally, and A02 blocks regulated outputs without traceability stamps, but neither file defines the DCF → URS → downstream document dependency chain at SoS/invariant level.
Impact: The architecture may still handle this in later document-factory blocks, but the SoS layer currently lacks the top-level source-chain boundary needed for freeze confidence.
Follow-up: Review A04_5 and the document-generation compliance addendum in Phase 8. If the flow exists there, add a cross-reference or SoS principle; if not, create a required modification.

## DEC-0010 — Add UI/product workflow surface principle

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 UI/product workflow coverage
Category: Missing
Decision: A01/A02 are missing a principle-level UI/product workflow statement for review/confirm surfaces, proposed vs committed labels, staged vs committed task visibility, advisory chat surface, and export/download state visibility.
Reason: A01 includes a conceptual User Review / Confirm endpoint, but neither A01 nor A02 defines product-surface invariants that make governance visible and hard to misread in the UI.
Impact: A backend/contract-correct product could still produce confusing user flows unless UI state discipline is specified before freeze.
Follow-up: Carry this into Phase 12 as a likely UI/UX spec requirement unless an earlier reviewed block already resolves it.

## DEC-0011 — Clarify traceability stamp scope by artifact type

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 traceability stamping
Category: Conflict
Decision: Clarify the required traceability stamp set by artifact type before freeze.
Reason: A01 defines a minimum stamp set for reports/exports and lists standards bundle, contract, and architecture pack as recommended. A02 applies mandatory traceability to reports/exports/documents but still lists only preset/profile/task pool/calendar as the minimum set. Controlled documents likely require template, standards bundle, document schema, source document, and contract provenance when used.
Impact: Ambiguous stamp requirements could weaken document-generation provenance or cause inconsistent export/report/document behavior.
Follow-up: Reconcile during Phase 8 Document Factory and Phase 9 Reporting/Export review, or in an approved modification batch.

## DEC-0012 — Clarify document metadata status versus review freeze status

Date: 2026-06-10
Reviewed file/block: Phase 2 — A01/A02 metadata
Category: Conflict
Decision: Treat A01/A02 front-matter `status: released` as potentially confusing until pack-level freeze status is clarified.
Reason: Review control states the pack is a candidate specification and not frozen final authority. A01/A02 metadata says released, which may be read later as frozen/approved unless the metadata lifecycle is clarified.
Impact: Future users could over-trust individual document status before the full review is complete.
Follow-up: Defer broad metadata cleanup/clarification to the manifest/pack-integrity or final freeze review unless the user approves an earlier metadata pass.

## DEC-0013 — Defer detailed invariant enforcement mapping

Date: 2026-06-10
Reviewed file/block: Phase 2 — A02 implementation checks
Category: Defer
Decision: Do not resolve detailed invariant-to-schema/validation/test-vector enforcement mapping during Phase 2.
Reason: A02 provides a useful implementation checklist, but verifying actual enforcement belongs to the contract, schema, validation, and test-vector review phases.
Impact: No implementation code is reviewed or written now; enforcement coverage remains a later review obligation.
Follow-up: In Phase 11, map each global invariant to schemas, validation scripts, and test vectors.

## DEC-0014 — Keep A03 subsystem authority baseline

Date: 2026-06-10
Reviewed file/block: Phase 3 — A03 Subsystems Authority
Category: Keep
Decision: Keep A03 as the authority baseline for subsystem ownership, allowed operation classes, anti-coupling rules, and canonical call graph.
Reason: A03 reinforces A01/A02 by identifying subsystem responsibilities, authoritative owners, operation classes, non-ownership constraints, and contract-based integration.
Impact: Later subsystem, contract, action-block, schema, and validation reviews must preserve this authority map unless a logged freeze modification changes it.
Follow-up: Resolve the specific authority-matrix ambiguities logged in DEC-0016 and DEC-0017 before final freeze.

## DEC-0015 — Keep A04_1 orchestration boundary and safe-failure spine

Date: 2026-06-10
Reviewed file/block: Phase 3 — A04_1 Orchestration
Category: Keep
Decision: Keep A04_1 as the orchestration baseline for intent classification, workflow selection, governance gating, contract routing/version negotiation, traceability context propagation, deterministic decision policy, standard errors, and never-claim-success-without-proof behavior.
Reason: A04_1 clearly states that Orchestration is a controller/policy layer, not a data-truth store, and requires missing inputs to be requested, conflicts to be surfaced, truth-mutating transitions to require confirmation, and failed calls not to be represented as success.
Impact: Implementation must keep Orchestration thin, contract-driven, and proof-based, rather than allowing it to become an implicit data owner.
Follow-up: Verify A04_2 and contracts preserve the same boundary.

## DEC-0016 — Clarify governed asset owner hierarchy

Date: 2026-06-10
Reviewed file/block: Phase 3 — A03 Authority Matrix
Category: Conflict
Decision: Clarify whether Profile Library, Calendar Logic, and Contract Registry are standalone subsystems, governed asset libraries under existing subsystems, or registry assets owned by another block.
Reason: A03 canonical subsystem list does not include Profile Library or Calendar Logic as subsystems, but the authority table names Profile Library and Calendar Logic Asset as owners. A03 also lists Contracts as a governed asset type but does not provide a corresponding ownership row, while A04_1 says Orchestration maintains a contract registry.
Impact: Authority ownership is directionally usable but not freeze-clean; later implementers could disagree on where profile, calendar, and contract registry truth lives.
Follow-up: Resolve during Phase 5 for Profile/Calendar and Phase 10 for Contract Registry, or add an A03 clarification in the approved modification batch.

## DEC-0017 — Resolve Document metadata registry ownership

Date: 2026-06-10
Reviewed file/block: Phase 3 — A03 Authority Matrix
Category: Conflict
Decision: Replace ambiguous ownership wording for Document metadata registry with one primary authoritative owner and one reference-holder rule.
Reason: A03 currently says Document metadata registry is owned by “Document Factory (or WP if attached),” which weakens the single-source-of-truth discipline used elsewhere in A03.
Impact: Document metadata could become duplicated or inconsistently mutated between DOC and WP unless authority is clarified.
Follow-up: Reconcile during Phase 8 Document Factory review. Preferred freeze direction: DOC owns generated document metadata/provenance; WP stores references/links/status projections unless the later document block defines otherwise.

## DEC-0018 — Resolve Security & Compliance integration mechanism

Date: 2026-06-10
Reviewed file/block: Phase 3 — A03/A04_1 SEC integration
Category: Conflict
Decision: Clarify whether Security & Compliance is invoked through a formal orchestration contract or enforced as internal orchestration policy without a separate contract.
Reason: A03 includes Security & Compliance as a subsystem and states that subsystems integrate via contracts. Its call graph includes Orchestration → SEC, but A04_1 contract registry does not list a SEC contract.
Impact: Security enforcement remains conceptually present but integration is not freeze-clean.
Follow-up: Resolve during Phase 10 Security/Compliance and Contract Registry review, or add an explicit “no separate SEC contract” policy if SEC is internal policy enforcement.

## DEC-0019 — Replace GATE-Plan policy-choice wording with explicit rule

Date: 2026-06-10
Reviewed file/block: Phase 3 — A04_1 Governance Gates
Category: Modify
Decision: A04_1 should replace the GATE-Plan entry condition phrase “committed tasks exist OR user requests advisory planning on staged set (policy choice)” with an explicit, deterministic rule.
Reason: Governance gates are supposed to be enforceable. Leaving staged-set planning as a policy choice creates ambiguity around whether planning may operate on uncommitted staged tasks and how such output must be labeled.
Impact: Planning behavior could vary between implementations unless the permitted inputs and labels are fixed.
Follow-up: Resolve during Phase 6 Planning review or in an approved A04_1 modification.

## DEC-0020 — Add orchestration document-generation gate placeholder

Date: 2026-06-10
Reviewed file/block: Phase 3 — A04_1 Governance Gates
Category: Missing
Decision: A04_1 is missing an explicit orchestration gate for document generation/drafting/review/issue, even as a high-level placeholder.
Reason: A04_1 routes document generation to Document Factory and includes documents in traceability context, but its canonical gate list covers Stage, Commit, Plan, Apply, and Export only. Controlled document generation is a major product flow and should not appear as an ungated side-route.
Impact: The DCF/URS/document chain remains under-specified at orchestration level until Phase 8, and product/UI flows could omit necessary review/confirmation states.
Follow-up: Review A04_5 and the document-generation addendum in Phase 8; then add or cross-reference a document gate if confirmed missing.

## DEC-0021 — Align A04_1 stamping gate with artifact-specific traceability

Date: 2026-06-10
Reviewed file/block: Phase 3 — A04_1 Traceability Context Propagation
Category: Modify
Decision: A04_1 stamping-gate requirements should be aligned with artifact-specific traceability rules before freeze.
Reason: A04_1 session context tracks architecture pack, standards bundle, contract versions, active document/export IDs, and staged artifacts, but its stamping gate only validates preset/profile/task pool/calendar. This repeats the Phase 2 traceability ambiguity and is too narrow for controlled documents.
Impact: Orchestration might allow document/export generation with incomplete provenance unless the minimum stamp set is split by artifact type.
Follow-up: Reconcile with DEC-0011 during Phase 8 Document Factory and Phase 9 Reporting/Export review.

## DEC-0022 — Defer detailed AI and UI surface resolution

Date: 2026-06-10
Reviewed file/block: Phase 3 — A03/A04_1 AI and UI coverage
Category: Defer
Decision: Do not resolve detailed AI advisory-chat behavior or UI/product surface requirements during Phase 3.
Reason: A04_1 supports deterministic intent handling, proposal/commitment labeling, confirmations, and safe failure, but the detailed AI roles and UI surfaces are better reviewed in Knowledge/Standards, Document Factory, Reporting/Export, and UX/Product Surface phases.
Impact: DEC-0008 and DEC-0010 remain open carried risks, not blockers for completing Phase 3.
Follow-up: Carry AI-role detail to Phases 7 and 8; carry UI/product-surface detail to Phase 12.

## DEC-0023 — Keep WP truth, lifecycle, ID, and dependency backbone

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2 Work Package Spine
Category: Keep
Decision: Keep A04_2 as the baseline for WP/task truth, lifecycle transitions, deterministic ID allocation, non-reuse/tombstoning, dependency integrity, mutability rules, and WP error semantics.
Reason: A04_2 cleanly makes WP the single source of truth for WP objects, Task objects, committed dates, lifecycle transitions, deterministic ID issuance, and dependency validity.
Impact: Later planning, document, reporting, schema, and validation reviews must derive from WP truth and must not create shadow truth.
Follow-up: Verify schema and test-vector coverage in Phase 11.

## DEC-0024 — Keep WP contract mutation boundary and confirmation discipline

Date: 2026-06-10
Reviewed file/block: Phase 4 — WP contracts and action blocks
Category: Keep
Decision: Keep the WP contract direction that WP mutations are M2-only, truth-mutating actions require confirmation, stage actions are stage-only, and Orchestration is the caller.
Reason: The main WP contract sets allowed modes, side-effect classes, confirmation requirements, and target/payload fields for core WP actions. The reviewed action blocks preserve M2-only mutation semantics.
Impact: Implementation must keep all WP truth mutations behind explicit contract calls and confirmations.
Follow-up: Reconcile catalog/schema naming issues before freeze.

## DEC-0025 — Keep user-driven no-profile baseline as controlled fallback

Date: 2026-06-10
Reviewed file/block: Phase 4 — `VALOR-contract-orch-wp-user-driven-baseline.yaml`
Category: Keep
Decision: Keep the user-driven no-profile baseline concept as a controlled fallback when governed profile data is missing.
Reason: The baseline contract explicitly forbids guessing, requires USER_INPUT as the duration source, requires planning-basis setup, duration overrides, and explicit confirmation before export.
Impact: This supports controlled planning/export when a profile is unavailable, without allowing fabricated durations.
Follow-up: Integrate its data fields into A04_2 or cross-reference them explicitly; see DEC-0031.

## DEC-0026 — Reconcile WP architecture, contract, and action-block catalogs

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2, WP contracts, WP action blocks
Category: Conflict
Decision: Reconcile the WP action catalog before freeze.
Reason: A04_2 lists WP_GET, WP_LIST, TASK_GET, TASK_LIST, WP_STAGE_TASKS, WP_VALIDATE_STAGE, WP_COMMIT_STAGED_TASKS, WP_UPDATE_TASK_FIELDS, WP_UPDATE_DEPENDENCIES, WP_CLOSE, and WP_VALIDATE. The main WP contract includes WP_GET, WP_CREATE, WP_STAGE_TASKS, WP_COMMIT_STAGED_TASKS, WP_UPDATE_TASK_FIELDS, WP_APPLY_PLAN_PROPOSAL, and WP_BIND_PRESET_CONTEXT. The manifest lists only three WP action-block files: WP_APPLY_PLAN_PROPOSAL, WP_BIND_PRESET_CONTEXT, and WP_UPDATE_TASK_FIELDS.
Impact: Different implementers could build different WP APIs unless the architecture, contract, and action-block inventories are aligned.
Follow-up: Decide whether missing actions are contract-only, future actions, or must receive action-block files before freeze.

## DEC-0027 — Standardize the schedule-apply action

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2, WP contract, WP_APPLY_PLAN_PROPOSAL action block
Category: Conflict
Decision: Standardize whether applying a planning proposal is performed through WP_UPDATE_TASK_FIELDS or the dedicated WP_APPLY_PLAN_PROPOSAL action.
Reason: A04_2 says applying schedule dates uses WP_UPDATE_TASK_FIELDS, while the main WP contract and action block define WP_APPLY_PLAN_PROPOSAL as the schedule-apply action.
Impact: The proposal-vs-commitment boundary remains directionally strong, but the implementation entry point is ambiguous.
Follow-up: Resolve in Phase 6 Planning review or approved modification batch.

## DEC-0028 — Remove provisional task-ID ambiguity from staged tasks

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2 staged task semantics
Category: Modify
Decision: A04_2 should remove or clarify the phrase allowing provisional IDs for TASK_STAGED.
Reason: A04_2 also states that staged task preview has no committed IDs, and A02 requires no task IDs until WP_COMMIT_STAGED_TASKS succeeds. Provisional identifiers may be useful for previews, but they must not be confused with authoritative task_id values.
Impact: Without clarification, staging could accidentally allocate or expose IDs that look authoritative before commit.
Follow-up: Define any preview identifier as `preview_task_ref` or equivalent, not `task_id`, unless a later approved policy explicitly changes the invariant.

## DEC-0029 — Clarify WP relationship to physical execution evidence

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2 task date fields and A01 boundary carry-forward
Category: Conflict
Decision: Clarify that WP may store status/date summaries, user-entered actual dates, or references to execution evidence, but does not own physical execution evidence truth.
Reason: A04_2 includes optional actual_start_date and actual_end_date as execution evidence fields, while the SoS boundary states physical execution data is outside Valor and only referenced or human-owned.
Impact: The WP model could overreach into execution evidence ownership unless the boundary is clarified.
Follow-up: Reconcile with later Document Factory, Reporting, and compliance/security review if evidence references are needed.

## DEC-0030 — Standardize WP schema references

Date: 2026-06-10
Reviewed file/block: Phase 4 — WP contract and WP action blocks
Category: Conflict
Decision: Standardize result schema references for WP actions.
Reason: The main WP contract uses `schemas/objects/work_package_schema.json`, while the reviewed WP action blocks use `schemas/wp.json`. Repository search found `schemas/wp.json` only as a reference inside action blocks, not as an indexed schema file.
Impact: Validation and implementation can drift if action blocks point to a different or missing schema path.
Follow-up: Resolve during Phase 11 schema review or approved action-block cleanup.

## DEC-0031 — Integrate user-driven baseline fields into WP architecture

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2 and user-driven baseline contract
Category: Missing
Decision: A04_2 is missing explicit WP fields or references for planning_basis, planning_label, duration override source, duration override value, and confirmation record used by the user-driven baseline contract.
Reason: The user-driven baseline contract introduces planning basis, user-input duration overrides, and append-only confirmation behavior, but A04_2 does not define where these are stored in WP truth.
Impact: The fallback policy is useful but partially orphaned unless WP truth formally owns or references the required fields.
Follow-up: Add WP data-model fields or a cross-reference once edits are approved.

## DEC-0032 — Standardize selector/context and stamp naming

Date: 2026-06-10
Reviewed file/block: Phase 4 — A04_2, WP contract, WP_BIND_PRESET_CONTEXT action block
Category: Modify
Decision: Standardize the selector/context payload shape and naming across A04_2, the main WP contract, and WP_BIND_PRESET_CONTEXT.
Reason: A04_2 uses `preset_ref`, `profile_ref`, `standards_bundle_ref`, and `calendar_logic_ref`; the main WP contract uses `task_set_ref` and `preset_context`; the action block uses `preset`, `profile`, `calendar`, and `bundle` objects. These represent the same traceability concepts but with inconsistent naming.
Impact: Traceability stamping and selector binding could become brittle across UI, contracts, and schemas.
Follow-up: Reconcile during Phase 5 Preset/Profile/Calendar review or approved modification batch.

## DEC-0033 — Defer detailed schema and validation enforcement mapping

Date: 2026-06-10
Reviewed file/block: Phase 4 — WP schemas/validation carry-forward
Category: Defer
Decision: Do not resolve detailed WP schema, validation-script, and test-vector enforcement during Phase 4.
Reason: Phase 4 identified schema-reference and catalog-alignment issues, but full schema/test coverage belongs to Phase 11.
Impact: Phase 4 is complete without implementation or schema edits, but DEC-0026 and DEC-0030 must be carried into Phase 11.
Follow-up: In Phase 11, map WP invariants to object schemas, contract schemas, validation scripts, and test vectors.
