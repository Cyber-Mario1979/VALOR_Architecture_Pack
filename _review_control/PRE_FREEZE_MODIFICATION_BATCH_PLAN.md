# Pre-Freeze Modification Batch Plan

Status: PREPARED
Review branch: review-spec-freeze-control
Date: 2026-06-10

## 0. Purpose

This plan converts the completed no-freeze review into a controlled specification-edit batch.

It does **not** authorize implementation.
It does **not** create a delivery plan.
It does **not** create a clean implementation repository.
It does **not** edit architecture/spec files yet.

The batch objective is to turn the current candidate architecture pack into a freeze-ready specification authority.

Source inputs:

- `_review_control/PHASE13_FINAL_FREEZE_REVIEW.md`
- `_review_control/SESSION_HANDOFF.md`
- `_review_control/DECISION_LOG.md`
- `_review_control/PHASE12_DECISIONS_PENDING.md`

## 1. Batch Outcome

The batch is successful when:

1. all no-freeze blockers from Phase 13 are resolved or formally deferred;
2. architecture, contracts, action blocks, schemas, libraries, templates, addendums, test vectors, and validation scripts are internally aligned;
3. Canvas-specific wording is removed or replaced with product-neutral surface language;
4. the pack can be honestly labeled freeze-ready;
5. the user can decide whether to freeze the pack and then move to delivery-plan creation.

## 2. Exact Files to Edit or Create

### 2.1 Control Files

Edit:

- `_review_control/DECISION_LOG.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`
- `_review_control/PHASE12_DECISIONS_PENDING.md`
- `_review_control/PHASE13_FINAL_FREEZE_REVIEW.md`

Create if needed:

- `_review_control/FREEZE_READINESS_CHECKLIST.md`
- `_review_control/FREEZE_MODIFICATION_CHANGELOG.md`

Purpose:

- merge pending Phase 12 decisions into the main decision log or mark them consolidated;
- track each pre-freeze edit against a decision ID;
- preserve review memory and freeze readiness criteria.

### 2.2 Pack Positioning / Status / Glossary

Edit:

