# ADR-0001: Python 3.13 as the initial Python version

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

CompAI is initially developed in Python ([CLAUDE.md](../../CLAUDE.md) §1). Creating the project environment required an interpreter version and a `requires-python` declaration.

## Verified Facts

- `pyproject.toml` declares `requires-python = ">=3.13"` (commit `0ca1e45`).
- `.venv` was created with CPython 3.13.5 (`.venv/pyvenv.cfg`).
- No `.python-version` file exists; the interpreter version is not pinned.

## Decision

Use Python 3.13 as the initial version, with `>=3.13` as the minimum declared version.

## Known Reasons

- Python 3.13.5 was the version already installed in the development environment.
- No technical evaluation of Python versions was performed.

## Hypotheses

- Python 3.13 is sufficient for P0 needs. Not verified.

## Open Questions

- Is `>=3.13` the right lower bound? Compatibility with earlier versions has not been evaluated.
- The declared range allows Python 3.14 or later, which has not been tested.
- Should the interpreter version be pinned (e.g. `.python-version`)?
- Python as the primary language is a project premise (CLAUDE.md §1), not the result of a comparison with other languages.

## Consequences

- Development and execution currently require Python 3.13 or later.
- The lower bound may need revision when distribution of the CLI is considered.
