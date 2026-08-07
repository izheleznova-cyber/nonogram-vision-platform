"""
Example: create lesson stages.
"""

from core.lesson.answer_spec import AnswerSpec
from core.lesson.asset_ref import AssetRef
from core.lesson.stage import Stage
from core.lesson.task import Task


def main() -> None:
    print("Old stage")

    stage_old = Stage(
        number=1,
        puzzle_id="IMG000123",
    )

    print(stage_old)

    print()

    print("New stage")

    task = Task(
        id="solve",
        title="Solve nonogram",
        asset_ref=AssetRef(
            asset_id="IMG000123",
        ),
        answer_spec=AnswerSpec(
            type="NonogramSolution",
        ),
    )

    stage_new = Stage(
        number=1,
        puzzle_id="IMG000123",
        tasks=[task],
    )

    print(stage_new)

    print()

    print("Tasks")

    for task in stage_new.tasks:
        print(f"{task.id:10} {task.title}")


if __name__ == "__main__":
    main()