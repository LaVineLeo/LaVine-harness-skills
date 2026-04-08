# Machine-Readable Artifact: Swarm-Profile (v3.0)

## Schema Definition
This document acts as a highly compressed, machine-readable YAML proxy representing project configuration facts. It is utilized by a Swarm Orchestrator to allocate permissions and sandbox context.

`yaml
version: '3.0'
project_orchestration:
  sandbox_bounds:
    permitted_write: ['src/', 'config/']
    forbidden: ['.git/', '.env']
  swarm_topology:
    - type: Orchestrator
      responsibilities: ['Routing', 'Task Breakdown']
    - type: Coder
      responsibilities: ['Logic Execution', 'Test Generation']
    - type: Reviewer
      responsibilities: ['Debt Logging', 'Guardrail Auditing']
  token_economy:
    strict_compression: true
    max_context_window_fraction: 0.8
`

## Self-Healing Hooks
When a Coder agent fails a test execution 3 consecutive times, it must:
1. Truncate current context buffer.
2. Read the nearest Debt Validation artifact.
3. Automatically escalate to the Reviewer terminal.
