from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Prediction:
    """
    Student hypothesis about the puzzle.
    """

    timestamp: float

    progress: float

    text: str