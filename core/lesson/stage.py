"""
Lesson stage.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Stage:
    """
    One lesson stage.

    References one puzzle.
    """

    number: int

    puzzle_id: str
