<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Harness Abstraction

## Problem

Earlier Harness work was useful, but still too coupled to the specific project it came from.
That means another team still had to manually rewrite too much before the system became theirs.

## Abstraction Goal

The new abstraction is:

```text
project-specific facts
  -> profile document

generic operating logic
  -> reusable skill

stable file skeleton
  -> deterministic template assets
```

## Why This Split Works

- the profile captures real project facts
- the skill captures reusable translation logic
- the scaffold captures stable file roles

That means the next repo does not need to reinvent the Harness shape.
It only needs to provide its own facts.

## What Should Stay Generic

- folder structure
- file roles
- plan flow
- archive rules
- quality and boundary prompts

## What Should Come From The Profile

- project purpose
- repo map
- routing rules
- workflow steps
- source-of-truth decisions
- quality priorities
- no-go areas

## Failure Mode To Avoid

The main failure mode is turning the generic skill into a hidden project-specific manual.
If a rule only makes sense for one repo, it should come from the profile or the generated target repo, not from the generic Harness skill.

