<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Customization Playbook

Use this file immediately after scaffolding a new Harness.

## First Pass

1. Rename or remove example paths that do not exist in the real repo.
2. Rewrite `core-specs/AGENTS-v2.md` so every referenced doc actually exists.
3. Fill `docs/architecture/monorepo-map-v2.md` with real ownership and dependency rules.
4. Replace placeholder validation notes in `docs/validation/checks-v2.md` with real commands.
5. Create the first task plan in `plans/active/` if the work is non-trivial.

## What To Customize Early

- domain names and package names
- datasets, services, or workflow boundaries
- deployment or runtime assumptions
- validation commands that the agent can run directly
- recurring review rules that should become durable docs or automation

## What To Leave Flexible

- local implementation details inside a stable boundary
- tooling choices that are already easy for the agent to infer
- optional docs that are not yet justified by real repeated work

## First Round Of Hardening

- Add one domain-specific architecture file if the repo has a non-obvious layer.
- Add one focused invariant if the same mistake is likely to repeat.
- Add one validation command that proves the most important path still works.
- Add one debt-log entry instead of letting uncertain cleanup block progress.

## Smell Checks

Update the scaffold if any of these are true:

- `core-specs/AGENTS-v2.md` is growing into a long manual.
- agents keep asking where ownership lives.
- validation is implied but not written down.
- important design decisions live only in chat or external docs.
- cleanup comments repeat without becoming rules, tests, or scripts.

