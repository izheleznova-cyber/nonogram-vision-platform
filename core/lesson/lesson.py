"""
Lesson model.
"""

from dataclasses import dataclass

from core.dataset.passport_record import PassportRecord


@dataclass(slots=True)
class Lesson:
    """
    Lesson description.
    """

    name: str

    title: str

    ids: list[str]

    max_width: int

    max_height: int

    @property
    def count(self) -> int:
        return len(self.ids)


@dataclass(slots=True)
class LessonItem:
    """
    One puzzle inside a lesson.
    """

    number: int

    passport: PassportRecord