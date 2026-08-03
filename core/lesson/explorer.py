"""
Lesson explorer.

Provides convenient access to lesson content.
"""

from __future__ import annotations

from core.dataset.passport_database import PassportDatabase
from core.dataset.passport_record import PassportRecord

from .lesson import Lesson


class LessonExplorer:
    """
    Provides access to lesson puzzles.
    """

    def __init__(
        self,
        database: PassportDatabase,
    ) -> None:

        self._database = database

    def passports(
        self,
        lesson: Lesson,
    ) -> list[PassportRecord]:
        """
        Return passports for all lesson puzzles.
        """

        result: list[PassportRecord] = []

        for puzzle_id in lesson.ids:

            result.append(
                self._database.record(
                    puzzle_id
                )
            )

        return result
