"""
Example: create a lesson task.
"""

from core.lesson.answer_spec import AnswerSpec
from core.lesson.asset_ref import AssetRef
from core.lesson.task import Task

from dataclasses import FrozenInstanceError



def main() -> None:
    asset = AssetRef(
        asset_id="IMG000005",
    )

    answer = AnswerSpec(
        type="NonogramSolution",
    )

    task = Task(
        id="task_001",
        title="Solve nonogram",
        asset_ref=asset,
        answer_spec=answer,
    )

    print("Task")
    print(task)

    print()

    print("Fields")
    print(f"id          : {task.id}")
    print(f"title       : {task.title}")
    print(f"asset id    : {task.asset_ref.asset_id}")
    print(f"answer type : {task.answer_spec.type}")

    print()
    print("Frozen check")

    try:
        asset.asset_id = "IMG000123"
    except FrozenInstanceError as e:
        print(f"OK: {e}")


if __name__ == "__main__":
    main()