"""
Example: demo lesson stages.
"""

from core.lesson.answer_spec import AnswerSpec
from core.lesson.asset_ref import AssetRef
from core.lesson.stage import Stage
from core.lesson.task import Task


def build_demo_stages() -> list[Stage]:
    """
    Build demo stages for Lesson Designer.
    """

    return [
        Stage(
            number=1,
            puzzle_id="IMG000001",
            tasks=[
                Task(
                    id="solve",
                    title="Solve nonogram",
                    asset_ref=AssetRef(
                        asset_id="IMG000001",
                    ),
                    answer_spec=AnswerSpec(
                        type="NonogramSolution",
                    ),
                ),
            ],
        ),
        Stage(
            number=2,
            puzzle_id="IMG000002",
            tasks=[
                Task(
                    id="solve",
                    title="Solve nonogram",
                    asset_ref=AssetRef(
                        asset_id="IMG000002",
                    ),
                    answer_spec=AnswerSpec(
                        type="NonogramSolution",
                    ),
                ),
                Task(
                    id="check",
                    title="Check solution",
                    asset_ref=AssetRef(
                        asset_id="IMG000002",
                    ),
                    answer_spec=AnswerSpec(
                        type="CheckResult",
                    ),
                ),
            ],
        ),
        Stage(
            number=3,
            puzzle_id="IMG000003",
            tasks=[
                Task(
                    id="solve",
                    title="Solve nonogram",
                    asset_ref=AssetRef(
                        asset_id="IMG000003",
                    ),
                    answer_spec=AnswerSpec(
                        type="NonogramSolution",
                    ),
                ),
                Task(
                    id="hypothesis",
                    title="Describe image",
                    asset_ref=AssetRef(
                        asset_id="IMG000003",
                    ),
                    answer_spec=AnswerSpec(
                        type="Text",
                    ),
                ),
                Task(
                    id="reflection",
                    title="Explain hypothesis",
                    asset_ref=AssetRef(
                        asset_id="IMG000003",
                    ),
                    answer_spec=AnswerSpec(
                        type="Text",
                    ),
                ),
            ],
        ),
    ]


def main() -> None:
    stages = build_demo_stages()

    for stage in stages:
        print(f"Stage {stage.number}")

        for task in stage.tasks:
            print(f"  {task.id:12} {task.title}")

        print()


if __name__ == "__main__":
    main()
