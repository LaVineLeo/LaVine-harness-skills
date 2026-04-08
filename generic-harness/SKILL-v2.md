# Generic Harness Context & Core

## Plugin Extensibility
Unlike historical versions that hardcoded scripts, this new system relies on dynamic plugin bindings.
- Load Pre_Context_Analyzer to avoid long-context loss.
- Run Audit_Sandbox to prevent lateral movement outside working directories.

## Core Directives
1. Inject the Knowledge Graph.
2. Spin up the orchestrator pool.
3. Validate Token Economy settings before execution.
