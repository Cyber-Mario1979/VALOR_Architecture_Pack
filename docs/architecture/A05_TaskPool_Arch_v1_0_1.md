---
id: VALOR-block-A05-task-pool-architecture
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
  - VALOR-block-A04-2-work-package-architecture
summary: "Block A05 — Task Pool Library Architecture: governed catalog of atomic tasks with metadata, default dependency wiring, deterministic selection rules, enum-aligned task_type, and high-complexity process-equipment FAT chain coverage."
acceptance_criteria:
  - Defines Task Pool as the authoritative source of atomic task definitions and metadata.
  - Defines atomic task entity schema and local governed-library lifecycle metadata.
  - Defines deterministic selection rules and version pinning.
  - Defines default dependency wiring and insertion blocks.
  - Includes full FAT prep/execution/report/acceptance chain for high-complexity process equipment.
  - Keeps task_type aligned to the WP/TP task_type enum.
  - Defines governance/change control expectations and integrity invariants.
---

# Task Pool Library Architecture (Atomic Tasks + Metadata + Selection Rules)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.

## 1. Purpose and Authority

The Task Pool Library (TP) is Valor's authoritative catalog of reusable, atomic task definitions.

It exists to:

- standardize CQV task decomposition;
- enable deterministic task suggestion and staging;
- provide consistent metadata for planning, reporting, and document generation;
- provide default dependency wiring that can be instantiated into WP tasks.

TP is authoritative for:

- atomic task definitions;
- task metadata;
- default dependency wiring patterns;
- versioned task-pool change control.

TP is not authoritative for:

- WP task instances;
- committed dates;
- execution evidence;
- user/site tailoring decisions;
- schedule computation.

## 2. Canonical v1.0.1 Task Pool

The declared task pool asset for this blocker is:

- `libraries/task_pool/TP-PE-HIGH_v1.0.1.yaml`
- task_pool_id: `TP-PE-HIGH`
- version: `v1.0.1`
- scope: ProcessEquipment / High / Project

Architecture examples should reference `TP-PE-HIGH` for the declared high-complexity process-equipment baseline.

## 3. TaskPool Entity Schema

A TaskPool must include:

- task_pool_id;
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
- description;
- owner_function;
- integrity;
- governance;
- task_type_policy;
- tasks.

The governed lifecycle metadata is local governed-library metadata only. It does not mean the task pool is frozen, final, released, or regulated-approved.

## 4. Atomic Task Entity Schema

An AtomicTask is a reusable definition, not a WP task instance.

Required fields:

- atomic_task_id;
- name;
- phase;
- task_type;
- owner_role_default;
- applicability_tags;
- required_inputs;
- outputs;
- duration_ref;
- dependency_wiring.

Optional fields:

- flags;
- notes.

Atomic tasks must not embed numeric durations. Durations are referenced by `duration_ref.profile_key` and resolved by Profile Library.

## 5. Task Type Policy

`task_type` must remain aligned to the WP/TP task_type enum:

- AUTHORING
- REVIEW
- APPROVAL
- EXECUTION
- REPORTING
- VENDOR_WAIT
- PROCUREMENT_WAIT
- LEAD_TIME

Non-enum duration meaning belongs in Profile Library under `profile_task_semantic`, not in Task Pool `task_type`.

## 6. Dependency Wiring

Dependency wiring expresses default relationships when atomic tasks are instantiated into a WP.

Fields:

- predecessors: array of wiring refs;
- each predecessor ref includes atomic_task_id, dependency_type, and lag_days.

Baseline dependency support is FS only for v1.0.1 unless a later controlled update expands the model.

Dependency wiring must be acyclic.

## 7. Selection Rules

Task selection is deterministic and governed by:

- explicit preset binding;
- selection context;
- include/exclude rules;
- optionality flags;
- version pinning.

Given the same task_pool_id/version and selection context, resolution must return the same ordered task set.

