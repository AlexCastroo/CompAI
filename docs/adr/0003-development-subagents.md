# ADR-0003: Read-only development subagents

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

CompAI is developed with Claude Code. The project owner wanted analysis and review separated from implementation, while remaining the final decision-maker.

## Verified Facts

- `.claude/agents/tech-lead.md` and `.claude/agents/code-reviewer.md` exist (commit `1f01884`).
- Both declare `tools: Read, Glob, Grep`, `permissionMode: plan`, and `model: inherit` in their frontmatter.
- Neither declares `Edit`, `Write`, or `Bash` in its `tools` list.
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
- The declared `tools` list and `permissionMode: plan` are sufficient to keep both subagents read-only. Not verified against Claude Code's actual behavior.

## Open Questions

- Effective permission enforcement: whether Claude Code actually prevents these subagents from modifying files with the current configuration.
- Alternatives not evaluated:
  - Main session only, without subagents.
  - Subagents with write access.
- Actual effectiveness, cost, and latency of using the subagents.
- Duplication between CLAUDE.md §5 and the agent definitions.
- Whether the Code Reviewer should flag outdated documentation. Overlaps with the Documentation Agent question in [ADR-0004](0004-documentation-strategy.md).
- Name collision with planned product agents ([roadmap](../roadmap.md), Phase 6).

## Consequences

- The main session is intended to be the only writer of project files.
- Reviews require the main session to provide the real diff and the acceptance criteria.
- Subagent behavior is defined in two places, [CLAUDE.md](../../CLAUDE.md) §5 and `.claude/agents/`. Both must be kept consistent when either changes.