- `README.md`
- `manifest.yaml` after all content edits
- `docs/architecture/A00_Specs_Architecture_Pack_Arch_v1_0_1.md`
- `docs/architecture/A01_SoS_Context_Capability_Arch_v1_0_1.md`
- `docs/architecture/A02_Principles_Invariants_Arch_v1_0_1.md`
- `docs/architecture/A03_Subsystems_Authority_Arch_v1_0_1.md`
- `docs/architecture/A09_Governance_Branching_Arch_v1_0_1.md`
- `docs/architecture/A10_Security_Compliance_Arch_v1_0_1.md`
- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`
- `docs/architecture/A15_Global_Glossary_Arch_v1_0_1.md`

Purpose:

- remove misleading “implementation-ready / fully aligned” claims until freeze-ready;
- define status taxonomy: released, candidate, freeze-ready, frozen, proposed, applied, final, closed;
- clarify Security & Compliance as policy-first unless separated as a callable subsystem;
- clarify subsystem/library ownership hierarchy.

### 2.3 Contract and Action Registry

Edit:

- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`
- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-wp.yaml`
- `contracts/VALOR-contract-orch-wp-user-driven-baseline.yaml`
- `contracts/VALOR-contract-orch-plan.yaml`
- `contracts/VALOR-contract-orch-doc.yaml`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `contracts/VALOR-contract-orch-ks.yaml`
- `contracts/VALOR-contract-orch-ps.yaml`
- `action_blocks/WP_UPDATE_TASK_FIELDS.yaml`
- `action_blocks/WP_BIND_PRESET_CONTEXT.yaml`
- `action_blocks/WP_APPLY_PLAN_PROPOSAL.yaml`
- `action_blocks/BUILD_REPORT.yaml`

Create:

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Create or formally defer in `CONTRACT_REGISTRY_v1.0.1.yaml`:

- `contracts/VALOR-contract-orch-tp.yaml`
- `contracts/VALOR-contract-orch-prof.yaml`
- `contracts/VALOR-contract-orch-cal.yaml`
- `contracts/VALOR-contract-orch-sec.yaml`

Purpose:

- define one canonical action catalog;
- map public command vocabulary to contract action types;
- declare required, optional, special-purpose, and deferred contracts;
- align architecture action names with contract/action-block names.

### 2.4 Work Package / Planning / Governed Libraries

Edit:

- `docs/architecture/A04_2_WorkPackage_Arch_v1_0_1.md`
- `docs/architecture/A04_4_Planning_Arch_v1_0_1.md`
- `docs/architecture/A05_TaskPool_Arch_v1_0_1.md`
- `docs/architecture/A06_PresetSystem_Arch_v1_0_1.md`
- `docs/architecture/A07_CalendarLogic_Arch_v1_0_1.md`
- `docs/architecture/A08_ProfileLibrary_Arch_v1_0_1.md`
- `libraries/task_pool/TP-PE-HIGH_v1.0.1.yaml`
- `libraries/preset_library/PS-PE-HIGH_v1.0.1.yaml`
- `libraries/profile_library/PROF-PE-HIGH_v1.0.1.yaml`
- `libraries/calendar/CAL-WORKWEEK_v1.0.1.yaml`

Purpose:

- standardize selector/context/stamp naming;
- normalize task/profile taxonomy;
- remove or reclassify profile/calendar rule duplication;
- define duration-unit handling;
- define no-profile/user-driven baseline planning behavior;
- resolve FAT execution chain scope;
- define staged planning policy.

### 2.5 Knowledge & Standards

Edit:

- `docs/architecture/A12_Knowledge_Standards_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-ks.yaml`
- `schemas/contracts/ks_standard.schema.json`
- `schemas/contracts/ks_standards_list.schema.json`
- `schemas/contracts/ks_bundle.schema.json`
- `schemas/contracts/ks_bundles_list.schema.json`
- `schemas/contracts/ks_template.schema.json`
- `schemas/contracts/ks_templates_list.schema.json`
- `schemas/contracts/ks_anchors_list.schema.json`
- `schemas/contracts/ks_citation_resolved.schema.json`
- `schemas/contracts/ks_bundle_validation.schema.json`

Create minimal K&S data or explicitly create a no-bundle policy file:

- `libraries/knowledge_standards/README.md`
- `libraries/knowledge_standards/bundles/BND-CQV-BASE_v1.0.1.yaml`
- `libraries/knowledge_standards/standards/STD-CQV-BASE_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-URS_v1.0.1.yaml`

Purpose:

- decide whether minimal governed K&S data ships in v1;
- define no-bundle/no-standards behavior if data is deferred;
- enforce anchored citation schemas;
- define excerpt authorization/redaction request and output semantics;
- define standards-aware advisory boundaries.

### 2.6 Document Factory / DCF / URS Source Chain

Edit:

- `docs/architecture/A04_5_DocumentFactory_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-doc.yaml`
- `schemas/objects/document_metadata_schema.json`
- `schemas/contracts/doc_draft_result.schema.json`
- `schemas/contracts/doc_artifact_result.schema.json`
- `schemas/documents/index.json`
- `templates/T4_URS_Template_V1_0_1.md`
- `templates/T5_RTM_Template_V1_0_1.md`
- `templates/T6_DQ_Template_V1_0_1.md`
- `templates/T7_IQ_Protocol_Template_V1_0_1.md`
- `templates/T8_OQ_Protocol_Template_V1_0_1.md`
- `templates/T9_PQ_Protocol_Template_V1_0_1.md`
- `templates/T10_VSR_Template_V1_0_1.md`

Create:

- `docs/architecture/A04_5A_DCF_Intake_SourceChain_Arch_v1_0_1.md`
- `schemas/objects/dcf_source_schema.json`
- `schemas/objects/urs_source_chain_schema.json`
- `test_vectors/expected_dcf_intake_candidate.json`
- `test_vectors/expected_accepted_urs_source_chain.json`

Purpose:

- define DCF intake object;
- define AI extraction as candidate-only;
- define extraction confidence/review/acceptance states;
- define accepted URS source gate for RTM/DQ/IQ/OQ/PQ/VSR;
- align document lifecycle/action catalog;
- align template IDs and timestamp policy;
- enforce token-clean output validation.

### 2.7 Reporting & Export

Edit:

- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `action_blocks/BUILD_REPORT.yaml`
- `schemas/contracts/report_result.schema.json`
- `schemas/contracts/export_result.schema.json`
- `schemas/objects/csv_export_schema.json`

Create if export remains in scope:

- `action_blocks/RPT_GENERATE_EXPORT.yaml`
- `schemas/contracts/export_request.schema.json`
- `templates/export/WP_TASK_EXPORT_v1.0.1.csv.header`

Purpose:

- decide whether export is included in freeze or formally deferred;
- define export action path;
- define CSV header/template source;
- align report/export schema with A04_6;
- separate proposed from committed schedule fields;
- define artifact registry/read behavior or defer explicitly.

### 2.8 Product Surface / UX Addendums

Edit:

- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Canvas_Rendering_Record_Layout_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Document_Generation_Compliance_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Planning_Invariants_UX_Contract_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Reporting_Export_Projection_Contract_v1.0.1A.md`

