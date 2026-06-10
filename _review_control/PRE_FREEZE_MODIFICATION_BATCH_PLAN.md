# Pre-Freeze Modification Batch Plan

Status: PREPARED — STRICT FREEZE COVERAGE RULE APPLIED
Review branch: review-spec-freeze-control
Date: 2026-06-10

## 0. Purpose

This plan converts the completed no-freeze review into a controlled specification-edit batch.

This plan does not authorize implementation, delivery-plan creation, clean-repo creation, or architecture/specification edits until the user explicitly approves a scoped batch step.

## 1. Working Principle Across All Blockers

No minimum, placeholder, or governance-only solution is acceptable for freeze.

For each blocker:

1. define the declared product scope;
2. require full coverage for that declared scope;
3. if full coverage is not possible, reduce the declared scope or keep freeze blocked.

Do not defer items merely because they are not blockers now.

If an item affects architecture clarity, freeze readiness, implementation contracts, validation, product behavior, source-of-truth, traceability, schemas, or UI minimum behavior, it must be resolved before freeze.

Only **Can’t do now** items may move to later delivery planning. A Can’t do now item requires implementation work, external systems, detailed visual design, old/current code audit, clean repository creation, or post-freeze integration work.

## 2. Corrected K&S Freeze Rule

K&S must be freeze-ready as a **full internal governed standards set** for the declared VALOR CQV scope, with controlled external references to original standards.

Required K&S direction:

- internal written governed standards in VALOR/company wording;
- controlled reference to original external standards;
- source identity, version, date, and authority;
- anchors/citation model;
- source-to-internal requirement mapping;
- excerpt/redaction/refusal rules;
- schema enforcement;
- test vectors;
- missing standards bundle = blocked/incomplete state, not normal operation.

Not acceptable for regulated CQV freeze operation:

- minimum governed K&S;
- metadata-only K&S;
- no-bundle/no-standards mode;
- placeholder standards;
- governance-only standards language.

If full K&S coverage cannot be produced for the current declared VALOR CQV scope, reduce the declared VALOR CQV scope or keep freeze blocked.

## 3. Must-Resolve-Before-Freeze Work Groups

### 3.1 Authority, Status, and Terminology

Files:

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

Acceptance criteria:

- Declared product scope is explicit.
- README no longer claims freeze or implementation readiness unless all freeze blockers are closed.
- Status taxonomy defines released, candidate, freeze-ready, frozen, final, closed, proposed, and applied.
- UI/product surfaces are projections, not truth owners.

### 3.2 Contract Registry and Action Catalog

