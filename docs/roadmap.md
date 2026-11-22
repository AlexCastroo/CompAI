# CompAI Roadmap

> **This is the only official planning reference for CompAI.**
> It records the current phase, the status of each phase, and open decisions.
> No phase or item is approved for implementation merely because it appears here.
> Historical source: [roadmap-original.md](roadmap-original.md) (preserved verbatim, not maintained).

## 1. Vision

CompAI is an AI-assisted software engineering tool, initially developed in Python. Its long-term goal is to help developers understand, analyze, develop, review, and maintain software repositories.

CompAI is also a practical learning project: understanding what is built, and why, is as important as delivering working software.

Development principles and the working method are defined in [CLAUDE.md](../CLAUDE.md) (§4 and §7) and are not repeated here.

## 2. Priority Model

| Priority | Name | Status |
|---|---|---|
| **P0** | Foundations | **Current scope** |
| P1 | Professional Capabilities | Tentative |
| P2 | Advanced Capabilities | Tentative |

- **P0 outcome:** a modular Python CLI capable of identifying and inspecting software repositories.
- **P1 outcome (tentative):** CompAI can use language models and controlled tools to assist with software engineering tasks.
- **P2 outcome (tentative):** a more extensible, measurable, secure, and configurable engineering platform.

LLM integrations and CompAI's own agents will not start until the fundamentals of the CLI and Project Intelligence have been built and understood.

Status values: `planned`, `in progress`, `done`, `postponed`, `discarded`. P1 and P2 items are `tentative` until explicitly approved.

## 3. Current Status

- **Priority:** P0.
- **Phase:** Phase 1 — Software Architecture Fundamentals (in progress). Phase 0 completed on 2026-11-21.

## 4. Phases

### Phase 0 — Environment and Fundamentals

- **Priority:** P0
- **Status:** done
- **Objective:** prepare the environment and understand the foundations.

| Item | Status | Evidence |
|---|---|---|
| Python available | done | CPython 3.13.5 (`.venv/pyvenv.cfg`) — see [ADR-0001](adr/0001-python-version.md) |
| Git available and repository initialized | done | Git history |
| uv, `.venv`, `pyproject.toml`, `uv.lock` | done | Commit `0ca1e45` — see [ADR-0002](adr/0002-uv.md) |
| Understand virtual environments and dependencies | done | Learning note validated: [entornos-y-dependencias-python.md](learning/entornos-y-dependencias-python.md); `.venv` rebuild with `uv sync` verified by the project owner |
| Python modules, packages, classes, types, exceptions | done | Studied and reviewed by the project owner with ChatGPT, outside the repository (2026-11-20); no learning note or exercise recorded in the repository |
| Processes and the filesystem | done | Marked done by the project owner (2026-11-20); no learning note or exercise recorded |
| Repository configuration (`.gitignore`, Ruff, pytest) | done | `.gitignore` configured (commit `bdb2462`); Ruff and pytest configured, `ruff check`, `ruff format --check` and `pytest` pass — see [ADR-0005](adr/0005-quality-tools.md) |
| Initial technical documentation | done | `docs/` created; ADR-0001 to ADR-0004 `Accepted` |

**Outcome:** a prepared development environment and a project structure that we understand.

### Phase 1 — Software Architecture Fundamentals

