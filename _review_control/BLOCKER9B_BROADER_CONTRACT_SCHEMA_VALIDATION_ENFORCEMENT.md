# Blocker 9B — Broader Contract / Schema Validation Enforcement Review

Status: COMPLETED FOR SCOPED CONTRACT / SCHEMA / VECTOR ALIGNMENT — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-13
Review branch: review-spec-freeze-control

## Scope

This blocker aligned active non-deferred contract/action catalog metadata, registry aliases, selected action blocks, selected non-K&S schemas, and selected non-K&S static vectors after Blocker 9A introduced governance/security/registry schemas and A11 canonical envelope alignment.

## Files updated

Contract and registry catalog files:

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`
- `contracts/VALOR-contract-orch-wp.yaml`
- `contracts/VALOR-contract-orch-wp-user-driven-baseline.yaml`
- `contracts/VALOR-contract-orch-plan.yaml`
- `contracts/VALOR-contract-orch-doc.yaml`
- `contracts/VALOR-contract-orch-ps.yaml`
- `contracts/VALOR-contract-orch-ks.yaml`

Action block files:

- `action_blocks/WP_UPDATE_TASK_FIELDS.yaml`
- `action_blocks/WP_APPLY_PLAN_PROPOSAL.yaml`
- `action_blocks/WP_BIND_PRESET_CONTEXT.yaml`

Schemas and vectors:

- `schemas/contracts/action_block.schema.json`
- `schemas/contracts/contract_registry.schema.json`
- `schemas/contracts/contract_response.schema.json`
- `schemas/contracts/doc_draft_result.schema.json`
- `test_vectors/registry/registry_validation_vectors.json`
- `test_vectors/expected_doc_metadata.json`

Review control files:

- `_review_control/BLOCKER9B_BROADER_CONTRACT_SCHEMA_VALIDATION_ENFORCEMENT.md`
- `_review_control/REVIEW_STATE.md`
- `_review_control/SESSION_HANDOFF.md`

## Decisions applied

- Aligned active non-deferred contract action catalogs with explicit aliases/internal aliases, confirmation rules, statuses, and result schema references where missing.
- Updated RPT registry aliases to match the RPT contract and action blocks.
- Corrected the three WP action blocks to match `action_block.schema.json` shape.
- Aligned `WP_APPLY_PLAN_PROPOSAL` required payload fields to the WP contract: `plan_proposal_id`, `date_updates`, `planning_provenance_stamps`, and `calendar_logic_ref`.
- Corrected the PS example request to the A11 envelope: `contract`, `contract_version`, `action_id`, `action_type`, `mode`, `payload`, and `context.timestamp_utc`.
- Strengthened `contract_response.schema.json` so success requires `error: null` and failure requires `result: null` with a structured error object.
- Strengthened `action_block.schema.json` to distinguish canonical action blocks from alias blocks and prevent public aliases such as `BUILD_REPORT` from validating as canonical `action_type` values.
- Strengthened `contract_registry.schema.json` for registry category, owner, schema defaults, and action entry metadata.
- Updated registry vectors to separate full-object schema validation from semantic fragment validation.
- Aligned DOC draft result schema and vector by supporting intended DOC draft metadata fields and replacing stale `validation_summary` with `validation_result`.
- Touched `VALOR-contract-orch-ks.yaml` only for metadata-neutral contract/action catalog consistency and preserved TESTING_ONLY / PRODUCT_TESTING_ONLY regulated-use blocking.

## Explicit non-scope / deferrals

- `manifest.yaml` was not edited.
- Manifest was not regenerated.
- `smoke_test.py` was not edited.
- `scripts/pack_validation/generate_manifest.py` was not edited.
- `scripts/pack_validation/verify_manifest.py` was not edited.
- CI was not edited.
- No executable validator was implemented.
- No artifacts were generated.
- No templates were imported or converted.
- K&S schemas, K&S vectors, K&S library assets, and K&S source metadata were not edited.
- K&S was not promoted beyond TESTING_ONLY / PRODUCT_TESTING_ONLY.
- No source metadata was invented.
- No real regulated CQV/GMP output was approved.
- No implementation, delivery planning, clean repo, or ASBP audit was started.

## Remaining blockers

- Manifest regeneration and final manifest verification.
- Final freeze-readiness review.
- K&S user/site source metadata acceptance gate for real regulated CQV/GMP use.
- Real template source metadata acceptance before regulated use.
- Any future executable validation tooling remains deferred until explicitly approved.
