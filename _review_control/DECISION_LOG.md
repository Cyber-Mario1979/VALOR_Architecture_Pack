# VALOR Architecture Pack Decision Log

Status: ACTIVE
Review branch: review-spec-freeze-control

## Decision Format

Each decision should use this format:

```text
Decision ID:
Date:
Reviewed file/block:
Category: Keep | Modify | Missing | Conflict | Defer
Decision:
Reason:
Impact:
Follow-up:
```

---

## Prior Decisions

DEC-0001 through DEC-0081 were logged during Phases 0 through 8 and remain active.

Detailed text for prior decisions is preserved in repository history and summarized in `REVIEW_STATE.md`.

Active prior themes:

- candidate pack accepted, not frozen;
- no implementation during architecture review;
- SoS/product boundary retained;
- global invariant spine retained;
- AI role, DCF/document source chain, UI/product surface, and artifact-specific traceability require freeze clarification;
- A03/A04_1 authority and orchestration retained as baseline;
- asset-owner hierarchy, Security and Compliance integration, document metadata ownership, staged-plan policy, and document-generation gate require clarification;
- A04_2/WP spine retained as baseline;
- WP action catalog, schedule-apply naming, staged preview IDs, external execution evidence boundary, schema references, user-driven baseline fields, and selector/context naming require cleanup;
- governed library spine retained, but TP/PS/PROF/CAL data and schemas require normalization;
- Planning retained as proposal-only, but Planning action naming, apply boundary, unit handling, and provenance stamps require alignment;
- K&S retained as read-only citation/standards authority, but K&S data, schemas, contract actions, excerpt authorization, and standards-aware advisory boundary require cleanup;
- Document Factory retained as artifact/provenance owner, but DCF intake, accepted URS source-chain, DOC lifecycle contract, document schemas/templates, and AI extraction/drafting boundary require cleanup.

---

## DEC-0082 — Keep Reporting & Export projection-only authority

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 Reporting & Export
Category: Keep
Decision: Keep RPT as a projection and publishing layer that generates reports/exports from WP truth without mutating authoritative data.
Reason: A04_6 clearly defines RPT as projection-only, authoritative only for report/export artifact content, computed metrics with declared rules, and output stamping/provenance; it explicitly does not own WP/task truth or schedule truth.
Impact: Reporting/export implementation must never correct or mutate WP/task data while generating artifacts.
Follow-up: Ensure contract/action specs preserve projection-only behavior.

## DEC-0083 — Keep deterministic report/export reproducibility baseline

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 Reporting & Export
Category: Keep
Decision: Keep A04_6 reproducibility requirements for report/export artifacts.
Reason: A04_6 requires deterministic output from the same WP snapshot, stamps, schema version, and report type, and requires recording snapshot hash, schema version, stamps, generation timestamp, and action_id.
Impact: Later schemas and tests must verify reproducibility and metadata capture.
Follow-up: Validate in Phase 11 schemas/test vectors.

## DEC-0084 — Keep BUILD_REPORT as candidate report action

Date: 2026-06-10
Reviewed file/block: Phase 9 — RPT contract and BUILD_REPORT action block
Category: Keep
Decision: Keep BUILD_REPORT as a useful candidate action for deterministic WP/task reporting.
Reason: The RPT contract and action block define BUILD_REPORT as read-only/idempotent and based on WP snapshots.
Impact: BUILD_REPORT can remain as the initial report action, but the wider RPT catalog must be reconciled before freeze.
Follow-up: Resolve action catalog alignment in DEC-0086.

## DEC-0085 — Keep strict projection-only export/report addendum rules, but remove Canvas terminology

Date: 2026-06-10
Reviewed file/block: Phase 9 — Reporting/Export addendum
Category: Modify
Decision: Keep the addendum’s projection-only and strict export intent, but replace Canvas-specific wording with product-neutral report/export artifact language.
Reason: The addendum correctly states Build Report and Export must not change WP/task truth, plan proposals, applied stamps, or missing-field truth; however, it refers to Canvas objects and WP Canvas, which conflicts with product-neutral architecture language.
Impact: Projection rules remain strong while avoiding legacy/UI-specific wording in the frozen spec.
Follow-up: Edit only after explicit user approval.

## DEC-0086 — Reconcile RPT architecture action catalog with RPT contract/action block

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6, RPT contract, BUILD_REPORT action block
Category: Conflict
Decision: Reconcile the RPT action catalog before freeze.
Reason: A04_6 lists RPT_LIST_ARTIFACTS, RPT_GET_ARTIFACT, RPT_GENERATE_REPORT, RPT_GENERATE_EXPORT, RPT_VALIDATE_STAMPS, and RPT_VALIDATE_SCHEMA. The RPT contract/action block currently expose only BUILD_REPORT.
Impact: Export generation, artifact retrieval, stamp validation, and schema validation cannot be contract-enforced from the current contract.
Follow-up: Choose canonical action names and align A04_6, RPT contract, and action blocks after approval.

