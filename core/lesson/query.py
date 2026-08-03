"""
Lesson search query.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LessonQuery:
    """
    Search parameters for lesson builder.
    """

    #
    # Geometry
    #

    max_width: int | None = None
    max_height: int | None = None

    #
    # Classification
    #

    category: str | None = None
    subcategory: str | None = None

    #
    # Difficulty
    #

    difficulty: int | None = None

    #
    # Recognition
    #

    recognition_level: str | None = None

    #
    # Appearance
    #

    color: str | None = None
    has_face: bool | None = None

    #
    # Source
    #

    source: str | None = None
