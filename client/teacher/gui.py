"""
Main teacher window.
"""

from __future__ import annotations
from pathlib import Path
from core.lesson.loader import load_lesson 

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class TeacherGui(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Teacher GUI")

        self.resize(
            1000,
            700,
        )

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

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

        self.info = QLabel(
            "Select lesson"
        )

        #
        # Buttons
        #

        self.open_button = QPushButton(
            "Open lesson"
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QVBoxLayout(self)

        layout.addWidget(
            self.title
        )

        content = QHBoxLayout()

        #
        # Left panel
        #

        left = QVBoxLayout()

        left.addWidget(
            self.lesson_list
        )

        left.addWidget(
            self.open_button
        )

        #
        # Right panel
        #

        right = QVBoxLayout()

        right.addWidget(
            self.info
        )

        content.addLayout(
            left,
            stretch=1,
        )

        content.addLayout(
            right,
            stretch=2,
        )

        layout.addLayout(content)

    def _connect_signals(self) -> None:
        """
        Connect widget signals.
        """

        self.lesson_list.currentTextChanged.connect(
            self._lesson_selected
        )

        self.open_button.clicked.connect(
            self._open_lesson
        )

    def _lesson_selected(
        self,
        lesson_name: str,
    ) -> None:

        if not lesson_name:
            return

        path = (
            Path("../nonogram-dataset/lessons")
            / lesson_name
        )

        lesson = load_lesson(path)

        self.info.setText(
            f"""Name:
    {lesson.name}

    Title:
    {lesson.title}

    Puzzles:
    {lesson.count}

    Maximum size:
    {lesson.max_width} × {lesson.max_height}
    """
        )


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

    def _open_lesson(self) -> None:
        """
        Open selected lesson.
        """

        item = self.lesson_list.currentItem()

        if item is None:
            return

        lesson_name = item.text()

        path = (
            Path("../nonogram-dataset/lessons")
            / lesson_name
        )

        lesson = load_lesson(path)

        print()

        print("=" * 60)
        print("OPEN LESSON")
        print("=" * 60)

        print(f"Name       : {lesson.name}")
        print(f"Title      : {lesson.title}")
        print(f"Puzzles    : {lesson.count}")
        print(f"Max width  : {lesson.max_width}")
        print(f"Max height : {lesson.max_height}")