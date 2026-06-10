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

## DEC-0001 — Use VALOR_Architecture_Pack as candidate spec

Date: 2026-06-10
Reviewed file/block: README.md, manifest.yaml, A00 intake
Category: Keep
Decision: Use `VALOR_Architecture_Pack` as the candidate Architecture Pack for review.
Reason: The repository is already structured as a specification pack with architecture docs, contracts, action blocks, templates, governed libraries, schemas, validation tools, test vectors, and manifest discipline.
Impact: The pack becomes the starting point for product specification freeze review.
Follow-up: Continue block-by-block review before freeze.

## DEC-0002 — Do not treat current pack as frozen final spec yet

Date: 2026-06-10
Reviewed file/block: README.md, A00 intake
Category: Modify
Decision: The pack is not frozen yet and must be reviewed before becoming product specification authority.
Reason: Strong claims such as implementation-ready must be verified, and gaps around AI, DCF-to-URS, UI/product surface, and delivery planning must be reviewed.
Impact: No clean implementation repo or delivery plan starts until review completes.
Follow-up: Review A01/A02 next.

## DEC-0003 — Repo is review memory

Date: 2026-06-10
Reviewed file/block: Review process decision
Category: Keep
Decision: Store review memory in `_review_control` inside the repository instead of relying on ChatGPT history or uploaded sources.
Reason: The review will span multiple sessions and needs persistent, inspectable state.
Impact: Each session must read `REVIEW_STATE.md` and `SESSION_HANDOFF.md` before continuing.
Follow-up: Keep `REVIEW_STATE.md` and `SESSION_HANDOFF.md` updated after every session.

## DEC-0004 — No implementation during architecture review

Date: 2026-06-10
Reviewed file/block: Review process decision
Category: Keep
Decision: Do not write implementation code during architecture/specification review.
Reason: The product specification must drive implementation, not the old implementation repo or assumptions.
Impact: Current ASBP implementation/rebuild remains stopped.
Follow-up: After review, create delivery plan and perform old repo asset assessment.

