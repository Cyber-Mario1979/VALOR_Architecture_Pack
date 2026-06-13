# Blocker 8B — Negative and E2E Test Vector Coverage

Status: COMPLETED FOR SCOPED NON-K&S NEGATIVE AND E2E TEST VECTOR COVERAGE — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scope

This blocker added controlled non-K&S negative and E2E test-vector coverage for blocked, refused, incomplete, and traceable WP → PLAN → DOC → RPT behavior.

## Files created

Negative vectors:

- `test_vectors/negative/wp_negative_vectors.json`
- `test_vectors/negative/plan_negative_vectors.json`
- `test_vectors/negative/doc_negative_vectors.json`
- `test_vectors/negative/rpt_negative_vectors.json`

E2E vectors:

- `test_vectors/e2e/e2e_positive_wp_plan_doc_rpt.json`
- `test_vectors/e2e/e2e_negative_gate_failures.json`

## Negative behavior covered

WP negative coverage:

- `WP_COMMIT_STAGED_TASKS` without required provenance stamps.
- `WP_APPLY_PLAN_PROPOSAL` without valid `plan_proposal_id`.
- `WP_APPLY_PLAN_PROPOSAL` with stale or non-`PROPOSED` proposal.
- `WP_STAGE_TASKS` with invalid `task_type`.
- Dependency cycle in staged/committed task set.

PLAN negative coverage:

- `PLAN_GENERATE_PROPOSAL` with `PROFILE_BASED` basis but missing `profile_ref`.
- No-profile basis without full duration override provenance.
- Missing/incomplete `calendar_logic_ref`.
- Dependency cycle in input graph.
- Unsupported unit conversion.

DOC negative coverage:

- URS draft missing required source input such as `intended_use`.
- Missing `source_chain_provenance`.
- `doc_type=DCF` generation request while DCF generation is inactive.
- DOC finalization missing testing-only stamp.
- Real regulated output requested while K&S/template/bundle/citation assets are `TESTING_ONLY / PRODUCT_TESTING_ONLY`.

RPT negative coverage:

- `target_scope=ALL_WPS`.
- Missing stamps.
- Missing source snapshot hash.
- Attempted truth mutation through RPT.
- Gantt dates missing or finish-before-start.
- Generic JSON/CSV export requested as freeze baseline.

## E2E flows covered

Positive E2E flow:

- `WP_BIND_PRESET_CONTEXT`
- `WP_STAGE_TASKS`
- `WP_COMMIT_STAGED_TASKS`
- `PLAN_GENERATE_PROPOSAL`
- `WP_APPLY_PLAN_PROPOSAL`
- `DOC_GENERATE_DRAFT`
- `RPT_GENERATE_STATUS_REPORT`
- `RPT_GENERATE_WORKBOOK_EXPORT`
- `RPT_GENERATE_GANTT_CHART`

Positive assertions:

- Staging is `STAGED`.
- Commit is `COMMITTED`.
- Plan is `PROPOSED`.
- Dates are committed only through `WP_APPLY_PLAN_PROPOSAL`.
- DOC output is `DRAFT / PRODUCT_TESTING_ONLY`.
- RPT outputs are projection-only artifacts.
- Testing-only stamp is present where applicable.
- PLAN/DOC/RPT do not mutate WP truth except through the approved WP apply path.

Negative E2E flow coverage:

- PLAN failure stops downstream DOC/RPT success claims.
- DOC source-chain failure stops finalization.
- RPT `ALL_WPS` / missing-stamp failure creates no artifact.

## K&S boundary

K&S references in these vectors are metadata-only references:

- `BND-CQV-BASE v1.0.1`
- `STD-CQV-BASE v1.0.1`
- `TPL-URS v1.0.1`
- `TPL-DCF v1.0.1`
- `PRODUCT_TESTING_ONLY`
- required testing-only visible stamp

No K&S schemas, K&S vectors, K&S bundles, K&S standard records, or K&S source acceptance gates were edited.

## Explicit non-scope / deferrals

- No existing root vector rewrites were performed.
- No schema creation or schema edits were performed.
- No K&S schema/vector edits were performed.
- K&S was not promoted to regulated-active use.
- No real regulated CQV/GMP output was approved.
- Manifest was not regenerated.
- Full document render schema redesign was deferred.
- DCF generation/finalization was not activated.
- No artifacts were generated.
- No templates were imported or converted.
- No implementation, delivery planning, clean repo, or ASBP audit was started.
- No new public callable actions were added.
- Broad governance/security/registry schema work was deferred.
- Validator tooling rewrite was deferred.

## Remaining blockers

- K&S user/site source metadata acceptance gate for real regulated CQV/GMP use.
- Broader contract/schema validation enforcement after scoped vector coverage.
- Governance/audit/security/registry schemas/tests.
- Manifest regeneration.
- Final freeze-readiness review.
