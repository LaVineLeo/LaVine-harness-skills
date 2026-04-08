<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Template Selection

Choose the narrowest template that still matches the real repository shape.

## `software`

Choose `software` when the repository primarily owns application code or infrastructure code.

Use it for:

- web, backend, mobile, CLI, or full-stack products
- SDKs, services, workers, or internal developer tooling
- monorepos with `apps/`, `packages/`, and `infra/`

Expect the scaffold to optimize for:

- package and service boundaries
- runtime validation and dependency directions
- tests, type checks, and integration checks

## `research`

Choose `research` when the repository primarily owns experiments, datasets, evaluations, or analytical outputs.

Use it for:

- model evaluation repos
- scientific experiments
- benchmark suites
- analysis-heavy projects with reproducibility requirements

Expect the scaffold to optimize for:

- provenance and reproducibility
- immutable raw data and explicit derived outputs
- experiment configs, metrics, and report validation

## `general`

Choose `general` when the repository is not primarily a codebase or research lab, but still needs a legible agent operating system.

Use it for:

- writing systems
- operations playbooks
- business workflows
- multi-step delivery processes with references and templates

Expect the scaffold to optimize for:

- canonical references
- reusable deliverables and automation
- workflow ownership and approval paths

## When Two Templates Could Work

- Prefer `software` if most changes land in code and the repo has executable systems.
- Prefer `research` if reproducibility and experiment tracking are the dominant concerns.
- Prefer `general` if the repo is mostly process, content, or deliverable orchestration.

If the repo spans more than one mode, start with the dominant one and add domain-specific docs after the first scaffold pass.

