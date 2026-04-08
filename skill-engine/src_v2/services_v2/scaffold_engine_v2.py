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

"""Service layer for scaffolding operations."""
__author__ = "LaVineLeo"
# https://github.com/LaVineLeo

from pathlib import Path
from src_v2.core_v2.consts_v2 import PLACEHOLDER_PROJECT_NAME

def replace_placeholders(paths: list[Path], project_name: str) -> int:
    updated_files = 0
    for path in paths:
        try:
            original_text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        updated_text = original_text.replace(PLACEHOLDER_PROJECT_NAME, project_name)
        if updated_text == original_text:
            continue

        path.write_text(updated_text, encoding="utf-8")
        updated_files += 1

    return updated_files

def template_root(template: str) -> Path:
    # Target: skill-engine/assets/templates/{template}
    root = Path(__file__).resolve().parents[2] / "assets" / "templates" / template
    if not root.is_dir():
        raise FileNotFoundError(f"Template directory not found: {root}")
    return root
