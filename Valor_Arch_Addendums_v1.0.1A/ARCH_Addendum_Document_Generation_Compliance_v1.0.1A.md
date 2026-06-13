---
id: VALOR-arch-addendum-doc-generation
version: v1.0.1A
revision_context: Blocker 7A
revision_date: 2026-06-12
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: pre_freeze_controlled
dependencies: []
summary: Document generation product-surface rules: separate document artifacts, token-clean output, no operational footer text, UTC metadata, optional labeled local display time, and testing-only stamp behavior.
acceptance_criteria:
  - Document bodies contain no template tokens or placeholder braces.
  - Document outputs are represented as generated document artifacts/records, not as required Canvas objects.
  - Documents never contain operational/runtime footer text.
  - Contract/audit/provenance timestamps remain UTC; optional local display time is explicitly labeled.
---

# Document Generation Compliance Addendum

## 1) Separate document artifacts / records

- Each generated document is a separate document artifact/record.
- A WP record/output view may include a **Documents** index list of references only.
- This addendum does not require a specific Canvas runtime, UI screen, or artifact renderer.

## 2) Token-clean rule (strict)

Final document output MUST NOT contain:

- `{{ ... }}` tokens;
- `{}` or `{ }` placeholders;
- `<...>` placeholders.

If required content is missing, the output must either remain `INCOMPLETE` or show an explicitly controlled incomplete value such as `TBD`; it must not invent missing source data.

## 3) No operational/footer text inside documents

Document bodies must not include runtime/UI lines such as:

- `Mode: ...`;
- `State: ...`;
- `Canvas ready`;
- `Next → ...`;
- `To commit: ...`.

Operational guidance must remain outside the generated document body.

## 4) Timestamp rule

- Contract/audit/provenance metadata timestamps use UTC, such as `generated_at_utc` or `timestamp_utc`.
- Optional user-facing local display timestamps may be shown only when explicitly labeled as display/local time.
- `Africa/Cairo` may be used as a display/local timezone label only; it must not replace canonical UTC metadata.

## 5) Testing-only document output

When DOC uses TESTING_ONLY / PRODUCT_TESTING_ONLY K&S/template/bundle/citation assets, the document output must visibly carry:

`PRODUCT TESTING ONLY — NOT APPROVED FOR REAL-LIFE REGULATED CQV/GMP USE.`

Such output must not be represented as real regulated CQV/GMP output.

---

## CHANGELOG

| Date | Changes | Type / Version |
| ---- | ------- | -------------- |
| 2026-06-12 | Blocker 7A normalized document artifact terminology, UTC/local timestamp rule, and testing-only document output stamp behavior | Pre-freeze controlled update |
| 2026-01-03 | First Issue | v1.0.1A |
