"""
Migration helpers for lesson models.
"""

from __future__ import annotations

from .answer_spec import AnswerSpec
from .asset_ref import AssetRef
from .lesson import Lesson
from .stage import Stage
from .task import Task


def build_stages(lesson: Lesson) -> list[Stage]:
    """
    Build Stage objects from a legacy Lesson.
    """

    stages: list[Stage] = []

    for number, puzzle_id in enumerate(lesson.ids, start=1):
        task = Task(
            id=f"solve_{number}",
            title="Solve nonogram",
            asset_ref=AssetRef(asset_id=puzzle_id),
            answer_spec=AnswerSpec(type="NonogramSolution"),
        )

        stages.append(
            Stage(
                number=number,
                puzzle_id=puzzle_id,
                tasks=[task],
            )
        )

    return stages


def build_lesson(
    name: str,
    title: str,
    stages: list[Stage],
    max_width: int,
    max_height: int,
) -> Lesson:
    """
    Build a legacy Lesson from Stage objects.
    """

    ids = [
        stage.puzzle_id
        for stage in sorted(stages, key=lambda s: s.number)
    ]

    return Lesson(
        name=name,
        title=title,
        ids=ids,
        max_width=max_width,
        max_height=max_height,
    )