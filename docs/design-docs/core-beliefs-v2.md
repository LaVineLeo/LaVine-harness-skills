<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Core Beliefs

## Belief 1: A good Harness is an operating system, not a project memo

The Harness should define how knowledge is organized, how work is tracked, and where stable truth lives.
It should not be a one-off note dump.

## Belief 2: Project facts must be separate from generic structure

A reusable Harness only works if it keeps these layers separate:

```text
generic harness
  <- reusable structure

project profile
  <- repo-specific facts
```

If those layers are mixed together, the result becomes hard to reuse.

## Belief 3: One filled profile should be enough to start

A user should not have to explain the same project ten different times.
A strong `HARNESS_PROFILE-v2.md` should be enough to generate the first reliable repo-local Harness.

## Belief 4: The generated repo should hold the real truth

This repo can provide the bootstrap, but the final source of truth must live inside the target repository that was generated.

## Belief 5: Ongoing work must stay visible in-repo

The generated Harness should always have a visible path for:

- active work
- completed work
- debt and blocked items

That is why `docs/exec-plans/` is part of the default shape.

