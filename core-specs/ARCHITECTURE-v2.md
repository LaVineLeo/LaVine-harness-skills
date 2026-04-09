# Cognitive Architecture Map (V3)

## Decoupled Triad System

1. **Generic Harness (The Kernel/Base)**
   Provides abstract schema definitions and invariant policies. It does NOT contain single strings from the project domain. It's the ruleset engine.
   
2. **Project Profile (The Knowledge Graph)**
   A constrained environment full of YAML/JSON objects. The old sprawling Markdowns are gone. Contains facts, secrets-map, and routing paths.
   
3. **Skill Engine (The Actuator/Swarm Kernel)**
   The live Python components that orchestrate the Swarm. Contains pre-commit checks, token optimizers, and Git diff interceptors.

## Semantic Token Economy
Layers exist to isolate token inflation. Agents only query the layer they belong to.

## Appendix A: Swarm Node Operational Mechanics
```yaml
node_class: Orchestrator
memory_bounds: 128MB
token_limits:
  hard_cap: 128000
  soft_cap: 100000
  sliding_window_strategy: 'LRU_Context_Dump'
execution_matrix:
  can_map_reduce: true
  can_write: false
  can_spawn_coders: true
---
node_class: Coder
memory_bounds: 512MB
tool_clearance:
  shell_access: 'restricted_sandboxed'
  network_access: 'blocked'
  allowed_binaries: ['python', 'git', 'sed', 'grep']
error_handling: 'Fallback_To_Reviewer_Audit'
---
node_class: Reviewer
role: 'Security & Debt Auditor'
output_target: 'docs/exec-plans/tech-debt-tracker-v2.md'
heuristics:
  - 'Check for AST drift'
  - 'Check for unhandled exceptions in newly generated .py files'
```

## Appendix D: Complete Data Graph Abstraction
The data graph is not text. Instead of passing massive READMEs to LLMs, we construct a condensed graph:
- `Entity(Project)` -> `Has_Rule(Lint_Python)`
- `Entity(ModuleX)` -> `Depends_On(ModuleY)`
By traversing this graph, the Orchestrator feeds only the localized neighborhood of context to the Coder.

## Appendix E: Token Truncation Algorithm
```python
def heuristic_truncate(context, cap=80000):
    if len(context) > cap:
        return prune_by_relevance(context, priority)
    return context
```
