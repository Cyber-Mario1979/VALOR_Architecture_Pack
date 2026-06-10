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

DEC-0001 through DEC-0066 were logged during Phases 0 through 7 and remain active.

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
- Planning retained as proposal-only, but Planning action naming, apply boundary, unit handling, and provenance stamps require alignment;
- K&S retained as read-only citation/standards authority, but K&S data, schemas, contract actions, excerpt authorization, and standards-aware advisory boundary require cleanup.

---

## DEC-0067 — Keep Document Factory authority and lifecycle baseline

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 Document Factory
Category: Keep
Decision: Keep A04_5 as the baseline for DOC authority, non-ownership rules, document lifecycle, provenance metadata, and deterministic generation pipeline.
Reason: A04_5 clearly states DOC generates controlled CQV documents from WP truth, governed templates, standards bundles/citations, and user inputs; owns document artifacts/metadata/rendering; does not mutate WP truth; and cannot own approvals/signatures.
Impact: DOC can be retained as the document artifact/provenance owner, while WP remains the source of WP/task truth and humans remain responsible for approval.
Follow-up: Reconcile contract/schema/template gaps before freeze.

## DEC-0068 — Keep human review and finalization boundary

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 Document Factory
Category: Keep
Decision: Keep the DRAFT → REVIEW_READY → FINAL lifecycle and the requirement for explicit confirmation before finalization.
Reason: A04_5 defines document states, validation gates, final checksum, immutability of final documents, and user confirmation for finalization.
Impact: Document generation remains controlled and review-gated rather than auto-approved.
Follow-up: Ensure DOC contract exposes the lifecycle actions needed to enforce the model.

## DEC-0069 — Keep token-clean final-output rule, but replace Canvas terminology

Date: 2026-06-10
Reviewed file/block: Phase 8 — Document Generation Compliance Addendum
Category: Modify
Decision: Keep the token-clean/no-runtime-footer rules for final document outputs, but replace Canvas-specific wording with product-neutral document artifact terminology before freeze.
Reason: The addendum correctly requires final documents to contain no template tokens/placeholders and no runtime/footer guidance, but it describes each document as a separate Canvas object, which is UI-specific and may confuse architecture/product surfaces.
Impact: Final output cleanliness is preserved while avoiding legacy or surface-specific terminology in the frozen spec.
Follow-up: Edit addendum only after explicit user approval.

## DEC-0070 — Add DCF intake and extraction model

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5, DOC contract, templates, addendum
Category: Missing
Decision: Add an explicit DCF intake model, including DCF source object, extraction behavior, candidate field mapping, human acceptance, and provenance.
Reason: Phase 8 scope requires DCF intake and AI extraction review, but A04_5 and the DOC contract do not define DCF intake, DCF-derived source fields, extraction actions, confidence/review states, or candidate-only acceptance. Search for DCF surfaced no concrete DCF model/template in scoped assets.
Impact: The DCF → URS flow remains incomplete and cannot be considered freeze-ready.
Follow-up: Resolve in an approved Document Factory/DCF modification batch.

## DEC-0071 — Add accepted URS source-of-truth dependency for downstream documents

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 and templates
Category: Missing
Decision: Add an explicit rule that downstream RTM/DQ/IQ/OQ/PQ/VSR generation must depend on an accepted or human-approved URS source, with traceable URS references.
Reason: The RTM template describes traceability of URS requirements through the validation lifecycle, but A04_5 does not define accepted URS as the source gate for downstream document generation.
Impact: Downstream document generation may proceed without a governed accepted URS source unless the dependency is specified.
Follow-up: Add source-chain rules during approved Document Factory edits; verify in Phase 11 test vectors.

## DEC-0072 — Reconcile DOC architecture action catalog with DOC contract

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 and `VALOR-contract-orch-doc.yaml`
Category: Conflict
Decision: Reconcile the DOC action catalog before freeze.
Reason: A04_5 lists DOC_GENERATE_DRAFT, DOC_VALIDATE, DOC_MARK_REVIEW_READY, DOC_FINALIZE, DOC_REGENERATE, DOC_GET, and DOC_LIST. The DOC contract exposes only DOC_GENERATE_DRAFT and DOC_FINALIZE_ARTIFACT.
Impact: The lifecycle cannot be fully contract-enforced if validation, review-ready transition, regeneration, get, and list actions are absent or renamed.
Follow-up: Choose canonical DOC action names and update architecture/contract after approval.

## DEC-0073 — Add orchestration-level document-generation gate

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 carry-forward from Phase 3
Category: Missing
Decision: Add an orchestration-level document-generation gate that coordinates draft, validate, review-ready, finalize, and regenerate flows.
Reason: A04_5 defines a document lifecycle and pipeline, but earlier A04_1 gate list did not include document-generation. The document flow should be visible as a governed orchestration gate, not just a DOC-internal pipeline.
Impact: Product workflow and implementation may omit required review/confirmation states unless the gate is explicit.
Follow-up: Update A04_1/A04_5 together when edits are approved.

