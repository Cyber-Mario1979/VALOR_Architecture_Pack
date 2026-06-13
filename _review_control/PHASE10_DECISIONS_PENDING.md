# Phase 10 Decisions Pending Decision Log Merge

Status: PENDING_MERGE_TO_DECISION_LOG
Review branch: review-spec-freeze-control
Date: 2026-06-10

Reason: Direct updates to `_review_control/DECISION_LOG.md` returned repeated GitHub 409 SHA mismatch errors during the Phase 10 review session. This file preserves the Phase 10 decisions in repo memory until they can be merged into the main decision log.

## DEC-0097 — Keep governance gates, confirmations, and audit trail baseline

Date: 2026-06-10
Reviewed file/block: Phase 10 — A09 Governance & Branching
Category: Keep
Decision: Keep A09 as the baseline for governance gates, mandatory confirmations, readiness checks, branching concepts, approval records, overrides, and append-only audit events.
Reason: A09 defines Stage, Validate, Commit, Apply, Finalize, and Close gates; requires human confirmation for truth-changing or regulated-output actions; and defines append-only audit event fields, event types, stamps, and safe-failure behavior.
Impact: Implementation must retain CQV-style governance and auditability as first-class behavior.
Follow-up: Align the gate list with document-generation and export actions during approved freeze cleanup.

## DEC-0098 — Keep human/external approval boundary

Date: 2026-06-10
Reviewed file/block: Phase 10 — A09 Governance & Branching and A10 Security & Compliance
Category: Keep
Decision: Keep the boundary that Valor may record governance confirmations and prepare artifacts, but does not replace QMS approvals, electronic signatures, vendor contractual actions, real identity verification, or human authority.
Reason: A09 explicitly excludes QMS approvals, electronic signatures, and vendor contractual actions. A10 states identity/authorization are not cryptographically verified in v0.1.x and relies on role context, confirmations, audit capture, and refusal.
Impact: Product behavior must not imply legally binding approval/signature capability unless later integrated with validated identity/e-signature systems.
Follow-up: Reflect this boundary in UI/product wording during Phase 12.

## DEC-0099 — Keep Security & Compliance safe-output model

Date: 2026-06-10
Reviewed file/block: Phase 10 — A10 Security & Compliance
Category: Keep
Decision: Keep A10 as the baseline for non-disclosure, CQV-safe outputs, data minimization, sensitive project data handling, soft access controls, security audit events, and fail-closed behavior for regulated outputs.
Reason: A10 defines protected content, refusal behavior, no fabricated regulated facts, proposal-vs-commitment labeling, redaction options, excerpt controls, and no silent partial success.
Impact: All subsystem outputs must respect A10 constraints, especially DOC/RPT/K&S outputs and advisory responses.
Follow-up: Reconcile A10 policies into contracts and schemas where enforcement is required.

## DEC-0100 — Keep Contract Registry versioning and envelope baseline

Date: 2026-06-10
Reviewed file/block: Phase 10 — A11 Contract Registry
Category: Keep
Decision: Keep A11 as the baseline for contract definition, canonical envelope, SemVer compatibility policy, pre-call validation, subsystem validation, side-effect classification, and contract-level error semantics.
Reason: A11 defines contracts as mandatory formal subsystem interfaces, requires Orchestration to use contracts only, defines request/response envelopes, and sets compatibility/error rules.
Impact: Later implementation must not use hidden coupling or informal workflow calls outside contract actions.
Follow-up: Reconcile the registry catalog with actual contract files and action catalogs.

## DEC-0101 — Clarify Security & Compliance integration mechanism

Date: 2026-06-10
Reviewed file/block: Phase 10 — A10 and A11 SEC integration
Category: Modify
Decision: Clarify in the frozen spec that Security & Compliance is policy-first and enforced primarily by Orchestration/subsystem validators, with `VALOR-contract-orch-sec` only needed if SEC becomes a separated callable subsystem.
Reason: A10 states SEC is not a standalone feature and is enforced primarily by Orchestration with validator support, while A11 lists a SEC contract as optional if separated. This resolves the earlier ambiguity but should be stated explicitly across A03/A04/A10/A11.
Impact: Implementers will not create an unnecessary SEC contract unless a separated SEC subsystem is intentionally introduced.
Follow-up: Add a concise cross-reference in approved modifications.

## DEC-0102 — Clarify status and freeze terminology

