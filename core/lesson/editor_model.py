"""
Editable lesson model.

Used by Lesson Designer.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .stage import Stage


@dataclass(slots=True)
class EditorLesson:
    """
    Editable lesson.

    Unlike the legacy Lesson, this model stores
    Stage objects directly.
    """

    name: str

    title: str

    max_width: int

    max_height: int

    stages: list[Stage] = field(
        default_factory=list,
    )
