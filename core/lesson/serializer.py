"""
Lesson manifest serializer.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .manifest_types import Manifest


def save_manifest(
    manifest: Manifest,
    filename: str | Path,
) -> None:
    """
    Save lesson manifest to JSON.
    """

    path = Path(filename)

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            manifest,
            file,
            indent=4,
            ensure_ascii=False,
        )


def load_manifest(
    filename: str | Path,
) -> Manifest:
    """
    Load lesson manifest from JSON.
    """

    path = Path(filename)

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)