---
id: VALOR-block-A15-global-glossary
block type: Arch
version: v1.0.1
owner: Nexus
editor: Senior Architect
status: pre_freeze_controlled
date: 2026-06-12
dependencies:
  - VALOR-block-A00-specs-architecture-pack
  - VALOR-block-A01-sos-context-capability
  - VALOR-block-A02-principles-invariants
summary: "Centralized, canonical glossary of technical terms used across the Valor architecture pack."
acceptance_criteria:
  - Provides authoritative definitions for core Valor architecture terms.
  - Uses one term per heading for easy parsing.
---

# Global Glossary (Centralized)

## System of Systems (SoS)
A federation of independently governed subsystems that interact through explicit interfaces to deliver higher-level capabilities, while each subsystem retains its own authority and evolution path.

## Orchestration
The coordinating subsystem that routes user intent into contract actions, enforces governance gates, validates readiness, and ensures stamps and audit events are produced.

## Work Package (WP)
The authoritative container for scope, tasks, dependencies, validations, and lifecycle state representing a governed unit of CQV work.

## Contract
A versioned, schema-defined interface between subsystems defining actions, envelopes, validation rules, and error semantics.

## Invariant (INV)
A hard-stop rule that must not be violated across the system.

## Stamp
A provenance tuple written into outputs indicating the exact versions of governed assets used.

## DOC
The Document Factory subsystem that generates controlled document drafts and finalized document artifacts from WP truth, source input sets, governed template references, governed bundle/citation references, and required provenance stamps. DOC does not own WP truth, template truth, standards truth, or source-capture truth.

## DCF
A source-capture / input-collection document type or concept used to collect and structure source data for downstream document generation. In Blocker 6A, DCF may be referenced by DOC through `dcf_ref` or `source_input_set`, but DCF artifact generation/finalization is deferred until a governed `TPL-DCF` record and approved source metadata exist.

## URS
User Requirements Specification. In VALOR DOC source-chain semantics, URS is a generated controlled output that consumes WP truth, DCF/source input data where available, governed URS template references, governed bundle/citation references, and provenance stamps.

## Source Capture
The controlled act of collecting source data from users, site records, templates, forms, or approved inputs before DOC uses that data to generate a document. Source capture does not authorize DOC to invent missing source data.

## Source Input Set
A versioned or traceable set of source fields supplied to DOC for document generation, including completion status and provenance. It may include DCF references, user-entered source fields, and WP-derived facts.

## Template Governance Record
A governed K&S record describing a template’s identity, version, document type, owner, lifecycle status, usage classification, required inputs, required stamps, citation/anchor policy, and regulated-use gate.

## Template Source Metadata
Metadata describing the original template source, including source owner, source file name/path, checksum or hash, effective status, review status, usage classification, and acceptance gate.

## Testing-Only Document Output
A generated document draft or artifact that may be used for product testing only because one or more required template, bundle, standard, citation, or source metadata assets remain TESTING_ONLY / PRODUCT_TESTING_ONLY or unaccepted for regulated use. It must carry the required testing-only stamp and must not be represented as real regulated CQV/GMP output.

---

## CHANGELOG
| Date       | Changes     | Type / Version |
| ---------- | ----------- | -------------- |
| 2026-06-12 | Blocker 6A DOC/DCF/URS source-chain glossary definitions added | Pre-freeze controlled update |
| 2025-12-23 | First Issue | Arch_v1.0.1    |
