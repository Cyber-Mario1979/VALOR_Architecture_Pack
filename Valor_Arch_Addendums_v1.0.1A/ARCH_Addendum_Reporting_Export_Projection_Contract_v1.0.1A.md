---
id: VALOR-arch-addendum-reporting-export
version: v1.0.1A
revision_context: Blocker 7A
revision_date: 2026-06-12
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: pre_freeze_controlled
dependencies: []
summary: Projection-only product-surface rules for Work Package Status Report, Workbook Export, and Gantt Chart artifacts.
acceptance_criteria:
  - RPT artifacts are projection-only and never mutate WP/task truth.
  - Product surface distinguishes status report, workbook export, and Gantt chart artifacts.
  - CSV is not treated as the v1.0.1 freeze baseline.
  - ALL_WPS remains out of scope unless bounded to an explicit selected WP set.
---

# Reporting & Export — Projection Contract

## 1) Projection-only invariants

RPT actions MUST NOT change:

- WP/task truth;
- owners;
- dates;
- status;
- IDs;
- plan proposals;
- applied stamps;
- missing/source-field truth state.

If the user asks to correct data while reporting/exporting:

- instruct them to update WP/task truth or apply a plan first;
- then re-run the report/export artifact generation.

## 2) Declared RPT baseline artifacts

The v1.0.1 product-surface baseline contains:

1. `WORK_PACKAGE_STATUS_REPORT`
2. `WORK_PACKAGE_WORKBOOK_EXPORT`
3. `WORK_PACKAGE_GANTT_CHART`

CSV is not the v1.0.1 freeze baseline.

## 3) Work Package Status Report

`RPT_GENERATE_STATUS_REPORT` generates a separate status report artifact/record.

The product surface should identify:

- artifact type = `WORK_PACKAGE_STATUS_REPORT`;
- projection only = true;
- source WP snapshot reference/hash;
- generated_at_utc;
- required stamps;
- proposed schedule data, if shown, clearly separated from committed WP date truth.

## 4) Workbook Export

`RPT_GENERATE_WORKBOOK_EXPORT` generates an Excel workbook artifact.

The product surface should identify:

- artifact type = `WORK_PACKAGE_WORKBOOK_EXPORT`;
- output format = `.xlsx`;
- projection only = true;
- source WP snapshot reference/hash;
- required stamps.

## 5) Gantt Chart

`RPT_GENERATE_GANTT_CHART` generates a separate Excel-based Gantt chart artifact.

The product surface should identify:

- artifact type = `WORK_PACKAGE_GANTT_CHART`;
- output format = `.xlsx`;
- projection only = true;
- source WP snapshot reference/hash;
- proposed vs committed schedule basis.

## 6) Target scope

Supported:

- `SINGLE_WP`
- `SELECTED_WP_SET`

Out of scope:

- `ALL_WPS`

If `ALL_WPS` is requested, Orchestration must ask the user to select a bounded WP set or refuse in strict mode.

## 7) Timestamp rule

- Contract/audit/provenance metadata timestamps use UTC.
- Optional local display time may be shown only when explicitly labeled as display/local time.
- Local display time must not replace UTC metadata.

---

## CHANGELOG

| Date | Changes | Type / Version |
| ---- | ------- | -------------- |
| 2026-06-12 | Blocker 7A normalized reporting/export product surface to status report, workbook export, and Gantt chart artifacts; removed CSV baseline wording | Pre-freeze controlled update |
| 2026-01-03 | First Issue | v1.0.1A |
