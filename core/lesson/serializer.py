"""
Lesson serializer.
"""

from __future__ import annotations

import json
from pathlib import Path

from .lesson import Lesson


def save_lesson(
    lesson: Lesson,
    path: str | Path,
) -> None:
    """
    Save lesson into a directory.
    """

    path = Path(path)

    #
    # Create directory if necessary.
    #

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    #
    # manifest.json
    #

    manifest = {
        "name": lesson.name,
        "title": lesson.title,
        "count": lesson.count,
        "max_width": lesson.max_width,
        "max_height": lesson.max_height,
    }

    (path / "manifest.json").write_text(
        json.dumps(
            manifest,
            indent=4,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    #
    # ids.txt
    #

    (path / "ids.txt").write_text(
        "\n".join(lesson.ids) + "\n",
        encoding="utf-8",
    )