- **Priority:** P0
- **Status:** in progress
- **Objective:** design a maintainable application before introducing AI.
- **Note:** learning a concept is not the same as adopting it in the code. Adopting an architectural pattern requires an ADR. See [OD-1](#od-1--hexagonal-architecture-in-p0).
- **Method:** each item is explained, applied to a small part of CompAI, and tested. Items are worked in this order because each builds on the previous ones. Unit testing is applied in every item.

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | Package structure | done | Installable package in `src/compai/` with `uv_build`; `tests/test_package.py` passes — see [ADR-0006](adr/0006-package-structure.md) |
| 2 | Separation of responsibilities | planned | — |
| 3 | Configuration and error handling | planned | — |
| 4 | Interfaces and abstractions | planned | — |
| 5 | Dependency injection | planned | — |
| 6 | SOLID principles | planned | — |
| 7 | Hexagonal Architecture (decides [OD-1](#od-1--hexagonal-architecture-in-p0)) | planned | — |
| 8 | Unit testing (applied in every item) | in progress | — |

Practice cases must not anticipate Phase 2 and Phase 3 functionality; scope is reviewed at each item.

**Outcome:** a small, modular, tested Python application.

### Phase 2 — CLI Foundation

- **Priority:** P0
- **Status:** planned
- **Objective:** create the first functional CompAI interface.
- **Items:** project initialization command (see [OD-3](#od-3--init-command)); project identification; configuration loading; basic repository exploration; information and diagnostic commands.

**Outcome:** CompAI can run from the terminal and recognize a software project.

### Phase 3 — Project Intelligence

- **Priority:** P0
- **Status:** planned
- **Objective:** enable CompAI to understand repository structure.
- **Items:** filesystem exploration; technology identification; structural analysis; relevant file detection; initial project map generation; exclusion of sensitive files and irrelevant directories (see [OD-2](#od-2--minimum-security-in-p0)).

**Outcome:** CompAI generates a structured description of a repository.

### Phase 4 — LLM Integration

- **Priority:** P1 · **Status:** tentative
- **Items:** tokens and context windows; messages, roles, and prompts; OpenAI API; streaming; tool calling; error handling and rate limits; provider abstraction.

### Phase 5 — Agent Runtime and Agent Loop

- **Priority:** P1 · **Status:** tentative
- **Items:** model vs agent; Agent Loop; tool registry; tool execution; result management; iteration limits; permission control; error handling and completion.

### Phase 6 — Specialized Agents

- **Priority:** P1 · **Status:** tentative
- **Items:** Tech Lead, Code Reviewer, Developer, and QA product agents, initially working independently.
- **Note:** these are future CompAI **product** agents. They are distinct from the Claude Code **development** subagents used to build CompAI ([CLAUDE.md](../CLAUDE.md) §5, [ADR-0003](adr/0003-development-subagents.md)).

### Phase 7 — Context Engineering and Memory

- **Priority:** P1 · **Status:** tentative
- **Items:** context engineering; file selection; project summaries; decision and task memory; SQLite persistence; Markdown knowledge; context across sessions.

### Phase 8 — RAG and Semantic Search

- **Priority:** P2 · **Status:** tentative
- **Items:** embeddings; vector databases; chunking; semantic and hybrid retrieval; reranking; relevance evaluation; integration with Project Intelligence.

### Phase 9 — Claude Code and Ollama Integration

- **Priority:** P2 · **Status:** tentative
- **Items:** supported Claude Code integration; delegating a task vs running a custom Agent Loop; local models with Ollama; adapters; capability management; comparison of results.
- Integrations must use officially supported interfaces and respect the applicable terms of service.

### Phase 10 — Evaluation, Observability, and Security

- **Priority:** P2 · **Status:** tentative
- **Items:** execution traces; token consumption and costs; latency; structured logs; agent evaluations; test datasets; response quality; secret management; tool permissions; prompt injection protection; action auditing.
- **Note:** basic security measures are not postponed to this phase. See [OD-2](#od-2--minimum-security-in-p0).

### Phase 11 — MCP and Advanced Code Analysis

- **Priority:** P2 · **Status:** tentative
- **Items:** MCP fundamentals, servers, clients, tools, and resources; AST; Tree-sitter; LSP; dependency analysis; structural repository maps.

### Phase 12 — Workflows and Product Evolution

- **Priority:** P2 · **Status:** tentative
- **Items:** configurable workflows; task delegation; agent coordination; change review; Git integration; process automation; future visual interface (Studio); distribution and documentation.

## 5. P0 Exit Criteria

To be defined. See [OD-4](#od-4--p0-exit-criteria).

## 6. Technology Status

| Technology | Purpose | Status | Reference |
|---|---|---|---|
| Python 3.13 | Language and runtime | adopted (decision `Accepted`) | [ADR-0001](adr/0001-python-version.md) |
| uv | Environment and dependencies | adopted (decision `Accepted`) | [ADR-0002](adr/0002-uv.md) |
| uv_build | Build backend | adopted (decision `Accepted`) | [ADR-0006](adr/0006-package-structure.md) |
| Git | Version control | adopted | — |
| Typer | CLI framework | planned | CLAUDE.md §3 |
| Rich | Terminal presentation | planned | CLAUDE.md §3 |
| pytest | Testing | adopted (decision `Accepted`) | [ADR-0005](adr/0005-quality-tools.md) |
| Ruff | Linting and formatting | adopted (decision `Accepted`) | [ADR-0005](adr/0005-quality-tools.md) |
| Pyright or mypy | Type checking | candidate | — |
| Structured logging | Logging | candidate | — |
| Pydantic | Data validation | candidate | — |
| TOML or YAML | Configuration format | candidate | — |
| SQLite | Persistence | candidate (P1) | — |
| OpenAI API, Ollama, Claude Code | Model providers and execution engines | candidate (P1/P2) | — |

`adopted` means present in the project. `planned` means intended but not installed. `candidate` means mentioned in the original roadmap with no decision. Every new dependency requires the owner's approval (CLAUDE.md §3).

## 7. Long-Term Conceptual Areas

Conceptual, not an approved design.

- **Core:** projects, agents, tasks, workflows, context, memory, permissions and policies. Must not depend directly on specific providers or execution engines.
- **Providers and execution backends:** model providers, external execution backends, and CompAI's own runtime.
- **Project Intelligence:** exploration, technology identification, file and dependency analysis, architecture mapping, indexing, context retrieval.
- **Infrastructure:** persistence, configuration, logging, security, evaluation, observability.

## 8. Open Decisions

### OD-1 — Hexagonal Architecture in P0

- **Question:** should Hexagonal Architecture (Ports & Adapters) be adopted during P0?
- **Owner position:** it will not be imposed before its fundamentals are understood and actually needed.
- **Status:** open.

### OD-2 — Minimum security in P0

- **Question:** which basic security measures does P0 need?
- **Owner position:** security must not wait until Phase 4. P0 already needs basic measures to protect sensitive files and to control repository exploration.
- **Status:** open. Scope and measures to be defined; nothing implemented.

### OD-3 — `init` command

- **Question:** what is the responsibility of the project initialization command?
- **Owner position:** its responsibility, behavior, and effects on the target repository must be defined before implementation.
- **Status:** open.

### OD-4 — P0 exit criteria

- **Question:** what criteria define P0 as complete?
- **Status:** open.

## 9. Not Carried Over from the Original Roadmap

| Original section | Where it lives now |
|---|---|
| §2 Development Principles | [CLAUDE.md](../CLAUDE.md) §4 |
| §7 Development Method | [CLAUDE.md](../CLAUDE.md) §7 |
| §8 Role of Claude Code | [CLAUDE.md](../CLAUDE.md) §5 |
| §9 Documentation Strategy | [ADR-0004](adr/0004-documentation-strategy.md) and [docs/README.md](README.md) |
| §10 Definition of Success | [CLAUDE.md](../CLAUDE.md) §9 |
| "Verify VS Code" (Phase 0) | Omitted: personal development environment, not a project requirement |

## 10. Change Log

| Date | Change | Reason | Approved by |
|---|---|---|---|
| 2026-11-17 | Roadmap created from the original roadmap | Adapt the original to CompAI's current state | Project owner |
| 2026-11-21 | Phase 0 marked done; Phase 1 in progress | All Phase 0 items done; Ruff and pytest configured (ADR-0005) | Project owner |
| 2026-11-22 | Phase 1 items ordered and tracked in a table | Each item builds on the previous ones | Project owner |
