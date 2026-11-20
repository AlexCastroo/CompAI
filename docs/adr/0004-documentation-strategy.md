# ADR-0004: Documentation strategy

- **Status:** Accepted
- **Date:** 2026-11-17

## Context

CompAI is a learning project. Its documentation must evolve with the code and avoid duplicated, contradictory, or unnecessary content.

## Verified Facts

- Before this decision, the only documentation was `README.md` and `CLAUDE.md`.
- The original roadmap existed outside the repository.
- The operational documentation rules (language, sources of truth, validation criteria, document states, maintenance, ADR template) are defined in [docs/README.md](../README.md).

## Decision

Stated by the project owner on 2026-11-17 unless a different date is noted.

- Official documentation lives in the repository, in Markdown, under `docs/`.
- Learning notes are written in Spanish; technical documentation, architecture, and ADRs in English; code and identifiers in English. Detailed rules: [docs/README.md §2](../README.md#2-language-rules).
- General learning (`docs/learning/`) is kept separate from its application in CompAI. Learning notes link to that application instead of duplicating it.
- Only validated information is documented as fact. Criteria: [docs/README.md §4](../README.md#4-validation-criteria).
- [roadmap.md](../roadmap.md) is the only official planning reference. The original roadmap is preserved verbatim in [roadmap-original.md](../roadmap-original.md) and is not maintained.
- (2026-11-20) `docs/working-state.md` is a local session continuity checkpoint: it records where work stopped, what is in progress, and the next step. It is ignored by Git, is not published, and is not part of the official documentation. It does not duplicate phase status or planning from [roadmap.md](../roadmap.md); it links to the roadmap when referring to project progress.

## Known Reasons

- Avoid duplicated, contradictory, or unnecessary documentation (project owner).
- Rationale for the language split: not documented.

## Hypotheses

- Separating general learning from its application in CompAI reduces duplication and keeps learning notes stable while the project changes. Not verified.

## Open Questions

- Documentation tooling (site generators, automatic link checking): not evaluated.
- Documentation Agent restricted to `docs/`: under consideration, not approved, not implemented.
  - Whether it provides more value than a documentation checklist.
  - Its design, permissions, and enforcement mechanism.
  - Overlap with the Code Reviewer flagging outdated documentation ([ADR-0003](0003-development-subagents.md)).

## Consequences

- Documentation maintenance follows the rules in [docs/README.md §6](../README.md#6-maintenance-rules), and document states follow [§5](../README.md#5-document-states).
- Maintaining documentation in two languages and keeping it synchronized with the code creates additional work for each change.
- Session context exists only on the local machine: it is not shared through the repository and is lost if the working copy is deleted.