## DEC-0087 — Add explicit export contract/action path

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 and RPT contract
Category: Missing
Decision: Add an explicit export-generation contract/action path or formally defer export implementation before freeze.
Reason: A04_6 and the addendum define export behavior, but the current RPT contract only supports BUILD_REPORT and does not expose RPT_GENERATE_EXPORT or an equivalent export action.
Impact: Export is part of the architecture promise but not sufficiently represented in the current contract/action layer.
Follow-up: Resolve before final freeze or formally mark export as deferred.

## DEC-0088 — Align report/export stamp policy with artifact-specific traceability

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 traceability stamping
Category: Modify
Decision: Align RPT stamp policy with artifact-specific traceability decisions.
Reason: A04_6 defines a minimum stamp set of preset/profile/task_pool/calendar and recommends standards bundle, template, planning logic, contract, and architecture pack stamps when available. Earlier phases identified that document/report/export/advisory artifacts need artifact-specific stamp rules.
Impact: Reports and exports may under-stamp K&S, document metadata, planning proposal, or architecture/contract provenance unless rules are split by artifact type.
Follow-up: Reconcile with Phase 11 schemas and Phase 13 final freeze modifications.

## DEC-0089 — Enforce proposed-vs-committed truth in reports

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 planning/reporting carry-forward
Category: Modify
Decision: Reports that include planning data must explicitly label PROPOSED plan data versus COMMITTED WP date truth.
Reason: A04_6 says Planning may provide plan proposals for schedule overview reports and outputs must clearly label PROPOSED vs COMMITTED, while RPT is not authoritative for schedule truth.
Impact: Users could otherwise mistake proposed schedules for committed WP truth.
Follow-up: Add schema/report-section fields that separate proposed_start/end from committed_start/end and include plan_id/proposal state when applicable.

## DEC-0090 — Reconcile CSV export schema with A04_6 baseline columns

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 and `csv_export_schema.json`
Category: Conflict
Decision: Reconcile CSV export schema columns with the A04_6 baseline export columns.
Reason: A04_6 recommends columns including task_name, phase, task_type, owner_role, predecessor_ids, dependency_type, lag_days, proposed/committed/actual dates, and notes. The current CSV row schema uses a smaller/different set including task_description, owner, start_date, finish_date, elapsed_days, remaining_days, lateness_days, and time_elapsed_percent.
Impact: Export consumers may receive a schema different from the architecture promise.
Follow-up: Resolve during Phase 11 schema validation and approved schema cleanup.

## DEC-0091 — Replace permissive export result schema with enforceable schema

Date: 2026-06-10
Reviewed file/block: Phase 9 — `export_result.schema.json`
Category: Conflict
Decision: Replace or expand `export_result.schema.json` so it enforces export artifact metadata, schema version, stamps, format, and content/file reference.
Reason: The current export result schema has empty required fields, empty properties, and allows all additional properties.
Impact: Export contract validation cannot enforce the A04_6 artifact result structure.
Follow-up: Resolve in Phase 11 schema validation.

## DEC-0092 — Align report result schema with A04_6 and addendum report requirements

Date: 2026-06-10
Reviewed file/block: Phase 9 — `report_result.schema.json`, A04_6, reporting/export addendum
Category: Conflict
Decision: Align report result schema with A04_6 report types and the addendum’s report structure.
Reason: A04_6 lists multiple report types, the addendum defines report sections such as Overview, WP Snapshot, Tasks Snapshot, Plans Snapshot, Documents Snapshot, Risks/Issues, Status Summary, and Next Steps, while the schema currently supports only WP_TASKS_REPORT and requires fields that do not capture stamps/projection-only status/artifact metadata.
Impact: Report output validation does not fully enforce the architecture or addendum requirements.
Follow-up: Resolve in Phase 11 schema validation and approved reporting cleanup.

## DEC-0093 — Clarify strict export file-only policy and template compliance source

Date: 2026-06-10
Reviewed file/block: Phase 9 — Reporting/Export addendum
Category: Missing
Decision: Clarify strict export behavior, including the source of the required CSV template/header and how exact compliance is verified.
Reason: The addendum says export must refuse if exact template compliance cannot be guaranteed, produce a downloadable file, not print CSV inline, and copy the CSV header verbatim from the template file. Search did not surface a distinct export template/header file in this scoped review.
Impact: Strict export cannot be implemented deterministically unless the template/header source and validation rule are explicit.
Follow-up: Add/export template or formally define the CSV schema as the canonical template.

