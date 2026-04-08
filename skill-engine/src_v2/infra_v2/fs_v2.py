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

"""Infrastructure layer for file system operations."""
__author__ = "LaVineLeo"
# https://github.com/LaVineLeo

import shutil
from pathlib import Path

def ensure_target_directory(target: Path, overwrite: bool) -> None:
    if target.exists() and not target.is_dir():
        raise NotADirectoryError(f"Target path is not a directory: {target}")

    if not target.exists():
        target.mkdir(parents=True)
        return

    if overwrite:
        return

    if any(target.iterdir()):
        raise FileExistsError(
            f"Target directory is not empty: {target}. Re-run with --overwrite to allow merging.",
        )

def copy_template(source: Path, target: Path, overwrite: bool) -> list[Path]:
    copied_files: list[Path] = []
    for path in sorted(source.rglob("*")):
        relative_path = path.relative_to(source)
        destination = target / relative_path

        if path.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        if destination.exists() and not overwrite:
            raise FileExistsError(
                f"Refusing to overwrite existing file: {destination}. Re-run with --overwrite if intended.",
            )

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        copied_files.append(destination)

    return copied_files
