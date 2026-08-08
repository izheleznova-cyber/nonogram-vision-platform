"""
Lesson browser.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

from client.teacher.designer import LessonDesigner


class LessonBrowser(QWidget):
    """
    Lesson browser.
    """

    def __init__(self) -> None:
        super().__init__()

        self.designer = LessonDesigner()

        layout = QVBoxLayout(self)

        layout.addWidget(
            self.designer
        )