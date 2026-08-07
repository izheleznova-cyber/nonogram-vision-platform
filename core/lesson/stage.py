"""
Lesson stage.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .task import Task


@dataclass(slots=True)
class Stage:
    """
    One lesson stage.

    Stage is backward compatible with the current Lesson Builder.

    Existing code may continue using ``puzzle_id``.

    New Lesson Designer should populate ``tasks``.
    """

    number: int

    puzzle_id: str

    tasks: list[Task] = field(default_factory=list)