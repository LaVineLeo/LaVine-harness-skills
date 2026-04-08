<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# Harness Profile Schema

Use this file when interpreting a `HARNESS_PROFILE-v2.md`.

## Required Sections

### `Project Identity`
Must answer:
- what the project is called
- what kind of repo shape it has
- who the main users are
- what outcome matters most

### `Project Purpose`
Must explain why the project exists and what success means.

### `Repo Map`
Must list the important repos, packages, or surfaces and say:
- where they live
- what they do
- which one is higher priority when they conflict
- which one is source of truth for a topic
- which ones should not be changed by default

### `User Success Path`
Must explain the most important external-facing path.
This is what drives doc and quickstart priorities.

### `Main Workflows`
Must explain the repeated flows the Harness should route correctly.
Each workflow should have a trigger, read-first docs, main steps, outputs, validation, and escalation path.

### `Git Workflow`
Must explain branch, commit, tag, PR, and rebase rules.

### `Quality Priorities`
Must rank what matters most so the generated docs do not speak in generic slogans.

### `Skills And Tools`
Must list special skills, tools, or references the target Harness should know about.

### `Boundaries`
Must define default no-go areas, approval-needed areas, and legacy paths.

## Missing Information Rule

If one of these sections is missing, do not invent detailed project rules.
Instead:
- ask the smallest useful question
- or leave a clear TODO in the generated repo