Create:

- `docs/architecture/A13_Product_Surface_Arch_v1_0_1.md`

Purpose:

- replace Canvas terminology with product-neutral surface terminology;
- classify UI/product surfaces as projections, not truth owners;
- define minimum required product surfaces and states;
- define confirmation/review, advisory/help, export/download, DCF/URS/K&S/redaction, validation-error, and artifact-state surfaces;
- defer detailed wireframes only.

### 2.9 Schemas, Validation, Test Vectors

Edit:

- `schemas/contracts/contract_request.schema.json`
- `schemas/contracts/contract_response.schema.json`
- `schemas/objects/work_package_schema.json`
- `schemas/objects/task_schema.json`
- `schemas/contracts/staged_task_set.schema.json`
- `schemas/contracts/plan_proposal.schema.json`
- `schemas/contracts/plan_validation_result.schema.json`
- `schemas/contracts/preset.schema.json`
- `schemas/contracts/ps_presets_list.schema.json`
- `schemas/contracts/ps_resolve_result.schema.json`
- `schemas/contracts/report_result.schema.json`
- `schemas/contracts/export_result.schema.json`
- `schemas/documents/*.schema.json`
- `validation/validate_render_inputs.py`
- `smoke_test.py`
- `scripts/pack_validation/generate_manifest.py`
- `scripts/pack_validation/verify_manifest.py`

Create:

- `schemas/objects/audit_event_schema.json`
- `schemas/objects/security_event_schema.json`
- `schemas/objects/contract_registry_schema.json`
- `validation/validate_contract_catalog.py`
- `validation/validate_architecture_traceability.py`
- `test_vectors/negative_missing_stamps.json`
- `test_vectors/negative_dependency_cycle.json`
- `test_vectors/negative_wrong_mode_for_commit.json`
- `test_vectors/negative_restricted_excerpt.json`
- `test_vectors/negative_export_strict_refusal.json`
- `test_vectors/e2e_preset_stage_commit_plan_apply_doc_report.json`
- `test_vectors/e2e_dcf_urs_downstream_docs.json`

Purpose:

- make schemas enforce architecture decisions;
- split render-token coverage from JSON Schema nested requirements;
- validate contract/action catalog consistency;
- validate governance/security/registry structures;
- add negative and E2E test coverage;
- regenerate/verify manifest after edits.

## 3. Exact Decisions to Implement

### 3.1 Authority / Status / Terminology

Implement:

- DEC-0007, DEC-0010, DEC-0011, DEC-0012
- DEC-0016, DEC-0018, DEC-0020, DEC-0021
- DEC-0036
- DEC-0101, DEC-0102
- DEC-0125, DEC-0126, DEC-0128, DEC-0129

### 3.2 Contract / Action Registry Alignment

Implement:

- DEC-0025, DEC-0026, DEC-0031, DEC-0032
- DEC-0037, DEC-0038
- DEC-0048, DEC-0049, DEC-0052, DEC-0054
- DEC-0061
- DEC-0072
- DEC-0086, DEC-0087, DEC-0094
- DEC-0103, DEC-0104, DEC-0105
- DEC-0112, DEC-0116
- DEC-0127

### 3.3 WP / Planning / Libraries

Implement:

- DEC-0023, DEC-0024, DEC-0027, DEC-0028, DEC-0029, DEC-0030, DEC-0033
- DEC-0039, DEC-0040, DEC-0041, DEC-0042, DEC-0043
- DEC-0045, DEC-0046, DEC-0050, DEC-0051, DEC-0053
- DEC-0113

### 3.4 K&S / Standards

Implement:

- DEC-0056, DEC-0057, DEC-0058, DEC-0059, DEC-0060
- DEC-0062, DEC-0063, DEC-0064, DEC-0065
- DEC-0079
- DEC-0095
- DEC-0106
- DEC-0134

### 3.5 DOC / DCF / URS Source Chain

