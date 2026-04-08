# Skill Engine Actuation Protocol

## Orchestrator Actuation
Reads the Machine-Readable YAML from the Project Profile and instantiates the multi-agent nodes.

## Sandbox & Security
The Skill engine no longer copies files blindly. It calculates an AST delta, establishes a read/write constraint ring, and generates an ephemeral sandbox-policy.json.

## Memory Management
Truncates conversation buffers via context sliding windows if tokens exceed 80% boundary.
