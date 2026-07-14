"""
Main student window.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from .widgets.toolbar import Toolbar
from .widgets.board_widget import BoardWidget
from .widgets.prediction_panel import PredictionPanel
from .widgets.status_panel import StatusPanel


class StudentGui(QWidget):
    """
    Main student window.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Student GUI")

        self.resize(
            1200,
            900,
        )

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self.toolbar = Toolbar()

        self.board = BoardWidget()

        self.prediction = PredictionPanel()

        self.status = StatusPanel()

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

        #
        # Toolbar
        #
        layout.addWidget(
            self.toolbar,
        )

        #
        # Puzzle image
        #
        layout.addWidget(
            self.board,
            stretch=1,
        )

        #
        # Prediction panel
        #
        layout.addWidget(
            self.prediction,
        )

        #
        # Status line
        #
        layout.addWidget(
            self.status,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:
        """
        Connect widget signals.

        GameSession will be connected later.
        """
        pass
