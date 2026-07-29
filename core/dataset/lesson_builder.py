"""
lesson_builder.py

Build lesson folders from passport records.
"""

from __future__ import annotations

import json
from pathlib import Path

from core.dataset.lesson import Lesson
from core.dataset.passport_record import PassportRecord


def build_lesson(
    *,
    records: list[PassportRecord],
    lesson_dir: Path,
    name: str,
    title: str,
    max_width: int,
    max_height: int,
) -> Lesson:
    """
    Build lesson from passport records.

    Parameters
    ----------
    records
        Passport records.

    lesson_dir
        Target lesson directory.

    name
        Lesson identifier.

    title
        Human readable lesson title.

    max_width
        Maximum puzzle width.

    max_height
        Maximum puzzle height.
    """

    lesson = Lesson(name=name)

    selected: list[PassportRecord] = []

    for record in records:

        if (
            record.width <= max_width
            and record.height <= max_height
        ):
            selected.append(record)
            lesson.puzzle_ids.append(record.id)

    selected.sort(
        key=lambda record: (
            record.width,
            record.height,
            record.id,
        )
    )

    lesson_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    save_ids(
        lesson_dir,
        selected,
    )

    save_manifest(
        lesson_dir,
        name=name,
        title=title,
        count=len(selected),
        max_width=max_width,
        max_height=max_height,
    )

    print(f"Lesson: {name}")
    print(f"Puzzles: {len(selected)}")
    return lesson


def save_ids(
    lesson_dir: Path,
    records: list[PassportRecord],
) -> None:
    """
    Save ids.txt
    """

    ids_path = lesson_dir / "ids.txt"

    with ids_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        for record in records:
            file.write(f"{record.id}\n")


def save_manifest(
    lesson_dir: Path,
    *,
    name: str,
    title: str,
    count: int,
    max_width: int,
    max_height: int,
) -> None:
    """
    Save manifest.json
    """

    manifest = {
        "name": name,
        "title": title,
        "count": count,
        "max_width": max_width,
        "max_height": max_height,
    }

    manifest_path = lesson_dir / "manifest.json"

    with manifest_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            manifest,
            file,
            indent=4,
            ensure_ascii=False,
        )
