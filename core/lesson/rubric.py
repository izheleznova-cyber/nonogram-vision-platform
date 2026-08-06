"""
Lesson assessment rubric.
"""

from __future__ import annotations

from dataclasses import dataclass

from .criterion import Criterion


@dataclass(slots=True)
class Rubric:
    """
    Lesson assessment rules.
    """

    criteria: list[Criterion]