Date: 2026-06-10
Reviewed file/block: Phase 10 — A09/A10/A11 metadata and governance terminology
Category: Conflict
Decision: Define a status taxonomy that distinguishes document front-matter `released`, review-control `candidate/not frozen`, branch `FROZEN`, document `FINAL`, WP `CLOSED`, and final pack `frozen`.
Reason: Many architecture files use `status: released`, A09 uses branch state `FROZEN`, and review-control says the pack is not frozen. Without a taxonomy, users may confuse released individual documents with a frozen architecture pack.
Impact: Freeze readiness and user trust may be undermined by ambiguous status terms.
Follow-up: Resolve during final freeze modification batch or manifest/pack-integrity review.

## DEC-0103 — Reconcile canonical contract registry with actual contract files

Date: 2026-06-10
Reviewed file/block: Phase 10 — A11 and manifest contract list
Category: Conflict
Decision: Reconcile A11’s canonical contract list with actual contract files before freeze.
Reason: A11 lists core contracts plus support contracts for TP, PS, PROF, CAL and optional SEC. The manifest shows contracts for DOC, KS, PLAN, PS, RPT, WP, and WP user-driven baseline, but not TP/PROF/CAL/SEC. The user-driven baseline contract also is not represented in A11’s canonical list.
Impact: Registry authority is not freeze-clean; implementers may not know which contracts are required, missing, optional, or special-purpose.
Follow-up: Update A11 and/or add missing contracts or formal deferrals after approval.

## DEC-0104 — Add a concrete contract registry metadata artifact

Date: 2026-06-10
Reviewed file/block: Phase 10 — A11 Contract Registry
Category: Missing
Decision: Add a concrete registry metadata artifact or table that lists each active contract, owner, version, action catalog, schema refs, dependencies, and status.
Reason: A11 defines what registry metadata must include, but the repository currently relies on individual contract files and manifest entries; the manifest does not include action catalogs, owner semantics, dependencies, registry status, or compatibility notes.
Impact: Contract completeness and freeze readiness cannot be verified from one canonical registry artifact.
Follow-up: Add registry metadata during approved cleanup or explicitly state A11 plus manifest is the registry approach.

## DEC-0105 — Add registry validation for action-catalog completeness

Date: 2026-06-10
Reviewed file/block: Phase 10 — A11 and prior contract findings
Category: Modify
Decision: Add an explicit registry validation requirement that architecture action catalogs, contract files, action-block files, and schemas must agree before freeze.
Reason: Earlier phases found mismatches in WP, Planning, DOC, RPT, and K&S action catalogs. A11 already requires action_type existence and known contracts, but does not define a pack-level consistency check across architecture docs, contracts, action blocks, and schemas.
Impact: Contract mismatches could survive into implementation unless the registry validates catalog completeness.
Follow-up: Enforce during Phase 11 validation/scripts review.

## DEC-0106 — Strengthen excerpt authorization and redaction enforcement

Date: 2026-06-10
Reviewed file/block: Phase 10 — A10 Security & Compliance with K&S carry-forward
Category: Modify
Decision: Strengthen how excerpt authorization and redaction options are represented in contracts and outputs.
Reason: A10 defines standards/copyright controls, redaction options, and restricted excerpt refusal, but previous K&S/DOC/RPT reviews found that request fields, authorization context, and applied-policy outputs are not yet contract/schema-enforced.
Impact: Licensed/internal/confidential content and sensitive project data could be inconsistently handled.
Follow-up: Reconcile A10 with K&S/DOC/RPT contracts and schemas in Phase 11.

## DEC-0107 — Clarify audit log ownership and storage

Date: 2026-06-10
Reviewed file/block: Phase 10 — A09 Governance & Branching
Category: Missing
Decision: Define who owns the audit trail and where audit events are stored or referenced.
Reason: A09 requires append-only audit events for governance-relevant actions and security events, but does not clearly assign audit-log ownership to Governance, Orchestration, WP, a registry, or an artifact store.
Impact: Audit trail implementation could fragment across subsystems.
Follow-up: Resolve in approved governance/registry cleanup or Phase 11 schema/test review.

## DEC-0108 — Defer detailed governance/security/registry schema validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 10 — A09/A10/A11
Category: Defer
Decision: Do not perform detailed governance, security, or contract-registry schema/test-vector validation during Phase 10.
Reason: Phase 10 reviewed architecture authority and identified registry/security integration gaps; formal schema/test validation belongs to Phase 11.
Impact: Phase 10 is complete without implementation or schema edits.
Follow-up: In Phase 11, validate governance/audit, security, contract registry, and contract envelope schemas/tests against A09/A10/A11.
