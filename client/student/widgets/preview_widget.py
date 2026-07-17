"""
Mini preview of current puzzle state.
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QColor,
    QPainter,
)
from PyQt6.QtWidgets import QWidget

from core.game.session import GameSession
from core.puzzle.player import (
    EMPTY,
    FILLED,
    CROSSED,
)


class PreviewWidget(QWidget):
    """
    Small preview of the current
    player board.
    """
    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.session: GameSession | None = None

        # self.setFixedWidth(220)
        self.setMinimumSize(
            220,
            220,
        )
    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_session(
        self,
        session: GameSession,
    ) -> None:

        self.session = session

        self.update()

    # ---------------------------------------------------------
    # Painting
    # ---------------------------------------------------------

    def paintEvent(
        self,
        event,
    ) -> None:

        painter = QPainter(self)

        painter.fillRect(
            self.rect(),
            Qt.GlobalColor.white,
        )

        if self.session is None:
            return

        board = self.session.board

        margin = 10

        cell = min(
            (self.width() - 2 * margin) // board.width,
            (self.height() - 2 * margin) // board.height,
        )

        cell = max(cell, 2)
    
        for row in range(board.height):

            for col in range(board.width):

                state = board.state(
                    row,
                    col,
                )

                x = margin + col * cell
                y = margin + row * cell

                if state == FILLED:

                    painter.fillRect(
                        x,
                        y,
                        cell,
                        cell,
                        Qt.GlobalColor.black,
                    )

                elif state == CROSSED:

                    painter.fillRect(
                        x,
                        y,
                        cell,
                        cell,
                        QColor(210, 210, 210),
                    )

                else:

                    painter.fillRect(
                        x,
                        y,
                        cell,
                        cell,
                        Qt.GlobalColor.white,
                    )
