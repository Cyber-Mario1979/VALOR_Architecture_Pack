---
id: VALOR-block-A12-knowledge-standards-architecture
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: frozen_controlled
date: 2026-06-12
summary: "A12 — K&S architecture with governed internal standards, controlled external references, TESTING_ONLY operating state, source-metadata acceptance gate, citation/refusal rules, and blocked regulated-use behavior."
---

# Knowledge & Standards System Architecture

## 1. Purpose and Authority

K&S is the governed read-only standards authority for VALOR CQV outputs. K&S provides internal VALOR/company-worded governed standards, controlled external reference metadata and anchors, source-to-internal mapping, standards bundles, template governance records, citation resolution, excerpt/refusal policy, lifecycle control, and blocked-state behavior.

K&S is not authoritative for WP/task truth, generated DOC/RPT content, human/site approvals, or external standard ownership.

## 2. Declared v1.0.1 K&S Scope

The declared K&S scope is `BND-CQV-BASE_v1.0.1`, `BND-CSV-ADDON_v1.0.1`, `BND-CLEANROOM-ADDON_v1.0.1`, `STD-CQV-BASE_v1.0.1`, URS/RTM/DQ/IQ/OQ/PQ/VSR template governance records, and the `TPL-DCF_v1.0.1` PRODUCT_TESTING_ONLY DCF source-capture template family governance record.

The CQV Base Bundle covers WP/RPT standards citation needs, URS, RTM, DQ, IQ, OQ, PQ, VSR, risk-based CQV lifecycle expectations, traceability, documentation and approval expectations, CSV add-on trigger behavior, and cleanroom/HVAC add-on trigger behavior.

`TPL-DCF_v1.0.1` is a governed DCF source-capture template family record for product testing only. It records metadata for four user-provided DCF source-candidate variants: Cleanroom, Computerized Systems, Process Equipment, and Utilities. It does not import DOCX or Markdown template content into the repository, does not activate DCF artifact generation/finalization, and does not approve real regulated CQV/GMP use.

## 3. TESTING_ONLY Operating State

`TESTING_ONLY` is a governed state for product testing, dry runs, internal trials, validation of product behavior, and end-to-end workflow testing.

PRODUCT_TESTING / FIELD_TRIAL mode is an allowed use of TESTING_ONLY / PRODUCT_TESTING_ONLY K&S assets. It supports ASBP — AI System Builder Program / AI System Builder product construction, internal dry runs, product behavior validation, document generation testing, report generation testing, E2E workflow validation, and evaluation by parallel professional/market testers.

FIELD_TRIAL is an operating label under PRODUCT_TESTING_ONLY, not a new schema/machine enum.

PRODUCT_TESTING / FIELD_TRIAL outputs are not official GMP records and must carry the required testing-only stamp where applicable.

Source metadata acceptance is not required for PRODUCT_TESTING / FIELD_TRIAL mode.

`TESTING_ONLY` assets may support product testing only when:

- `testing_use_allowed: true`;
- `regulated_output_allowed: false`;
- `testing_only_stamp_required: true`;
- testing metadata has not expired;
- the output carries this visible stamp: `PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE.`

`TESTING_ONLY` assets must never support real-life regulated CQV/GMP output. If a user requests regulated output while K&S is `TESTING_ONLY`, the system must block/refuse or mark the output incomplete.

Missing real external source edition, document date, or locator does not block product testing when the asset is `TESTING_ONLY`; it does block real regulated use.

## 4. Regulated-Release Approval Gate

Assets are not approved for regulated CQV/GMP use unless a separate controlled acceptance patch records user/site acceptance of exact external source edition/version, document date, source locator/anchor locator, source applicability, source-to-internal mapping, and template governance records.

Do not mark any K&S asset `ACTIVE` during the testing-only gate.

REGULATED_RELEASE remains conditional upon K&S/source metadata acceptance, template source metadata acceptance, and any required user/site acceptance gates.

This gate does not block PRODUCT_TESTING / FIELD_TRIAL freeze, ASBP product construction, product testing, field trials, document generation testing, or report generation testing.

## 5. Source Text and Citation Rule

Internal VALOR standards are the operative governed requirements. External standards are controlled source authorities only. K&S must not copy or reproduce external standards text. The default external excerpt policy is `NO_EXCERPTS`.

Citations must resolve to a governed internal requirement or controlled source anchor and include usage classification, regulated-output allowance, excerpt policy, and lifecycle status.

Unknown anchors must refuse with `ANCHOR_NOT_FOUND`. Restricted excerpt requests must refuse with `EXCERPT_BLOCKED`.

## 6. Lifecycle and Expiry Control

Every standards bundle, internal standard, external reference register, source mapping file, and template governance record must include owner, effective_date, source_checked_date, review_cycle_months, next_review_due, expiry_date, status, usage_classification, testing_use_allowed, regulated_output_allowed, testing_only_stamp_required, approval_status, user_site_acceptance_required, source_metadata_acceptance_status, testing_expired_behavior, and regulated_expired_behavior.

Allowed statuses:

- TESTING_ONLY
- PRE_FREEZE_USER_REVIEW_REQUIRED
- ACTIVE
- DUE_FOR_REVIEW
- EXPIRED
- SUPERSEDED
- BLOCKED

If testing metadata expires, product testing must block until renewed. If regulated output is requested while required K&S assets are testing-only, unaccepted, missing, expired, invalid, unmapped, or not approved for regulated use, regulated CQV/GMP output must be blocked/refused or marked incomplete.

Silent fallback to old standards and no-standards mode are prohibited.

## 7. Add-on Trigger Rules

CSV add-on trigger: computerized system, automation, data integrity, electronic record/signature, recipe, audit trail, alarm/report, or configurable software scope requires `BND-CSV-ADDON_v1.0.1`.

Cleanroom/HVAC add-on trigger: classified area, cleanroom, HVAC serving classified GMP space, ISO 8, Grade D, environmental control, pressure cascade, airflow, filtration, temperature, humidity, or monitoring interface scope requires `BND-CLEANROOM-ADDON_v1.0.1`.

Testing behavior: add-ons may support product testing if testing metadata is valid and the required stamp is applied.

Regulated behavior: block regulated output unless the required add-on bundle is approved for regulated use.

## 8. Downstream Stamping Requirements

When DOC or RPT uses testing-only K&S assets, generated outputs must stamp the required testing-only visible stamp, bundle ID/version, internal standard ID/version, template ID/version if used, mapped requirement IDs, source reference IDs, source anchor IDs, usage classification, regulated-output allowance, and lifecycle/review/expiry status.

## 9. Pre-freeze User Review Gate

Where exact external standard edition, document date, or locator has not been user/site accepted, K&S records may be `TESTING_ONLY` for product testing but remain not approved as regulated standards basis. This is a controlled blocked/incomplete state for real regulated use.

## CHANGELOG

| Date | Changes | Type / Version |
| ---- | ------- | -------------- |
| 2026-06-12 | Blocker 6B DCF template governance record added for PRODUCT_TESTING_ONLY source-capture metadata | Pre-freeze controlled update |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | Blocker 3 governed standards bundle aligned | Pre-freeze controlled update |
| 2026-06-12 | Blocker 3A TESTING_ONLY operating state added; regulated use remains blocked | Pre-freeze controlled update |
