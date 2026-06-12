# VALOR Knowledge & Standards Library

Status: PRE_FREEZE_USER_REVIEW_REQUIRED
Owner: K&S
Effective date: 2026-06-12
Source checked date: 2026-06-12
Review cycle months: 36
Next review due: 2029-06-12
Expiry date: 2029-06-12

## Purpose

This folder contains the governed Knowledge & Standards content pack for the declared VALOR CQV v1.0.1 scope. The operative requirements are internal VALOR/company-worded requirements. External standards are controlled source authorities only and must not be copied into generated outputs.

## Declared v1.0.1 K&S scope

The CQV base bundle covers WP standards citation needs, RPT standards citation needs, URS, RTM, DQ, IQ, OQ, PQ, VSR, risk-based CQV lifecycle expectations, traceability, documentation control, approvals, reporting/reference behavior, computerized-system add-on trigger, and cleanroom/HVAC add-on trigger.

## Controlled bundle files

- `bundles/BND-CQV-BASE_v1.0.1.yaml`
- `bundles/BND-CSV-ADDON_v1.0.1.yaml`
- `bundles/BND-CLEANROOM-ADDON_v1.0.1.yaml`
- `standards/STD-CQV-BASE_v1.0.1.yaml`
- `references/external_references_v1.0.1.yaml`
- `mapping/source_to_internal_requirements_v1.0.1.yaml`
- `templates/TPL-URS_v1.0.1.yaml`
- `templates/TPL-RTM_v1.0.1.yaml`
- `templates/TPL-DQ_v1.0.1.yaml`
- `templates/TPL-IQ_v1.0.1.yaml`
- `templates/TPL-OQ_v1.0.1.yaml`
- `templates/TPL-PQ_v1.0.1.yaml`
- `templates/TPL-VSR_v1.0.1.yaml`

## Source-control rule

External standards such as ISPE Baseline Guide Vol. 5, ISPE GAMP 5, EU GMP Annex 15, EU GMP Annex 11, ASTM E2500, ICH Q9, ICH Q10, 21 CFR Part 11, ISO 14644, and local EDA/site GMP requirements are referenced by controlled source IDs, source metadata, and anchors. Their original text is not reproduced.

Where edition year, exact document date, or clause locator was not provided in the task source input, the record is marked `PRE_FREEZE_USER_REVIEW_REQUIRED`. Such records cannot silently operate as approved source authorities.

## Blocked-state rule

Regulated CQV output must be blocked or marked incomplete when the required K&S bundle, internal standard, source reference, mapping file, template record, or anchor is missing, expired, superseded, unreviewed, invalid, unmapped, or not approved for use.

No no-standards mode, metadata-only operating mode, placeholder bundle, or governance-only standard is freeze-ready for regulated CQV output.
