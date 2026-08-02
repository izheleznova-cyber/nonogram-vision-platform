"""
Main teacher window.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
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

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            10,
            10,
            10,
            10,
        )

        layout.setSpacing(8)

        layout.addWidget(
            self.title
        )