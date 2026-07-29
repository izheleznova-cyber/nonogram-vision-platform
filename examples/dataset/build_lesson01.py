"""
Build lesson01_build.

Create lesson01_build from all puzzles
with size <= 10x10.
"""

from __future__ import annotations

import json

from core.dataset.passport_reader import read_passports
from core.dataset.paths import DATASET_ROOT
from core.dataset.paths import WORKBOOK


LESSON_NAME = "lesson01_build"

MAX_WIDTH = 10
MAX_HEIGHT = 10


def save_ids(lesson_dir, records) -> None:
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


def save_manifest(lesson_dir, records) -> None:
    """
    Save manifest.json
    """

    manifest = {
        "name": LESSON_NAME,
        "title": "Первые шаги",
        "count": len(records),
        "max_width": MAX_WIDTH,
        "max_height": MAX_HEIGHT,
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


def main() -> None:

    records = read_passports(WORKBOOK)

    selected = []

    for record in records:

        if (
            record.width <= MAX_WIDTH
            and record.height <= MAX_HEIGHT
        ):
            selected.append(record)

    selected.sort(
        key=lambda r: (
            r.width,
            r.height,
            r.id,
        )
    )

    lesson_dir = (
        DATASET_ROOT
        / "lessons"
        / LESSON_NAME
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
        selected,
    )

    print("=" * 60)
    print(LESSON_NAME)
    print("=" * 60)
    print()

    print(f"Puzzles: {len(selected)}")
    print()

    for record in selected:

        print(
            f"{record.id:10s} "
            f"{record.width:2d}x{record.height:<2d}  "
            f"{record.category:12s} "
            f"{record.title}"
        )

    print()
    print("Done.")


if __name__ == "__main__":
    main()