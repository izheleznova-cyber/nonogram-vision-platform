"""
Expected answer specification.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AnswerSpec:
    """
    Describes the expected answer type.

    Concrete answer specifications will extend this model.
    """

    type: str

