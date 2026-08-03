"""
Main teacher application.

Entry point for the teacher platform.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .builder import LessonBuilder
from .browser import LessonBrowser
from .monitor import LessonMonitor


class TeacherGui(QWidget):
    """
    Main teacher window.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(
            "Teacher platform"
        )

        self.resize(
            500,
            300,
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

        self.build_button = QPushButton(
            "Build lesson"
        )

        self.browser_button = QPushButton(
            "Lesson Designer"
        )

        self.monitor_button = QPushButton(
            "Monitor"
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QVBoxLayout(self)

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.build_button
        )

        layout.addWidget(
            self.browser_button
        )

        layout.addWidget(
            self.monitor_button
        )

        layout.addStretch()

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:

        self.build_button.clicked.connect(
            self._build_lesson
        )

        self.browser_button.clicked.connect(
            self._show_lessons
        )

        self.monitor_button.clicked.connect(
            self._show_monitor
        )

    # ---------------------------------------------------------
    # Slots
    # ---------------------------------------------------------

    def _build_lesson(self) -> None:

        self.builder = LessonBuilder()

        self.builder.show()

    def _show_lessons(self) -> None:

        self.browser = LessonBrowser()

        self.browser.show()

    def _show_monitor(self) -> None:

        self.monitor = LessonMonitor()

        self.monitor.show()