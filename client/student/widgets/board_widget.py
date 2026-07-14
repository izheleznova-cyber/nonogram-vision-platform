"""
Interactive board widget.

Current version:
    Displays rendered PNG.

Future:
    - Draw Puzzle using QPainter
    - Mouse interaction
    - Zoom
    - Selection
"""

from __future__ import annotations

from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QPixmap,
    QResizeEvent,
    QMouseEvent,
)
from PyQt6.QtWidgets import QLabel

from core.puzzle.model import Puzzle
from core.puzzle.player import PlayerBoard


class BoardWidget(QLabel):
    """
    Puzzle board widget.

    Stage 1
        Display rendered PNG.

    Stage 2
        Draw Puzzle directly.

    Stage 3
        Interactive solving.
    """

    def __init__(self):

        super().__init__()

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setMinimumSize(
            900,
            600,
        )

        self.setScaledContents(False)

        #
        # Current puzzle.
        #
        self._puzzle: Puzzle | None = None

        #
        # Current player board.
        #
        self._player: PlayerBoard | None = None

        #
        # Temporary rendered image.
        #
        self._pixmap: QPixmap | None = None

        #
        # Future selection.
        #
        self.current_row: int | None = None
        self.current_col: int | None = None

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_puzzle(
        self,
        puzzle: Puzzle,
    ) -> None:
        """
        Set current puzzle.
        """

        self._puzzle = puzzle

        self.update()

    def set_player(
        self,
        player: PlayerBoard,
    ) -> None:
        """
        Set current player board.
        """

        self._player = player

        self.update()

    def load_image(
        self,
        image: Path,
    ) -> None:
        """
        Load rendered PNG.

        Temporary until QPainter renderer
        is implemented.
        """

        self._pixmap = QPixmap(
            str(image)
        )

        self._update_pixmap()

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _update_pixmap(
        self,
    ) -> None:

        if self._pixmap is None:
            return

        scaled = self._pixmap.scaled(

            self.size(),

            Qt.AspectRatioMode.KeepAspectRatio,

            Qt.TransformationMode.SmoothTransformation,

        )

        self.setPixmap(
            scaled
        )

    # ---------------------------------------------------------
    # Qt Events
    # ---------------------------------------------------------

    def resizeEvent(
        self,
        event: QResizeEvent,
    ) -> None:

        super().resizeEvent(event)

        self._update_pixmap()

    def mousePressEvent(
        self,
        event: QMouseEvent,
    ) -> None:
        """
        Future:
            cell selection.
        """

        super().mousePressEvent(event)

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self) -> None:
        """
        Refresh board.
        """

        self.update()
