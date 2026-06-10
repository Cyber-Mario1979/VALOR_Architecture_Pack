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
