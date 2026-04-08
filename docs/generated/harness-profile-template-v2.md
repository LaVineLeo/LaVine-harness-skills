<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# HARNESS_PROFILE Template

Use this file as the first input for `skill-engine`.
Fill the sections with real project facts before asking the skill to scaffold the Harness.

## Project Identity
- project_name:
- project_type: monorepo | multi-repo | single-repo
- primary_users:
- primary_outcome:
- current_stage:

## Project Purpose
Describe what the project is for in 5-10 lines.
Focus on what users or operators need the project to do.

## Repo Map
For each important repo or package, add one block.

### repo_or_package_name
- path:
- role:
- priority:
- source_of_truth:
- public_or_internal:
- when_to_route_here:
- what_not_to_change_by_default:

## User Success Path
Describe the most important external success path.

- first_success_moment:
- docs_surface:
- quickstart_surface:
- sdk_or_client_surface:
- biggest_user_confusions:

## Main Workflows
Add one block per repeated workflow.

### workflow_name
- trigger:
- read_first:
- main_steps:
- outputs:
- validation:
- escalation_path:

## Git Workflow
- branch_rule:
- commit_rule:
- tag_rule:
- pr_rule:
- rebase_rule:

## Quality Priorities
Rank the most important quality axes.

- reliability:
- usability:
- clarity:
- security:
- speed:
- consistency:

## Skills And Tools
- special_skills:
- required_external_tools:
- required_references:

## Boundaries
- default_no_go_areas:
- areas_that_require_explicit_confirmation:
- legacy_paths_or_archives:

## Open Questions
List the important unknowns the skill should leave as TODOs instead of guessing.

