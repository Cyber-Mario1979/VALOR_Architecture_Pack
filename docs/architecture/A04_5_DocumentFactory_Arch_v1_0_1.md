---
id: VALOR-block-A04-5-document-factory-architecture
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
  - VALOR-block-A04-2-work-package-architecture
  - VALOR-block-A12-knowledge-standards-architecture
summary: "Block A04.5 — Document Factory System Architecture: generates controlled CQV documents from WP truth, source input sets, governed templates, and standards citations, producing audit-grade provenance metadata without mutating WP truth."
acceptance_criteria:
  - Defines Document Factory’s authority and non-ownership boundaries.
  - Defines entities (Document, DocumentMetadata, CitationSet, SourceInputSet, and DCF source-capture references) and required metadata fields.
  - Defines generation pipeline with source-chain validation and governance hooks.
  - Defines active and deferred contract actions for document generation.
  - Enforces provenance stamping, anchored citations, and determinism requirements.
  - Defines product-surface behavior for DRAFT, FINAL, INCOMPLETE, BLOCKED, and PRODUCT_TESTING_ONLY document outputs.
  - Defines error taxonomy and safe failure behavior suitable for CQV audit expectations.
---

# Document Factory System Architecture

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Document Factory (DOC) is the subsystem responsible for producing controlled CQV document drafts and finalized document artifacts from:

- authoritative WP/task truth (WP System);
- source input sets, including optional DCF references where available;
- governed templates (K&S);
- governed standards bundles and anchored citations (K&S);
- user-supplied project specifics captured through WP fields, DCF/source-capture records, or explicit validated inputs.

DOC is authoritative for:

- generated document artifact content;
- generated document provenance metadata;
- deterministic rendering and content assembly rules;
- source-chain validation for document generation and finalization.

DOC is not authoritative for:

- WP/task truth;
- DCF source truth or user/site source ownership;
- template truth;
- standards/bundle/citation truth;
- planning truth;
- approvals/signatures.

DOC must not mutate WP truth, template truth, K&S truth, or DCF/source-capture truth.

---

## 2. Boundary and Non-Ownership Rules

### 2.1 DOC Owns

- Generated document artifacts and their lifecycle state.
- Document content outputs where supported by approved renderer policy.
- Document metadata records, including doc_id, versions, stamps, citations, checksums, and source-chain provenance.
- Validation rules specific to document completeness, template requirements, source-input completeness, and finalization readiness.

### 2.2 DOC Does Not Own

- WP/task truth.
- Standards/template truth (read-only consumption from K&S).
- DCF/source-capture truth (read-only consumption as source input).
- Export/report truth (RPT subsystem).
- Approvals and signatures.

---

## 3. Core Entities (Authoritative Data Model)

### 3.1 Document

A Document is a generated artifact associated with a WP.

Required fields:

- doc_id (string, immutable)
- doc_type (enum): DCF | VMP | URS | RA | RTM | DQ | IQ | OQ | PQ | VSR | REPORT
- doc_version (string; semver or incrementing)
- wp_id (string)
- state (enum): DRAFT | REVIEW_READY | FINAL | INCOMPLETE | BLOCKED
- created_at_utc, updated_at_utc
- template_ref: {template_id, template_version}
- bundle_ref: {bundle_id, bundle_version} (if applicable)
- citation_set (if standards/templates/citations are used)
- source_chain_provenance
- content_format (enum): MARKDOWN | DOCX | PDF (policy-dependent)
- content (string or binary reference)
- checksum (string) (for FINAL, mandatory)

### 3.2 DCF Source-Capture Concept and Governance Record

DCF is a source-capture / input-collection document type or concept for DOC source-chain purposes.

DCF may be referenced by DOC through:

- `dcf_ref`; or
- `source_input_set` entries.

`TPL-DCF_v1.0.1.yaml` exists as a governed PRODUCT_TESTING_ONLY DCF source-capture template family metadata record with four domain variants:

- Cleanroom;
- Computerized Systems;
- Process Equipment;
- Utilities.

DCF artifact generation and DCF artifact finalization are not active in Blocker 7A. If `doc_type: DCF` is requested for generation or finalization, DOC must return `BLOCKED` or `INCOMPLETE` behavior unless DCF generation/finalization is separately activated by an approved scoped change.

`TPL-DCF_v1.0.1` membership in `BND-CQV-BASE_v1.0.1` is PRODUCT_TESTING_ONLY source-capture governance. It does not approve real regulated CQV/GMP use.

### 3.3 SourceInputSet

A SourceInputSet is the validated set of source inputs supplied to DOC for generation. It may include WP-derived fields, DCF references, user-entered source fields, and source completion status.

For URS generation, the source input set must cover the required URS source-input family where applicable:

