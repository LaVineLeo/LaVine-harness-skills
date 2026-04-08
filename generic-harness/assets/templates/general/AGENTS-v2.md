# Swarm Agent Protocol bounds

## Access & Operation Matrix

All autonomous agents must abide by the Swarm sandbox guardrails. We no longer use simple scattered text guides. All directions are structural.

### [Orchestrator Node]
- **Role**: Map complex directives to targeted file constraints.
- **Constraints**: NEVER execute file edits. ONLY read core-specs/ARCHITECTURE-v2.md and assign bounds.

### [Coder Node]
- **Role**: Operates exclusively in the bounded sandbox parsed by the Orchestrator.
- **Constraints**: 
  - Token compression: Do not stream unrelated files.
  - Zero-Hallucination rule: Before assuming a module API, grep_search its signature.

### [Reviewer & Auditor Node]
- **Role**: Validates boundaries after the Coder operates.
- **Constraints**: Emphasizes Security. Write directly to debt-log-v2.md upon heuristic failure.

## Reflection & Rollback
If validation fails:
1. Halt execution.
2. Engage Reflection Mode: Output the differential logic graph to a local .temp and verify against invariants-v2.md.
