"""
Lesson Designer widget.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSplitter,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QFileDialog,
)


from core.lesson.lesson import Lesson
from core.lesson.stage import Stage

from core.lesson.migration import build_stages
from examples.demo_stage_model import build_demo_stages

from client.teacher.toolbar import LessonToolbar
from client.teacher.stage_explorer import StageExplorer

from client.teacher.task_list import TaskList
from client.teacher.property_view import PropertyView

from core.lesson.task import Task
from core.lesson.asset_ref import AssetRef
from core.lesson.answer_spec import AnswerSpec

from core.lesson.editor_model import EditorLesson
from core.lesson.editor_migration import (
    to_editor,
    to_lesson,
)

from pathlib import Path

from PyQt6.QtWidgets import QFileDialog

from core.lesson.editor_migration import to_lesson
from core.lesson.serializer import save_manifest

from core.lesson.manifest import (
    build_manifest,
    build_editor_manifest,
)

from core.lesson.serializer import load_manifest
from core.lesson.editor_loader import build_editor_lesson

from core.dataset.passport_database import PassportDatabase

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

        self.database = PassportDatabase()

        #
        # Temporary demo model.
        #

        self.lesson = EditorLesson(
            name="lesson01",
            title="Aircraft",
            max_width=50,
            max_height=42,
            stages=build_demo_stages(),
        )

        self.stage_tree.set_stages(
            self.lesson.stages
        )

        self._current_stage: Stage | None = None

            
    def _create_ui(self) -> None:
        """
        Create the user interface.
        """

        layout = QVBoxLayout(self)

        title = QLabel("Lesson Designer")
        layout.addWidget(title)

        #
        # Toolbar
        #

        self.toolbar = LessonToolbar()
        layout.addWidget(self.toolbar)

        #
        # Main area
        #

        splitter = QSplitter()
        layout.addWidget(splitter)

        #
        # Stage tree
        #

        self.stage_tree = StageExplorer()
        self.stage_tree.setHeaderLabel("Stages")
        splitter.addWidget(self.stage_tree)

        #
        # Task list
        #

        self.task_list = TaskList()
        splitter.addWidget(self.task_list)

        self.task_list.currentRowChanged.connect(
            self._on_task_selected
        )

        #
        # Property list
        #

        self.property_view = PropertyView()
        splitter.addWidget(self.property_view)

        self.property_view.title_changed = (
            self._refresh_task_list
        )

        #
        # Signals
        #

        self.stage_tree.currentItemChanged.connect(
            self._on_stage_selected
        )

        self.toolbar.add_stage_button.clicked.connect(
            self._add_stage
        )

        self.toolbar.add_task_button.clicked.connect(
            self._add_task
        )

        self.toolbar.delete_button.clicked.connect(
            self._delete_task
        )

        self.toolbar.open_button.clicked.connect(
            self._load_lesson
        )

        self.toolbar.save_button.clicked.connect(
            self._save_lesson
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

        if current is None:
            return

        index = self.stage_tree.indexOfTopLevelItem(current)

        if index < 0:
            return

        stage = self.lesson.stages[index]

        self._current_stage = stage

        asset_ids = []

        for task in stage.tasks:
            asset_ids.append(
                task.asset_ref.asset_id
            )

        self.property_view.set_assets(asset_ids)

        self.task_list.set_tasks(stage.tasks)

        if self.task_list.count():
            self.task_list.setCurrentRow(0)
        else:
            self.property_view.clear()

        if self.task_list.count():
            self.task_list.setCurrentRow(0)

    def load_lesson(
        self,
        lesson: Lesson,
    ) -> None:
        """
        Load a lesson into the designer.
        """

        self._lesson = lesson

        self.stage_tree.clear()
        
        #
        # Build Stage objects from the legacy Lesson.
        #

        self.lesson = EditorLesson(
            name=lesson.name,
            title=lesson.title,
            max_width=lesson.max_width,
            max_height=lesson.max_height,
            stages=build_stages(lesson),
        )

        #
        # Populate the tree.
        #

        for stage in self.lesson.stages:
            item = QTreeWidgetItem(
                [f"Stage {stage.number}"]
            )

            self.stage_tree.addTopLevelItem(item)

        if self.stage_tree.topLevelItemCount():
            self.stage_tree.setCurrentItem(
                self.stage_tree.topLevelItem(0)
            )

    def _on_task_selected(
        self,
        row: int,
    ) -> None:
        """
        Show task properties.
        """

        if self._current_stage is None:
            return

        if row < 0:
            return

        task = self._current_stage.tasks[row]

        self.property_view.show_task(task)

    def _add_stage(self) -> None:
        """
        Add a new empty stage.
        """

        number = len(self.lesson.stages) + 1

        stage = Stage(
            number=number,
            puzzle_id="",
            tasks=[],
        )

        self.lesson.stages.append(stage)

        self.stage_tree.set_stages(
            self.lesson.stages
        )

        self.stage_tree.setCurrentItem(
            self.stage_tree.topLevelItem(number - 1)
        )

    def _add_task(self) -> None:
        """
        Add a new task to the selected stage.
        """

        if self._current_stage is None:
            return

        number = len(self._current_stage.tasks) + 1

        task = Task(
            id=f"task_{number}",
            title="Solve nonogram",
            asset_ref=AssetRef(asset_id=""),
            answer_spec=AnswerSpec(
                type="NonogramSolution",
            ),
        )

        self._current_stage.tasks.append(task)

        self.task_list.set_tasks(
            self._current_stage.tasks
        )

        self.task_list.setCurrentRow(
            self.task_list.count() - 1
        )

    def _refresh_task_list(self) -> None:
        """
        Refresh task titles after editing.
        """

        if self._current_stage is None:
            return

        row = self.task_list.currentRow()

        self.task_list.set_tasks(
            self._current_stage.tasks
        )

        if row >= 0:
            self.task_list.setCurrentRow(row)

    def _delete_task(self) -> None:
        """
        Delete the selected task.
        """

        if self._current_stage is None:
            return

        row = self.task_list.currentRow()

        if row < 0:
            return

        del self._current_stage.tasks[row]

        self.task_list.set_tasks(
            self._current_stage.tasks
        )

        self.property_view.clear()

        if self.task_list.count():
            self.task_list.setCurrentRow(
                min(row, self.task_list.count() - 1)
            )

    def _save_lesson(self) -> None:
        """
        Save the current lesson.
        """

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save lesson",
            "lesson.json",
            "Lesson (*.json)",
        )

        if not filename:
            return

        manifest = build_editor_manifest(
            self.lesson
        )

        save_manifest(
            manifest,
            Path(filename),
        )

    def _load_lesson(self) -> None:
        """
        Load lesson from manifest.
        """

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open lesson",
            "",
            "Lesson (*.json)",
        )

        if not filename:
            return

        manifest = load_manifest(filename)

        self.lesson = build_editor_lesson(
            manifest
        )

        self.stage_tree.set_stages(
            self.lesson.stages
        )

        if self.stage_tree.topLevelItemCount():
            self.stage_tree.setCurrentItem(
                self.stage_tree.topLevelItem(0)
            )