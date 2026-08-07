"""
Task list widget.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QListWidget

from core.lesson.task import Task


class TaskList(QListWidget):
    """
    Displays tasks of the selected stage.
    """

    def set_tasks(
        self,
        tasks: list[Task],
    ) -> None:
        """
        Populate the task list.
        """

        self.clear()

        for task in tasks:
            self.addItem(task.title)
