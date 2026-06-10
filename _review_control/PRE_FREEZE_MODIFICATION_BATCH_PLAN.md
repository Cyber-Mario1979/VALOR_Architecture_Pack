# Pre-Freeze Modification Batch Plan

Status: PREPARED — DEFER RULE TIGHTENED
Review branch: review-spec-freeze-control
Date: 2026-06-10

## 0. Purpose

This plan converts the completed no-freeze review into a controlled specification-edit batch.

It does **not** authorize implementation.
It does **not** create a delivery plan.
It does **not** create a clean implementation repository.
It does **not** edit architecture/specification files yet.

The batch objective is to turn the current candidate architecture pack into a freeze-ready specification authority.

Source inputs:

- `_review_control/PHASE13_FINAL_FREEZE_REVIEW.md`
- `_review_control/SESSION_HANDOFF.md`
- `_review_control/DECISION_LOG.md`
- `_review_control/PHASE12_DECISIONS_PENDING.md`

## 1. New Deferral Rule

Do **not** use broad “deferred items” logic.

No item may be deferred merely because it is not a blocker now.

If an item affects any of the following, it must be resolved before freeze:

- architecture clarity;
- freeze readiness;
- implementation contracts;
- validation;
- product behavior;
- source-of-truth;
- traceability;
- schemas;
- UI minimum behavior.

Only **Can’t do now** items may move to later delivery planning.

A **Can’t do now** item is one that requires one or more of:

- implementation work;
- external systems;
- detailed visual design;
- old/current code audit;
- clean repository creation;
- post-freeze integration work.

Everything else stays inside the pre-freeze modification batch.

## 2. Items That Remain Must-Resolve-Before-Freeze

The following are mandatory pre-freeze work and must not be deferred.

### 2.1 Authority, Status, and Terminology

Files to edit:

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

Decisions to implement:

- DEC-0007, DEC-0010, DEC-0011, DEC-0012
- DEC-0016, DEC-0018, DEC-0020, DEC-0021
- DEC-0036
- DEC-0101, DEC-0102
- DEC-0125, DEC-0126, DEC-0128, DEC-0129

Acceptance criteria:

- README no longer claims the pack is implementation-ready unless all blockers are closed.
- Status taxonomy defines released, candidate, freeze-ready, frozen, final, closed, proposed, and applied.
- Security & Compliance integration is consistently described as policy-first unless a SEC contract is explicitly introduced.
- UI/product surfaces are explicitly projections, not truth owners.

### 2.2 Contract Registry and Action Catalog

Files to edit:

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

Files to create:

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Contracts to add or explicitly classify in the registry:

- `contracts/VALOR-contract-orch-tp.yaml`
- `contracts/VALOR-contract-orch-prof.yaml`
- `contracts/VALOR-contract-orch-cal.yaml`
- `contracts/VALOR-contract-orch-sec.yaml`

Decisions to implement:

- DEC-0025, DEC-0026, DEC-0031, DEC-0032
- DEC-0037, DEC-0038
- DEC-0048, DEC-0049, DEC-0052, DEC-0054
- DEC-0061
- DEC-0072
- DEC-0086, DEC-0087, DEC-0094
- DEC-0103, DEC-0104, DEC-0105
- DEC-0112, DEC-0116
- DEC-0127

Acceptance criteria:

- A single registry identifies active, optional, special-purpose, and not-in-scope contracts.
- Architecture action catalogs, contract YAML files, action-block YAML files, and schema refs align.
- Public command names are mapped to canonical contract action types.
- TP/PROF/CAL/SEC contract status is explicit.

### 2.3 WP, Planning, and Governed Libraries

Files to edit:

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

Decisions to implement:

- DEC-0023, DEC-0024, DEC-0027, DEC-0028, DEC-0029, DEC-0030, DEC-0033
- DEC-0039, DEC-0040, DEC-0041, DEC-0042, DEC-0043
- DEC-0045, DEC-0046, DEC-0050, DEC-0051, DEC-0053
- DEC-0113

Acceptance criteria:

- WP truth, planning proposal behavior, selector/context/stamps, durations, task taxonomy, profile/calendar boundaries, and no-profile baseline are consistent.
- Profile and Calendar responsibilities do not duplicate each other.
- FAT execution chain is either included in the workflow or explicitly scoped out with product impact stated.

### 2.4 K&S and Standards Bundle Readiness

Files to edit:

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

Files to create at minimum:

