"""
Prediction panel.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
)


class PredictionPanel(QWidget):
    """
    Student prediction.
    """

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)
        

        layout.addWidget(
            QLabel(
                "Current working hypothesis"
            )
        )

        self.editor = QTextEdit()

        self.editor.setMaximumHeight(
            120
        )

        layout.addWidget(
        self.editor
        )

        self.save_button = QPushButton(
            "Save hypothesis"
        )

        layout.addWidget(
            self.save_button
        )
