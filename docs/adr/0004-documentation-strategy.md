# ADR-0004: Documentation strategy

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

CompAI is a learning project. Its documentation must evolve with the code and avoid duplicated, contradictory, or unnecessary content.

## Verified Facts

- Before this decision, the only documentation was `README.md` and `CLAUDE.md`.
- The original roadmap existed outside the repository.

## Decision (stated by the project owner, 2026-11-17)

- Official documentation lives in the repository, in Markdown, under `docs/`.
- Language: learning notes in Spanish; technical documentation, architecture, and ADRs in English; code and identifiers in English.
- General learning (`docs/learning/`) is kept separate from its application in CompAI. Learning notes link to that application instead of duplicating it.
- Only validated information is documented (criteria in [docs/README.md](../README.md)).
- [roadmap.md](../roadmap.md) is the only official planning reference. The original roadmap is preserved verbatim in [roadmap-original.md](../roadmap-original.md) and is not maintained.
- A Documentation Agent restricted to `docs/` is under consideration. Its design and permissions are **pending approval** and it is not implemented.

## Known Reasons

- Avoid duplicated, contradictory, or unnecessary documentation (project owner).
- Rationale for the language split: not documented.

## Hypotheses

- Separating general learning from its application in CompAI reduces duplication and keeps learning notes stable while the project changes. Not verified.

## Open Questions

- Documentation tooling (site generators, automatic link checking): not evaluated.
- Whether a Documentation Agent provides more value than a documentation checklist.
- Documentation Agent design, permissions, and enforcement mechanism.

## Consequences

- A change that alters documented behavior should update the documentation in the same change.
- Documents carry an explicit state (`Draft`, `Validated`; ADRs: `Proposed`, `Accepted`, `Superseded`).