- `libraries/knowledge_standards/README.md`
- `libraries/knowledge_standards/bundles/BND-CQV-BASE_v1.0.1.yaml` or an explicit no-bundle policy file
- `libraries/knowledge_standards/standards/STD-CQV-BASE_v1.0.1.yaml` or metadata-only equivalent
- `libraries/knowledge_standards/templates/TPL-URS_v1.0.1.yaml` or template registry equivalent

Decisions to implement:

- DEC-0056, DEC-0057, DEC-0058, DEC-0059, DEC-0060
- DEC-0062, DEC-0063, DEC-0064, DEC-0065
- DEC-0079
- DEC-0095
- DEC-0106
- DEC-0134

Acceptance criteria:

- Standards bundle nullability/no-bundle behavior is explicit.
- K&S governed data exists at least as metadata/anchors, or a no-bundle mode is explicitly specified.
- K&S schemas enforce standards, bundles, anchors, citations, templates, and excerpt policies.
- Restricted excerpt/redaction behavior is represented in request/response schemas.

### 2.5 DOC, DCF, and URS Source Chain

Files to edit:

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

Files to create:

- `docs/architecture/A04_5A_DCF_Intake_SourceChain_Arch_v1_0_1.md`
- `schemas/objects/dcf_source_schema.json`
- `schemas/objects/urs_source_chain_schema.json`
- `test_vectors/expected_dcf_intake_candidate.json`
- `test_vectors/expected_accepted_urs_source_chain.json`

Decisions to implement:

- DEC-0067, DEC-0068, DEC-0069
- DEC-0070, DEC-0071, DEC-0073, DEC-0074, DEC-0077, DEC-0078, DEC-0080
- DEC-0131, DEC-0134

Acceptance criteria:

- DCF intake and AI extraction are candidate-only until human acceptance.
- Accepted URS source gate exists for RTM/DQ/IQ/OQ/PQ/VSR generation.
- DOC action catalog and lifecycle contract align.
- Document metadata schema enforces provenance.
- Template IDs and timestamp policy are consistent.
- Token-clean output can be validated.

### 2.6 RPT and Export

Files to edit:

- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `action_blocks/BUILD_REPORT.yaml`
- `schemas/contracts/report_result.schema.json`
- `schemas/contracts/export_result.schema.json`
- `schemas/objects/csv_export_schema.json`

Files to create if export remains in freeze scope:

- `action_blocks/RPT_GENERATE_EXPORT.yaml`
- `schemas/contracts/export_request.schema.json`
- `templates/export/WP_TASK_EXPORT_v1.0.1.csv.header`

Decisions to implement:

- DEC-0082, DEC-0083, DEC-0084, DEC-0085
- DEC-0088, DEC-0089, DEC-0090, DEC-0091, DEC-0092, DEC-0093
- DEC-0133

Acceptance criteria:

- RPT action catalog and contract align.
- Export is either included with explicit action/file/header path, or it is not claimed as a freeze-ready capability.
- Report/export schemas enforce artifact metadata, stamps, projection-only flag, and proposed/committed separation.
- Artifact registry/read behavior is defined at minimum.

### 2.7 Product Surface Minimum Specification

Files to edit:

- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Canvas_Rendering_Record_Layout_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Document_Generation_Compliance_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Planning_Invariants_UX_Contract_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Reporting_Export_Projection_Contract_v1.0.1A.md`

Files to create:

- `docs/architecture/A13_Product_Surface_Arch_v1_0_1.md`

Decisions to implement:

- DEC-0130, DEC-0131, DEC-0132, DEC-0133, DEC-0134, DEC-0135

Acceptance criteria:

- Canvas terminology is removed.
- Minimum product surfaces and states are specified.
- Confirmation/review surfaces are defined for commit, apply, finalize, export, and close.
- Advisory/help/follow-up behavior is defined.
- Export/download/artifact-state behavior is defined.
- DCF/URS/K&S/redaction surfaces are defined.
- Detailed wireframes remain classified as Can’t do now.

### 2.8 Schemas, Validation, and Test Vectors

Files to edit:

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

Files to create:

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

Decisions to implement:

- DEC-0110, DEC-0111, DEC-0114, DEC-0115, DEC-0118, DEC-0119, DEC-0120
- DEC-0117

Acceptance criteria:

- Contract envelope schemas match A11 and contract examples.
- Stub/permissive schemas are replaced.
- Dotted render-token validation is separated from JSON Schema required semantics.
- Contract catalog validator exists.
- Governance/audit/security/registry schemas and tests exist.
- Negative/invariant vectors exist.
- E2E core workflow vectors exist.
- `python smoke_test.py` passes.
- `python scripts/pack_validation/verify_manifest.py` passes after manifest regeneration.

## 3. Items Allowed as “Can’t Do Now”

Only these may move to later delivery planning, because they require implementation, external systems, detailed visual design, old-code audit, clean repo creation, or post-freeze integration work:

- Pixel-level UI/wireframes and visual design.
- Detailed delivery plan.
- Old/current ASBP implementation audit.
- Clean implementation repository creation.
- Full production-grade identity/e-signature integration.
- Detailed PM/ERP/procurement integration.
- Optional advanced planning/resource optimization beyond deterministic baseline.
- Real integration with external QMS/e-signature/identity systems.
- Physical execution evidence ingestion from external systems.

These items must still be named in the frozen pack if relevant, but they are not required to be solved before freeze.

## 4. Items Previously Treated as Deferred That Are Pulled Back Into Pre-Freeze Work

The following may no longer be deferred broadly and must be handled in the pre-freeze batch:

- Full K&S source library beyond minimal metadata/anchors is pulled back as: define minimal metadata/anchors or explicit no-bundle/no-standards mode before freeze.
- Full export implementation beyond report-only output is pulled back as: either define the export action/header/schema path or remove/de-scope export as a freeze-ready capability.
- TP/PROF/CAL/SEC callable contracts are pulled back as: classify each as active, optional, special-purpose, or not-in-scope in the contract registry before freeze.
- Stub/permissive schemas are pulled back as: replace them or mark the related capability not freeze-ready.
- Artifact registry/read behavior is pulled back as: define minimum artifact identity/status/read model or de-scope the affected artifact feature.
- Standards bundle nullability is pulled back as: define mandatory bundle, nullable bundle, or no-bundle mode before freeze.
- UI minimum behavior is pulled back as: define minimum product surfaces/states before freeze; only visual design is Can’t do now.
- Negative and E2E test coverage is pulled back as: add minimum coverage sufficient for freeze-readiness claims.
- Governance/audit/security/registry schemas/tests are pulled back as: define minimum schemas/tests before freeze.

## 5. Expected Order of Edits

### Step 0 — Control hygiene

Files:

- `_review_control/DECISION_LOG.md`
- `_review_control/PHASE12_DECISIONS_PENDING.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`
- `_review_control/PRE_FREEZE_MODIFICATION_BATCH_PLAN.md`

Actions:

- Record this strict deferral rule.
- Remove broad deferral language from control logic.
- Mark this plan as the current control authority.
- Do not edit architecture/specification files yet unless user approves batch execution.

Acceptance gate:

- Control files clearly distinguish must-resolve-before-freeze from Can’t do now.

### Step 1 — Status, glossary, authority, and README cleanup

Acceptance gate:

- No misleading freeze/implementation-ready language remains.
- Status taxonomy is explicit.
- Security & Compliance integration is explicit.
- UI surfaces are projections, not truth owners.

### Step 2 — Contract registry and action catalog cleanup

Acceptance gate:

- Registry, architecture, contracts, and action blocks agree on contract/action names.
- Optional/not-in-scope contracts are classified instead of broadly deferred.

### Step 3 — WP, Planning, and governed-library cleanup

Acceptance gate:

- WP truth, planning proposal behavior, selector/context/stamps, durations, task taxonomy, profile/calendar boundaries, and no-profile baseline are consistent.

### Step 4 — K&S cleanup

Acceptance gate:

- Standards bundle policy, citation model, no-bundle behavior, excerpt/redaction handling, and K&S schemas are freeze-ready.

### Step 5 — DOC/DCF source-chain cleanup

Acceptance gate:

- DCF intake, accepted URS gate, downstream document source chain, AI drafting boundary, DOC lifecycle, token-clean validation, and timestamp policy are defined.

### Step 6 — RPT/export cleanup

Acceptance gate:

- Reports and exports are projection-only, schema-enforced, stamp-aware, and proposed/committed-safe.
- Any export de-scope is explicit and does not leave export claimed as freeze-ready.

### Step 7 — Product surface cleanup

Acceptance gate:

- Canvas terminology is removed.
- Minimum product surfaces and states are specified.
- Only detailed visual design/wireframes move to Can’t do now.

### Step 8 — Schema, validation, and test-vector cleanup

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
- Freeze readiness checklist passes.
- Any Can’t do now item is listed with reason and delivery-planning destination.
- User can make a freeze/no-freeze decision.

## 6. Next Controlled Action After This Rule Update

Await user approval to execute Step 0 — Control hygiene.

No architecture/specification files should be edited until that approval is explicit.
