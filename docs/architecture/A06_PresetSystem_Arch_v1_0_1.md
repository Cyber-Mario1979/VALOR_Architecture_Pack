---
id: VALOR-block-A06-preset-system-architecture
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: frozen_controlled
date: 2026-06-12
dependencies:
  - VALOR-block-A00-specs-architecture-pack
  - VALOR-block-A01-sos-context-capability
  - VALOR-block-A02-principles-invariants
  - VALOR-block-A03-subsystems-authority
  - VALOR-block-A05-task-pool-architecture
  - VALOR-block-A07-calendar-logic-architecture
  - VALOR-block-A08-profile-library-architecture
summary: "Block A06 — Preset System Architecture: versioned selectors that bind task pool, profile, testing-only standards bundle, and calendar logic, using deterministic inclusion/exclusion and tailoring rules for staging CQV work packages."
acceptance_criteria:
  - Defines Preset System authority and boundaries.
  - Defines `PS-PE-HIGH` as the canonical high-complexity process-equipment preset ID.
  - Defines primary applicability fields: equipment_domain, complexity, scope.
  - Defines optional matching hints as secondary only.
  - Defines deterministic selection and tailoring rules.
  - Defines testing-only K&S binding without approving regulated CQV/GMP use.
  - Defines mandatory stamp propagation requirements for downstream subsystems.
---

# Preset System Architecture (Selectors + Binding Rules)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Preset System (PS) provides versioned, governed presets that convert a high-level context into a fully specified work recipe:

- which task pool version to use;
- which profile version to use;
- which standards bundle and templates are in scope;
- which calendar logic version applies;
- which tasks are required, optional, inserted, or excluded;
- which departments/roles are in scope;
- which stamps must propagate downstream.

PS is authoritative for:

- preset definitions and rules;
- binding references to governed assets;
- deterministic tailoring decisions encoded as rules;
- stamp set construction for downstream use.

PS is not authoritative for:

- WP/task truth instances;
- schedule computation;
- document generation;
- reports/exports;
- real regulated CQV/GMP approval.

## 2. Canonical v1.0.1 Preset

The canonical high-complexity process-equipment preset is:

- preset_id: `PS-PE-HIGH`
- version: `v1.0.1`
- library path: `libraries/preset_library/PS-PE-HIGH_v1.0.1.yaml`

Do not rename this preset to `PRESET-PE-HIGH`.

Examples, architecture text, test vectors, and downstream stamps should use `PS-PE-HIGH` unless a later controlled migration introduces a new ID.

## 3. Preset Entity Schema

A preset record must include:

- preset_id;
- version;
- revision_date;
- status;
- usage_classification;
- effective_date;
- source_checked_date;
- review_cycle_months;
- next_review_due;
- expiry_date;
- review_required;
- expired_behavior;
- name;
- description;
- applicability;
- bindings;
- rules;
- stamps;
- regulated_use_rule where a testing-only K&S bundle is bound.

The governed lifecycle metadata is local governed-library metadata only. It does not mean the preset is frozen, final, released, or regulated-approved.

## 4. Applicability Model

Primary applicability fields are:

- equipment_domain;
- complexity;
- scope.

For `PS-PE-HIGH`, the primary applicability is:

```yaml
equipment_domain: ProcessEquipment
complexity: High
scope: Project
```

Optional matching hints may be retained for user convenience or future matching logic, but they are secondary only and must not replace the primary schema.

Allowed optional matching hints include:

- system_type;
- tags_any;
- tags_all;
- scope_hints.

If primary fields conflict with matching hints, the preset resolver must return `CONFLICT` and require a controlled preset update or explicit user decision.

## 5. Bindings

A preset must bind explicit governed asset versions.

For `PS-PE-HIGH v1.0.1`, the required bindings are:

- task_pool_ref: `TP-PE-HIGH v1.0.1`;
- profile_ref: `PROF-PE-HIGH v1.0.1`;
- calendar_logic_ref: `CAL-WORKWEEK v1.0.1`, wrapper around canonical `CAL-WORKWEEK v1`;
- standards_bundle_ref: `BND-CQV-BASE v1.0.1`, with `TESTING_ONLY / PRODUCT_TESTING_ONLY` usage.

