"""
Example: round-trip lesson migration.
"""

from core.lesson.lesson import Lesson
from core.lesson.migration import build_lesson, build_stages


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
        max_height=50,
    )

    print("Original ids")
    print(lesson.ids)

    print()

    stages = build_stages(lesson)

    restored = build_lesson(
        name=lesson.name,
        title=lesson.title,
        stages=stages,
        max_width=lesson.max_width,
        max_height=lesson.max_height,
    )

    print("Restored ids")
    print(restored.ids)

    print()

    print("Migration OK:", lesson.ids == restored.ids)


if __name__ == "__main__":
    main()
