"""
Lesson monitor.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class LessonMonitor(QWidget):
    """
    Lesson monitor.
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Lesson Monitor")
        )