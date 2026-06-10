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

## Prior Decisions

DEC-0001 through DEC-0055 were logged during Phases 0 through 6 and remain active.

Detailed text for prior decisions is preserved in repository history and summarized in `REVIEW_STATE.md`.

Active prior themes:

- candidate pack accepted, not frozen;
- no implementation during architecture review;
- SoS/product boundary retained;
- global invariant spine retained;
- AI role, DCF/document source chain, UI/product surface, and artifact-specific traceability require freeze clarification;
- A03/A04_1 authority and orchestration retained as baseline;
- asset-owner hierarchy, Security and Compliance integration, document metadata ownership, staged-plan policy, and document-generation gate require clarification;
- A04_2/WP spine retained as baseline;
- WP action catalog, schedule-apply naming, staged preview IDs, external execution evidence boundary, schema references, user-driven baseline fields, and selector/context naming require cleanup;
- governed library spine retained, but TP/PS/PROF/CAL data and schemas require normalization;
- Planning retained as proposal-only, but Planning action naming, apply boundary, unit handling, and provenance stamps require alignment.

---

## DEC-0056 — Keep K&S read-only authority model

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 Knowledge & Standards
Category: Keep
Decision: Keep K&S as the read-only governed authority for curated reference metadata, bundles, anchors, citation policies, template versions, and required-input definitions.
Reason: A12 clearly defines K&S as an immutable, versioned, read-only source of governed reference assets and separates it from WP truth, DOC outputs, RPT outputs, and approvals.
Impact: Downstream Document Factory, Reporting, and advisory responses must consume K&S as controlled reference authority rather than embedding uncontrolled standards content.
Follow-up: Confirm implementation contracts and schemas enforce the model before freeze.

## DEC-0057 — Keep anchored citation and excerpt-policy model

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 Knowledge & Standards
Category: Keep
Decision: Keep the anchored citation model and excerpt-policy controls as the K&S citation baseline.
Reason: A12 requires citations to be precise, stable, versioned, anchored, and governed; it also defines excerpt policies for metadata-only, public excerpt, internal-only, and no-excerpt handling.
Impact: Document generation and standards-aware advice must use anchored references and must not output restricted excerpts.
Follow-up: Reconcile contract/schema enforcement gaps in DEC-0061 and DEC-0062.

## DEC-0058 — Keep K&S contract as candidate, but not freeze-clean

Date: 2026-06-10
Reviewed file/block: Phase 7 — `VALOR-contract-orch-ks.yaml`
Category: Keep
Decision: Keep the K&S contract as a useful candidate contract.
Reason: The contract provides read-only list/read actions for standards, templates, bundles, anchors, citation resolution, and bundle validation, with Orchestration as caller and K&S as owner.
Impact: The contract can support controlled K&S access after action and schema alignment.
Follow-up: Resolve action-catalog and schema gaps before freeze.

## DEC-0059 — Add real K&S governed data or formally defer it

Date: 2026-06-10
Reviewed file/block: Phase 7 — K&S standards/bundles/templates data search
Category: Missing
Decision: Add actual K&S governed data files for standards records, bundles, anchors, and template records, or formally defer them as seed-data gaps before freeze.
Reason: A12 defines StandardRecord, TemplateRecord, Bundle, Anchor, and AnchoredRef entities, but repository search did not surface actual standards/bundle data files beyond schemas and architecture. Phase 5 also found the seed preset uses null standards bundle references.
Impact: Standards-aware document generation and advisory AI cannot be freeze-ready without at least minimal governed K&S data or a formal no-bundle/no-standards operating policy.
Follow-up: Carry to Phase 8 Document Factory and Phase 11 schema/test review.

## DEC-0060 — Clarify standards bundle nullability policy

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 and Phase 5 standards-bundle carry-forward
Category: Missing
Decision: Define whether a preset/workflow may operate without a standards bundle, and if so require an explicit no-bundle policy and output label.
Reason: A12 assumes bundles are versioned selections of standards/templates, while Phase 5 found `standards_bundle_ref: null` in the seed preset. The current architecture does not define how document generation or advisory outputs behave when no standards bundle is bound.
Impact: Without a no-bundle policy, downstream outputs may appear standards-governed when no standards authority was actually applied.
Follow-up: Resolve with K&S, Preset, Document Factory, and Reporting traceability rules.

