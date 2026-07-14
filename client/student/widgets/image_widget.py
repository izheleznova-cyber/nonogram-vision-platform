"""
Image widget.
"""

from __future__ import annotations

from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QSizePolicy


class ImageWidget(QLabel):
    """
    Puzzle image widget.
    """

    def __init__(self):

        super().__init__()

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setMinimumSize(
            400,
            300,
        )

        self.setScaledContents(False)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

    def load_image(
        self,
        image: Path,
    ) -> None:
        """
        Load PNG.
        """

        pixmap = QPixmap(str(image))

        self.setPixmap(pixmap)
