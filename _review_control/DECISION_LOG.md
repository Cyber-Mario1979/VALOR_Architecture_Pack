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

DEC-0001 through DEC-0033 were logged during Phases 0 through 4 and remain active. Their detailed text is preserved in repository history and summarized in `REVIEW_STATE.md`.

Active prior themes:

- candidate pack accepted, not frozen;
- no implementation during architecture review;
- SoS/product boundary retained;
- global invariant spine retained;
- AI role, DCF/document source chain, UI/product surface, and artifact-specific traceability require freeze clarification;
- A03/A04_1 authority and orchestration retained as baseline;
- asset-owner hierarchy, Security and Compliance integration, document metadata ownership, staged-plan policy, and document-generation gate require clarification;
- A04_2/WP spine retained as baseline;
- WP action catalog, schedule-apply naming, staged preview IDs, external execution evidence boundary, schema references, user-driven baseline fields, and selector/context naming require cleanup.

---

## DEC-0034 — Keep governed library architecture spine

Date: 2026-06-10
Reviewed file/block: Phase 5 — A05/A06/A07/A08
Category: Keep
Decision: Keep the architecture spine for Task Pool, Preset System, Profile Library, and Calendar Logic.
Reason: A05 defines Task Pool as the authoritative atomic task catalog; A06 defines Preset as the governed selector/binder; A08 defines Profile as governed duration/lead-time data; A07 defines Calendar Logic as governed working-day rules.
Impact: Later Planning, Reporting, Document Factory, schemas, and validation must consume these governed assets rather than embedding durations, selections, or calendar rules in prompts or ad hoc logic.
Follow-up: Reconcile library/schema/contract gaps before final freeze.

## DEC-0035 — Keep seed library files as useful candidate data, not freeze-clean data

Date: 2026-06-10
Reviewed file/block: Phase 5 — governed library YAML files
Category: Keep
Decision: Keep the current seed library files as useful candidate/reference data for review.
Reason: The task pool, preset, profile, and calendar files demonstrate the intended CQV flow and provide concrete IDs/versions for task staging, duration resolution, and working-week logic.
Impact: The library files are valuable but must not be treated as freeze-clean without schema and consistency cleanup.
Follow-up: Validate and normalize during Phase 11; make targeted edits only after user approval.

## DEC-0036 — Clarify governed library owner hierarchy

Date: 2026-06-10
Reviewed file/block: Phase 5 — A05/A06/A07/A08 owner model
Category: Modify
Decision: Clarify the owner hierarchy for Task Pool, Preset, Profile Library, and Calendar Logic in A03/A04-level authority language before freeze.
Reason: Phase 5 confirms these are governed asset libraries with authority over their own data, but Phase 3 already found ambiguity around whether Profile Library and Calendar Logic are standalone subsystems or governed assets.
Impact: Implementation and contracts could drift if TP/PS/PROF/CAL are inconsistently treated as subsystems, libraries, or registry assets.
Follow-up: Resolve with A03/A04 clarification or during Phase 10 Contract Registry review.

## DEC-0037 — Add or formally defer TP/PROF/CAL contract files

Date: 2026-06-10
Reviewed file/block: Phase 5 — A05/A07/A08 contract references
Category: Missing
Decision: Decide before freeze whether `VALOR-contract-orch-tp`, `VALOR-contract-orch-prof`, and `VALOR-contract-orch-cal` must exist as contract files or be formally deferred.
Reason: A05, A08, and A07 each define implementation-ready contract names/actions, but repository search did not find matching contract files for TP, PROF, or CAL. The manifest shows a PS contract but not TP/PROF/CAL contracts.
Impact: The architecture promises contract-mediated access, but implementation contract authority is incomplete unless those contracts are added or explicitly deferred.
Follow-up: Revisit in Phase 10 Contract Registry and Phase 11 schema/validation review.

## DEC-0038 — Reconcile Preset architecture with seed preset schema

