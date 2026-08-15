"""Render a role announcement from a public-safe workflow configuration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = {
    "project_id",
    "project_title",
    "application_deadline",
    "engagement_start",
    "engagement_end",
    "open_positions",
    "decision_owner_role",
}


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        config = json.load(handle)
    missing = sorted(REQUIRED_FIELDS - config.keys())
    if missing:
        raise ValueError(f"Missing required configuration fields: {', '.join(missing)}")
    if config["automation"].get("human_approval_required") is not True:
        raise ValueError("human_approval_required must remain true")
    return config


def render(config: dict, responsibilities: str, criteria: str) -> str:
    return f"""# Research team opportunity

**Project:** {config['project_title']}
**Period:** {config['engagement_start']} to {config['engagement_end']}
**Application deadline:** {config['application_deadline']}
**Open positions:** {config['open_positions']}

## Responsibilities

{responsibilities}

## Selection criteria

{criteria}

Applications are reviewed by accountable human decision-makers. Automated tools may assist with administrative organization and evidence summarization but do not make final employment decisions.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--responsibilities", required=True)
    parser.add_argument("--criteria", required=True)
    args = parser.parse_args()
    print(render(load_config(args.config), args.responsibilities, args.criteria))


if __name__ == "__main__":
    main()
