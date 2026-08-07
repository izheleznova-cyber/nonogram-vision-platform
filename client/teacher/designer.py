"""
Lesson Designer widget.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QLabel,
    QListWidget,
    QPushButton,
    QSplitter,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from core.lesson.lesson import Lesson
from core.lesson.stage import Stage

from core.lesson.migration import build_stages
from examples.demo_stage_model import build_demo_stages

class LessonDesigner(QWidget):
    """
    Lesson Designer.

    Allows configuring how students should complete
    a lesson.

    At this stage only the UI skeleton is implemented.
    """

    def __init__(self) -> None:
        super().__init__()

        self._create_ui()

        #
        # Temporary demo model.
        #

        self._stages = build_demo_stages()

        self._populate_demo_data()
    
    def _create_ui(self) -> None:
        """
        Create the user interface.
        """

        layout = QVBoxLayout(self)

        title = QLabel("Lesson Designer")
        layout.addWidget(title)

        splitter = QSplitter()
        layout.addWidget(splitter)

        #
        # Stage tree
        #

        self.stage_tree = QTreeWidget()
        self.stage_tree.setHeaderLabel("Stages")
        splitter.addWidget(self.stage_tree)

        #
        # Task list
        #

        self.task_list = QListWidget()
        splitter.addWidget(self.task_list)

        #
        # Property list
        #

        self.property_list = QListWidget()
        splitter.addWidget(self.property_list)

        #
        # Save button
        #

        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)

        #
        # Signals
        #

        self.stage_tree.currentItemChanged.connect(
            self._on_stage_selected
        )

    def _populate_demo_data(self) -> None:
        """
        Populate the stage tree from demo Stage objects.
        """

        self.stage_tree.clear()

        for stage in self._stages:
            item = QTreeWidgetItem(
                [f"Stage {stage.number}"]
            )

            self.stage_tree.addTopLevelItem(item)

        if self.stage_tree.topLevelItemCount():
            self.stage_tree.setCurrentItem(
                self.stage_tree.topLevelItem(0)
            )

    def _on_stage_selected(
        self,
        current: QTreeWidgetItem | None,
        previous: QTreeWidgetItem | None,
    ) -> None:
        """
        Update task list when another stage is selected.
        """

        del previous

        self.task_list.clear()

        if current is None:
            return

        index = self.stage_tree.indexOfTopLevelItem(current)

        if index < 0:
            return

        stage = self._stages[index]

        for task in stage.tasks:
            self.task_list.addItem(task.title)

    def load_lesson(
        self,
        lesson: Lesson,
    ) -> None:
        """
        Load a lesson into the designer.
        """

        self._lesson = lesson

        self.stage_tree.clear()
        self.task_list.clear()
        self.property_list.clear()

        #
        # Build Stage objects from the legacy Lesson.
        #

        self._stages = build_stages(lesson)

        #
        # Populate the tree.
        #

        for stage in self._stages:
            item = QTreeWidgetItem(
                [f"Stage {stage.number}"]
            )

            self.stage_tree.addTopLevelItem(item)

        if self.stage_tree.topLevelItemCount():
            self.stage_tree.setCurrentItem(
                self.stage_tree.topLevelItem(0)
            )