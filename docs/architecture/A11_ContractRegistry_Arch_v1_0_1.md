---
id: VALOR-block-A11-contract-registry-architecture
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: released
date: 2025-12-23
dependencies:
  - VALOR-block-A00-specs-architecture-pack
  - VALOR-block-A01-sos-context-capability
  - VALOR-block-A02-principles-invariants
  - VALOR-block-A03-subsystems-authority
  - VALOR-block-A04-1-orchestration-architecture
summary: "Block A11 — Contract Registry Architecture: canonical contract IDs, versioning strategy, action envelopes, compatibility policy, and validation rules enabling Orchestration to coordinate subsystems deterministically."
acceptance_criteria:
  - Defines what a contract is in Valor and why contracts are mandatory.
  - Defines canonical contract identifiers, action catalogs, and per-contract versioning rules (SemVer).
  - Defines the standard envelope schema and required fields (traceability-aware).
  - Defines compatibility policy (major/minor/patch behavior) and negotiation rules.
  - Defines validation, error semantics, and fail-safe behaviors for contract invocation.
  - Defines a registry metadata schema for documenting contracts in the pack.
---

# Contract Registry Architecture (IDs + Versioning + Envelopes + Compatibility)

Terminology: See **A15_Global_Glossary_Arch_v1_0_1.md** for definitions.


## 1. Purpose
Contracts are the formal interface between Valor subsystems. They exist to:
- prevent hidden coupling,
- enforce governance and safety invariants,
- guarantee deterministic behavior and auditability,
- enable a “system of systems” to evolve without constant rewrites.

Orchestration may only invoke registered callable subsystem behavior through contracts. If a behavior in the declared callable product scope cannot be expressed as a registered contract action, it is not freeze-ready behavior.

Non-callable governed support authorities may be consumed only through registered callable contracts or governed library references; they are not independent public/user-callable contract endpoints unless explicitly promoted in a later declared scope.

---

## 2. What a Contract Is (Canonical Definition)
A contract is a versioned specification containing:
- contract_id and contract_version (SemVer),
- registry category (public/user-callable, internal service/resolver, policy extension, or other approved category),
- an action catalog (action_type list) with required/optional fields,
- request/response envelope schemas,
- validation rules and error taxonomy,
- invariants that must be enforced by the contract implementer,
- stamp propagation requirements (when relevant),
- side-effect class and confirmation requirement for every action.

A contract is not:
- a prompt narrative,
- a hidden rules list,
- an informal “workflow description” without schema,
- a public command by itself.

Public command names are aliases. The canonical executable identity is the registered `action_type`.

---

## 3. Canonical Registry Categories and Contract IDs

The canonical registry artifact for v1.0.1 is:

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

The registry is the pack-level catalog that classifies active contracts, support authorities, public aliases, canonical action types, schemas, side-effect classes, confirmation rules, and active/deferred status.

### 3.1 Public/User-Callable Contracts
These may be invoked by Orchestration when the user directly requests the related behavior:

- `VALOR-contract-orch-wp` — Orchestration ↔ Work Package System
- `VALOR-contract-orch-plan` — Orchestration ↔ Planning (Advisory)
- `VALOR-contract-orch-doc` — Orchestration ↔ Document Factory
- `VALOR-contract-orch-rpt` — Orchestration ↔ Reporting & Export
- `VALOR-contract-orch-ks` — Orchestration ↔ Knowledge & Standards when the user directly asks for standards, citation, source, bundle, template, or standards-aware advisory behavior

### 3.2 Public/User-Callable Policy Extension
- `VALOR-contract-orch-wp-user-driven-baseline` — a WP-owned policy extension for user-driven no-profile planning baseline behavior.

This extension does not create a second owner of WP truth. It is a scoped WP contract extension for explicit user-driven planning basis, duration overrides, and confirmation recording.

### 3.3 Internal Service/Resolver Contracts
- `VALOR-contract-orch-ps` — Orchestration ↔ Preset System as an internal preset resolver and binding authority.

PS is active in the declared scope as an internal service/resolver. It is not an independent public/user-callable subsystem unless explicitly promoted in a later declared scope.

### 3.4 Non-Callable Governed Support Authorities
The following are governed support authorities in the declared scope, not standalone public contracts:

