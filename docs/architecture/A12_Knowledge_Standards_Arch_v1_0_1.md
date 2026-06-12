---
id: VALOR-block-A12-knowledge-standards-architecture
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
  - VALOR-block-A10-security-compliance-architecture
summary: "Block A12 — Knowledge & Standards System Architecture: governed internal VALOR standards, controlled external source references, versioned bundles, anchors, source-to-internal mapping, expiry/review lifecycle, citation/refusal rules, and blocked-state behavior for CQV-safe output."
acceptance_criteria:
  - Defines K&S as read-only governed content with versioned bundles and anchors.
  - Defines internal VALOR/company-worded standards as the operative governed requirements.
  - Defines controlled external source authorities without reproducing external copyrighted text.
  - Defines lifecycle/expiry/review fields and blocked-state behavior.
  - Defines source-to-internal requirement mapping and schema enforcement.
  - Defines contract actions to list/read bundles/templates/anchors and validate references.
  - Defines stamping and provenance requirements for downstream DOC/RPT systems.
  - Defines error semantics and safe handling aligned with Security & Compliance constraints.
---

# Knowledge & Standards System Architecture

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

Knowledge & Standards (K&S) is the governed read-only standards authority for VALOR CQV outputs. K&S provides:

- internal VALOR/company-worded governed standards;
- controlled external reference metadata and anchors;
- source-to-internal requirement mapping;
- standards bundles;
- template governance records;
- citation resolution;
- excerpt/redaction/refusal policy;
- lifecycle, review, expiry, and blocked-state behavior.

K&S is authoritative for standards metadata, bundle/version identity, anchors, citation policy, mapping records, template governance records, and standards-basis validation.

K&S is not authoritative for WP/task truth, DOC/RPT generated content, human/site approvals, or external standard ownership.

## 2. Declared v1.0.1 K&S Scope

The declared freeze scope is the VALOR CQV Base Bundle:

- `BND-CQV-BASE_v1.0.1`
- `BND-CSV-ADDON_v1.0.1`
- `BND-CLEANROOM-ADDON_v1.0.1`
- `STD-CQV-BASE_v1.0.1`
- URS, RTM, DQ, IQ, OQ, PQ, and VSR template governance records.

The CQV Base Bundle covers WP standards citation needs, RPT standards citation needs, URS, RTM, DQ, IQ, OQ, PQ, VSR, risk-based CQV lifecycle expectations, traceability expectations, documentation and approval expectations, CSV add-on trigger behavior, and cleanroom/HVAC add-on trigger behavior.

## 3. Operative Internal Standards Rule

Internal VALOR standards are the operative governed requirements. External standards are controlled source authorities only.

K&S must not copy or reproduce ISO, ISPE, ASTM, EU GMP, ICH, FDA, local regulatory, site GMP, or other external standard text unless an explicitly approved public excerpt source and excerpt policy allow it. The default policy for external references is `NO_EXCERPTS`.

K&S stores source identity, source authority, source version/date fields, anchor IDs, and mapping references. It does not store clause-by-clause copyrighted source text.

## 4. Governed Library Files

Canonical K&S library root:

- `libraries/knowledge_standards/README.md`
- `libraries/knowledge_standards/references/external_references_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CQV-BASE_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CSV-ADDON_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CLEANROOM-ADDON_v1.0.1.yaml`
- `libraries/knowledge_standards/standards/STD-CQV-BASE_v1.0.1.yaml`
- `libraries/knowledge_standards/mapping/source_to_internal_requirements_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-URS_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-RTM_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-DQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-IQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-OQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-PQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-VSR_v1.0.1.yaml`

## 5. Lifecycle and Expiry Control

Every standards bundle, internal standard, external reference register, source mapping file, and template governance record must include:

- owner;
- effective_date;
- source_checked_date;
- review_cycle_months;
- next_review_due;
- expiry_date;
- status;
- review_required;
- expired_behavior.

Allowed statuses:

- ACTIVE
- DUE_FOR_REVIEW
- EXPIRED
- SUPERSEDED
- BLOCKED
- PRE_FREEZE_USER_REVIEW_REQUIRED

No standard or bundle is valid forever. If the core K&S bundle, required add-on bundle, internal standard, source reference, mapping file, anchor, or template governance record is missing, expired, invalid, unreviewed, or unapproved, dependent regulated CQV output must be blocked or marked incomplete.

Silent fallback to old standards and no-standards mode are prohibited for regulated CQV output.

## 6. Anchors and Citations

Citations must resolve to a governed internal requirement or controlled source anchor. A citation must include:

- asset_type;
- asset_id;
- asset_version;
- anchor_id;
- source identity where applicable;
- excerpt policy applied;
- lifecycle status used at generation time.

Unknown anchors must refuse with `ANCHOR_NOT_FOUND`. Restricted excerpt requests must refuse with `EXCERPT_BLOCKED`.

## 7. Source-to-Internal Requirement Mapping

Each internal requirement must map to controlled source anchors through `source_to_internal_requirements_v1.0.1.yaml`.

If an internal requirement has no mapping, or if the mapped source reference is missing, expired, invalid, or unreviewed, K&S validation must block dependent regulated CQV output.

## 8. Add-on Trigger Rules

CSV add-on trigger:

- Trigger bundle: `BND-CSV-ADDON_v1.0.1`.
- Trigger condition: computerized system, automation, data integrity, electronic record/signature, recipe, audit trail, alarm/report, or configurable software scope.
- Failure behavior: block dependent regulated CQV output when triggered bundle is missing, expired, invalid, or unreviewed.

Cleanroom/HVAC add-on trigger:

- Trigger bundle: `BND-CLEANROOM-ADDON_v1.0.1`.
- Trigger condition: classified area, cleanroom, HVAC serving classified GMP space, ISO 8, Grade D, environmental control, pressure cascade, airflow, filtration, temperature, humidity, or monitoring interface scope.
- Failure behavior: block dependent regulated CQV output when triggered bundle is missing, expired, invalid, or unreviewed.

## 9. Contract Actions

K&S is accessed via `VALOR-contract-orch-ks`.

Read actions:

- KS_LIST_STANDARDS
- KS_READ_STANDARD
- KS_LIST_TEMPLATES
- KS_READ_TEMPLATE
- KS_LIST_BUNDLES
- KS_READ_BUNDLE
- KS_LIST_ANCHORS
- KS_RESOLVE_CITATION

Validation actions:

- KS_VALIDATE_CITATION_SET
- KS_VALIDATE_TEMPLATE_REQUIREMENTS
- KS_VALIDATE_SOURCE_MAPPING
- KS_VALIDATE_BUNDLE_INTEGRITY

## 10. Downstream Stamping Requirements

When DOC or RPT uses K&S assets, generated outputs must stamp:

- bundle_id/version;
- internal standard ID/version;
- template ID/version if used;
- mapped requirement IDs;
- source reference IDs;
- source anchor IDs;
- lifecycle/review/expiry status used at generation time.

## 11. Pre-freeze User Review Gate

Where the task source input did not provide exact external standard edition, document date, or locator, K&S records must remain `PRE_FREEZE_USER_REVIEW_REQUIRED`. Such records are not approved standards basis for final regulated CQV output until user/site review accepts the source metadata and mapping.

This gate is not a deferment. It is a controlled blocked/incomplete state.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | Blocker 3 K&S governed standards bundle, lifecycle/expiry gates, source mapping, add-on triggers, and schema enforcement aligned | Pre-freeze controlled update |
