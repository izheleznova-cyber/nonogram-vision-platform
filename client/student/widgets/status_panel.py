"""
Status panel.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)


class StatusPanel(QWidget):
    """
    Lesson status.
    """

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            5,
            5,
            5,
            5,
        )

        layout.setSpacing(
            20,
        )

        self.progress = QLabel(
            "Progress: 0%"
        )

        self.time = QLabel(
            "Time: 00:00"
        )

        self.checks = QLabel(
            "Checks: ∞"
        )

        layout.addWidget(
            self.progress
        )

        layout.addStretch()

        layout.addWidget(
            self.time
        )

        layout.addStretch()

        layout.addWidget(
            self.checks
        )

    def set_checks(
        self,
        current: int,
        maximum: int,
    ) -> None:

        self.checks.setText(
            f"Checks: {current}/{maximum}"
        )

    def set_time(
        self,
        seconds: int,
    ) -> None:

        minutes = seconds // 60
        seconds = seconds % 60

        self.time.setText(
            f"Time: {minutes:02}:{seconds:02}"
        )


    def set_progress(
        self,
        value: float,
    ) -> None:

        self.progress.setText(
            f"Progress: {value:.0%}"
        )

