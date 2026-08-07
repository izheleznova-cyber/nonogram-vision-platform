"""
Example: build a lesson manifest.
"""

from pprint import pprint

from core.lesson.lesson import Lesson
from core.lesson.manifest import build_manifest


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

    pprint(manifest)


if __name__ == "__main__":
    main()
