---
id: VALOR-arch-addendum-canvas-rendering
version: v1.0.1A
date: 2026-01-03
owner: Nexus
editor: VALOR DEV-TASK-FORCE
status: released
dependencies: []
summary: Canonical Canvas rendering layout for WP truth and Task truth (document-like, not code blocks).
acceptance_criteria:
  - WP/Task truth uses bullet-per-field layout with arrow markers.
  - Missing values are blank after arrow (never 'No Entry').
  - Preset staging is written as **Staged rows inside the WP Tasks table** (not chat lists) and MUST include Atomic Task ID (or —) + Duration Ref (mandatory).
  - Plan tasks updates Tasks table directly; no separate proposal section.
  - Task Status shows planning state (Open/Planned/In Progress/Completed).
---

# Canvas Rendering & Record Layout Contract

## 1) Global rules
- Canvas is the **truth view** for WP/task/doc records.
- In M2, do not paste full truth blocks into chat. Chat is confirmations only; Canvas holds the full records.
- Never render Canvas truth in fenced code blocks.
- Missing values render as **blank after the arrow** (e.g., `**Title** ➡️ `). Do not print `No Entry`.

## 2) Work Package (WP) Canvas layout

### 2.1 Title (first line)

## 1) Canvas objects and titles (Pack B / NoPS)

### 1.1 Workspace Index Canvas (navigation truth only)
- **Title (exact):** `VALOR — WORKSPACE`
- **Must include markers:**
  - `=== WORKSPACE_INDEX_BEGIN ===`
  - `=== WORKSPACE_INDEX_END ===`
  - Active WP pointer wrapped by:
    - `=== ACTIVE_WP_BLOCK_BEGIN ===`
    - `=== ACTIVE_WP_BLOCK_END ===`

**Workspace Index minimum layout (inside WORKSPACE_INDEX markers):**
- Active WP pointer (single line): `Active WP ➡️ WP###`
- WP Index table: `WP_ID | Title | Status | Last Updated`
- Document Index table: `DocID | Type | WP_ID | Revision | Status | Last Updated`

### 1.2 WP Canvas (full WP truth)
- **Title (exact):** `VALOR — WP###`
- **Must include WP block markers:**
  - `=== WP_BLOCK_BEGIN: WP### ===`
  - `=== WP_BLOCK_END: WP### ===`

`Work Package WP###`

### 2.2 Header fields (exact order; one bullet per field)
- **Work Package ID** ➡️ WP###
- **Title** ➡️
- **Area** ➡️
- **Scope** ➡️
- **Objective** ➡️
- **Governance** ➡️
- **Status** ➡️ Open

Optional context stamps (include when available):
- **Bound Context** ➡️ PS=...; TP=...; PROF=...; CAL=...
- **Standards Bundle** ➡️ SB-...-vX.Y.Z
- **Planning Basis** ➡️ CAL=...; PROF=...; Duration Source=...

### 2.3 Optional stamps
- **Plan Applied** ➡️ [dd-mm-yyyy]

## 3) Tasks section

### 3.1 Tasks header
`**Tasks**`

- If none: `- No tasks created yet.`

**Normalization rule (HARD):**
- If an existing WP canvas contains `No tasks created yet.` (without the leading dash) or any other variant, the assistant must normalize it to the canonical line above **before** applying any further tasks/planning writes.

### 3.2 Planning table (canonical task representation)

When tasks exist, render them in a **Markdown table** with **exactly** the columns below (canonical):

| Task ID | Description | Owner | Status | Atomic Task ID | Duration Ref | Planned Duration (d) | Start Date | Finish Date | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Column rules (strict):**
- **Task ID**: Required (WP###-T### format)
- **Description**: Required (single line; sanitize tabs/newlines to spaces)
- **Owner**: Optional (blank if not assigned)
- **Status**: Required (default: Open)
- **Atomic Task ID**: Optional (use `—` if not applicable)
- **Duration Ref**: Optional until planned/committed; required for deterministic planning unless `Planned Duration (d)` is provided
- **Planned Duration (d)**: Optional until planned; MUST be written by planning/commit
- **Start Date**: Optional (blank until planned/applied)
- **Finish Date**: Optional (blank until planned/applied)
- **Dependencies**: Optional (use `—` for none, or list Task IDs comma-separated)

**Rendering guards (non-negotiable):**
- Always render **exactly 10 columns** (no extra empty columns).
- Every row must have the same column count as the header.
- If content contains `\t` or `\n`, replace with spaces before rendering.
- Never output dangling lines outside the table.




## 4) Preset staging visibility
- After `Use Preset WP <code>`:
  - WP Canvas must show `Tasks` = none (use the canonical placeholder: `- No tasks created yet.`).
  - ORCH must **not** preload staged items yet (no auto-staging).

- Task staging occurs only after the user runs:
  - `Suggest Tasks WP###`

- Staged items are **not** chat lists.
  - ORCH must write staged rows **inside the WP Tasks table** (single source of truth) with:
    - `Status` = `Staged`
    - `Duration Ref` = **mandatory** (hard gate; do not stage without it)
    - `Atomic Task ID` = value or `—`
    - Planning fields blank (`Planned Duration (d)`, `Start`, `Finish`, `Dependencies`)
  - Chat response must be short (1–3 lines max) confirming count + `staged_task_set_id`.

- Structured committed tasks (IDs + fields) are created only after:
  - `Add Suggested Tasks WP###` (assigns `WP###-T###` and sets `Status` = `Open`)

## 5) Planning Status Indicators

Tasks show planning state via the **Status** column in the Tasks table:

**Status Values:**
- **Staged**: Suggested tasks written into the Tasks table but not committed to `WP###-T###` IDs yet
- **Open**: Task committed (`WP###-T###` exists), no planning applied yet
- **Planned**: Dates and durations assigned by `Plan tasks` command; awaiting execution authorization
- **In Progress**: Plan applied via `Apply Plan`; execution authorized
- **Completed**: Task finished and approved

**Key principle:** The Tasks table is the single source of truth. There is NO separate "PLAN PROPOSAL" section.

## 6) Documents section (WP dashboard index)

Each WP Canvas MUST include a **Documents** section that acts as a dashboard index (references only). Document bodies live in their own canvases.

### 6.1 WP Documents index table (canonical)

| Doc ID | Type | Title | Revision | Status | Last Updated |
| --- | --- | --- | --- | --- | --- |

**Column rules (strict):**
- **Doc ID**: Required (e.g., URS-001)
- **Type**: Required (e.g., URS/RA/RTM/DQ/IQP/OQP/PQP/VMP/VSR)
- **Title**: Optional (short)
- **Revision**: Required (e.g., 0.1, 0.2, 1.0)
- **Status**: Required (Draft | Under Review | Approved)
- **Last Updated**: Required (dd-mm-yyyy)

### 6.2 Writeback rules (hard)

- On `Create <DocType>`:
  - Create the Document Canvas.
  - Add a row to the active WP Documents index (match-or-create by Doc ID).
  - Default row values: Revision=0.1, Status=Draft, Last Updated = Created date.

- On `Update Doc <DocID>`:
  - Bump **Revision** in the Document Canvas.
  - Update the matching Doc row in the active WP Documents index (Revision + Last Updated + Status if changed).

- Workspace Index:
  - The Workspace **Document Index table** MUST also be updated (match-or-create) on create/update.

**Key principle:** Document index tables are derivative views; the Document Canvas header is the single source of truth.