- intended use;
- GMP relevance;
- user needs;
- critical requirements;
- interfaces;
- constraints;
- assumptions;
- acceptance expectations.

If required source fields are missing, DOC must block generation/finalization or mark the output incomplete according to explicit incomplete-output policy. DOC must not invent missing source data.

### 3.4 DocumentMetadata (Provenance Record)

A provenance record is mandatory for audit-grade outputs.

Required fields:

- doc_id
- doc_version
- generation_action_id (ACT-*)
- generation_timestamp_utc
- inputs_snapshot:
  - wp_snapshot_hash
  - source_input_set_hash
  - dcf_ref or dcf_snapshot_hash where DCF is used
  - user_inputs_hash (optional)
- source_input_completion_status
- source_chain_provenance
- stamps (see §6)
- citations (see §3.5)
- validation_summary (errors/warnings)
- generator_version (doc_factory_version)

### 3.5 CitationSet (Anchored References)

Citations must be stable and anchored.

Citation item fields:

- asset_type: internal_standard | template | bundle | source_anchor
- asset_id
- asset_version
- anchor_id
- anchor_title
- excerpt_policy: METADATA_ONLY | INTERNAL_ONLY | NO_EXCERPTS
- lifecycle_status
- usage_classification
- regulated_output_allowed
- retrieval_timestamp_utc (optional)

External standards text must not be reproduced by DOC. DOC must rely on K&S-resolved internal requirements, controlled source-anchor metadata, and excerpt/refusal policy.

---

## 4. URS Source Chain

URS is a generated controlled DOC output. For URS generation:

- `doc_type` must be `URS`.
- DOC consumes authoritative WP truth.
- DOC may consume `dcf_ref` and/or `source_input_set`.
- DOC consumes governed `template_ref` for `TPL-URS`.
- DOC consumes governed `bundle_ref` and `citation_set` from K&S.
- DOC consumes provenance stamps for WP, preset/task pool/profile/calendar where relevant, template, bundle, internal standard, contract, and K&S status.

URS generation must not infer or invent intended use, GMP relevance, user needs, critical requirements, interfaces, constraints, assumptions, or acceptance expectations. Missing required source data must produce BLOCKED or INCOMPLETE behavior.

---

## 5. Document Lifecycle and Product Surface

### 5.1 States

- DRAFT: generated content intended for iterative editing.
- REVIEW_READY: content passes completeness checks and is ready for formal review.
- FINAL: content is finalized with checksum; further edits require new version.
- INCOMPLETE: content is explicitly incomplete because required source-chain, stamp, template, bundle, citation, or testing-only data is missing.
- BLOCKED: generation or finalization is refused because a hard gate is not satisfied.
- PRODUCT_TESTING_ONLY: generated output or governed template/standards basis may support product testing only and must not be represented as regulated-ready CQV/GMP output.

### 5.2 Active Lifecycle Actions

Only these DOC actions are active for the current declared scope:

- `DOC_GENERATE_DRAFT`
- `DOC_FINALIZE_ARTIFACT`

### 5.3 Deferred Lifecycle Actions

The following actions are not active in Blocker 7A and must not be treated as freeze-ready unless later approved:

- `DOC_VALIDATE`
- `DOC_MARK_REVIEW_READY`
- `DOC_REGENERATE`
- `DOC_GET`
- `DOC_LIST`

Hard rule:

- FINAL documents are immutable; new changes require a new doc_version.
- Finalization must refuse or mark incomplete if the draft lacks required source-chain provenance, template_ref, bundle_ref, citation_set, provenance_stamps, required testing-only stamp, source-input completion status, or checksum/final artifact metadata.
- Contract/audit/provenance metadata timestamps use UTC. Optional local display time may be shown only if explicitly labeled as display/local time.

---

## 6. Traceability and Stamping (Mandatory)

### 6.1 Required Stamp Set

A generated document must include, at minimum:

- preset_id/version (if preset-driven)
- profile_id/version (if schedule/durations referenced or required by template)
- task_pool_id/version (if tasks derived from task pool)
- calendar_id/version and canonical calendar version where relevant
- standards_bundle_id/version/status/usage classification where any standards or templates are referenced
- internal_standard_id/version where citation requirements are used
- template_id/version (always)
- source_input_set_ref or source_input_set_hash
- dcf_ref or dcf_snapshot_hash where DCF is used
- source_input_completion_status
- testing-only output stamp when K&S/template/bundle/citation assets are TESTING_ONLY / PRODUCT_TESTING_ONLY
- doc_factory_version
- contract_id/version used for DOC call

### 6.2 Stamp Placement

DOC must ensure stamps appear in:

- document header / document control section;
- document metadata record.

If a required stamp is missing, DOC must refuse or mark incomplete with:

