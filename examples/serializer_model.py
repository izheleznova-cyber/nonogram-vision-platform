"""
Example: save and load a lesson manifest.
"""

from pprint import pprint

from core.lesson.lesson import Lesson
from core.lesson.manifest import build_manifest
from core.lesson.serializer import (
    load_manifest,
    save_manifest,
)


def main() -> None:
    lesson = Lesson(
        name="lesson01",
        title="Aircraft",
        ids=[
            "IMG000001",
            "IMG000002",
            "IMG000003",
        ],
        max_width=50,
        max_height=42,
    )

    manifest = build_manifest(lesson)

    save_manifest(
        manifest,
        "lesson.json",
    )

    restored = load_manifest(
        "lesson.json",
    )

    pprint(restored)

    print()

    print("Validation")

    assert restored["name"] == lesson.name
    assert restored["title"] == lesson.title
    assert restored["max_width"] == lesson.max_width
    assert restored["max_height"] == lesson.max_height

    assert len(restored["stages"]) == 3

    assert (
        restored["stages"][0]["tasks"][0]["asset_ref"]["asset_id"]
        == "IMG000001"
    )

    assert (
        restored["stages"][0]["tasks"][0]["answer_spec"]["type"]
        == "NonogramSolution"
    )

    print("OK")



if __name__ == "__main__":
    main()
