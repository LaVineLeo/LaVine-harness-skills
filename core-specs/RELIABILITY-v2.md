<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# RELIABILITY

A reusable Harness builder is reliable only if the generated repo stays understandable after the first run.

## Reliability Rules

- generated files must have stable roles
- internal references must stay consistent
- missing project facts should become TODOs, not fabricated certainty
- the bootstrap script should be deterministic for the stable skeleton
- the skill should ask only for missing high-value information
