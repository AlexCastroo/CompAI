# CompAI Documentation

Entry point and rules for CompAI's documentation.

## 1. Map

| Path | Content | Language |
|---|---|---|
| [roadmap.md](roadmap.md) | Official planning reference: phases, status, open decisions | English |
| [roadmap-original.md](roadmap-original.md) | Original roadmap, preserved verbatim. Historical, not maintained | As original |
| [adr/](adr/) | Architecture Decision Records | English |
| [learning/](learning/) | General concepts studied during the project | Spanish |

### Architecture Decision Records

| ADR | Title | Status |
|---|---|---|
| [0001](adr/0001-python-version.md) | Python 3.13 as the initial Python version | Accepted |
| [0002](adr/0002-uv.md) | uv for environment and dependency management | Accepted |
| [0003](adr/0003-development-subagents.md) | Read-only development subagents | Accepted |
| [0004](adr/0004-documentation-strategy.md) | Documentation strategy | Accepted |

### Learning notes

| Note | Status |
|---|---|
| [Entornos virtuales y gestión de dependencias en Python](learning/entornos-y-dependencias-python.md) | Validated |

## 2. Language Rules

- `learning/`: Spanish.
- Everything else in `docs/`: English.
- Code, identifiers, file names, and commands: English, unchanged.
- `roadmap-original.md` keeps its original content and is exempt from these rules.

## 3. Sources of Truth

Each type of information has a single source. Other documents link to it instead of copying it.

| Information | Source of truth |
|---|---|
| Dependencies and versions | `pyproject.toml` and `uv.lock` |
| Current phase, status, and open decisions | [roadmap.md](roadmap.md) |
| Technical decisions and their reasons | [adr/](adr/) |
| Rules for Claude Code | [CLAUDE.md](../CLAUDE.md) |
| Development subagent behavior | `.claude/agents/` |
| General concepts | [learning/](learning/) |

## 4. Validation Criteria

Only validated information is documented as fact.

| Type | Validated when |
|---|---|
| Decision | The project owner explicitly approves it (ADR `Accepted`) |
| Code behavior | It is on `main` and tests were executed with evidence |
| Commands and instructions | They were executed and the result was checked |
| Dependencies | They are declared in `pyproject.toml` / `uv.lock` |
| Concepts (`learning/`) | Explained, reviewed by the owner, and backed by sources for external facts |
| P1 / P2 roadmap items | Never validated in advance; always `tentative` until approved |
| Subagent output | Never validated by itself; it is advisory |

Unvalidated content must be explicitly labeled (`Draft`, `Proposed`, "Not verified", "Open question").

## 5. Document States

- **General documents and learning notes:** `Draft` → `Validated`.
- **ADRs:** `Proposed` → `Accepted` → `Superseded by ADR-XXXX` (when replaced). ADRs are never deleted.

Only the project owner promotes a document to `Validated` or an ADR to `Accepted`.

## 6. Maintenance Rules

- Update documentation in the same change that alters documented behavior.
- Do not create documents speculatively or split content into very small files.
- Separate verified facts, decisions, hypotheses, and open questions.
- Never invent rationale: write "Not documented" or "Not evaluated" when a reason is unknown.
- Documentation changes are reviewed by the project owner before being accepted.

## 7. ADR Template

New ADRs use the next free number: `adr/NNNN-short-title.md`.

```markdown
# ADR-NNNN: Title

- **Status:** Proposed | Accepted | Superseded by ADR-XXXX
- **Date:** YYYY-MM-DD

## Context
Problem and circumstances that required a decision.

## Verified Facts
Checkable facts, each with its source (file, commit, command output).

## Decision
What was decided.

## Known Reasons
Only reasons actually stated or documented. No retrospective justification.

## Hypotheses
Assumptions that have not been verified.

## Open Questions
Alternatives not evaluated and pending questions.

## Consequences
Effects of the decision on the project.
```
