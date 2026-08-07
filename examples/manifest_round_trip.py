"""
Example: complete lesson manifest round-trip.
"""

from core.lesson.lesson import Lesson
from core.lesson.manifest import (
    build_lesson_from_manifest,
    build_manifest,
)
from core.lesson.serializer import (
    load_manifest,
    save_manifest,
)


def main() -> None:
    # ------------------------------------------------------------------
    # Create legacy lesson
    # ------------------------------------------------------------------

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

    print("Original lesson")
    print(lesson)

    print()

    # ------------------------------------------------------------------
    # Lesson -> Manifest
    # ------------------------------------------------------------------

    manifest = build_manifest(lesson)

    print("Manifest created")

    # ------------------------------------------------------------------
    # Manifest -> JSON
    # ------------------------------------------------------------------

    save_manifest(
        manifest,
        "lesson.json",
    )

    print("Manifest saved")

    # ------------------------------------------------------------------
    # JSON -> Manifest
    # ------------------------------------------------------------------

    restored_manifest = load_manifest(
        "lesson.json",
    )

    print("Manifest loaded")

    # ------------------------------------------------------------------
    # Manifest -> Lesson
    # ------------------------------------------------------------------

    restored_lesson = build_lesson_from_manifest(
        restored_manifest,
    )

    print("Lesson restored")

    print()

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    print("Validation")

    assert restored_lesson.name == lesson.name
    assert restored_lesson.title == lesson.title

    assert restored_lesson.ids == lesson.ids

    assert restored_lesson.max_width == lesson.max_width
    assert restored_lesson.max_height == lesson.max_height

    print("OK")


if __name__ == "__main__":
    main()
