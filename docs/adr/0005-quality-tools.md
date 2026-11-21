# ADR-0005: Ruff and pytest as development quality tools

- **Status:** Accepted
- **Date:** 2026-11-20

## Context

Phase 0 includes repository configuration with Ruff and pytest ([roadmap](../roadmap.md), Phase 0). Both are part of the initial stack ([CLAUDE.md](../../CLAUDE.md) §3). No Python code exists yet, so linting, formatting, and testing can be in place before the first module is written.

## Verified Facts

- `pyproject.toml` declares a `dev` dependency group with `pytest>=9.2.0` and `ruff>=0.17.6`. `uv.lock` resolves it, and `uv lock --check` exits with 0.
- Installed versions: ruff 0.17.6, pytest 9.2.0 (`uv run ruff --version`, `uv run pytest --version`).
- Ruff configuration in `pyproject.toml`: `line-length = 88`, `target-version = "py313"`, `extend-exclude = ["*.md"]`, lint `select = ["I", "UP", "B", "F", "E4", "E7", "E9"]`, format `quote-style = "double"` and `indent-style = "space"`.
- `uv run ruff check .` reports "All checks passed!" and `uv run ruff format --check .` exits with 0.
- The selected rules are applied: a sample file outside the repository produced `I001`, `F401`, `UP035`, `UP006`, and `B006`.
- Without the Markdown exclusion, `ruff format` included the repository's `.md` files (observed with ruff 0.17.6, `-v` output). With it, no `.md` file is included.
- pytest configuration in `pyproject.toml` uses the native `[tool.pytest]` table (supported since pytest 9): `testpaths = ["tests"]`, `addopts = ["-ra", "--strict-markers", "--strict-config"]`. The classic `[tool.pytest.ini_options]` format was also tested and works.
- `uv run pytest` reports `configfile: pyproject.toml`, `testpaths: tests`, and "1 passed" (exit 0) with `tests/test_environment.py`, which checks that the environment runs Python 3.13 or later.
- `--strict-config` is effective: a misspelled key (`testpathz`) made pytest fail with "Unknown config option" (exit 4).
- `testpaths` limits collection: in a probe project outside the repository, a test file outside `tests/` was not collected.
- `.gitignore` excludes `.pytest_cache/` and `.ruff_cache/`.

## Decision

- Use **Ruff** for linting and formatting, and **pytest** for automated tests.
- Both are development dependencies in the `dev` group managed by uv, and run through `uv run`.
- Lint rules: Ruff's defaults (`E4`, `E7`, `E9`, `F`) plus `I` (import sorting), `UP` (modern syntax), and `B` (likely bugs).
- Ruff does not process Markdown files.
- Tests live in `tests/` at the repository root. pytest is configured in `pyproject.toml` with the native `[tool.pytest]` table, collecting only from `tests/` and running with `-ra`, `--strict-markers`, and `--strict-config`.

## Known Reasons

Discussed with the project owner on 2026-11-20 and 2026-11-21:

- Ruff and pytest are part of the planned stack ([CLAUDE.md](../../CLAUDE.md) §3).
- Ruff replaces several separate tools (linter, formatter, import sorter) with one tool and one configuration.
- `I`, `UP`, and `B` add consistency, current Python 3.13 idioms, and detection of real bugs, with little noise.
- Markdown is excluded because documentation is outside Ruff's responsibility and [roadmap-original.md](../roadmap-original.md) must stay verbatim ([ADR-0004](0004-documentation-strategy.md)).
- The native `[tool.pytest]` table is consistent with the rest of `pyproject.toml` and the project already requires pytest 9 or later.
- `--strict-markers` and `--strict-config` turn typos into errors instead of silently ignoring them.
- Tests verify behavior instead of relying on assumptions ([CLAUDE.md](../../CLAUDE.md) §4), and code behavior is only validated with executed tests ([docs/README.md §4](../README.md#4-validation-criteria)).

## Hypotheses

- The selected rule set is useful without excessive noise. Not verified on project code; no code exists yet.
- pytest is sufficient for P0 testing needs. Not verified.

## Open Questions

- Alternatives not evaluated in practice: flake8 + black + isort, pylint, `unittest`.
- Additional rule families: `S` (security) as part of [OD-2](../roadmap.md#od-2--minimum-security-in-p0); `SIM` and `N` once code exists.
- Importing the CompAI package from tests depends on the package layout and `[build-system]`, not yet decided.
- Test coverage measurement (e.g. `pytest-cov`): not evaluated.
- Running the checks automatically (pre-commit hooks, CI): not evaluated.

## Consequences

- `uv sync` installs the development tools together with the environment.
- Python code is expected to pass `ruff check` and `ruff format --check`.
- `uv run pytest` is expected to pass (exit 0) before changes are merged.
- Unknown pytest options and unregistered markers fail the test run.
- Python code blocks inside Markdown documentation are neither linted nor formatted.
- The Python version is declared in two places (`requires-python` and Ruff's `target-version`); both must be kept consistent.