Date: 2026-06-10
Reviewed file/block: Phase 5 — A06 and `PS-PE-HIGH_v1.0.1.yaml`
Category: Conflict
Decision: Reconcile the seed preset file with A06 Preset schema before freeze.
Reason: A06 requires applicability fields such as equipment_domain, complexity, and scope, plus bindings and a rule_set. The seed preset uses system_type, tags_any, scope_hints, rules.matching/staging, and has `standards_bundle_ref: null`.
Impact: Preset resolution and stamp propagation can become brittle if architecture and seed data use different selector schemas.
Follow-up: Normalize schema in Phase 11 or approved modification batch; decide whether null standards bundle is allowed and how it must be stamped.

## DEC-0039 — Remove calendar-rule duplication from Profile data

Date: 2026-06-10
Reviewed file/block: Phase 5 — A07/A08 and `PROF-PE-HIGH_v1.0.1.yaml`
Category: Conflict
Decision: Remove or reclassify calendar-rule fields from the Profile Library data model.
Reason: A08 states Profile is not authoritative for calendar rules, while A07 states Calendar Logic owns working-day/weekend/holiday rules. The seed profile embeds `calendar_policy` with working days, weekends, and successor rule.
Impact: Profile and Calendar assets could contradict each other and produce non-deterministic planning/reporting behavior.
Follow-up: Keep only profile duration/lead-time data in Profile; reference the Calendar asset by ID/version through Preset/WP context.

## DEC-0040 — Normalize task taxonomy between Task Pool and Profile entries

Date: 2026-06-10
Reviewed file/block: Phase 5 — A05/A08 and task/profile library files
Category: Conflict
Decision: Normalize `task_type`, phase, and profile-key taxonomy between Task Pool and Profile entries.
Reason: Task Pool task_type values follow the A05/A04 enum, while Profile context selectors use values such as CYCLE, PROTOCOL_AUTHORING, REPORT, MANUFACTURING_LEADTIME, and VENDOR_COORDINATION_BLOCK. These are not the same as the task_type enum used by atomic tasks.
Impact: Profile resolution may fail or become dependent on implicit translation rules that are not specified.
Follow-up: Either align profile context selectors to task enum values or define an explicit subtype/profile-selector taxonomy.

## DEC-0041 — Add missing FAT execution chain or mark it out of scope

Date: 2026-06-10
Reviewed file/block: Phase 5 — A05 and `TP-PE-HIGH_v1.0.1.yaml`
Category: Missing
Decision: Add a clear FAT execution chain to the high-complexity process equipment task pool, or explicitly mark FAT execution as out of scope for the seed dataset.
Reason: A05 gives a canonical PO/lead-time/FAT/shipment/site-receipt chain, while the seed task pool moves from manufacturing lead time to FAT scheduling and then logistics; logistics requires FAT complete, but no FAT execution task appears in the dependency chain.
Impact: Generated schedules may skip a major CQV/vendor execution block.
Follow-up: Resolve during approved task-pool cleanup or Phase 6 Planning review if planning exposes the gap.

## DEC-0042 — Clarify standards bundle nullability in presets

Date: 2026-06-10
Reviewed file/block: Phase 5 — A06 and `PS-PE-HIGH_v1.0.1.yaml`
Category: Missing
Decision: Clarify whether presets may have no standards bundle, and if so define a formal no-bundle policy.
Reason: A06 treats standards bundle binding and stamp propagation as part of preset authority, while the seed preset has `standards_bundle_ref: null` and `bundle: null`.
Impact: Document generation, standards-aware review, and regulated export stamping could lack expected standards provenance.
Follow-up: Carry to Phase 7 Knowledge and Standards and Phase 8 Document Factory review.

## DEC-0043 — Integrate user-driven no-profile baseline with Profile architecture

