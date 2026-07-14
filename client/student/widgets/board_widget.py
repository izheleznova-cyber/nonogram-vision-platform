"""
Interactive board widget.

Step 1:
Draw empty grid using QPainter.
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QColor,
    QPainter,
    QPen,
)
from PyQt6.QtWidgets import QWidget


class BoardWidget(QWidget):
    """
    Interactive puzzle board.

    First version:
    only draws an empty grid.
    """

    CELL_SIZE = 20

    GRID_WIDTH = 50
    GRID_HEIGHT = 42

    LEFT_MARGIN = 120
    TOP_MARGIN = 120

    def __init__(self):

        super().__init__()

        #
        # Current puzzle
        #
        self._puzzle = None

        #
        # Current player board
        #
        self._player = None

        self.setMinimumSize(
            900,
            700,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # Temporary compatibility
    # ---------------------------------------------------------

    def load_image(
        self,
        image,
    ) -> None:
        """
        Temporary stub.

        Needed so existing examples
        continue to run.
        """
        self.update()

    def set_puzzle(
        self,
        puzzle,
    ) -> None:
        """
        Set current puzzle.
        """

        self._puzzle = puzzle

        self.update()

    def set_player(
        self,
        player,
    ) -> None:
        """
        Set current player board.
        """

        self._player = player

        self.update()

    def refresh(
        self,
    ) -> None:
        """
        Refresh board.
        """

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

        self._draw_grid(painter)

    # ---------------------------------------------------------
    # Grid
    # ---------------------------------------------------------

    def _draw_grid(
        self,
        painter: QPainter,
    ) -> None:

        thin_pen = QPen(
            QColor(190, 190, 190)
        )
        thin_pen.setWidth(1)

        thick_pen = QPen(
            Qt.GlobalColor.black
        )
        thick_pen.setWidth(2)

        #
        # Vertical lines
        #

        for col in range(self.GRID_WIDTH + 1):

            x = (
                self.LEFT_MARGIN
                + col * self.CELL_SIZE
            )

            if col % 5 == 0:
                painter.setPen(thick_pen)
            else:
                painter.setPen(thin_pen)

            painter.drawLine(
                x,
                self.TOP_MARGIN,
                x,
                self.TOP_MARGIN
                + self.GRID_HEIGHT * self.CELL_SIZE,
            )

        #
        # Horizontal lines
        #

        for row in range(self.GRID_HEIGHT + 1):

            y = (
                self.TOP_MARGIN
                + row * self.CELL_SIZE
            )

            if row % 5 == 0:
                painter.setPen(thick_pen)
            else:
                painter.setPen(thin_pen)

            painter.drawLine(
                self.LEFT_MARGIN,
                y,
                self.LEFT_MARGIN
                + self.GRID_WIDTH * self.CELL_SIZE,
                y,
            )
