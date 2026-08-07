"""
Task property view.
"""

from __future__ import annotations

from PyQt6.QtWidgets import QListWidget

from core.lesson.task import Task


class PropertyView(QListWidget):
    """
    Displays properties of a task.
    """

    def show_task(
        self,
        task: Task,
    ) -> None:
        """
        Display task properties.
        """

        self.clear()

        self.addItem(f"id: {task.id}")
        self.addItem(f"title: {task.title}")
        self.addItem(
            f"asset: {task.asset_ref.asset_id}"
        )
        self.addItem(
            f"answer: {task.answer_spec.type}"
        )
