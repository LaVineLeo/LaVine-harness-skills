<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# skill-engine

## Purpose

`skill-engine` is the main v2 deliverable in this repo.
It should let a team fill one profile document, then generate a strong first Harness for a target monorepo.

## Input

- a filled `HARNESS_PROFILE-v2.md`
- a target repository path
- optional clarifications for missing high-value facts

## Output

A first Harness structure with:

- `core-specs/AGENTS-v2.md`
- `core-specs/ARCHITECTURE-v2.md`
- `docs/design-docs/`
- `docs/exec-plans/`
- `docs/generated/`
- `docs/product-specs/`
- `docs/references/`
- top-level principle docs like `core-specs/DESIGN-v2.md`, `core-specs/PLANS-v2.md`, `core-specs/PRODUCT_SENSE-v2.md`, `core-specs/QUALITY_SCORE-v2.md`, `core-specs/RELIABILITY-v2.md`, and `core-specs/SECURITY-v2.md`

## Non-Goals

- it should not pretend to know missing project facts
- it should not hard-code one product's routing rules into the generic skill
- it should not generate fake certainty where the profile is incomplete

