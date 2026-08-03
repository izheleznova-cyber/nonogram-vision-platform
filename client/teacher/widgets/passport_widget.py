"""
Passport preview widget.
"""

from __future__ import annotations
from core.dataset.passport_record import PassportRecord

from PyQt6.QtWidgets import (
    QLabel,
    QFormLayout,
    QWidget,
)


class PassportWidget(QWidget):
    """
    Display passport information.
    """

    def __init__(self) -> None:
        super().__init__()

        self._create_widgets()

        self._build_layout()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_passport(
        self,
        passport: PassportRecord,
    ) -> None:
        """
        Display passport.
        """

        self.id.setText(
            passport.id
        )

        self.title.setText(
            passport.title
        )

        self.category.setText(
            passport.category
        )

        self.difficulty.setText(
            str(passport.difficulty)
        )

        self.size.setText(
            f"{passport.width} × {passport.height}"
        )

        self.color.setText(
            passport.color
        )

        self.source.setText(
            passport.source
        )


    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        self.id = QLabel()

        self.title = QLabel()

        self.category = QLabel()

        self.difficulty = QLabel()

        self.size = QLabel()

        self.color = QLabel()

        self.source = QLabel()

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QFormLayout(self)

        layout.addRow(
            "ID",
            self.id,
        )

        layout.addRow(
            "Title",
            self.title,
        )

        layout.addRow(
            "Category",
            self.category,
        )

        layout.addRow(
            "Difficulty",
            self.difficulty,
        )

        layout.addRow(
            "Size",
            self.size,
        )

        layout.addRow(
            "Color",
            self.color,
        )

        layout.addRow(
            "Source",
            self.source,
        )
