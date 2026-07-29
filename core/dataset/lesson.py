"""
Lesson description.

A lesson is a collection of puzzle IDs prepared
by the teacher for one class.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Lesson:
    """
    Collection of puzzles for one lesson.
    """

    name: str

    puzzle_ids: list[str] = field(default_factory=list)