## 6. Testing-Only K&S Binding Rule

`PS-PE-HIGH` may bind to `BND-CQV-BASE v1.0.1` only as testing-only K&S while Blocker 3A remains in effect.

Required K&S binding fields:

- status: `TESTING_ONLY`;
- usage_classification: `PRODUCT_TESTING_ONLY`;
- testing_use_allowed: `true`;
- regulated_output_allowed: `false`;
- real_life_use_allowed: `false`;
- testing_only_stamp_required: `true`;
- required_output_stamp: `PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE.`

This binding supports product testing, dry runs, internal trials, behavior validation, and E2E workflow testing only.

It does not approve real regulated CQV/GMP output. Regulated output remains blocked/refused/marked incomplete until user/site source metadata acceptance is complete.

## 7. Rule Set

Rules define how to tailor the resolved task set and metadata.

A rule has:

- rule_id;
- rule_type: INCLUDE, EXCLUDE, OPTIONAL, INSERT, OVERRIDE, REQUIRE;
- condition;
- target;
- payload;
- priority;
- rationale.

Presets may not embed numeric durations or lead times. Presets reference governed profile keys only.

## 8. Deterministic Resolution Model

Resolving a preset produces a Preset Resolution object containing:

- preset_id/version;
- pinned task_pool_ref;
- pinned profile_ref;
- pinned calendar_logic_ref;
- pinned standards_bundle_ref;
- resolved rule decisions;
- resolved task set constraints;
- resolved departments/roles in scope;
- stamp set for downstream propagation.

Rule precedence is deterministic:

1. higher priority wins;
2. if same priority, OVERRIDE > INSERT > INCLUDE/EXCLUDE > OPTIONAL;
3. if still tied, stable sort by rule_id;
4. unresolved conflicts return `CONFLICT`.

## 9. Stamp Propagation Requirements

PS is responsible for producing the stamp set that Orchestration must carry into:

- WP staging and commit;
- Planning requests;
- document generation;
- reporting/export artifacts;
- downstream provenance and validation.

The minimum stamp set must include:

- preset_id/version;
- task_pool_id/version;
- profile_id/version;
- calendar_id/version and canonical calendar version where applicable;
- standards_bundle_id/version/status/usage_classification where applicable.

If Orchestration cannot confirm the stamp set, it must block commit/export/finalization paths that depend on those stamps.

## 10. Compatibility and Versioning Policy

A preset version is immutable once published as a governed version.

Any change to bindings, primary applicability, rule behavior, or output stamps requires a new version or a controlled pre-freeze update.

Binding compatibility checks must verify:

- task pool version exists and is compatible;
- profile version contains all required duration entries for task duration refs;
- calendar version exists and supports required arithmetic;
- standards bundle status is valid for requested use;
- testing-only K&S is not used for regulated output.

If bindings are incompatible, PS must fail with `CONFLICT / BINDING_INCOMPATIBLE`.

## 11. Error Semantics

Standard codes:

- VALIDATION_ERROR: invalid context, missing required fields;
- NOT_FOUND: preset/version not found;
- CONFLICT: ambiguous match, incompatible bindings, nondeterministic rules;
- UNSUPPORTED_OPERATION: unsupported matching strategy;
- INTERNAL_ERROR: unexpected.

PS-specific subcodes:

- NO_MATCH
- MULTIPLE_MATCHES
- BINDING_INCOMPATIBLE
- RULESET_NONDETERMINISTIC
- RULE_CONTRADICTION
- TESTING_ONLY_STANDARDS_BUNDLE_BLOCKS_REGULATED_OUTPUT

## 12. Contract Alignment Dependency

Preset contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: made PS-PE-HIGH canonical, normalized primary applicability fields, retained matching hints as secondary, added testing-only K&S binding rule, and clarified stamp propagation | Pre-freeze controlled update |
