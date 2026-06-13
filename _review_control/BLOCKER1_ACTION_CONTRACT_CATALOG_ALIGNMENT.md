# Blocker 1 — Action and Contract Catalog Alignment

Status: PARTIALLY CLOSED — FREEZE STILL BLOCKED BY DOWNSTREAM RPT/K&S/SCHEMA ITEMS
Date: 2026-06-10
Review branch: review-spec-freeze-control

## User-approved direction

Use these categories for declared product scope:

1. Public/user-callable actions:
   - WP
   - PLAN
   - DOC
   - RPT
   - K&S when the user directly asks for standards/citation/advisory behavior

2. Internal service/resolver contracts:
   - PS may be active as an internal preset resolver/binding authority.
   - PS does not need to become an independent public callable subsystem unless explicitly required.

3. Non-callable governed support authorities:
   - TP
   - PROF
   - CAL

4. Policy-first cross-cutting control:
   - SEC

## Freeze rule applied

No partial or placeholder alignment is acceptable. If any claimed action cannot be fully mapped to owner, contract, canonical action_type, schemas, side-effect class, confirmation rule, and active/deferred status, reduce declared scope or keep freeze blocked.

## Files modified in this blocker

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`
- `docs/architecture/A11_ContractRegistry_Arch_v1_0_1.md`
- `docs/architecture/A04_1_Orchestration_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-rpt.yaml`
- `action_blocks/BUILD_REPORT.yaml`
- `action_blocks/WP_UPDATE_TASK_FIELDS.yaml`
- `action_blocks/WP_BIND_PRESET_CONTEXT.yaml`
- `action_blocks/WP_APPLY_PLAN_PROPOSAL.yaml`

## Decisions recorded

### B1-DEC-001 — Create canonical registry artifact

Decision: Created `contracts/CONTRACT_REGISTRY_v1.0.1.yaml` as the pack-level pre-freeze action/contract catalog.

Reason: A11 required a concrete registry artifact, and freeze requires one source of truth for contract IDs, action names, aliases, schemas, side-effect classes, confirmation rules, and status.

Impact: Registry now becomes the catalog reference that A11 and A04.1 point to.

### B1-DEC-002 — Public vs internal callable distinction

Decision: Not all active contracts are public/user-callable. WP, PLAN, DOC, RPT, and direct K&S requests are public/user-callable. PS is active internal service/resolver only.

Reason: Preset resolution is needed by orchestration flows, but PS does not need to become an independent user surface.

Impact: Public command aliases are absent for PS actions; internal aliases are allowed.

### B1-DEC-003 — TP/PROF/CAL are non-callable governed support authorities

Decision: TP, PROF, and CAL are classified as non-callable governed support authorities.

Reason: They are governed data/logic assets consumed by PS/WP/PLAN/RPT flows, not standalone public contract endpoints in the declared scope.

Impact: Missing TP/PROF/CAL contract files no longer create a registry contradiction for this declared scope.

### B1-DEC-004 — SEC is policy-first cross-cutting control

Decision: SEC is not a callable contract in this declared scope.

Reason: A10/A11 review already supported SEC as policy-first and enforced through orchestration, subsystem validators, governance gates, and redaction/refusal rules.

Impact: `VALOR-contract-orch-sec` is only required if SEC is later intentionally separated into a callable subsystem.

### B1-DEC-005 — Add VALIDATE_ONLY side-effect class

Decision: `VALIDATE_ONLY` is an allowed side-effect class.

Reason: Existing PLAN/K&S/RPT validation actions are neither read-only retrieval nor artifact generation; they perform deterministic checks without truth mutation.

Impact: A11 and the registry now include VALIDATE_ONLY.

### B1-DEC-006 — RPT canonical action naming

Decision: `RPT_GENERATE_REPORT` is the canonical contract action. `BUILD_REPORT` is a public command alias/action-block label, not the canonical contract action_type.

Reason: A04.6 listed canonical RPT actions while the current RPT contract exposed only BUILD_REPORT. This created catalog drift.

Impact: RPT contract and BUILD_REPORT action block now map to `RPT_GENERATE_REPORT`.

### B1-DEC-007 — Keep export/artifact path freeze-blocked

Decision: RPT export/list/get claims are not represented as freeze-ready yet.

Reason: Export request schema, export action block, strict header/template source, artifact metadata, and list/get registry behavior are not fully aligned yet.

Impact: `RPT_GENERATE_EXPORT`, `RPT_VALIDATE_SCHEMA`, `RPT_LIST_ARTIFACTS`, and `RPT_GET_ARTIFACT` remain cataloged but freeze-blocked pending RPT/export cleanup.

### B1-DEC-008 — K&S catalog mapped, content blocker retained

Decision: K&S public action mapping is cataloged for direct standards/citation/advisory requests, but full governed K&S content coverage remains a separate freeze blocker.

Reason: Blocker 1 aligns actions/contracts; it does not complete the full K&S standards bundle/content/schema/test obligation.

Impact: K&S is not freeze-complete until the K&S blocker is resolved.

## Remaining freeze blockers after Blocker 1

- RPT export/list/get schema/action/artifact/header alignment.
- Full governed K&S content/schema/test coverage.
- Contract/schema validation enforcement, including contract registry schema and semantic catalog validator.
- Manifest regeneration after all content edits.

## Blocker 1 done state

Blocker 1 is complete for category decision and primary catalog alignment.

Freeze remains blocked because several cataloged actions are intentionally marked freeze-blocked rather than falsely declared complete.