Files:

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
- create `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Acceptance criteria:

- Registry, architecture, contracts, and action blocks agree on contract/action names.
- TP/PROF/CAL/SEC are added as callable contracts or explicitly classified outside the declared callable-contract scope.
- Public command names map to canonical contract action types.

### 3.3 WP, Planning, and Governed Libraries

Files:

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

Acceptance criteria:

- Declared WP/planning/library scope has full coverage.
- WP truth, proposal behavior, stamps, durations, taxonomy, profile/calendar boundaries, and no-profile baseline are consistent.
- FAT execution chain is included in declared scope or declared scope is reduced with impact stated.

### 3.4 K&S and Standards Bundle Readiness

Files:

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
- create `libraries/knowledge_standards/README.md`
- create `libraries/knowledge_standards/bundles/BND-CQV-BASE_v1.0.1.yaml`
- create `libraries/knowledge_standards/standards/STD-CQV-BASE_v1.0.1.yaml`
- create `libraries/knowledge_standards/templates/TPL-URS_v1.0.1.yaml`
- create `libraries/knowledge_standards/mapping/source_to_internal_requirements_v1.0.1.yaml`

Acceptance criteria:

- Declared VALOR CQV scope has full internal governed K&S coverage.
- Internal standards are written in VALOR/company wording.
- Original external standards are referenced with source identity, version, date, and authority.
- Source-to-internal requirement mapping exists.
- Anchors/citation model exists and is schema-enforced.
- Excerpt/redaction/refusal rules are schema-enforced and tested.
- Missing standards bundle creates blocked/incomplete state.
- No metadata-only, placeholder, no-bundle, or governance-only standards mode remains as regulated CQV operation.

### 3.5 DOC, DCF, and URS Source Chain

Files:

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
- create `docs/architecture/A04_5A_DCF_Intake_SourceChain_Arch_v1_0_1.md`
- create `schemas/objects/dcf_source_schema.json`
- create `schemas/objects/urs_source_chain_schema.json`
- create `test_vectors/expected_dcf_intake_candidate.json`
- create `test_vectors/expected_accepted_urs_source_chain.json`

Acceptance criteria:

- DCF intake and AI extraction are candidate-only until human acceptance.
- Accepted URS source gate exists for RTM/DQ/IQ/OQ/PQ/VSR generation.
- DOC action catalog and lifecycle contract align.
- Document metadata schema enforces provenance.
- Template IDs and timestamp policy are consistent.
- Token-clean output can be validated.

### 3.6 RPT and Export

Files:

- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `action_blocks/BUILD_REPORT.yaml`
- `schemas/contracts/report_result.schema.json`
- `schemas/contracts/export_result.schema.json`
- `schemas/objects/csv_export_schema.json`
- create `action_blocks/RPT_GENERATE_EXPORT.yaml` if export remains in scope
- create `schemas/contracts/export_request.schema.json` if export remains in scope
- create `templates/export/WP_TASK_EXPORT_v1.0.1.csv.header` if export remains in scope

Acceptance criteria:

- Declared RPT/export scope has full coverage.
- Export is fully defined or removed from the declared freeze-ready capability scope.
- Report/export schemas enforce artifact metadata, stamps, projection-only flag, and proposed/committed separation.
- Artifact registry/read behavior is defined for declared artifacts.

### 3.7 Product Surface Minimum Specification

Files:

- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Canvas_Rendering_Record_Layout_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Document_Generation_Compliance_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Planning_Invariants_UX_Contract_v1.0.1A.md`
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Reporting_Export_Projection_Contract_v1.0.1A.md`
- create `docs/architecture/A13_Product_Surface_Arch_v1_0_1.md`

Acceptance criteria:

- Declared product surface scope has full minimum behavior coverage.
- Canvas terminology is removed.
- Confirmation/review surfaces are defined for commit, apply, finalize, export, and close.
- Advisory/help/follow-up behavior is defined.
- Export/download/artifact-state behavior is defined.
- DCF/URS/K&S/redaction surfaces are defined.
- Only detailed visual design/wireframes move to Can’t do now.

### 3.8 Schemas, Validation, and Test Vectors

Files:

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
- create `schemas/objects/audit_event_schema.json`
- create `schemas/objects/security_event_schema.json`
- create `schemas/objects/contract_registry_schema.json`
- create `validation/validate_contract_catalog.py`
- create `validation/validate_architecture_traceability.py`
- create negative and E2E test vectors listed in Phase 13 review

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

## 4. Items Allowed as Can’t Do Now

Only these may move to later delivery planning:

- Pixel-level UI/wireframes and visual design.
- Detailed delivery plan.
- Old/current ASBP implementation audit.
- Clean implementation repository creation.
- Full production-grade identity/e-signature integration.
- Detailed PM/ERP/procurement integration.
- Optional advanced planning/resource optimization beyond deterministic baseline.
- Real integration with external QMS/e-signature/identity systems.
- Physical execution evidence ingestion from external systems.

## 5. Wording Replaced by This Rule Update

The following wording is removed as acceptable freeze logic:

- “minimum governed K&S”
- “metadata-only K&S”
- “no-bundle/no-standards mode” as normal regulated CQV operation
- “placeholder standards”
- “governance-only standards language”
- “Create minimal K&S data”
- “metadata-only equivalent”
- “explicit no-bundle policy file” as a normal operating option
- “schemas are replaced or formally deferred” for declared scope
- “artifact registry/read behavior is defined or deferred” for declared artifact scope
- “export remains claimed while export path is undefined”

## 6. Items Pulled Back Into Pre-Freeze Work

- Full internal governed K&S for the declared VALOR CQV scope.
- Source identity, version, date, authority, and source-to-internal requirement mapping.
- Anchors/citation model and schema enforcement.
- Excerpt/redaction/refusal rules and tests.
- Missing standards bundle blocked/incomplete behavior.
- Export action/header/schema path if export remains declared.
- TP/PROF/CAL/SEC contract classification in the registry.
- Stub/permissive schemas.
- Artifact registry/read behavior for declared artifacts.
- UI minimum behavior.
- Negative and E2E test coverage.
- Governance/audit/security/registry schemas/tests.

## 7. Expected Order of Edits

1. Control hygiene.
2. Status, glossary, authority, and README cleanup.
3. Contract registry and action catalog cleanup.
4. WP, Planning, and governed-library cleanup.
5. K&S cleanup.
6. DOC/DCF source-chain cleanup.
7. RPT/export cleanup.
8. Product surface cleanup.
9. Schema, validation, and test-vector cleanup.
10. Manifest, final review, and freeze-readiness check.

## 8. Next Controlled Action

Await user approval to execute Step 0 — Control hygiene.

No architecture/specification files should be edited until that approval is explicit.
