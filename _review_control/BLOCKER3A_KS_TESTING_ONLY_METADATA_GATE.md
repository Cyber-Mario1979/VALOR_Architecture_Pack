# Blocker 3A — K&S Testing-Only Metadata Gate

Status: COMPLETED WITH CONNECTOR-LIMITED FILE EXCEPTIONS
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scoped task

Apply a K&S testing-only metadata correction so the internal governed K&S content pack may be used for product testing, dry runs, internal trials, validation of product behavior, and end-to-end workflow testing, while remaining blocked for real regulated CQV/GMP output.

## Decision recorded

A new governed operating state is added:

- `TESTING_ONLY`

Meaning:

- Product testing use is allowed when testing metadata is current.
- Regulated CQV/GMP output is not allowed.
- Real-life use is not allowed.
- Testing-only output requires the visible stamp: `PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE.`
- Exact external source editions, document dates, clause numbers, and locators remain unaccepted for regulated use.
- A separate controlled acceptance patch is required before any K&S asset may be promoted for real regulated CQV/GMP use.

## Lifecycle model applied

Allowed lifecycle statuses:

- TESTING_ONLY
- PRE_FREEZE_USER_REVIEW_REQUIRED
- ACTIVE
- DUE_FOR_REVIEW
- EXPIRED
- SUPERSEDED
- BLOCKED

Required metadata fields added to the model:

- usage_classification
- testing_use_allowed
- regulated_output_allowed
- testing_only_stamp_required
- real_life_use_allowed
- approval_status
- user_site_acceptance_required
- source_metadata_acceptance_status
- testing_expired_behavior
- regulated_expired_behavior

## Files successfully updated

- `libraries/knowledge_standards/references/external_references_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CQV-BASE_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CSV-ADDON_v1.0.1.yaml`
- `libraries/knowledge_standards/bundles/BND-CLEANROOM-ADDON_v1.0.1.yaml`
- `libraries/knowledge_standards/mapping/source_to_internal_requirements_v1.0.1.yaml`
- `schemas/contracts/ks_standard.schema.json`
- `schemas/contracts/ks_standards_list.schema.json`
- `schemas/contracts/ks_bundle.schema.json`
- `schemas/contracts/ks_bundles_list.schema.json`
- `schemas/contracts/ks_template.schema.json`
- `schemas/contracts/ks_templates_list.schema.json`
- `schemas/contracts/ks_citation_resolved.schema.json`
- `schemas/contracts/ks_external_references.schema.json`
- `schemas/contracts/ks_source_mapping.schema.json`
- `schemas/contracts/ks_bundle_validation.schema.json`
- `docs/architecture/A12_Knowledge_Standards_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-ks.yaml`
- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`
- K&S testing-only test vectors under `test_vectors/`

## Connector-limited normalization update

Connector updated successfully:

- `libraries/knowledge_standards/README.md`
- `libraries/knowledge_standards/templates/TPL-URS_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-RTM_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-DQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-IQ_v1.0.1.yaml`
- `libraries/knowledge_standards/templates/TPL-OQ_v1.0.1.yaml`

Connector blocked:

- `libraries/knowledge_standards/templates/TPL-PQ_v1.0.1.yaml`

Per fallback protocol, connector writes stopped after the block. Remaining normalization for `STD-CQV-BASE`, `TPL-PQ`, `TPL-VSR`, and review-control notes was applied locally and is pending commit.

When GitHub connector limitations prevent safe full-file edits, the assistant must use a user-apply package fallback rather than shrinking governed specification content into illustrative summaries.

## External references correction

External reference records now use testing placeholders where source metadata has not been accepted:

- `version_or_edition: TESTING_PLACEHOLDER_NOT_APPROVED`
- `document_date: TESTING_PLACEHOLDER_NOT_APPROVED`
- `locator: TESTING_TOPIC_ANCHOR_NOT_APPROVED_FOR_REGULATED_USE`
- `regulated_use_status: NOT_APPROVED_FOR_REGULATED_USE`
- `testing_use_allowed: true`
- `regulated_output_allowed: false`

No external standards text was copied or reproduced.

## Testing behavior

K&S may support product testing only when:

- requested use is product testing;
- the asset is `TESTING_ONLY`;
- testing metadata has not expired;
- required K&S assets are present;
- every output carries the required testing-only stamp.

## Regulated-use behavior

If a user requests real regulated CQV/GMP output while K&S is `TESTING_ONLY`, the system must block/refuse or mark the output incomplete.

If testing metadata expires, even product testing must block until renewed.

No no-standards mode or silent fallback to old standards is allowed.

## Test vectors created

- `test_vectors/ks_positive_testing_only_bundle_resolves_for_product_test.json`
- `test_vectors/ks_negative_testing_only_bundle_blocks_regulated_output.json`
- `test_vectors/ks_negative_testing_only_expired_blocks_testing.json`
- `test_vectors/ks_negative_unaccepted_source_blocks_regulated_output.json`

## Remaining K&S gate

K&S remains not approved as a real regulated CQV/GMP standards basis until user/site source metadata acceptance is completed in a separate controlled acceptance patch.

## Non-scope confirmation

No implementation work, delivery plan creation, clean implementation repository creation, old/current ASBP audit, unrelated blocker work, or manifest regeneration was performed.