- TP — Task Pool Library
- PROF — Profile Library
- CAL — Calendar Logic

They may be selected, consumed, referenced, stamped, and validated through PS/WP/PLAN/RPT flows, but they are not public/user-callable contract endpoints in v1.0.1 freeze scope.

### 3.5 Policy-First Cross-Cutting Control
SEC is a policy-first cross-cutting control, not a standalone callable contract in the declared scope.

Security and compliance rules are enforced by:
- Orchestration pre-call validation,
- subsystem validators,
- governance gates,
- output redaction/refusal rules,
- audit/security event capture where applicable.

`VALOR-contract-orch-sec` is only required if SEC is intentionally separated into a callable subsystem in a later declared scope.

---

## 4. SemVer Rules (Compatibility Policy)

### 4.1 Contract Versioning
Contracts use SemVer: MAJOR.MINOR.PATCH

- **MAJOR**: breaking changes (schema changes, renamed fields, action semantics changes)
- **MINOR**: backward-compatible additions (new optional fields, new actions)
- **PATCH**: bug fixes / clarifications with no behavior change required

### 4.2 Compatibility Requirements
Orchestration must:
- accept MINOR/PATCH upgrades within the same MAJOR,
- refuse incompatible MAJOR versions unless explicitly upgraded.

Subsystems must:
- reject requests using unsupported MAJOR versions,
- return CONFLICT / UNSUPPORTED_MAJOR_VERSION.

### 4.3 Negotiation Policy (Implementation Guidance)
Orchestration selects the highest supported MINOR within the required MAJOR.
If a subsystem returns a “supported_versions” list, orchestration may choose the best match deterministically.

---

## 5. Standard Envelope Schema (All Contracts)

### 5.1 Request Envelope (Canonical)
Required fields:
- contract (string)
- contract_version (string)
- action_id (string)
- action_type (string)
- mode (DESIGN|EXECUTION)
- payload (object)
- context (object with timestamp_utc)

Optional fields:
- actor (role/name)
- target (wp_id/task_id/doc_id/artifact_id)
- options (dry_run, return_content, strict, etc.)

Canonical structure:
```json
{
  "contract": "VALOR-contract-orch-wp",
  "contract_version": "v1.0.1",
  "action_id": "ACT-000001",
  "action_type": "WP_STAGE_TASKS",
  "mode": "EXECUTION",
  "actor": {"role": "User", "name": "optional"},
  "target": {"wp_id": "WP-0007"},
  "payload": {},
  "options": {"dry_run": false},
  "context": {"timestamp_utc": "2025-12-22T00:00:00Z"}
}
```

### 5.2 Response Envelope (Canonical)
Required fields:
- contract
- contract_version
- action_id
- ok (bool)
- result (object|null)
- error (object|null)

Canonical structure:
```json
{
  "contract": "VALOR-contract-orch-wp",
  "contract_version": "v1.0.1",
  "action_id": "ACT-000001",
  "ok": true,
  "result": {},
  "error": null
}
```

---

## 6. Stamp Propagation in Contracts

### 6.1 Stamp Requirements by Contract Category
- WP contract: stores preset/profile/task_pool/calendar refs in WP metadata; enforces staging/commit boundaries.
- WP user-driven baseline extension: records planning basis, user-provided duration sources, and required confirmations.
- PLAN contract: requires profile+calendar refs when profile-based planning is used and returns stamps + planning_logic_version.
- DOC contract: requires stamps + template/bundle refs; returns provenance metadata.
- RPT contract: requires stamp set for regulated reports/exports and returns schema_version + stamps.
- KS contract: resolves governed standards/templates/bundles/anchors and enforces citation/excerpt policy.
- PS contract: resolves/binds governed preset context internally and supplies preset/profile/task_pool/calendar/bundle references where applicable.

### 6.2 Stamp Validation Rule (Global)
For any action that generates regulated outputs (DOC_FINALIZE_ARTIFACT, RPT_GENERATE_EXPORT, etc.):
- missing stamp set → INVARIANT_VIOLATION / MISSING_TRACEABILITY_STAMPS.

---

## 7. Action Catalog Structure (Per Contract)