## DEC-0061 — Reconcile A12 K&S action catalog with K&S contract

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 and K&S contract
Category: Conflict
Decision: Reconcile A12’s K&S action catalog with `VALOR-contract-orch-ks.yaml` before freeze.
Reason: A12 includes KS_VALIDATE_CITATION_SET and KS_VALIDATE_TEMPLATE_REQUIREMENTS, but the contract does not define these actions. The contract defines list/read actions, KS_LIST_ANCHORS, KS_RESOLVE_CITATION, and KS_VALIDATE_BUNDLE_INTEGRITY only.
Impact: Citation-set and template-requirement validation may be expected by Document Factory but unavailable in the actual contract.
Follow-up: Add the missing actions or explicitly move them to a later phase/deferred contract scope.

## DEC-0062 — Replace permissive K&S schemas with enforceable schemas

Date: 2026-06-10
Reviewed file/block: Phase 7 — K&S contract schemas
Category: Conflict
Decision: Replace or expand the current K&S schemas so they enforce A12 required fields and response shapes.
Reason: Core K&S schemas such as `ks_standard`, `ks_bundle`, `ks_template`, `ks_citation_resolved`, and `ks_anchors_list` currently have empty required fields, empty properties, and allow any additional properties.
Impact: The contract references schemas, but those schemas do not yet enforce the governed K&S entity model, anchor model, or citation result structure.
Follow-up: Resolve during Phase 11 schema validation and approved schema cleanup.

## DEC-0063 — Add explicit standards-aware advisory AI boundary

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 AI advisory carry-forward
Category: Modify
Decision: Add an explicit standards-aware advisory boundary for AI responses using K&S.
Reason: A12 defines read-only standards metadata and anchored citations, but it does not fully spell out advisory behavior: no unsupported standards claims, no unanchored clause references, mark missing standards as missing, avoid turning metadata into approval, and keep human acceptance required.
Impact: Advisory chat could drift into unsupported or over-authoritative standards claims unless the AI boundary is explicit.
Follow-up: Reconcile with DEC-0008 and later Document Factory/advisory UX review.

## DEC-0064 — Strengthen excerpt authorization and request semantics

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 and K&S contract excerpt behavior
Category: Modify
Decision: Strengthen contract-level excerpt handling with explicit request fields, authorization context, and response policy indicators.
Reason: A12 defines access classification and excerpt policies, and the K&S contract includes EXCERPT_BLOCKED, but the contract does not define how a caller requests an excerpt, how authorization is represented, or how applied policy is returned consistently.
Impact: Excerpt behavior may be inconsistently implemented, especially for licensed/internal/confidential content.
Follow-up: Resolve with A10 Security & Compliance and K&S contract/schema cleanup.

## DEC-0065 — Align K&S provenance with artifact-specific traceability

Date: 2026-06-10
Reviewed file/block: Phase 7 — A12 stamping/provenance
Category: Modify
Decision: Align K&S provenance requirements with the broader artifact-specific traceability model.
Reason: A12 requires DOC/RPT outputs using K&S assets to stamp bundle_id/version, template_id/version, standard_id/version, and anchors in citations. Earlier phases require artifact-specific traceability for documents, reports, exports, and advisory outputs.
Impact: K&S traceability is directionally correct but must be merged into the global stamp rules so documents and reports have consistent provenance.
Follow-up: Reconcile during Phase 8 Document Factory and Phase 9 Reporting/Export.

## DEC-0066 — Defer full K&S schema and bundle validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 7 — K&S schemas and bundle data
Category: Defer
Decision: Do not perform full K&S schema validation or create standards bundle data during Phase 7.
Reason: Phase 7 identified the relevant schemas and data gaps, but full schema/test-vector validation belongs to Phase 11 and data creation requires explicit user-approved edits.
Impact: Phase 7 is complete without implementation or architecture/spec edits; K&S validation remains a carried risk.
Follow-up: In Phase 11, validate K&S schemas and any K&S library data against A12 and the K&S contract.
