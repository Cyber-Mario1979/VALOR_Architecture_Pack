# Blocker 6A — DOC / DCF / URS Source-Chain Alignment

Status: COMPLETED FOR SCOPED ARCHITECTURE AND CONTRACT ALIGNMENT — FREEZE STILL BLOCKED BY OTHER PRE-FREEZE WORK
Date: 2026-06-12
Review branch: review-spec-freeze-control

## Scope

This blocker covered DOC / DCF / URS source-chain architecture and contract alignment only.

## Files edited

- `docs/architecture/A04_5_DocumentFactory_Arch_v1_0_1.md`
- `contracts/VALOR-contract-orch-doc.yaml`
- `docs/architecture/A15_Global_Glossary_Arch_v1_0_1.md`

## Files reviewed with no edit required

- `contracts/CONTRACT_REGISTRY_v1.0.1.yaml`
  - Already preserved DOC as public/user-callable.
  - Already listed only active DOC actions: `DOC_GENERATE_DRAFT` and `DOC_FINALIZE_ARTIFACT`.
  - No deferred DOC actions were added.

## Decisions applied

- DCF was declared as a DOC source-capture / input-collection document type or concept.
- DCF may be referenced through `dcf_ref` or `source_input_set`.
- DCF artifact generation and finalization are not active in this slice.
- DCF artifact generation remains blocked/deferred until `TPL-DCF_v1.0.1.yaml` and approved source metadata exist.
- No `TPL-DCF_v1.0.1.yaml` was created.
- DCF was not added to `BND-CQV-BASE_v1.0.1`.
- URS generation requires `doc_type: URS` and consumes WP truth, DCF/source input set, governed `template_ref`, governed `bundle_ref` / `citation_set`, and provenance stamps.
- DOC must not invent intended use, GMP relevance, user needs, critical requirements, interfaces, constraints, assumptions, or acceptance expectations.
- Missing required DCF/source fields must block generation/finalization or mark the output incomplete.
- Active DOC actions were aligned to `DOC_GENERATE_DRAFT` and `DOC_FINALIZE_ARTIFACT` only.
- Deferred DOC actions remain deferred unless later approved: `DOC_VALIDATE`, `DOC_MARK_REVIEW_READY`, `DOC_REGENERATE`, `DOC_GET`, and `DOC_LIST`.
- `DOC_FINALIZE_ARTIFACT` now requires source-chain provenance, template_ref, bundle_ref, citation_set, provenance_stamps, and source-input completion status, with testing-only stamp handling when K&S remains testing-only.
- K&S remains the governed template/standard/citation authority.
- K&S remains TESTING_ONLY / PRODUCT_TESTING_ONLY only; real regulated CQV/GMP output remains blocked until required source metadata acceptance.
- A15 glossary now defines DOC, DCF, URS, Source Capture, Source Input Set, Template Governance Record, Template Source Metadata, and Testing-Only Document Output.

## Explicit deferrals

- No implementation work.
- No delivery plan.
- No clean repo.
- No ASBP audit.
- No product-surface cleanup.
- No real template import, upload, conversion, rewrite, or summary.
- No URS normative template rewrite.
- No full schema/test-vector hardening.
- No manifest regeneration.
- No K&S regulated-active promotion.
- No invented source editions, dates, clauses, anchors, or locators.
- No broad governance rewrite.

## Remaining dependencies / blockers

- K&S user/site source metadata acceptance for real regulated CQV/GMP use.
- Real template source metadata intake and acceptance before regulated use.
- Optional future `TPL-DCF_v1.0.1.yaml` creation and bundle membership decision after approved template source metadata exists.
- Product surface minimum behavior cleanup.
- Non-K&S schema/validation/test-vector cleanup.
- Governance/security/registry schemas/tests.
- Manifest regeneration.
- Final freeze-readiness review.
