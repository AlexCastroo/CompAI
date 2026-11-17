> **Historical reference — not maintained.**
> This is the original roadmap, preserved verbatim below this note.
> It is not an official planning reference. The official roadmap is [roadmap.md](roadmap.md).

---

# CompAI — Technical and Learning Roadmap

## 1. Project Vision

CompAI is an AI-assisted software engineering tool, initially developed in Python.

Its long-term goal is to help developers understand, analyze, develop, review, and maintain software repositories through project intelligence, specialized agents, context management, memory, and engineering workflows.

CompAI is not intended to be a simple wrapper around an LLM.

The goal is to build a modular system capable of working with different model providers and execution engines, managing agents, coordinating tasks, and maintaining useful knowledge about software projects.

**Learning objective:** acquire practical knowledge of Python, software architecture, AI engineering, LLMs, agents, RAG, evaluation, observability, and orchestration.

## 2. Development Principles

1. Learn before automating.
2. Never generate large amounts of code without understanding it.
3. Implement small, verifiable features.
4. Separate responsibilities and avoid unnecessary coupling.
5. Prefer simple solutions over premature complexity.
6. Document important technical decisions.
7. Use tests to verify behavior.
8. Do not introduce frameworks without justification.
9. Keep the architecture extensible without overengineering.
10. Do not implement advanced features before understanding their fundamentals.

## 3. Priority Model

CompAI development is organized into three priority levels.

### P0 — Foundations

The minimum foundation required to build a useful and maintainable initial product.

Current scope:

- Python fundamentals.
- Development environment and project configuration.
- Modular application architecture.
- CLI foundation.
- Repository identification and inspection.
- Basic project intelligence.

**P0 outcome:** a modular Python CLI capable of identifying and inspecting software repositories.

No product agents, LLM integrations, RAG, embeddings, or advanced orchestration are included in P0 unless explicitly approved.

### P1 — Professional Capabilities

Capabilities that make CompAI a more useful software engineering assistant.

Potential scope:

- LLM provider integration.
- Agent Loop and Agent Runtime.
- Specialized agents.
- Context engineering.
- Persistent memory.
- Initial execution workflows.

**P1 outcome:** CompAI can use language models and controlled tools to assist with software engineering tasks.

### P2 — Advanced Capabilities

Advanced features introduced when there is a clear technical and product justification.

Potential scope:

- RAG and semantic search.
- Multiple execution engines.
- Advanced evaluation and observability.
- MCP integrations.
- Advanced code analysis.
- Multi-agent orchestration.
- Configurable workflows and automation.

**P2 outcome:** a more extensible, measurable, secure, and configurable engineering platform.

Priorities may evolve as the project develops. No phase is automatically approved for implementation merely because it appears in this roadmap.

## 4. Technical Stack

### Language and environment
- Python.
- uv for environment and dependency management.
- Git for version control.

### Development and quality
- VS Code.
- pytest.
- Ruff.
- Pyright or mypy when justified.
- Structured logging.

### CLI
- Typer.
- Rich.

### Architecture and configuration
- Modular architecture.
- Separation of responsibilities.
- Hexagonal Architecture (Ports & Adapters) when appropriate.
- Pydantic when useful.
- TOML or YAML for configuration when justified.

### Persistence and knowledge
- Markdown for human-readable knowledge.
- SQLite for structured information and state.
- Embeddings and vector storage in later phases.

### Models and execution engines
- OpenAI API for learning to build a custom Agent Loop.
- Claude Code as an external development execution engine.
- Ollama for local model experimentation.
- Adapters to avoid coupling the Core to a specific provider.

Integrations must use officially supported interfaces and respect the applicable terms of service.

## 5. Conceptual Architecture

The long-term architecture separates four main responsibilities.

### A. Core
- Project management.
- Agents.
- Tasks.
- Workflows.
- Context.
- Memory.
- Permissions and policies.

The Core must not depend directly on OpenAI, Ollama, or Claude Code.

### B. Providers and Execution Backends
- Model providers: OpenAI and Ollama.
- External execution backends: Claude Code.
- CompAI's own runtime for executing its agents.

A model provider is not necessarily a complete agent. We must distinguish between models, tools, Agent Loop, and Agent Runtime.

### C. Project Intelligence
- Directory exploration.
- Language and framework identification.
- File and dependency analysis.
- Architecture mapping.
- Code indexing.
- Relevant context retrieval.

### D. Infrastructure
- Persistence.
- Configuration.
- Logging.
- Security.
- Evaluation.
- Observability.

## 6. Development Roadmap

### Phase 0 — Environment and Fundamentals
**Priority: P0**

Objective: prepare the environment and understand the foundations.

- Verify Python, Git, and VS Code.
- Understand virtual environments and dependencies.
- Learn Python modules, packages, classes, types, and exceptions.
- Understand processes and the filesystem.
- Configure the repository.
- Establish initial technical documentation.

Outcome: a prepared development environment and a project structure that we understand.

### Phase 1 — Software Architecture Fundamentals
**Priority: P0**

Objective: design a maintainable application before introducing AI.

- Package structure.
- Separation of responsibilities.
- Interfaces and abstractions.
- Dependency injection.
- SOLID principles.
- Hexagonal Architecture.
- Configuration and error handling.
- Unit testing.

Outcome: a small, modular, tested Python application.

### Phase 2 — CLI Foundation
**Priority: P0**

Objective: create the first functional CompAI interface.

- Project initialization command.
- Project identification.
- Configuration loading.
- Basic repository exploration.
- Information and diagnostic commands.

