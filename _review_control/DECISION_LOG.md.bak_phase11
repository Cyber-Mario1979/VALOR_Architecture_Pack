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
