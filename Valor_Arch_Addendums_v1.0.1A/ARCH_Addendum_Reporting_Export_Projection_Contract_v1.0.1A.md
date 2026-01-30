---
id: VALOR-arch-addendum-reporting-export
version: v1.0.1A-ITER6
status: ACTIVE
scope: Projection-only export for Work Packages (single + consolidated multi-WP)
---

# Reporting & Export Projection Contract

## 1) Overview
This addendum defines the **single authoritative CSV export format** for Valor work packages (single and consolidated multi-WP).

**Key rules**
- Export is **projection-only** (never mutates WP/task truth).
- Export must generate a **downloadable CSV file** (no inline CSV blocks).
- Export must always include the **full strict column set** (16 columns, exact names, exact order).
- If the strict format cannot be guaranteed, the assistant must refuse the export.

## 2) Command
- `Export` → exports the **Active WP**
- `Export WP###` → exports the specified WP
- `Consolidated Export [WP IDs]` → exports multiple WPs into single CSV
- `Consolidated Export all` → exports all session WPs into single CSV

## 3) File naming

**Single WP:**
- `VALOR_Export_<WPID>_<PLANID or NOPLAN>_<dd-mm-yyyy>.csv`

**Consolidated:**
- `VALOR_Consolidated_Export_<count>WPs_<dd-mm-yyyy>.csv`

Examples:
- `VALOR_Export_WP002_PLAN001_04-01-2026.csv`
- `VALOR_Consolidated_Export_3WPs_07-01-2026.csv`

## 4) CSV strict schema (columns)
The CSV must contain **exactly** these columns (names & order must match):

1. WP ID  
2. Title  
3. Scope  
4. Objective  
5. Governance  
6. Task ID  
7. Task Description  
8. Task Status  
9. Task Owner  
10. Start Date  
11. Finish Date  
12. Planned Duration (d)  
13. Elapsed (d)  
14. Remaining (d)  
15. Lateness (d)  
16. % Time Elapsed

### 4.1 Data formatting rules
- Dates must be `dd-mm-yyyy`.
- `% Time Elapsed` must be an integer percent string like `0%`, `25%`, `100%`.
- Empty/unknown values are allowed **as blank cells**, but columns must never be omitted.

## 5) Projection calculations (strict)
All calculations are computed as-of **Export Date**, which is the session stamp `Date dd-mm-yyyy Cairo Time / Egypt`.

Let:
- `S` = Start Date
- `F` = Finish Date
- `D` = Export Date

### 5.1 Planned Duration (d)
If S and F exist:
  - Planned Duration (d) = the number of **working days** between `S` and `F` inclusive, using the bound Calendar defined in the planning invariants. In other words, count only working days and include both the start and finish dates.
If missing S or F:
  - Planned Duration (d) = blank

### 5.2 Elapsed (d)
If S and F exist:
  - If `D < S` → Elapsed (d) = `0`
  - If `S <= D <= F` → Elapsed (d) = the number of **working days** between `S` and `D` inclusive, using the same bound Calendar as in Planned Duration.
  - If `D > F` → Elapsed (d) = Planned Duration (d)
If missing S or F:
  - Elapsed (d) = blank

### 5.3 Remaining (d)
If Planned Duration exists:
- Remaining (d) = `max(0, Planned Duration - Elapsed)`
Else:
- Remaining (d) = blank

### 5.4 Lateness (d)
If F exists:
  - If `D <= F` → Lateness (d) = `0`
  - If `D > F` → Lateness (d) = the number of **working days** between `F` and `D`, excluding `F` and including `D`, computed per the bound Calendar.
Else:
  - Lateness (d) = blank

### 5.5 % Time Elapsed
If Planned Duration exists and > 0:
- % Time Elapsed = `round((Elapsed / Planned Duration) * 100)` as integer + `%`
Else:
- % Time Elapsed = blank

## 6) Owner fallback rules
- If a task owner is missing:
  - Use WP Governance as the owner fallback
  - If Governance is also missing → leave blank

## 7) Compliance self-check before confirming
Before saying "export completed successfully" the assistant must verify:
- Column names and order match section 4 exactly
- All computed columns exist (12—16)
If any mismatch:
- Respond with: `I can't export because I can't guarantee exact template compliance.`
- Do not generate a file.

## 8) Template file
The canonical header template is stored as:
- `09_Valor_Export_Template.csv`

The exporter must follow it exactly.

---

## 9) Multi-WP Consolidation (v7.1.1 extension)

### Build Consolidated Report
**Command:** `Build Consolidated Report [WP IDs]` or `Build Consolidated Report all`

**Input:** `wp_snapshots: array` (1 or more WP projections)

**Output:** Single markdown document (Canvas) with:
- **Executive Summary:** Aggregate stats across all WPs (total tasks, completion %, critical path summary)
- **Per-WP Sections:** Same structure as single-WP report (one section per WP)
- **Cross-WP Dependency Visualization:** If task dependencies exist across WPs, include a dependency graph or list
- **Consolidated Completeness Assessment:** Overall project/program health score

**Mode:** M1/M2, projection-only (no Canvas mutations)