Each contract must define:
- action_type name,
- allowed modes,
- required payload fields,
- validation rules,
- result schema,
- public command aliases or internal aliases,
- active/deferred/freeze-blocked status,
- confirmation rule,
- side-effect classification.

Allowed side-effect classes:
- READ_ONLY
- VALIDATE_ONLY
- STAGE_ONLY
- MUTATES_TRUTH
- GENERATES_ARTIFACT

Example (WP contract snippet):
- WP_GET — READ_ONLY — no confirmation
- WP_STAGE_TASKS — STAGE_ONLY — no confirmation
- WP_COMMIT_STAGED_TASKS — MUTATES_TRUTH — confirmation required
- WP_UPDATE_TASK_FIELDS — MUTATES_TRUTH — confirmation required

Validation-only actions are distinct from read-only actions because they perform deterministic checks and may return pass/fail diagnostics, but they do not mutate truth or generate governed artifacts.

This classification is used by Orchestration, Governance, and SEC policy controls to enforce gates.

---

## 8. Validation and Guardrails

### 8.1 Pre-Call Validation (Orchestration)
Orchestration must validate:
- contract is known in `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`,
- contract_version is supported,
- action_type exists in the registered catalog,
- public command alias maps to exactly one canonical action_type,
- required fields are present,
- mode is permitted,
- side-effect class is known,
- if action is MUTATES_TRUTH, confirmation has been recorded,
- if action is a final regulated artifact action, required confirmation and stamp gates are satisfied.

### 8.2 Subsystem Validation (Implementer)
Subsystems must validate:
- schema correctness,
- invariants relevant to the domain (cycles, stamps, immutability),
- confirmation flags where the contract requires them,
- and must fail closed on missing required fields.

### 8.3 Idempotency Guidance
Actions should specify idempotency where relevant:
- READ actions: idempotent
- VALIDATE actions: idempotent for the same input set
- STAGE actions: idempotent if same inputs produce same staged hash
- COMMIT actions: either:
  - idempotent via staged_task_set_id (commit once), or
  - returns CONFLICT if already committed

---

## 9. Error Semantics (Contract-Level)
Standard codes (A01):
- MODE_VIOLATION
- VALIDATION_ERROR
- INVARIANT_VIOLATION
- NOT_FOUND
- CONFLICT
- UNSUPPORTED_OPERATION
- INTERNAL_ERROR

Contract-specific subcodes include:
- CONTRACT_NOT_REGISTERED
- ACTION_TYPE_UNKNOWN
- CONTRACT_VERSION_UNSUPPORTED
- UNSUPPORTED_MAJOR_VERSION
- PAYLOAD_SCHEMA_MISMATCH
- CONFIRMATION_REQUIRED

Example error:
```json
{
  "code": "CONFLICT",
  "subcode": "CONTRACT_VERSION_UNSUPPORTED",
  "message": "Requested contract_version v2.0.0 is not supported. Supported: v1.0.1.",
  "entity": "contract",
  "remediation": "Use a supported version or upgrade the orchestration contract registry."
}
```

---

## 10. Contract Registry Metadata Artifact

The pack-level registry artifact is:

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`

Each registry entry must include:
- contract_id,
- current version or active version,
- registry category,
- owner subsystem/control/authority,
- contract file path where applicable,
- public aliases or internal aliases,
- action catalog,
- side-effect class per action,
- confirmation rule per action,
- schema references,
- action block reference where applicable,
- active/deferred/freeze-blocked status,
- dependencies on governed support authorities or cross-cutting policy controls.

This enables:
- reproducible builds,
- audit trace (“which contract version governed this export”),
- safer evolution,
- pack-level action catalog validation.

Before freeze, A11, the registry artifact, contract files, action-block files, and schemas must agree. Any action marked freeze-blocked in the registry cannot be represented as freeze-ready product behavior.

---

---

## CHANGELOG
| Date       | Changes     | Type / Version |
| ---------- | ----------- | -------------- |
| 2026-06-10 | Pre-freeze Blocker 1 catalog classification, registry artifact, callable/internal/support/policy categories, and VALIDATE_ONLY side-effect class added | Arch_v1.0.1-control |
| 2025-12-23 | First Issue | Arch_v1.0.1    |
