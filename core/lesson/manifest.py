"""
Lesson manifest helpers.
"""

from __future__ import annotations

from typing import Any

from .lesson import Lesson
from .migration import build_stages


def build_manifest(lesson: Lesson) -> dict[str, Any]:
    """
    Build a serializable lesson manifest.
    """

    stages = build_stages(lesson)

    return {
        "name": lesson.name,
        "title": lesson.title,
        "max_width": lesson.max_width,
        "max_height": lesson.max_height,
        "stages": [
            {
                "number": stage.number,
                "tasks": [
                    {
                        "id": task.id,
                        "title": task.title,
                        "asset": task.asset_ref.asset_id,
                        "answer": task.answer_spec.type,
                    }
                    for task in stage.tasks
                ],
            }
            for stage in stages
        ],
    }
