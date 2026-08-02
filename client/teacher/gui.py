"""
Main teacher window.
"""

from __future__ import annotations
from pathlib import Path

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
)


class TeacherGui(QWidget):
    """
    Main teacher application window.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Teacher GUI")

        self.resize(
            1000,
            700,
        )

        self._create_widgets()

        self._build_layout()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self.title = QLabel(
            "Teacher platform"
        )

        self.lesson_list = QListWidget()

        for lesson in self._find_lessons():

            self.lesson_list.addItem(
                lesson
            )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QVBoxLayout(self)

        layout.addWidget(self.title)

        content = QHBoxLayout()

        content.addWidget(
            self.lesson_list,
            stretch=1,
        )

        self.info = QLabel(
            "Select lesson"
        )

        content.addWidget(
            self.info,
            stretch=2,
        )

        layout.addLayout(content)

    def _find_lessons(self) -> list[str]:
        """
        Return available lesson directories.
        """

        lessons_dir = Path("../nonogram-dataset/lessons")

        if not lessons_dir.exists():
            return []

        lessons = []

        for path in sorted(lessons_dir.iterdir()):

            if path.is_dir():
                lessons.append(path.name)

        return lessons