"""
Lesson model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Lesson:
    """
    One lesson description.

    A lesson contains only puzzle identifiers and
    basic metadata.

    It does not contain Puzzle objects.
    """

    name: str

    title: str

    ids: list[str]

    max_width: int

    max_height: int

    @property
    def count(self) -> int:
        """
        Number of puzzles.
        """
        return len(self.ids)