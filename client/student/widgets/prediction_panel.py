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

    def prediction(self) -> str:
        """
        Current text.
        """

        return self.editor.toPlainText()

    def clear(self) -> None:
        """
        Clear editor.
        """

        self.editor.clear()

    def _save_prediction(self) -> None:
        """
        Save current hypothesis.
        """

        print("Save button pressed")
        print("session =", self.session)

        if self.session is None:
            print("Session is None")
            return

        text = self.prediction.prediction().strip()

        print("text =", text)

        self.session.add_prediction(text)

        print("predictions =", len(self.session.predictions))

        self.prediction.clear()