## DEC-0074 — Resolve timestamp policy conflict

Date: 2026-06-10
Reviewed file/block: Phase 8 — templates and document-generation addendum
Category: Conflict
Decision: Resolve timestamp naming and timezone policy before freeze.
Reason: The document templates use `Generated (UTC)` and `doc.generated_utc`, while the addendum requires timestamps in `dd-mm-yyyy HH:MM Africa/Cairo` and says not to label timestamps as UTC unless they are actually UTC.
Impact: Generated documents may violate the addendum or produce inconsistent timestamp provenance.
Follow-up: Standardize document timestamp fields and display labels during approved template/schema cleanup.

## DEC-0075 — Fix document render-input schema required-field semantics

Date: 2026-06-10
Reviewed file/block: Phase 8 — document schemas
Category: Conflict
Decision: Fix document render-input schemas so required nested fields are enforceable under JSON Schema.
Reason: The URS render-input schema lists required values such as `doc.actors.approver` and `doc.stamps.bundle.id` as dotted strings in the top-level `required` array, which does not enforce nested object requirements in JSON Schema.
Impact: Template rendering may pass validation even when nested required values are missing.
Follow-up: Resolve in Phase 11 schema cleanup.

## DEC-0076 — Replace permissive DOC result schemas with enforceable schemas

Date: 2026-06-10
Reviewed file/block: Phase 8 — DOC result schemas
Category: Conflict
Decision: Replace or expand DOC draft/artifact result schemas so they enforce A04_5 document and metadata result structures.
Reason: `doc_draft_result.schema.json` and `doc_artifact_result.schema.json` currently have empty required fields and properties and allow all additional properties.
Impact: Contract result validation does not enforce doc_id, doc_type, state, content_format, metadata, stamps, citations, checksum, or validation summary.
Follow-up: Resolve during Phase 11 schema validation.

## DEC-0077 — Align document metadata schema with A04_5 provenance model

Date: 2026-06-10
Reviewed file/block: Phase 8 — document metadata schema and A04_5
Category: Modify
Decision: Align `document_metadata_schema.json` with A04_5 provenance requirements.
Reason: A04_5 requires generation_action_id, generation_timestamp_utc, input snapshot hashes, stamps, citations, validation_summary, and generator_version. The current document metadata schema only requires id and title and treats many fields as optional/additional.
Impact: Audit-grade provenance is not schema-enforced.
Follow-up: Resolve during Phase 11 object schema review.

## DEC-0078 — Align template IDs and naming with DOC/K&S architecture

Date: 2026-06-10
Reviewed file/block: Phase 8 — templates, template index, A04_5/A12 carry-forward
Category: Modify
Decision: Align template IDs/names with A04_5 and K&S TemplateRecord expectations.
Reason: A04_5 examples use template IDs such as TPL-URS; the DOC contract example uses TMP-URS; actual templates use IDs such as T4 and filenames such as T4_URS_Template_V1_0_1.md.
Impact: DOC/K&S template lookup and provenance stamps can drift unless IDs are canonical.
Follow-up: Normalize during K&S/template/schema cleanup.

## DEC-0079 — Resolve K&S bundle/citation dependency for document generation

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5, DOC contract, Phase 7 carry-forward
Category: Missing
Decision: Resolve how DOC behaves when K&S bundle/citation data is absent or null.
Reason: A04_5 requires templates, bundles, and anchored citations when applicable, while Phase 7 found K&S governed data missing or not discoverable and Phase 5 found a null standards bundle in the seed preset.
Impact: Standards-aware document generation cannot be freeze-ready without either real K&S data or a formal no-bundle/no-standards mode.
Follow-up: Resolve with K&S and Document Factory before freeze.

## DEC-0080 — Add explicit AI extraction/drafting boundary for documents

Date: 2026-06-10
Reviewed file/block: Phase 8 — A04_5 and DOC contract
Category: Missing
Decision: Add explicit AI extraction/drafting boundaries for document generation.
Reason: A04_5 supports user inputs and template population, but it does not define AI extraction from source documents, candidate-only drafting, confidence/uncertainty handling, human acceptance, or how missing fields are treated before review-ready/final states.
Impact: Document drafting could drift into unsupported content generation or implied acceptance.
Follow-up: Reconcile with DEC-0008 and DEC-0063 in an approved AI/document boundary update.

## DEC-0081 — Defer detailed document schema/template validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 8 — document schemas/templates
Category: Defer
Decision: Do not perform full document schema/template validation during Phase 8.
Reason: Phase 8 identified schema/template alignment issues, but formal validation across all document templates and schemas belongs to Phase 11.
Impact: Phase 8 is complete without schema or template edits.
Follow-up: In Phase 11, validate all document schemas/templates against A04_5, the DOC contract, and the compliance addendum.