- INVARIANT_VIOLATION / MISSING_TRACEABILITY_STAMPS; or
- VALIDATION_ERROR / SOURCE_CHAIN_PROVENANCE_MISSING.

### 6.3 K&S TESTING_ONLY Boundary

K&S remains the governed authority for templates, standards bundles, anchors, source mappings, and citation policy.

If template_ref, bundle_ref, internal standards, source anchors, or citation refs are TESTING_ONLY / PRODUCT_TESTING_ONLY, DOC output may support product testing only and must carry the required testing-only stamp:

`PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE.`

PRODUCT_TESTING / FIELD_TRIAL mode allows full DOC draft/final artifact generation for active document types, provided outputs carry the required testing-only stamp where applicable and are not represented as official GMP records.

FIELD_TRIAL is an operating label under PRODUCT_TESTING_ONLY, not a new schema/machine enum.

Source metadata acceptance is not required for PRODUCT_TESTING / FIELD_TRIAL document generation testing.

REGULATED_RELEASE remains conditional upon K&S/source metadata acceptance, template source metadata acceptance, and any required user/site acceptance gates.

DCF artifact generation/finalization remains inactive unless separately activated.

---

## 7. Generation Pipeline (Implementation-Ready)

### 7.1 Pipeline Stages

1) **Resolve Inputs**
   - Fetch WP truth snapshot (WP_GET).
   - Resolve source_input_set and optional dcf_ref.
   - Fetch template governance record and template reference from K&S (KS_READ_TEMPLATE).
   - Fetch standards bundle (KS_READ_BUNDLE) if applicable.
   - Validate required source inputs (template.required_inputs and source-chain policy).

2) **Validate Source Chain**
   - Confirm required source fields are present.
   - Confirm source input completion status.
   - Confirm DCF/source-capture provenance where DCF is referenced.
   - Refuse or mark incomplete where source data is missing.
   - Do not invent missing source data.

3) **Assemble Content**
   - Populate template placeholders using WP truth and validated source input fields.
   - Insert sections from task list if required.
   - Insert citations or references using K&S-resolved anchored citation objects.

4) **Validate Completeness**
   - Ensure required sections are populated or explicitly marked incomplete.
   - Ensure required citations are present where template mandates.
   - Ensure stamps are present.

5) **Render Output**
   - Generate Markdown baseline if rendering is supported.
   - If DOCX/PDF supported: render deterministically from approved source blocks.

6) **Finalize**
   - Confirm draft source-chain provenance.
   - Confirm template_ref, bundle_ref, citation_set, provenance_stamps, testing-only stamp, and source-input completion status.
   - Generate checksum.
   - Lock as FINAL or mark incomplete if controlled finalization requirements are not met.

### 7.2 Determinism Requirements

Given the same:

- WP snapshot;
- source_input_set;
- DCF reference/snapshot where used;
- template version;
- bundle version;
- citation set;
- user inputs;
- DOC version;

the output must be the same (content + checksum).

---

## 8. Document Factory Contract (Implementation-Ready)

DOC is invoked via `VALOR-contract-orch-doc`.

### 8.1 Active Actions

- `DOC_GENERATE_DRAFT`
- `DOC_FINALIZE_ARTIFACT`

### 8.2 Deferred Actions

Deferred unless later explicitly approved:

- `DOC_VALIDATE`
- `DOC_MARK_REVIEW_READY`
- `DOC_REGENERATE`
- `DOC_GET`
- `DOC_LIST`

### 8.3 Canonical Request Envelope (Generate URS Draft)

```json
{
  "contract": "VALOR-contract-orch-doc",
  "contract_version": "v1.0.1",
  "action_id": "ACT-000310",
  "action_type": "DOC_GENERATE_DRAFT",
  "mode": "EXECUTION",
  "target": {"wp_id": "WP-0007"},
  "payload": {
    "doc_type": "URS",
    "wp_snapshot": {"wp_id": "WP-0007", "tasks": "omitted_for_brevity"},
    "template_ref": {"template_id": "TPL-URS", "template_version": "v1.0.1"},
    "bundle_ref": {"bundle_id": "BND-CQV-BASE", "bundle_version": "v1.0.1", "status": "TESTING_ONLY", "usage_classification": "PRODUCT_TESTING_ONLY"},
    "source_input_set": {
      "source_input_set_id": "SRC-URS-0001",
      "source_input_completion_status": "COMPLETE_OR_INCOMPLETE",
      "required_fields_status": "omitted_for_brevity"
    },
    "dcf_ref": {"dcf_id": "DCF-0001", "dcf_status": "SOURCE_CAPTURE_ONLY"},
    "citation_set": [
      {"asset_type": "internal_standard", "asset_id": "STD-CQV-BASE", "asset_version": "v1.0.1", "anchor_id": "CQV-REQ-002"}
    ],
    "provenance_stamps": {
      "preset_ref": {"preset_id": "PS-PE-HIGH", "preset_version": "v1.0.1"},
      "profile_ref": {"profile_id": "PROF-PE-HIGH", "profile_version": "v1.0.1"},
      "task_pool_ref": {"task_pool_id": "TP-PE-HIGH", "task_pool_version": "v1.0.1"},
      "calendar_ref": {"calendar_id": "CAL-WORKWEEK", "calendar_version": "v1.0.1", "canonical_calendar_version": "v1"},
      "template_ref": {"template_id": "TPL-URS", "template_version": "v1.0.1"},
      "bundle_ref": {"bundle_id": "BND-CQV-BASE", "bundle_version": "v1.0.1", "status": "TESTING_ONLY"}
    },
    "testing_only_stamp": "PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE."
  },
  "options": {"return_content": true},
  "context": {"timestamp_utc": "2025-12-22T00:00:00Z"}
}
```

