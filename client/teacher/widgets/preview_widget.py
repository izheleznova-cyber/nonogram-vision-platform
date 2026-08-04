"""
Puzzle preview widget.
"""

from __future__ import annotations

from pathlib import Path
from core.dataset.paths import PREVIEW_DIR


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class PreviewWidget(QLabel):
    """
    Display puzzle preview.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setMinimumSize(
            220,
            220,
        )

        self.setText(
            "No preview"
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_preview(
        self,
        image_path: Path,
    ) -> None:

        pixmap = QPixmap(
            str(image_path)
        )

        if pixmap.isNull():

            self.setText(
                "Preview unavailable"
            )

            return

        self.setPixmap(

            pixmap.scaled(

                self.size(),

                Qt.AspectRatioMode.KeepAspectRatio,

                Qt.TransformationMode.SmoothTransformation,

            )

        )

    def set_passport(
        self,
        passport: PassportRecord,
    ) -> None:
        """
        Display preview for selected passport.
        """

        preview = PREVIEW_DIR / f"{passport.id}.png"

        if preview.exists():

            self.set_preview(
                preview,
            )

        else:

            self.clear()

            self.setText(
                "No preview",
            )