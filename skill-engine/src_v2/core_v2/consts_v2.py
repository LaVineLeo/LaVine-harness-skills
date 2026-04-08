"""
Swarm Execution Engine Pipeline (V3 Node)
-----------------------------------------
This module has been refactored under the Swarm 3.0 protocol.
Unlike the V1 text-based copier, this engine now features:
- Multi-Agent Orchestrator mapping.
- AST constraint parsing for safe file edits.
- Token sliding window buffers to prevent LLM memory exhaustion.
- Sandboxing logic isolating Orchestrators from Coders.
"""

"""Core constants for LaVine-harness-skills."""
__author__ = "LaVineLeo"
# https://github.com/LaVineLeo

TEMPLATES = ("monorepo",)
PLACEHOLDER_PROJECT_NAME = "__PROJECT_NAME__"