## DEC-0094 — Add RPT artifact registry/read model or defer it

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 and RPT contract
Category: Missing
Decision: Add an RPT artifact registry/read model or formally defer it.
Reason: A04_6 lists RPT_LIST_ARTIFACTS and RPT_GET_ARTIFACT and states RPT must record artifact metadata, but the contract only exposes BUILD_REPORT and does not define artifact listing/getting.
Impact: Generated reports/exports may lack retrievable artifact identity and metadata registry behavior.
Follow-up: Resolve with contract/schema review in Phase 10/11 or approved RPT cleanup.

## DEC-0095 — Add K&S and document metadata references to reporting inputs/outputs

Date: 2026-06-10
Reviewed file/block: Phase 9 — A04_6 and carried Phase 7/8 risks
Category: Missing
Decision: Add explicit RPT handling for K&S provenance and document metadata references where reports include standards/document traceability.
Reason: A04_6 says standards/templates may be referenced by ID/version and Document Factory metadata may be referenced by RPT, but the current RPT contract/action block does not include K&S/document metadata inputs or output structures.
Impact: Traceability reports may omit important document and standards provenance.
Follow-up: Reconcile with K&S and DOC metadata decisions in Phase 11.

## DEC-0096 — Defer full RPT schema/export validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 9 — reporting/export schemas
Category: Defer
Decision: Do not perform full reporting/export schema validation during Phase 9.
Reason: Phase 9 identified contract/action/schema mismatches, but full schema/test-vector validation belongs to Phase 11.
Impact: Phase 9 is complete without schema or spec edits.
Follow-up: In Phase 11, validate report_result, export_result, csv_export_schema, and any RPT contract schemas against A04_6 and the addendum.

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

\
## DEC-0109 — Keep validation scaffold as candidate quality gate

Date: 2026-06-10
Reviewed file/block: Phase 11 — schemas, validation, test vectors
Category: Keep
Decision: Keep the current validation scaffold as a useful candidate quality gate.
Reason: The pack includes manifest generation/verification scripts, render-input validation, a smoke test runner, schema files, and test vectors that provide an initial validation spine.
Impact: The validation scaffold can become the basis for freeze-readiness checks after enforcement gaps are closed.
Follow-up: Expand validation coverage before final freeze.

## DEC-0110 — Keep manifest integrity validation baseline

Date: 2026-06-10
Reviewed file/block: Phase 11 — manifest validation scripts
Category: Keep
Decision: Keep `generate_manifest.py`, `verify_manifest.py`, and smoke-test manifest verification as the pack integrity baseline.
Reason: The scripts deterministically hash files, record bytes, and verify missing, mismatched, and extra files against `manifest.yaml`.
Impact: Pack integrity can be checked reproducibly, but semantic architecture validation remains separate.
Follow-up: Keep manifest verification in the final validation suite.

## DEC-0111 — Keep render-input validator but classify it correctly

Date: 2026-06-10
Reviewed file/block: Phase 11 — `validation/validate_render_inputs.py`
Category: Keep
Decision: Keep the render-input validator as a placeholder coverage validator, not as a substitute for JSON Schema validation.
Reason: The validator checks dotted placeholder paths against render input payloads, which is useful for template rendering, but it is not general schema enforcement.
Impact: It should remain in the pack, but final validation must include proper JSON Schema and template-output checks.
Follow-up: Rename or document the validator scope clearly during cleanup.

## DEC-0112 — Reconcile contract envelope schemas with A11 and contract examples

Date: 2026-06-10
Reviewed file/block: Phase 11 — contract request/response schemas
Category: Conflict
Decision: Reconcile `contract_request.schema.json` and `contract_response.schema.json` with A11 and actual contract examples.
Reason: A11 and contract examples use `contract`, `contract_version`, `action_id`, `ok`, `result`, and `error`, while current schemas use `contract_id`, `status`, and `errors`, and require request `stamps` globally.
Impact: Contract validation will reject or under-validate canonical envelopes unless naming and required fields are standardized.
Follow-up: Resolve in schema cleanup before freeze.

## DEC-0113 — Expand WP/task schemas to match A04_2

Date: 2026-06-10
Reviewed file/block: Phase 11 — WP/task object schemas
Category: Conflict
Decision: Expand `work_package_schema.json` and `task_schema.json` to match A04_2 WP/task entities and lifecycle rules.
Reason: Current object schemas cover only a simplified ID/title/scope/task shape and omit A04_2 fields such as lifecycle_state, wp_type, complexity, references, task phase/type/status enums, dependencies, proposed/committed/actual dates, deterministic ID ledger, and mutability constraints.
Impact: WP truth cannot be validated against the architecture with the current schemas.
Follow-up: Align schemas with A04_2 and WP contract actions in Phase 11 cleanup.

