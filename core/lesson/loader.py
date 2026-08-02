"""
Lesson loader.
"""

from __future__ import annotations

import json
from pathlib import Path

from .lesson import Lesson

def load_lesson(path: str | Path) -> Lesson:
    """
    Load lesson from directory.
    """

    path = Path(path)

    #
    # manifest.json
    #

    manifest = json.loads(
        (path / "manifest.json").read_text(
            encoding="utf-8"
        )
    )

    #
    # ids.txt
    #

    ids = (
        path / "ids.txt"
    ).read_text(
        encoding="utf-8"
    ).splitlines()

    ids = [
        value.strip()
        for value in ids
        if value.strip()
    ]

    return Lesson(
        name=manifest["name"],
        title=manifest["title"],
        ids=ids,
        max_width=manifest["max_width"],
        max_height=manifest["max_height"],
    )