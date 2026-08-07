"""
Lesson Designer toolbar.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class LessonToolbar(QWidget):
    """
    Toolbar for Lesson Designer.
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QHBoxLayout(self)

        #
        # Stage
        #

        self.add_stage_button = QPushButton("+ Stage")
        layout.addWidget(self.add_stage_button)

        #
        # Task
        #

        self.add_task_button = QPushButton("+ Task")
        layout.addWidget(self.add_task_button)

        #
        # Delete
        #

        self.delete_button = QPushButton("Delete")
        layout.addWidget(self.delete_button)

        #
        # Move
        #

        self.up_button = QPushButton("↑")
        layout.addWidget(self.up_button)

        self.down_button = QPushButton("↓")
        layout.addWidget(self.down_button)

        #
        # Spacer
        #

        layout.addStretch()

        #
        # Save
        #

        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)
