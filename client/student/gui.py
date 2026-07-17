"""
Main student window.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
)

from .widgets.toolbar import Toolbar
from .widgets.board_widget import BoardWidget
from .widgets.prediction_panel import PredictionPanel
from .widgets.status_panel import StatusPanel
from core.game.session import GameSession
from .widgets.preview_widget import PreviewWidget


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

        from PyQt6.QtCore import QTimer
        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self._update_status
        )

        self.timer.start(1000)

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self.toolbar = Toolbar()

        self.board = BoardWidget()

        self.preview = PreviewWidget()
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
        # Puzzle + Preview
        #

        board_layout = QHBoxLayout()

        board_layout.setSpacing(10)

        board_layout.addWidget(
            self.board_scroll,
            stretch=1,
        )

        board_layout.addWidget(
            self.preview,
        )

        layout.addLayout(
            board_layout,
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

        self.session = session

        self.board.set_session(session)

        self.preview.set_session(session)

        self.status.set_checks(
            0,
            session.max_checks(),
        )

    def _check_solution(
        self,
    ) -> None:

        if self.session is None:
            return

        result = self.session.check()

        self.board.set_errors(
            result.incorrect_cells
        )

        self.status.set_checks(
            self.session.check_count,
            self.session.max_checks(),
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

    def _update_status(self) -> None:

        if self.session is None:
            return

        self.status.set_time(
            self.session.elapsed_seconds()
        )

        self.status.set_progress(
            self.session.progress()
        )

    def progress(self) -> float:

        total = 0
        correct = 0

        for row in range(self.puzzle.height):
            for col in range(self.puzzle.width):

                if self.puzzle.matrix[row][col]:

                    total += 1

                    if self.board.state(row, col) == FILLED:
                        correct += 1

        if total == 0:
            return 0.0

        return correct / total

