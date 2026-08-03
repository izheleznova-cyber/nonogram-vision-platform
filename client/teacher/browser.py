"""
Lesson browser.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class LessonBrowser(QWidget):
    """
    Lesson browser.
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Lesson Browser")
        )