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

"""Presentation layer acting as the CLI interface."""
__author__ = "LaVineLeo"
# https://github.com/LaVineLeo

import argparse
import sys
from pathlib import Path

from src_v2.core_v2.consts_v2 import TEMPLATES
from src_v2.infra_v2.fs_v2 import ensure_target_directory, copy_template
from src_v2.services_v2.scaffold_engine_v2 import replace_placeholders, template_root

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap the profile-driven LaVine-harness-skills scaffold into a target directory.",
    )
    parser.add_argument(
        "--template",
        default="monorepo",
        choices=TEMPLATES,
        help="Template to copy.",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Destination directory for the scaffold.",
    )
    parser.add_argument(
        "--project-name",
        required=True,
        help="Project name used for placeholder replacement.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting existing files in the target directory.",
    )
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    source = template_root(args.template)
    target = Path(args.target).expanduser().resolve()

    ensure_target_directory(target, args.overwrite)
    copied_files = copy_template(source, target, args.overwrite)
    updated_files = replace_placeholders(copied_files, args.project_name)

    print(f"Template: {args.template}")
    print(f"Target: {target}")
    print(f"Copied files: {len(copied_files)}")
    print(f"Text files updated: {updated_files}")
    return 0
