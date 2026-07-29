"""
Lesson loader.
"""

from __future__ import annotations

import json
from pathlib import Path

from core.dataset.lesson import Lesson


def load_lesson(
    lesson_dir: Path,
) -> Lesson:
    """
    Load lesson from directory.

    Directory structure:

        lesson/
            ids.txt
            manifest.json
    """

    manifest_path = lesson_dir / "manifest.json"
    ids_path = lesson_dir / "ids.txt"

    if not manifest_path.exists():
        raise FileNotFoundError(manifest_path)

    if not ids_path.exists():
        raise FileNotFoundError(ids_path)

    with manifest_path.open(
        "r",
        encoding="utf-8",
    ) as file:

        manifest = json.load(file)

    lesson = Lesson(
        name=manifest["name"],
    )

    with ids_path.open(
        "r",
        encoding="utf-8",
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            lesson.puzzle_ids.append(line)

    return lesson
