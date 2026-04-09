<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# DESIGN

This repo is about designing a reusable Harness operating system, not a single project manual.

## Core Rule

Keep these two things separate:

- generic Harness structure
- project-specific facts

## Current Design Goal

Make one filled profile document enough to bootstrap:

- `AGENTS-v2.md`
- `ARCHITECTURE-v2.md`
- `docs/design-docs/`
- `docs/exec-plans/`
- `docs/generated/`
- `docs/product-specs/`
- `docs/references/`
- top-level principle docs

## Design Smell

If a rule only makes sense for one product, it belongs in the profile or generated repo, not in the generic skill.