Implement:

- DEC-0067, DEC-0068, DEC-0069
- DEC-0070, DEC-0071, DEC-0073, DEC-0074, DEC-0077, DEC-0078, DEC-0080
- DEC-0131, DEC-0134

### 3.6 Reporting / Export

Implement:

- DEC-0082, DEC-0083, DEC-0084, DEC-0085
- DEC-0088, DEC-0089, DEC-0090, DEC-0091, DEC-0092, DEC-0093
- DEC-0133

### 3.7 Governance / Security / Registry

Implement:

- DEC-0097, DEC-0098, DEC-0099, DEC-0100
- DEC-0107
- DEC-0117

### 3.8 Schemas / Validation / Test Vectors

Implement:

- DEC-0110, DEC-0111, DEC-0114, DEC-0115, DEC-0118, DEC-0119, DEC-0120

### 3.9 Product Surface Minimum Specification

Implement:

- DEC-0130, DEC-0131, DEC-0132, DEC-0133, DEC-0134

## 4. Acceptance Criteria for Freeze Readiness

The pack may be recommended as freeze-ready only when all criteria below are met.

### 4.1 Authority and Status

- README no longer claims the pack is implementation-ready unless all blockers are closed.
- A glossary/status taxonomy defines released, candidate, freeze-ready, frozen, final, closed, proposed, applied.
- Security & Compliance integration is consistently described as policy-first unless a SEC contract is explicitly introduced.
- UI/product surfaces are explicitly projections, not truth owners.

### 4.2 Contract and Action Catalog

- A contract registry metadata artifact exists and lists all active, optional, special-purpose, and deferred contracts.
- Architecture action catalogs, contract YAML files, action-block YAML files, and schema refs are aligned.
- Public command names are mapped to canonical contract action types.
- Missing TP/PROF/CAL/SEC contracts are either added or formally deferred with rationale.

### 4.3 WP / Planning / Libraries

- WP schema, WP architecture, WP contract, and task library IDs/taxonomy align.
- Profile and Calendar responsibilities no longer duplicate each other.
- Duration-unit policy is explicit for working days, calendar days, weeks, and months.
- User-driven no-profile baseline is represented in WP/Planning behavior.
- Staged planning behavior is explicitly committed-only or preview-only.

### 4.4 K&S

- Standards bundle nullability/no-bundle behavior is explicit.
- Either minimal K&S governed data exists or standards content is formally deferred with output labels.
- K&S schemas enforce standards, bundles, anchors, citations, templates, and excerpt policies.
- Restricted excerpt/redaction behavior is represented in request/response schemas.

### 4.5 DOC / DCF

- DCF intake and AI extraction are candidate-only until human acceptance.
- Accepted URS source gate exists for downstream RTM/DQ/IQ/OQ/PQ/VSR generation.
- DOC action catalog and lifecycle contract are aligned.
- Document metadata schema enforces provenance.
- Template IDs and timestamp policy are consistent.
- Token-clean output can be validated.

### 4.6 RPT / Export

- RPT action catalog and contract are aligned.
- Export is either included with an explicit action/file/header path or formally deferred.
- Report/export schemas enforce artifact metadata, stamps, projection-only flag, and proposed/committed separation.
- Artifact registry/read behavior is defined or deferred.

### 4.7 Product Surface

- A minimum product surface spec exists.
- Canvas-specific terminology is removed from frozen architecture/addendum text.
- Confirmation/review surfaces are defined for commit, apply, finalize, export, and close.
- Advisory/help/follow-up behavior is defined.
- Export/download/artifact-state behavior is defined.
- DCF/URS/K&S/redaction surfaces are defined.

### 4.8 Schemas / Validation / Tests

- Contract envelope schemas match A11 and contract examples.
- Stub/permissive schemas are replaced or formally deferred.
- Dotted render-token validation is separated from JSON Schema required semantics.
- Contract catalog validator exists.
- Governance/audit/security/registry schemas and tests exist.
- Negative/invariant vectors exist.
- E2E core workflow vectors exist.
- `python smoke_test.py` passes.
- `python scripts/pack_validation/verify_manifest.py` passes after manifest regeneration.

## 5. Formally Deferred Items

These items should be explicitly marked deferred in the freeze-ready pack, not silently ignored:

- Pixel-level UI/wireframes and visual design.
- Detailed delivery plan.
- Old/current ASBP implementation audit.
- Clean implementation repository creation.
- Full production-grade identity/e-signature integration.
- Detailed PM/ERP/procurement integration.
- Optional advanced planning/resource optimization beyond deterministic baseline.
- If selected during cleanup: full K&S source library beyond minimal metadata/anchors.
- If selected during cleanup: full export implementation beyond report-only output.
- If selected during cleanup: TP/PROF/CAL/SEC callable contracts.

## 6. Expected Order of Edits

### Step 0 — Control hygiene

Files:

- `_review_control/DECISION_LOG.md`
- `_review_control/PHASE12_DECISIONS_PENDING.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`

Actions:

- Merge or consolidate pending Phase 12 decisions.
- Record this batch plan as the current control authority.
- Do not edit architecture/spec files yet unless user approves batch execution.

### Step 1 — Status, glossary, authority, and README cleanup

Files:

- `README.md`
- `docs/architecture/A00_Specs_Architecture_Pack_Arch_v1_0_1.md`
- `docs/architecture/A01_SoS_Context_Capability_Arch_v1_0_1.md`
- `docs/architecture/A02_Principles_Invariants_Arch_v1_0_1.md`
- `docs/architecture/A03_Subsystems_Authority_Arch_v1_0_1.md`
- `docs/architecture/A09_Governance_Branching_Arch_v1_0_1.md`
- `docs/architecture/A10_Security_Compliance_Arch_v1_0_1.md`
- `docs/architecture/A15_Global_Glossary_Arch_v1_0_1.md`

Acceptance gate:

- No misleading freeze/implementation-ready language remains.
- Status taxonomy is explicit.

### Step 2 — Contract registry and action catalog cleanup

Files:

- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`
- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`
- `contracts/*.yaml`
- `action_blocks/*.yaml`
- new `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Acceptance gate:

- Registry, architecture, contracts, and action blocks agree on contract/action names.

### Step 3 — WP, Planning, and governed-library cleanup

Files:

- A04_2, A04_4, A05, A06, A07, A08
- governed library YAML files under `libraries/`

Acceptance gate:

- WP truth, planning proposal behavior, selector/context/stamps, durations, task taxonomy, profile/calendar boundaries, and no-profile baseline are consistent.

### Step 4 — K&S cleanup

Files:

- A12
- K&S contract and schemas
- new or deferred K&S library files

Acceptance gate:

- Standards bundle policy, citation model, no-bundle behavior, excerpt/redaction handling, and K&S schemas are freeze-ready or formally deferred.

### Step 5 — DOC/DCF source-chain cleanup

Files:

- A04_5
- DOC contract/result schemas
- document metadata schema
- templates and document schemas
- new DCF/source-chain schemas/docs

Acceptance gate:

- DCF intake, accepted URS gate, downstream document source chain, AI drafting boundary, DOC lifecycle, token-clean validation, and timestamp policy are defined.

### Step 6 — RPT/export cleanup

Files:

- A04_6
- RPT contract/action block
- report/export schemas
- CSV schema/export header template

Acceptance gate:

- Reports and exports are projection-only, schema-enforced, stamp-aware, and proposed/committed-safe.

### Step 7 — Product surface cleanup

Files:

- addendums under `Valor_Arch_Addendums_v1.0.1A/`
- new `docs/architecture/A13_Product_Surface_Arch_v1_0_1.md`

Acceptance gate:

- Canvas terminology is removed.
- Minimum product surfaces and states are specified.
- Detailed wireframes remain deferred.

### Step 8 — Schema, validation, and test-vector cleanup

Files:

- `schemas/`
- `validation/`
- `test_vectors/`
- `smoke_test.py`
- `scripts/pack_validation/`

Acceptance gate:

- Schema enforcement, validation tools, negative vectors, and E2E vectors support freeze-readiness claims.

### Step 9 — Manifest, final review, and freeze-readiness check

Files:

- `manifest.yaml`
- `_review_control/FREEZE_READINESS_CHECKLIST.md`
- `_review_control/FREEZE_MODIFICATION_CHANGELOG.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`

Acceptance gate:

- Manifest regenerated and verified.
- Smoke test passes.
- Freeze readiness checklist passes or clearly identifies any remaining formal deferrals.
- User can make a freeze/no-freeze decision.

## 7. Next Controlled Action After This Plan

Await user approval to execute the pre-freeze modification batch.

No architecture/specification files should be edited until that approval is explicit.
