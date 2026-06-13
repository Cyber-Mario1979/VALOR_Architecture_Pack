# VALOR Architecture Pack Review Plan

Status: ACTIVE
Review branch: review-spec-freeze-control
Review mode: block-by-block specification freeze

## 1. Purpose

This plan controls how the VALOR Architecture Pack will be reviewed across multiple sessions.

The goal is to convert the current pack from candidate specification into a frozen or freeze-ready product specification authority.

## 2. Review Method

Every block is reviewed using the same output categories:

| Category | Meaning |
|---|---|
| Keep | Content is acceptable as-is for the frozen specification. |
| Modify | Content is useful but must be changed before freeze. |
| Missing | Required product/specification content is absent. |
| Conflict | Content conflicts with product direction, another spec block, or clear implementation need. |
| Defer | Issue is real but can be postponed with an explicit reason. |

## 3. Session Discipline

Each session reviews one block or one small block group only.

No implementation work is allowed during architecture review.

No old implementation repo audit is allowed until this review is complete.

No delivery plan is created until the architecture review decisions are stable enough to drive delivery.

## 4. Review Sequence

### Phase 0 — Control Setup

Status: in progress

Scope:

- create `_review_control` folder;
- create charter, plan, state, decision log, and handoff;
- confirm repo-memory process.

Exit condition:

- control files committed to review branch;
- user can create a lightweight ChatGPT Project instruction if desired;
- next session has starter prompt.

### Phase 1 — Intake and Map

Status: started

Files:

- `README.md`
- `manifest.yaml`
- `docs/architecture/A00_Specs_Architecture_Pack_Arch_v1_0_1.md`

Purpose:

- understand pack identity;
- confirm reading order;
- confirm file families;
- identify immediate confusion risks.

Exit condition:

- pack accepted or rejected as candidate architecture pack;
- review map recorded;
- next block selected.

### Phase 2 — SoS and Invariants

Files:

- `docs/architecture/A01_SoS_Context_Capability_Arch_v1_0_1.md`
- `docs/architecture/A02_Principles_Invariants_Arch_v1_0_1.md`

Purpose:

- confirm product boundary;
- confirm capability map;
- confirm global invariants;
- identify whether AI, DCF, UI, and document-generation expectations are covered or missing.

### Phase 3 — Authority and Orchestration

Files:

- `docs/architecture/A03_Subsystems_Authority_Arch_v1_0_1.md`
- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`

Purpose:

- confirm subsystem ownership;
- confirm orchestration role;
- confirm gating;
- confirm contract envelope and mode rules.

### Phase 4 — Work Package Spine

Files:

- `docs/architecture/A04_2_WorkPackage_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-wp.yaml`
- `contracts/VALOR-contract-orch-wp-user-driven-baseline.yaml`
- relevant action blocks for WP operations.

Purpose:

- confirm WP truth model;
- confirm staged vs committed tasks;
- confirm selector and context binding implications;
- confirm task dependency integrity;
- confirm ID and lifecycle rules.

### Phase 5 — Task Pool, Preset, Profile, Calendar

Files:

- `docs/architecture/A05_TaskPool_Arch_v1_0_1.md`
- `docs/architecture/A06_PresetSystem_Arch_v1_0_1.md`
- `docs/architecture/A08_ProfileLibrary_Arch_v1_0_1.md`
- `docs/architecture/A07_CalendarLogic_Arch_v1_0_1.md`
- `libraries/task_pool/`
- `libraries/preset_library/`
- `libraries/profile_library/`
- `libraries/calendar/`

Purpose:

- confirm selector flow;
- confirm task pool selection;
- confirm profile duration rules;
- confirm calendar scheduling rules;
- confirm standards bundle binding from preset/context.

### Phase 6 — Planning

Files:

- `docs/architecture/A04_4_Planning_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-plan.yaml`
- `action_blocks/WP_APPLY_PLAN_PROPOSAL.yaml`

Purpose:

- confirm advisory planning;
- confirm proposed vs committed schedule;
- confirm dependencies;
- confirm profile/calendar stamps;
- confirm apply boundary.

### Phase 7 — Knowledge and Standards

Files:

- `docs/architecture/A12_Knowledge_Standards_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-ks.yaml`
- relevant standards schemas and bundles.

Purpose:

- confirm standards authority;
- confirm citation and anchor model;
- confirm standards-aware advice boundary;
- confirm whether standard references are sufficient for document generation and advisory AI.

### Phase 8 — Document Factory and DCF/URS Flow

Files:

- `docs/architecture/A04_5_DocumentFactory_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-doc.yaml`
- document schemas;
- templates;
- `Valor_Arch_Addendums_v1.0.1A/ARCH_Addendum_Document_Generation_Compliance_v1.0.1A.md`.

Purpose:

- confirm document lifecycle;
- confirm DCF intake coverage;
- confirm AI extraction and drafting role;
- confirm URS source-of-truth behavior;
- confirm downstream RTM/DQ/IQ/OQ/PQ/VSR generation dependency on accepted URS;
- confirm human review and provenance.

### Phase 9 — Reporting and Export

Files:

- `docs/architecture/A04_6_Reporting_Export_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `action_blocks/BUILD_REPORT.yaml`
- reporting/export addendum.

Purpose:

- confirm export outputs;
- confirm stamps;
- confirm report projections;
- confirm artifact rules.

### Phase 10 — Governance, Security, Contract Registry

Files:

- `docs/architecture/A09_Governance_Branching_Arch_v1_0_1.md`
- `docs/architecture/A10_Security_Compliance_Arch_v1_0_1.md`
- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`

Purpose:

- confirm execution governance;
- confirm security and compliance boundaries;
- confirm contract versioning and compatibility rules.

### Phase 11 — Schemas, Validation, Test Vectors

Files:

- `schemas/`
- `validation/`
- `test_vectors/`
- `scripts/pack_validation/`

Purpose:

- confirm schemas match architecture;
- confirm validation tools are usable;
- confirm test vectors cover core workflows;
- identify gaps before implementation.

### Phase 12 — Addendums and UX/Product Surface

Files:

- `Valor_Arch_Addendums_v1.0.1A/`
- any UI/UX related specs found during review.

Purpose:

- confirm UX/product surface coverage;
- identify missing product screens;
- identify advisory chat requirements;
- identify if new UI spec is needed before freeze.

### Phase 13 — Final Freeze Review

Purpose:

- consolidate decisions;
- identify final modifications;
- decide freeze/no-freeze;
- prepare delivery-plan handoff.

Exit condition:

- user accepts final review outcome;
- architecture pack is frozen or a specific modification batch is approved.

## 5. Required Output Per Session

Each session must produce:

- reviewed files;
- keep decisions;
- modify decisions;
- missing items;
- conflicts/confusions;
- deferred items;
- open questions;
- next session scope;
- updated session handoff.

## 6. Current Next Review Block

After control setup, the next review block is:

Phase 2 — SoS and Invariants

Files:

- `docs/architecture/A01_SoS_Context_Capability_Arch_v1_0_1.md`
- `docs/architecture/A02_Principles_Invariants_Arch_v1_0_1.md`
