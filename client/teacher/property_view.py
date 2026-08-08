"""
Task property view.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QComboBox,
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

        self.asset_combo = QComboBox()

        self.answer_label = QLabel()

        layout.addRow("Id", self.id_label)
        layout.addRow("Title", self.title_edit)
        layout.addRow(
            "Asset",
            self.asset_combo,
        )
        layout.addRow("Answer", self.answer_label)

        self.title_edit.editingFinished.connect(
            self._title_changed
        )

        self.asset_combo.currentTextChanged.connect(
            self._asset_changed
        )

        self._asset_ids: list[str] = []
        
        self._task: Task | None = None

        self.title_changed = None

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

        index = self.asset_combo.findText(
            task.asset_ref.asset_id
        )

        if index >= 0:
            self.asset_combo.setCurrentIndex(index)

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
        self.asset_combo.clear()
        self.answer_label.clear()

    def _title_changed(self) -> None:
        """
        Store edited title back into the model.
        """

        if self._task is None:
            return

        self._task.title = self.title_edit.text()

        if self.title_changed is not None:
            self.title_changed()

    def set_assets(
        self,
        asset_ids: list[str],
    ) -> None:
        """
        Populate Asset combo box.
        """

        self._asset_ids = asset_ids

        self.asset_combo.clear()

        self.asset_combo.addItems(asset_ids)

    def _asset_changed(
        self,
        asset_id: str,
    ) -> None:
        pass