Ambiguity must return `CONFLICT`, not guessing.

Ordering is derived by:

1. dependency graph topological order;
2. stable tie-break by phase order;
3. stable tie-break by atomic_task_id.

## 8. High-Complexity Process Equipment FAT Chain

The declared high-complexity process-equipment path includes the FAT chain.

The chain is limited to project/task modeling only and does not add ERP/procurement integration, resource loading, execution evidence ingestion, or delivery planning.

Required FAT path:

```text
PEH-MFG-LEAD
→ PEH-FAT-SCHED
→ PEH-FAT-PREP
→ PEH-FAT-EXEC
→ PEH-FAT-REPORT
→ PEH-FAT-ACCEPTANCE
→ PEH-LOGISTICS
```

Required FAT task definitions:

- `PEH-FAT-SCHED`: vendor wait / scheduling coordination;
- `PEH-FAT-PREP`: authoring/preparation package;
- `PEH-FAT-EXEC`: FAT execution;
- `PEH-FAT-REPORT`: FAT report and punch-list summary;
- `PEH-FAT-ACCEPTANCE`: FAT acceptance / release-to-ship decision;
- `PEH-LOGISTICS`: logistics/delivery lead time after FAT acceptance.

FAT tasks may use `phase: OTHER` in v1.0.1 unless a later schema update adds `FAT` to the phase enum. The FAT-specific meaning is carried by atomic_task_id, name, tags, and profile semantics.

## 9. Duration References

Every atomic task requiring a duration must reference a profile key.

Approved FAT profile keys:

- FAT_SCHEDULING_DUR
- FAT_PREP_DUR
- FAT_EXECUTION_DUR
- FAT_REPORT_DUR
- FAT_ACCEPTANCE_DUR
- LOGISTICS_DELIVERY_DUR

If a task duration_ref cannot be resolved and no explicit stamped duration override exists on the WP task instance, Planning must refuse.

## 10. Governance and Change Control

Task pools are versioned and immutable per governed version.

Any change to tasks, metadata, default wiring, or applicability requires a new version or controlled pre-freeze update.

Pre-release integrity checks must include:

- schema validation;
- uniqueness of atomic_task_id;
- cycle detection;
- duration_ref.profile_key existence in the bound profile;
- dependency type support;
- tag consistency checks.

## 11. Error Semantics

Standard codes:

- VALIDATION_ERROR: invalid context or invalid filters;
- INVARIANT_VIOLATION: cycles, duplicate IDs, missing required fields;
- NOT_FOUND: pool/task not found;
- CONFLICT: ambiguous match or incompatible version refs;
- UNSUPPORTED_OPERATION: unsupported dependency type requested;
- INTERNAL_ERROR: unexpected.

TP-specific subcodes:

- POOL_CYCLE_DETECTED
- DUPLICATE_ATOMIC_TASK_ID
- CONTEXT_INSUFFICIENT
- VERSION_UNSUPPORTED
- DURATION_REF_NOT_FOUND
- FAT_CHAIN_INCOMPLETE

## 12. Integration Requirements

- Presets bind explicit task_pool_id/version.
- WP stages task instances from resolved atomic tasks.
- Planning reads WP task snapshots and resolves durations through Profile Library.
- Reporting and DOC consume WP truth; they do not mutate Task Pool.

## 13. Contract Alignment Dependency

Task Pool contract/action naming remains a later contract/action registry semantic validation dependency.

This blocker aligns the architecture and governed library content only. It does not edit contract files.

## CHANGELOG

| Date       | Changes | Type / Version |
| ---------- | ------- | -------------- |
| 2025-12-23 | First Issue | Arch_v1.0.1 |
| 2026-06-12 | WP/Planning/Governed Library cleanup: added governed-library lifecycle expectations, locked enum-aligned task_type policy, aligned TP-PE-HIGH references, and required FAT prep/execution/report/acceptance chain coverage | Pre-freeze controlled update |