Outcome: CompAI can run from the terminal and recognize a software project.

### Phase 3 — Project Intelligence
**Priority: P0**

Objective: enable CompAI to understand repository structure.

- Filesystem exploration.
- Technology identification.
- Structural analysis.
- Relevant file detection.
- Initial project map generation.
- Exclusion of sensitive files and irrelevant directories.

Outcome: CompAI generates a structured description of a repository.

### Phase 4 — LLM Integration
**Priority: P1**

Objective: understand how applications communicate with LLMs.

- Tokens and context windows.
- Messages, roles, and prompts.
- OpenAI API.
- Streaming.
- Tool calling.
- Error handling and rate limits.
- Provider abstraction.

Outcome: CompAI can communicate with a model through its own interface.

### Phase 5 — Agent Runtime and Agent Loop
**Priority: P1**

Objective: build the first custom agent.

- Difference between a model and an agent.
- Agent Loop.
- Tool registry.
- Tool execution.
- Result management.
- Iteration limits.
- Permission control.
- Error handling and completion.

Outcome: an initial agent capable of receiving a task, using authorized tools, and producing a result.

### Phase 6 — Specialized Agents
**Priority: P1**

Objective: organize engineering tasks through specialized roles.

Initial agents:

- Tech Lead: analyzes tasks and proposes technical solutions.
- Code Reviewer: reviews changes and identifies problems.
- Developer: implements authorized tasks.
- QA: proposes and executes tests.

Initially, agents will work independently. Coordination will be studied and introduced later.

Outcome: an initial system of specialized agents.

### Phase 7 — Context Engineering and Memory
**Priority: P1**

Objective: provide agents with relevant information without unnecessarily loading entire repositories.

- Context Engineering.
- File selection.
- Project summaries.
- Decision memory.
- Task memory.
- SQLite persistence.
- Markdown knowledge.
- Context management across sessions.

Outcome: CompAI retains useful knowledge and prepares relevant context for each task.

### Phase 8 — RAG and Semantic Search
**Priority: P2**

Objective: introduce intelligent information retrieval.

- Embeddings.
- Vector databases.
- Chunking.
- Semantic retrieval.
- Hybrid search.
- Reranking.
- Relevance evaluation.
- Integration with Project Intelligence.

Outcome: retrieval of relevant project and documentation information.

### Phase 9 — Claude Code and Ollama Integration
**Priority: P2**

Objective: work with different execution approaches.

- Supported Claude Code integration.
- Difference between delegating a task and executing a custom Agent Loop.
- Local models with Ollama.
- Adapters.
- Capability management.
- Comparison of results and limitations.

Outcome: CompAI can use different engines without confusing their responsibilities.

### Phase 10 — Evaluation, Observability, and Security
**Priority: P2**

Objective: move towards professional engineering standards.

- Execution traces.
- Token consumption and costs.
- Latency.
- Structured logs.
- Agent evaluations.
- Test datasets.
- Response quality.
- Secret management.
- Tool permissions.
- Prompt injection protection.
- Action auditing.

Outcome: a measurable, controllable, and more secure system.

### Phase 11 — MCP and Advanced Code Analysis
**Priority: P2**

Objective: extend integration and repository understanding capabilities.

- MCP fundamentals.
- MCP servers and clients.
- Tools and resources.
- AST.
- Tree-sitter.
- LSP.
- Dependency analysis.
- Structural repository maps.

Outcome: CompAI can integrate with external tools and understand code more deeply.

### Phase 12 — Workflows and Product Evolution
**Priority: P2**

Objective: evolve CompAI into a reusable engineering tool.

- Configurable workflows.
- Task delegation.
- Agent coordination.
- Change review.
- Git integration.
- Process automation.
- Future visual interface (Studio).
- Distribution and documentation.

Outcome: a consolidated initial version of CompAI.

## 7. Mandatory AI-Assisted Development Method

Every feature must follow this cycle:

1. **Concept:** explain the problem and the concepts we need to understand.
2. **Design:** compare alternatives and justify the architectural decision.
3. **Plan:** divide the work into small tasks.
4. **Implementation:** develop a specific part without unnecessary code.
5. **Testing:** verify behavior and analyze errors.
6. **Review:** inspect quality, architecture, security, and possible improvements.
7. **Documentation:** record what we learned and the decisions made.

We must not advance to the next learning unit until the previous one is reasonably understood.

## 8. Role of Claude Code

Claude Code acts as the implementation assistant inside the repository.

It must:

- Explain proposed changes before making them.
- Inspect existing code before proposing modifications.
- Avoid unnecessary rewrites.
- Implement small changes.
- Explain modified files.
- Run tests when appropriate.
- Identify uncertainties and risks.
- Present and justify important architectural decisions before implementation.
- Never assume the user understands a concept simply because the code works.

Subagents must be used selectively according to their responsibilities and configured permissions.

## 9. Documentation Strategy

Documentation is part of the development process, not an optional final activity.

- General learning material is documented in Spanish.
- Technical documentation, architecture, and ADRs are documented in English.
- Learning documents explain general concepts before their application in CompAI.
- Important architectural decisions are recorded through ADRs.
- Documentation must reflect validated knowledge and actual project decisions.
- Documentation changes must be reviewed before being accepted.

## 10. Definition of Success

CompAI is not successful simply because it executes commands or responds to prompts.

Success means building a modular, extensible, evaluable, and secure system while acquiring the ability to explain, maintain, and evolve every component independently.

**Fundamental priority: understand what we build.**
