# ADR-0003: Read-only development subagents

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

CompAI is developed with Claude Code. The project owner wanted analysis and review separated from implementation, while remaining the final decision-maker.

## Verified Facts

- `.claude/agents/tech-lead.md` and `.claude/agents/code-reviewer.md` exist (commit `1f01884`).
- Both declare `tools: Read, Glob, Grep`, `permissionMode: plan`, and `model: inherit`.
- [CLAUDE.md](../../CLAUDE.md) §5 defines their use as selective and advisory.

## Decision

Use two development-time subagents, both read-only, invoked selectively, with advisory output:

- **Tech Lead:** analysis and design.
- **Code Reviewer:** independent review of actual changes.

They are Claude Code development assistants, not CompAI product agents.

## Known Reasons (CLAUDE.md §5)

- Separate analysis and review from implementation.
- Review the actual diff independently, not only the implementer's summary.
- Keep final authority with the project owner.
- Avoid automatic delegation for small tasks.

## Hypotheses

- An independent read-only review reduces the risk of defects reaching the repository. Not measured.

## Open Questions

- Actual effectiveness, cost, and latency of using the subagents.
- Duplication between CLAUDE.md §5 and the agent definitions.
- Whether the Code Reviewer should flag outdated documentation.
- Name collision with planned product agents ([roadmap](../roadmap.md), Phase 6).

## Consequences

- The main session is the only writer of code.
- Reviews require the main session to provide the real diff and the acceptance criteria.
