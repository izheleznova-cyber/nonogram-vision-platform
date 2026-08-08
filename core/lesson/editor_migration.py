"""
Migration between Lesson and EditorLesson.
"""

from __future__ import annotations

from .editor_model import EditorLesson
from .lesson import Lesson
from .migration import (
    build_lesson,
    build_stages,
)


def to_editor(
    lesson: Lesson,
) -> EditorLesson:
    """
    Convert Lesson into EditorLesson.
    """

    return EditorLesson(
        name=lesson.name,
        title=lesson.title,
        max_width=lesson.max_width,
        max_height=lesson.max_height,
        stages=build_stages(lesson),
    )


def to_lesson(
    lesson: EditorLesson,
) -> Lesson:
    """
    Convert EditorLesson into Lesson.
    """

    return build_lesson(
        name=lesson.name,
        title=lesson.title,
        stages=lesson.stages,
        max_width=lesson.max_width,
        max_height=lesson.max_height,
    )
