<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Bootstrap Flow

Use this flow when building a Harness from a profile.

## Step 1: Read The Facts
Read the profile fully before writing anything.
Do not start by copying random docs from another repo.

## Step 2: Separate Generic From Specific
Build this split explicitly:

```text
profile
  <- project facts

skill
  <- reusable workflow logic

template
  <- stable file roles
```

## Step 3: Scaffold The Stable Shape
Create the stable skeleton first so later edits have a place to land.

## Step 4: Translate Facts Into Docs
Map the profile into:
- routing rules in `core-specs/AGENTS-v2.md`
- repo relationships in `core-specs/ARCHITECTURE-v2.md`
- design beliefs in `docs/design-docs/`
- product-specific docs in `docs/product-specs/`
- execution tracking in `docs/exec-plans/`
- top-level principle docs for design, planning, reliability, security, and quality

## Step 5: Leave Honest TODOs
If the profile does not define a real decision, the generated repo should say so clearly.

## Step 6: Validate The Harness
Before finishing:
- check that referenced files exist
- check that folder roles do not overlap confusingly
- check that `core-specs/AGENTS-v2.md` remains a map, not a giant manual

