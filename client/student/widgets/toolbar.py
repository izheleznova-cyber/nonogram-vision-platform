"""
Student toolbar.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
)


class Toolbar(QWidget):
    """
    Top toolbar.
    """

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout(self)

        #
        # Check solution
        #

        self.check_button = QPushButton(
            "Check"
        )

        #
        # Zoom controls
        #

        self.zoom_out_button = QPushButton("-")

        self.zoom_in_button = QPushButton("+")

        self.zoom_out_button.setFixedWidth(40)

        self.zoom_in_button.setFixedWidth(40)

        #
        # Layout
        #

        layout.addWidget(
            self.check_button
        )

        layout.addSpacing(20)

        layout.addWidget(
            self.zoom_out_button
        )

        layout.addWidget(
            self.zoom_in_button
        )

        layout.addStretch()