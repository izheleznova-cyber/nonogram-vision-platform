"""
Lesson assessment criterion.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Criterion:
    """
    One assessment criterion.
    """

    id: str
    title: str
    weight: float