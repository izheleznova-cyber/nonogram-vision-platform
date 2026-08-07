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

                        "asset_ref": {
                            "asset_id": task.asset_ref.asset_id,
                        },

                        "answer_spec": {
                            "type": task.answer_spec.type,
                        }, 
                    }
                    for task in stage.tasks
                ],
            }
            for stage in stages
        ],
    }


def build_lesson_from_manifest(
    manifest: Manifest,
) -> Lesson:
    """
    Build a Lesson from a lesson manifest.
    """

    ids: list[str] = []

    for stage in manifest["stages"]:
        for task in stage["tasks"]:
            ids.append(
                task["asset_ref"]["asset_id"]
            )

    return Lesson(
        name=manifest["name"],
        title=manifest["title"],
        ids=ids,
        max_width=manifest["max_width"],
        max_height=manifest["max_height"],
    )