## DEC-0114 — Replace permissive/stub schemas with enforceable schemas

Date: 2026-06-10
Reviewed file/block: Phase 11 — contract result schemas
Category: Conflict
Decision: Replace permissive or empty schemas with enforceable schemas.
Reason: Multiple schemas previously reviewed are stubs or overly permissive, including staged task set, plan proposal, DOC result, export result, and several K&S schemas.
Impact: Current validation can pass outputs that do not satisfy architecture or contract requirements.
Follow-up: Build enforceable schemas for all contract result types before freeze.

## DEC-0115 — Fix dotted required-field schema pattern

Date: 2026-06-10
Reviewed file/block: Phase 11 — document render-input schemas
Category: Conflict
Decision: Fix document schemas that use dotted strings in `required` arrays.
Reason: Dotted required strings are useful for the custom render-input validator, but they do not enforce nested requirements under JSON Schema semantics.
Impact: JSON Schema validation and custom placeholder validation currently imply different rules.
Follow-up: Split render-token coverage requirements from JSON Schema nested required declarations.

## DEC-0116 — Add architecture-to-contract/action/schema validation

Date: 2026-06-10
Reviewed file/block: Phase 11 — validation tools
Category: Missing
Decision: Add validation that compares architecture action catalogs, contract action catalogs, action-block files, and schemas.
Reason: Prior phases found repeated mismatches across WP, Planning, DOC, RPT, and K&S action names and result schemas. Current validation does not detect those mismatches.
Impact: Contract drift can survive smoke testing.
Follow-up: Add a registry/catalog validator before final freeze.

## DEC-0117 — Add governance, audit, security, and registry schemas/tests

Date: 2026-06-10
Reviewed file/block: Phase 11 — schemas and test vectors
Category: Missing
Decision: Add schemas and test vectors for governance audit events, security policy blocks, redaction/excerpt decisions, and contract registry metadata.
Reason: A09/A10/A11 define important governance/security/registry structures, but no matching schema/test coverage surfaced in Phase 11 search.
Impact: These critical control planes remain architecture-only and not validation-enforced.
Follow-up: Add schemas/tests or explicitly defer before freeze.

## DEC-0118 — Treat current test vectors as illustrative, not full coverage

Date: 2026-06-10
Reviewed file/block: Phase 11 — test vectors
Category: Modify
Decision: Treat current test vectors as illustrative seed examples, not freeze-complete validation coverage.
Reason: Existing vectors cover simple WP/stage/commit/plan/doc/report/export examples, but use mixed naming and older IDs, and do not cover the full architecture model.
Impact: Test vectors are useful, but they cannot support a freeze-readiness claim by themselves.
Follow-up: Normalize vectors to current canonical IDs, contracts, schemas, and governed library data.

## DEC-0119 — Add negative and invariant test vectors

Date: 2026-06-10
Reviewed file/block: Phase 11 — test vectors
Category: Missing
Decision: Add negative/invariant test vectors for safety and CQV failure paths.
Reason: The current vectors focus on expected successful artifacts and do not cover dependency cycles, ID reuse, missing stamps, wrong modes, unsupported contract versions, restricted excerpts, missing URS source, failed export strictness, or attempted truth mutation by RPT/DOC/PLAN.
Impact: Hard-stop invariants cannot be proven by the current tests.
Follow-up: Add negative vectors before final freeze.

## DEC-0120 — Add end-to-end core workflow test coverage

Date: 2026-06-10
Reviewed file/block: Phase 11 — test vectors and smoke test
Category: Missing
Decision: Add end-to-end workflow test vectors for core product flows.
Reason: The current smoke test validates manifest, schema loading, report vectors, and preset bindings, but not complete flows such as preset resolve → task stage → commit → plan → apply → doc draft/finalize → report/export, DCF → accepted URS → downstream RTM/DQ/IQ/OQ/PQ/VSR, or user-driven no-profile planning.
Impact: The pack cannot prove workflow-level readiness yet.
Follow-up: Add E2E vectors and validator execution after schema cleanup.

## DEC-0121 — Defer implementing schema/test fixes during Phase 11 review

Date: 2026-06-10
Reviewed file/block: Phase 11 — scope control
Category: Defer
Decision: Do not implement schema or test-vector fixes during Phase 11 review.
Reason: This phase is a specification review block, not an approved modification batch.
Impact: Findings are captured for the freeze modification batch; no architecture/spec files are edited now.
Follow-up: Carry fixes into Phase 13 consolidation or an approved pre-freeze cleanup batch.
