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

        self.check_button = QPushButton(
            "Check"
        )

        layout.addWidget(
            self.check_button
        )

        layout.addStretch()