Date: 2026-06-10
Reviewed file/block: Phase 5 — A08 and Phase 4 user-driven baseline carry-forward
Category: Missing
Decision: Add a cross-reference or rule in Profile/Planning architecture for the user-driven no-profile baseline path.
Reason: A08 says missing profile values require an override or profile update, while Phase 4 identified a separate user-driven baseline contract that allows USER_INPUT duration values when no profile exists.
Impact: Without integration, the profile-missing fallback path remains scattered between WP contract and Profile/Planning behavior.
Follow-up: Reconcile in Phase 6 Planning and approved freeze modification batch.

## DEC-0044 — Defer governed library schema validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 5 — governed library YAML files
Category: Defer
Decision: Do not perform full governed-library schema validation during Phase 5.
Reason: Phase 5 identified architecture/data mismatches, but formal schema validation belongs to Phase 11 with schemas, validation scripts, and test vectors.
Impact: Phase 5 is complete without implementation or schema edits; library consistency issues remain carried risks.
Follow-up: In Phase 11, validate TP/PS/PROF/CAL files against schemas and test vectors.

## DEC-0045 — Keep advisory planning authority boundary

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 Planning
Category: Keep
Decision: Keep Planning as an advisory subsystem that produces PROPOSED schedules only and never mutates WP truth.
Reason: A04_4 clearly states Planning combines WP truth, governed profile data, calendar logic, and optional resource hints to produce proposed schedules, while committed dates can only be written through an explicit WP apply step.
Impact: Implementation must preserve Planning as a proposal generator, not a schedule-truth owner.
Follow-up: Verify downstream Reporting and Export do not treat un-applied proposals as committed truth.

## DEC-0046 — Keep deterministic planning input and output spine

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 Planning
Category: Keep
Decision: Keep the deterministic planning spine: explicit WP snapshot, dependency graph, profile reference, calendar reference, policy options, PROPOSED labeling, apply_required flag, provenance stamps, and reproducibility requirements.
Reason: A04_4 requires explicit versioned inputs, rejects missing required inputs, labels all planning outputs as PROPOSED, and requires reproducibility from the same task snapshot, dependency graph, profile/calendar versions, and planning options.
Impact: This gives a strong planning baseline for later schema/test-vector review.
Follow-up: Align the contract/action names and stamp payloads with this spine before freeze.

## DEC-0047 — Keep plan contract as candidate, but not freeze-clean

Date: 2026-06-10
Reviewed file/block: Phase 6 — `VALOR-contract-orch-plan.yaml`
Category: Keep
Decision: Keep the plan contract as a useful candidate contract for Planning.
Reason: The contract defines Orchestration as caller, PLAN as owner, M2-only proposal generation, read/validate style behavior, response schemas, and planning error handling.
Impact: The contract can drive implementation after catalog and naming alignment.
Follow-up: Reconcile the contract with A04_4 action names, payload names, and provenance requirements.

## DEC-0048 — Standardize Planning action catalog and naming

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 and plan contract
Category: Conflict
Decision: Standardize the Planning action catalog before freeze.
Reason: A04_4 lists PLAN_VALIDATE_INPUTS, PLAN_VALIDATE_DEPENDENCIES, PLAN_PREVIEW, and PLAN_GENERATE, while the contract defines PLAN_GENERATE_PROPOSAL and PLAN_VALIDATE_PROPOSAL.
Impact: Different implementers could build incompatible planning APIs.
Follow-up: Choose one canonical action set and update architecture/contract/action references after user-approved edits.

## DEC-0049 — Standardize apply boundary action

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 and `WP_APPLY_PLAN_PROPOSAL.yaml`
Category: Conflict
Decision: Standardize whether schedule application is done through WP_UPDATE_TASK_FIELDS or WP_APPLY_PLAN_PROPOSAL.
Reason: A04_4 says Orchestration applies confirmed schedules by calling WP_UPDATE_TASK_FIELDS with committed date fields, while the scoped action block defines WP_APPLY_PLAN_PROPOSAL as the truth-mutating apply action.
Impact: The proposal-vs-commitment boundary is correct, but the implementation entry point remains ambiguous.
Follow-up: Preferred freeze direction is to make WP_APPLY_PLAN_PROPOSAL the explicit schedule-apply action and reserve WP_UPDATE_TASK_FIELDS for generic task updates, unless the user chooses the opposite.