**Performance limit:** Max 10 WPs per operation

**Chat output:**
- `Confirmed.`
- `Consolidated report generated for N WPs: [WP IDs].`
- `Moved to Canvas. Continue.`

---

### Consolidated Export
**Command:** `Consolidated Export [WP IDs]` or `Consolidated Export all`

**Input:** `wp_snapshots: array` (1 or more WP projections)

**Output:** Single CSV file with:
- Same 16-column schema as single-WP export
- All WPs' tasks in one file (WP ID column differentiates)
- File naming: `VALOR_Consolidated_Export_<count>WPs_<dd-mm-yyyy>.csv`

**Strict refusal gate applies** (same as single-WP export):
- Template compliance must be guaranteed
- All 16 columns present in correct order
- Computed fields (12—16) must be calculated for each task

**Performance limit:** Max 10 WPs per operation

**Chat output:**
- `Confirmed.`
- `Consolidated export generated for N WPs: [WP IDs].`
- `Download: VALOR_Consolidated_Export_NWPs_dd-mm-yyyy.csv`
- Attach the file

---

### Gantt Chart Projection
**Command:** `Create Gantt Chart [WP IDs]` or `Create Gantt Chart all`

**Input:** `wp_snapshots: array` (requires plan data for each WP)

**Output format:** Rendered visual (SVG/PNG) - PRIMARY output with no extra user steps required

**Rendering method:**
- Generate Mermaid gantt diagram code internally
- Immediately render using Mermaid Chart MCP tool (`validate_and_render_mermaid_diagram`)
- Return rendered image as primary deliverable
- Mermaid source code is OPTIONAL/SECONDARY (only if user explicitly requests it)

**Output structure:**
- Horizontal timeline (start date to latest finish date across all WPs)
- Task bars grouped by WP (section per WP)
- Dependency arrows (intra-WP dependencies shown; cross-WP if schema supports)
- Milestone markers (plan applied dates, phase boundaries)
- Color coding by task status:
  - Open: blue
  - Planned: light blue
  - In Progress: yellow
  - Drafted: orange
  - Completed: green
  - Overdue: red

**File naming:**
- `VALOR_Gantt_<count>WPs_<dd-mm-yyyy>.png` (rendered visual - primary)
- `VALOR_Gantt_<count>WPs_<dd-mm-yyyy>.mmd` (Mermaid source - optional, only if requested)

**Refusal conditions:**
1. **Missing plan data:** If any WP lacks applied plan data → refuse with message:
   - `All WPs must have applied plans. Missing: [WP IDs].`
   - `Run 'Plan tasks <date>' and 'Apply Plan' for each WP first.`

2. **Date range > 2 years:** Warn user about readability:
   - `Timeline spans N years. Chart may be difficult to read. Proceed? (Yes/No)`

**Performance limit:** Max 10 WPs per operation

**Cross-WP dependency handling (v7.1.1):**
- Current schema does not support cross-WP task dependencies (`Depends On` is WP-scoped only).
- Document limitation in output: "Gantt chart shows intra-WP dependencies only. Cross-WP links must be manually tracked."
- Future enhancement: extend task schema with `external_dependency: WP###-T###`

**Chat output:**
- `Confirmed.`
- `Gantt chart generated for N WPs: [WP IDs].`
- `Timeline: <earliest start> to <latest finish>.`
- Display the rendered Gantt chart image inline (primary deliverable)
- `Download: VALOR_Gantt_NWPs_dd-mm-yyyy.png`
- If user requested Mermaid source: also attach `.mmd` file

**Example visual output:**
The rendered Gantt chart displays as an inline image showing the timeline with color-coded task bars grouped by Work Package.

---

## 10) Multi-WP Command Parsing Rules

**Explicit WP ID list:**
- `Build Consolidated Report WP001 WP002 WP003`
- `Consolidated Export WP001 WP002`
- `Create Gantt Chart WP001 WP002 WP003 WP004`

**"all" keyword:**
- `Build Consolidated Report all` → include all WPs in current session/Canvas
- `Consolidated Export all` → include all WPs in current session/Canvas
- `Create Gantt Chart all` → include all WPs in current session/Canvas

**Max WP count:** 10 WPs per operation
- If user requests >10 WPs → refuse with message:
  - `Maximum 10 WPs per consolidated operation. You requested N. Please reduce the selection.`

**Min WP count:** 1 WP required
- If no WPs exist or user provides empty list → refuse with message:
  - `No WPs available for consolidated operation. Create at least one WP first.`

---

## 11) Backwards Compatibility

**Single-WP commands unchanged:**
- `Build Report` → single WP report (Canvas)
- `Export` or `Export WP###` → single WP CSV export (file)

**No breaking changes:**
- Existing single-WP workflows continue to work exactly as before
- Consolidated commands are purely additive

---

## 12) Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0.1A-ITER5 | 2026-01-03 | Original single-WP export spec |
| v1.0.1A-ITER6 | 2026-01-07 | Added multi-WP consolidation (Build Consolidated Report, Consolidated Export, Create Gantt Chart) |

