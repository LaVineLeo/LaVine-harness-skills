<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Harness Principles

Use this file when choosing what the scaffold should encode and what should stay flexible.

## Core Principles

- Keep humans on intent and review; let agents execute most local steps.
- Keep repository knowledge local, versioned, and discoverable.
- Treat `core-specs/AGENTS-v2.md` as a map, not a giant manual.
- Prefer progressive disclosure over one huge instruction file.
- Encode invariants mechanically when they repeat.
- Keep plans, validation notes, and debt in the repo so future agent runs can see them.
- Run continuous cleanup so weak patterns do not spread.

## What To Encode In The Repo

Encode information when the agent would otherwise have to guess:

- package, dataset, or workflow ownership
- dependency directions and stable boundaries
- validation commands and acceptance checks
- naming conventions that matter for consistency
- recurring review comments or cleanup expectations
- known debt that is real but not worth fixing yet

## What To Avoid

- Do not turn `core-specs/AGENTS-v2.md` into an encyclopedia.
- Do not rely on chat threads, external docs, or human memory as the only source of truth.
- Do not over-specify local implementation choices when the boundary is the real invariant.
- Do not let stale documentation remain unchallenged once it disagrees with the repo.

## Translation Into This Skill

- The templates start with a small map in `core-specs/AGENTS-v2.md`.
- The durable knowledge lives under `docs/`.
- `plans/active/` exists so non-trivial work is recorded in-repo.
- `docs/quality/debt-log-v2.md` exists so unsafe cleanup can be tracked without guessing.
- The generic-harness script only handles fixed placeholders; the real customization should happen in-repo after scaffolding.