## DEC-0050 — Close staged-set planning ambiguity

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 staged planning carry-forward
Category: Modify
Decision: A04_4 should explicitly state whether planning may operate on staged task sets.
Reason: A04_1 allowed “committed tasks exist OR user requests advisory planning on staged set” as a policy choice. A04_4 planning inputs are framed as WP truth and task snapshots with task_id values, which implies committed tasks, but it does not explicitly close the staged-set path.
Impact: Planning could accidentally generate apply-ready proposals from non-committed staged tasks unless the policy is explicit.
Follow-up: Define either committed-task-only planning, or a separate non-applyable staged-preview planning mode using preview task references.

## DEC-0051 — Reconcile duration units with Profile unit policy

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 and Phase 5 Profile carry-forward
Category: Conflict
Decision: Reconcile Planning duration handling with Profile unit policy before freeze.
Reason: A04_4 states duration is expressed in working days under calendar rules, while Profile architecture and seed data allow CALENDAR_DAYS, CALENDAR_WEEKS, and CALENDAR_MONTHS for vendor/lead-time blocks with no implicit conversion.
Impact: Planning may mis-handle vendor lead times unless unit handling is explicit.
Follow-up: Planning should distinguish WORKING_DAYS tasks from calendar-unit lead-time tasks, with approved conversion or no-conversion rules.

## DEC-0052 — Standardize calendar reference and policy source

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 and plan contract
Category: Modify
Decision: Standardize calendar naming and ensure Calendar Logic remains the single source of calendar rules.
Reason: A04_4 uses `calendar_logic_ref`, the plan contract uses `calendar_ref`, and A04_4 planning options include calendar_rule and holidays fields that could duplicate Calendar Logic authority if not constrained.
Impact: Calendar behavior could drift between planning options, profile data, and governed calendar assets.
Follow-up: Use one canonical calendar reference shape and treat ad hoc calendar policy fields as overrides only if governed and stamped.

## DEC-0053 — Integrate user-driven no-profile baseline into Planning

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4, plan contract, Phase 4 user-driven baseline carry-forward
Category: Missing
Decision: Planning needs an explicit rule for the user-driven no-profile baseline path.
Reason: A04_4 and the plan contract require profile references for planning, but Phase 4 kept a controlled fallback where no profile exists and durations come from USER_INPUT.
Impact: The controlled fallback cannot be planned consistently unless Planning accepts either a profile_ref or a declared USER_DRIVEN_NO_PROFILE basis with complete user-sourced durations and confirmation metadata.
Follow-up: Add the rule during approved planning/WP baseline reconciliation.

## DEC-0054 — Align planning provenance stamps across architecture, contract, and examples

Date: 2026-06-10
Reviewed file/block: Phase 6 — A04_4 and plan contract
Category: Modify
Decision: Align required planning provenance stamps across A04_4, the plan contract, and examples.
Reason: A04_4 requires preset, profile, task pool, calendar, planning logic, and contract stamps depending on applicability, while the example output only shows profile/calendar/planning logic and the plan contract does not explicitly require the full stamp set in payload/result policy.
Impact: Planning provenance may be incomplete, weakening report/export reproducibility.
Follow-up: Reconcile with artifact-specific traceability decisions and Phase 9 Reporting/Export.

## DEC-0055 — Defer planning schema validation to Phase 11

Date: 2026-06-10
Reviewed file/block: Phase 6 — plan schemas carry-forward
Category: Defer
Decision: Do not perform detailed planning schema validation during Phase 6.
Reason: Phase 6 confirmed referenced planning schema files exist, but formal schema inspection belongs to Phase 11.
Impact: Planning architecture/contract review is complete without schema edits.
Follow-up: In Phase 11, validate plan proposal and plan validation schemas against A04_4, the plan contract, and the apply action.
