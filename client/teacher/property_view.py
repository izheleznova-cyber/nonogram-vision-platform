"""
Task property view.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
)

from core.lesson.task import Task


class PropertyView(QWidget):
    """
    Displays task properties.
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QFormLayout(self)

        self.id_label = QLabel()

        self.title_edit = QLineEdit()

        self.asset_label = QLabel()

        self.answer_label = QLabel()

        layout.addRow("Id", self.id_label)
        layout.addRow("Title", self.title_edit)
        layout.addRow("Asset", self.asset_label)
        layout.addRow("Answer", self.answer_label)

        self.title_edit.editingFinished.connect(
            self._title_changed
        )

    def show_task(
        self,
        task: Task,
    ) -> None:
        """
        Display task properties.
        """

        self._task = task

        self.id_label.setText(task.id)

        self.title_edit.setText(task.title)

        self.asset_label.setText(
            task.asset_ref.asset_id
        )

        self.answer_label.setText(
            task.answer_spec.type
        )

    def clear(self) -> None:
        """
        Clear the panel.
        """

        self._task = None

        self.id_label.clear()
        self.title_edit.clear()
        self.asset_label.clear()
        self.answer_label.clear()

    def _title_changed(self) -> None:
        """
        Store edited title back into the model.
        """

        if self._task is None:
            return

        self._task.title = self.title_edit.text()