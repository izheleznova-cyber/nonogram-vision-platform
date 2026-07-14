"""
Student board widget.

Displays the current puzzle.
Currently shows a rendered PNG.

Later this widget will draw the puzzle
directly using QPainter.
"""

from __future__ import annotations

from pathlib import Path

from PyQt6.QtCore import Qt

from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import (
    QLabel,
    QSizePolicy,
)


class BoardWidget(QLabel):
    """
    Puzzle board widget.

    Current version:
        Displays rendered PNG.

    Future version:
        Draws puzzle directly from
        Puzzle + PlayerBoard.
    """

    def __init__(self):

        super().__init__()

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        #
        # Allow the board to grow.
        #
        self.setMinimumSize(
            300,
            300,
        )

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        #
        # We keep original aspect ratio.
        #
        self.setScaledContents(False)

        self._pixmap: QPixmap | None = None

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def load_image(
        self,
        image: Path,
    ) -> None:
        """
        Load rendered PNG.
        """

        self._pixmap = QPixmap(str(image))

        self._update_pixmap()

    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def resizeEvent(
        self,
        event,
    ) -> None:

        super().resizeEvent(event)

        self._update_pixmap()

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _update_pixmap(self) -> None:

        if self._pixmap is None:
            return

        scaled = self._pixmap.scaled(

            self.size(),

            Qt.AspectRatioMode.KeepAspectRatio,

            Qt.TransformationMode.SmoothTransformation,

        )

        self.setPixmap(scaled)
