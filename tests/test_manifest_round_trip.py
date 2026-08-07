"""
Test lesson manifest round-trip.
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


def test_manifest_round_trip(tmp_path) -> None:
    """
    Verify that a lesson survives the complete
    Lesson -> Manifest -> JSON -> Manifest -> Lesson
    round-trip without losing information.
    """

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

    # ----------------------------------------------------------
    # Lesson -> Manifest
    # ----------------------------------------------------------

    manifest = build_manifest(lesson)

    # ----------------------------------------------------------
    # Manifest -> JSON
    # ----------------------------------------------------------

    filename = tmp_path / "lesson.json"

    save_manifest(
        manifest,
        filename,
    )

    # ----------------------------------------------------------
    # JSON -> Manifest
    # ----------------------------------------------------------

    restored_manifest = load_manifest(
        filename,
    )

    # ----------------------------------------------------------
    # Manifest -> Lesson
    # ----------------------------------------------------------

    restored = build_lesson_from_manifest(
        restored_manifest,
    )

    # ----------------------------------------------------------
    # Validation
    # ----------------------------------------------------------

    assert restored.name == lesson.name
    assert restored.title == lesson.title

    assert restored.max_width == lesson.max_width
    assert restored.max_height == lesson.max_height

    assert restored.ids == lesson.ids

    assert len(restored.ids) == 3
