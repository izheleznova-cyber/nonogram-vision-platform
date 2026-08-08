"""
EditorLesson loader.
"""

from __future__ import annotations

from .answer_spec import AnswerSpec
from .asset_ref import AssetRef
from .editor_model import EditorLesson
from .stage import Stage
from .task import Task


def build_editor_lesson(
    manifest: dict,
) -> EditorLesson:
    """
    Build EditorLesson from manifest.
    """

    stages: list[Stage] = []

    for stage_data in manifest["stages"]:

        tasks: list[Task] = []

        for task_data in stage_data["tasks"]:

            tasks.append(
                Task(
                    id=task_data["id"],
                    title=task_data["title"],

                    asset_ref=AssetRef(
                        asset_id=task_data["asset_ref"]["asset_id"],
                    ),

                    answer_spec=AnswerSpec(
                        type=task_data["answer_spec"]["type"],
                    ),
                )
            )

        stages.append(
            Stage(
                number=stage_data["number"],
                puzzle_id="",
                tasks=tasks,
            )
        )

    return EditorLesson(
        name=manifest["name"],
        title=manifest["title"],
        max_width=manifest["max_width"],
        max_height=manifest["max_height"],
        stages=stages,
    )
