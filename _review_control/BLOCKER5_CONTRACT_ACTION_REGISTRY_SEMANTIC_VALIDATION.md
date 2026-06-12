# Blocker 5 — Contract/action registry semantic validation

Status: COMPLETED FOR SCOPED WP / PLAN / TP / PS / PROF / CAL SEMANTIC ALIGNMENT — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scope

This blocker covered only WP / PLAN / TP / PS / PROF / CAL contract-action semantic alignment.

## Files edited and verified

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`
  - Changed `PS_VALIDATE_BINDINGS` side effect from `READ_ONLY` to `VALIDATE_ONLY`.
  - Preserved PS as `INTERNAL_SERVICE_RESOLVER`.
  - Preserved TP / PROF / CAL as non-callable governed support authorities.
- `contracts/VALOR-contract-orch-wp.yaml`
  - Strengthened plan-apply provenance and testing-only K&S stamp handling.
- `contracts/VALOR-contract-orch-wp-user-driven-baseline.yaml`
  - Strengthened user-driven no-profile duration override provenance.
- `contracts/VALOR-contract-orch-plan.yaml`
  - Strengthened governed profile default, stamped no-profile exception, calendar wrapper semantics, mixed-unit behavior, and planning provenance stamps.
- `contracts/VALOR-contract-orch-ps.yaml`
  - Changed `PS_VALIDATE_BINDINGS` to `VALIDATE_ONLY` in the PS contract.
  - Preserved PS as internal resolver only.
- `libraries/profile_library/PROF-PE-HIGH_v1.0.1.yaml`
  - Changed only FAT selector context phase values from `FAT` to `OTHER`.
  - Preserved FAT profile keys, values, units, descriptions, and `profile_task_semantic`.
- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`
  - Replaced stale `PRESET-PE-HIGH` example with `PS-PE-HIGH`.
  - Replaced `equipment_type` with `equipment_domain`.
  - Included `complexity` and `scope`.

## Files reviewed with no edit required

- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`
  - Already preserves WP/PLAN public scope, PS internal resolver scope, and TP/PROF/CAL non-callable support-authority status.
- `libraries/task_pool/TP-PE-HIGH_v1.0.1.yaml`
  - TP FAT tasks already use phase `OTHER`; TP remains non-callable.
- `libraries/calendar/CAL-WORKWEEK_v1.0.1.yaml`
  - CAL remains non-callable and preserves the CAL-WORKWEEK v1.0.1 wrapper around canonical CAL-WORKWEEK v1 with UTC+02:00.

## Explicit action deferrals

The following were not added and remain deferred unless explicitly approved later:

- `WP_VALIDATE`
- `PS_VALIDATE_RULESET`
- `PLAN_PREVIEW`
- `WP_CLOSE`
- `WP_UPDATE_DEPENDENCIES`

PLAN preview remains represented as `PLAN_GENERATE_PROPOSAL` with `dry_run=true`.

## K&S rule preserved

K&S remains `TESTING_ONLY` / `PRODUCT_TESTING_ONLY` only. No K&S asset was promoted to active regulated use. No source editions, dates, clauses, or locators were invented.

## Non-scope confirmation

No implementation, delivery plan, clean repo, ASBP audit, DOC/DCF/URS work, product-surface work, unrelated blocker expansion, RPT/export expansion, broad governance-layer creation, public TP/PROF/CAL callable action, or phase-enum expansion was performed.

## Remaining blockers

Freeze remains blocked by other pre-freeze work, including K&S source metadata acceptance for real regulated use, DOC/DCF/URS source chain, product surface, non-K&S validation/test vectors, governance/security/registry schemas, manifest regeneration, and final freeze-readiness review.
