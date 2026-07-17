"""
Main student window.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
)

from .widgets.toolbar import Toolbar
from .widgets.board_widget import BoardWidget
from .widgets.prediction_panel import PredictionPanel
from .widgets.status_panel import StatusPanel
from core.game.session import GameSession


class StudentGui(QWidget):
    """
    Main student window.
    """

    def __init__(self) -> None:
        super().__init__()
        self.session: GameSession | None = None

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

        #
        # Scroll area
        #

        self.board_scroll = QScrollArea()

        self.board_scroll.setWidget(
            self.board
        )

        self.board_scroll.setWidgetResizable(
            False
        )

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
            self.board_scroll,
            stretch=1,
        )

        #
        # Prediction panel
        #
        layout.addWidget(
            self.prediction,
        )

        #
        # Status 
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
        """

        self.toolbar.check_button.clicked.connect(
            self._check_solution
        )

        #
        # Zoom
        #

        self.toolbar.zoom_in_button.clicked.connect(
            self.board.zoom_in
        )

        self.toolbar.zoom_out_button.clicked.connect(
            self.board.zoom_out
        )

        self.prediction.save_button.clicked.connect(
            self._save_prediction
        )

        


    def set_session(
        self,
        session: GameSession,
    ) -> None:
        """
        Connect GameSession.
        """

        self.session = session

        self.board.set_session(session)

    def _check_solution(
        self,
    ) -> None:

        if self.session is None:
            return

        result = self.session.check()

        self.board.set_errors(
            result.incorrect_cells
        )

    def _save_prediction(self) -> None:
        """
        Save current hypothesis.
        """
        print("Save button pressed")

        if self.session is None:
            return

        text = self.prediction.editor.toPlainText().strip()

        if not text:
            return

        self.session.add_prediction(text)

        self.prediction.editor.clear()

        print(
            self.session.predictions[-1]
        )

