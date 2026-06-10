# VALOR Architecture Pack Review Charter

Status: ACTIVE
Repository: Cyber-Mario1979/VALOR_Architecture_Pack
Review branch: review-spec-freeze-control
Baseline branch: main
Review mode: specification freeze review
Implementation allowed: No

## 1. Greater Goal

Create a reliable product specification authority for VALOR before any new implementation repository is created.

The greater downstream route is:

1. freeze VALOR Architecture Pack as product specification authority;
2. create a delivery plan from the frozen specification;
3. assess existing ASBP / prior implementation code against that delivery plan;
4. classify reusable assets into use-as-is, use-after-modification, and throw-away buckets;
5. create a new lightweight governance system for execution;
6. create a clean implementation repository;
7. implement only after specification and delivery plan are frozen.

## 2. Immediate Review Goal

Review the current VALOR Architecture Pack and decide whether each part should be:

- kept as-is;
- modified before freeze;
- treated as missing and added;
- treated as conflicting/confusing and resolved;
- deferred explicitly with a reason.

The output of this review is not code. The output is a frozen or freeze-ready architecture/specification pack.

## 3. Review Scope

The review covers:

- README and pack positioning;
- A00 through A15 architecture documents;
- action blocks;
- contracts;
- governed libraries;
- templates;
- schemas;
- validation scripts;
- test vectors;
- manifest and pack integrity discipline;
- addendums;
- AI role and advisory/document-generation boundaries;
- DCF to URS to downstream document-generation flow;
- UI/product workflow coverage;
- delivery-plan readiness.

## 4. Non-Scope

During this review, do not:

- write implementation code;
- create a new implementation repository;
- modify old ASBP implementation code;
- audit old ASBP code in detail;
- create delivery-plan milestones before the specification review is complete;
- claim the pack is frozen before all review blocks are complete;
- treat chat memory as authority.

## 5. Review Authority Order

For this review, source-of-truth order is:

1. current repo files on the active review branch;
2. `_review_control/REVIEW_STATE.md`;
3. `_review_control/DECISION_LOG.md`;
4. `_review_control/REVIEW_PLAN.md`;
5. `_review_control/SESSION_HANDOFF.md`;
6. user instruction in the current chat.

Chat history is not permanent authority. Decisions must be written into the repo control files.

## 6. Session Rules

Each session must:

1. read `REVIEW_STATE.md` first;
2. review only the current assigned block unless the user explicitly changes scope;
3. classify outcomes as Keep / Modify / Missing / Conflict / Defer;
4. update `DECISION_LOG.md` with decisions;
5. update `REVIEW_STATE.md` with current progress and next action;
6. update `SESSION_HANDOFF.md` for the next session;
7. stop after the scoped review is complete.

## 7. Definition of Done for a Review Block

A block is done when it has:

- files inspected;
- purpose understood;
- authority/boundary checked;
- product workflow relevance checked;
- AI impact checked where applicable;
- deterministic boundary checked;
- downstream implementation impact identified;
- decisions logged;
- open questions either resolved or carried forward.

## 8. Definition of Done for the Full Review

The review is done only when:

- README and A00 are reviewed;
- A01 through A15 are reviewed;
- action blocks are reviewed;
- contracts are reviewed;
- governed libraries are reviewed;
- templates are reviewed;
- schemas are reviewed;
- validation scripts are reviewed;
- test vectors are reviewed;
- addendums are reviewed;
- AI advisory, extraction, and document drafting roles are explicit;
- DCF to URS to downstream document flow is explicit;
- UI/product workflow gaps are resolved or formally deferred;
- all decisions are logged;
- open questions are closed or formally deferred;
- final freeze recommendation is accepted by the user.

## 9. After Review Completion

After the architecture review is complete, the next controlled work is:

1. create delivery plan;
2. audit old/current implementation repo against frozen deliverables;
3. create asset buckets;
4. create new governance system;
5. create clean implementation repo;
6. begin implementation.

## 10. Freeze Rule

Once the architecture pack is frozen, amendments are not accepted informally.

Any later change requires a formal change request with:

- reason;
- impacted files;
- impacted delivery plan item;
- risk of change;
- approval decision.
