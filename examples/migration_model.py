"""
Example: migrate a legacy lesson.
"""

from core.lesson.lesson import Lesson
from core.lesson.migration import build_stages


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

    stages = build_stages(lesson)

    print(f"Lesson: {lesson.title}")

    print()

    for stage in stages:
        print(stage)

        for task in stage.tasks:
            print(" ", task.id, task.asset_ref.asset_id)


if __name__ == "__main__":
    main()