### 8.4 Canonical Response Envelope

```json
{
  "contract": "VALOR-contract-orch-doc",
  "contract_version": "v1.0.1",
  "action_id": "ACT-000310",
  "ok": true,
  "result": {
    "doc_id": "DOC-0005",
    "doc_type": "URS",
    "doc_version": "v1.0.1",
    "state": "DRAFT",
    "content_format": "MARKDOWN",
    "content": "# URS\n...",
    "metadata": {
      "template_ref": {"template_id": "TPL-URS", "template_version": "v1.0.1"},
      "bundle_ref": {"bundle_id": "BND-CQV-BASE", "bundle_version": "v1.0.1", "status": "TESTING_ONLY"},
      "source_input_completion_status": "COMPLETE_OR_INCOMPLETE",
      "stamps": "omitted_for_brevity",
      "citations": []
    }
  },
  "error": null
}
```

---

## 9. Error Semantics (Document Factory)

Standard codes:

- VALIDATION_ERROR: missing required input fields, invalid template refs, incomplete source-chain data.
- INVARIANT_VIOLATION: missing stamps, attempt to mutate WP truth, finalize without checksum, finalize without required source-chain controls.
- MODE_VIOLATION: wrong mode.
- NOT_FOUND: missing template/bundle/wp/doc/draft/source reference.
- CONFLICT: ambiguous version refs, incompatible template vs doc_type.
- UNSUPPORTED_OPERATION: unsupported format request, blocked DCF artifact generation, blocked external excerpts.
- INTERNAL_ERROR: unexpected.

DOC-specific subcodes:

- TEMPLATE_REQUIRED_INPUT_MISSING
- SOURCE_INPUT_REQUIRED_FIELD_MISSING
- SOURCE_CHAIN_PROVENANCE_MISSING
- DCF_ARTIFACT_GENERATION_DEFERRED
- TESTING_ONLY_REGULATED_OUTPUT_BLOCKED
- MISSING_TRACEABILITY_STAMPS
- CANNOT_FINALIZE_WITH_ERRORS
- FINAL_IMMUTABLE
- FORMAT_NOT_SUPPORTED
- CITATION_ANCHOR_MISSING

Example error:

```json
{
  "code": "VALIDATION_ERROR",
  "subcode": "SOURCE_INPUT_REQUIRED_FIELD_MISSING",
  "message": "Cannot generate URS: missing required source input intended_use.",
  "field": "source_input_set.intended_use",
  "entity": "source_input_set",
  "remediation": "Provide the missing source input through DCF/source capture or mark the output incomplete."
}
```

---

## 10. Integration Points

- Orchestration coordinates DOC flows and enforces gates/confirmations.
- WP System provides authoritative snapshots; DOC must not patch WP truth.
- DCF/source capture provides source inputs where available; DOC must not create or approve DCF source truth.
- K&S provides templates, bundles, anchors, standards, citation policy, lifecycle status, and testing-only/regulated-use gates.
- Reporting may reference doc metadata for traceability but does not own docs.

---

---

## CHANGELOG
| Date       | Changes     | Type / Version |
| ---------- | ----------- | -------------- |
| 2026-06-12 | Blocker 7A DOC product-surface wording: DRAFT/FINAL/INCOMPLETE/BLOCKED/PRODUCT_TESTING_ONLY states aligned; TPL-DCF recognized as product-testing metadata while DCF artifact generation/finalization remains inactive | Pre-freeze controlled update |
| 2026-06-12 | Blocker 6A DOC/DCF/URS source-chain alignment: DCF source-capture concept declared, URS source chain defined, active/deferred DOC actions aligned, K&S TESTING_ONLY regulated-use block preserved | Pre-freeze controlled update |
| 2025-12-23 | First Issue | Arch_v1.0.1    |
