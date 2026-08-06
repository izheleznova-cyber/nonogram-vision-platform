"""
Lesson builder.
"""

from __future__ import annotations
from pathlib import Path

from .widgets.filters_widget import FiltersWidget
from core.dataset.passport_database import PassportDatabase
from core.dataset.paths import DATASET_ROOT

from core.lesson.query import LessonQuery
from .widgets.passport_widget import PassportWidget
from .widgets.preview_widget import PreviewWidget

from core.dataset.passport_record import PassportRecord


from PyQt6.QtWidgets import (
    QGroupBox,
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QInputDialog,
    QMessageBox,
)


class LessonBuilder(QWidget):
    """
    Lesson builder.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(
            "Lesson Builder"
        )

        self.resize(
            1200,
            700,
        )

        self._create_widgets()

        self.database = PassportDatabase()

        #
        # Current lesson
        #

        self._lesson: list[PassportRecord] = []

        self._lesson_directory = None

        self.filters.set_database(
            self.database
        )

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        #
        # Groups
        #
        self.filters = FiltersWidget()
        self.filters_box = QGroupBox(
            "Filters"
        )

        self.candidates_box = QGroupBox(
            "Candidates"
        )

        self.lesson_box = QGroupBox(
            "Lesson"
        )

        #
        # Lists
        #

        self.candidate_list = QListWidget()

        self.passport = PassportWidget()

        self.preview = PreviewWidget()

        self.passport_box = QGroupBox(
            "Passport"
        )

        self.lesson_list = QListWidget()

        #
        # Buttons
        #

        self.add_button = QPushButton(
            "Add →"
        )

        self.remove_button = QPushButton(
            "← Remove"
        )

        self.save_button = QPushButton(
            "Save"
        )

        self.save_as_button = QPushButton(
            "Save As..."
        )
        

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        layout = QHBoxLayout(self)

        #
        # Filters
        #

           
        filters = QVBoxLayout()

        filters.addWidget(
            self.filters
        )
        
        
        self.filters_box.setLayout(
            filters
        )

        #
        # Candidates
        #

        candidates = QVBoxLayout()

        candidates.addWidget(
            self.candidate_list
        )

        self.candidates_box.setLayout(
            candidates
        )

        #
        # Passport
        #

        passport = QVBoxLayout()

        passport.addWidget(self.preview)

        passport.addWidget(self.passport)

        passport.addStretch()

        self.passport_box.setLayout(
            passport
        )

        #
        # Lesson
        #

        lesson = QVBoxLayout()

        lesson.addWidget(
            self.lesson_list
        )

        lesson.addWidget(
            self.add_button
        )

        lesson.addWidget(
            self.remove_button
        )

        lesson.addStretch()

        lesson.addWidget(
            self.save_button
        )

        lesson.addWidget(
            self.save_as_button
        )

        self.lesson_box.setLayout(
            lesson
        )

        #
        # Main layout
        #

        layout.addWidget(
            self.filters_box,
            stretch=1,
        )

        layout.addWidget(
            self.candidates_box,
            stretch=2,
        )

        layout.addWidget(
            self.passport_box,
            stretch=2,
        )

        layout.addWidget(
            self.lesson_box,
            stretch=2,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(self) -> None:

        self.filters.find_button.clicked.connect(
            self._find_candidates
        )

        self.candidate_list.currentRowChanged.connect(
            self._candidate_selected
        )

        self.add_button.clicked.connect(
            self._add_to_lesson
        )

        self.remove_button.clicked.connect(
            self._remove_from_lesson
        )

        self.save_as_button.clicked.connect(
            self._save_as
        )

        self.save_button.clicked.connect(
            self._save
        )

    # ---------------------------------------------------------
    # Slots
    # ---------------------------------------------------------

    def _find_candidates(self) -> None:
        """
        Search passports matching current filters.
        """

        query = self.filters.query()

        passports = self.database.search(
            query
        )

        self._candidates = passports

        self.candidate_list.clear()

        for passport in passports:

            self.candidate_list.addItem(
                f"{passport.id:10}   {passport.title}"
            )

    def _candidate_selected(
        self,
        row: int,
    ) -> None:
        """
        Display selected passport.
        """

        if row < 0:
            return

        passport = self._candidates[row]

        self.passport.set_passport(
            passport
        )

        self.preview.set_passport(
            passport
        )

    def _add_to_lesson(self) -> None:
        """
        Add selected passport to lesson.
        """

        row = self.candidate_list.currentRow()

        if row < 0:
            return

        passport = self._candidates[row]

        self._lesson.append(
            passport
        )

        self.lesson_list.addItem(
            f"{len(self._lesson):2d}   "
            f"{passport.id:10}   "
            f"{passport.title}"
        )

    def _remove_from_lesson(
        self,
    ) -> None:
        """
        Remove selected passport from lesson.
        """

        row = self.lesson_list.currentRow()

        if row < 0:
            return

        #
        # Remove from model
        #

        del self._lesson[row]

        #
        # Rebuild list
        #

        self.lesson_list.clear()

        for index, passport in enumerate(
            self._lesson,
            start=1,
        ):

            self.lesson_list.addItem(
                f"{index:2d}   "
                f"{passport.id:10}   "
                f"{passport.title}"
            )

    def set_passport(
        self,
        passport: PassportRecord,
    ) -> None:
        """
        Display preview for selected passport.
        """

        #
        # Пока миниатюр нет.
        #

        self.clear()

        self.setText(
            "No preview"
        )

    def _save(
        self,
    ) -> None:
        """
        Save current lesson.
        """

        #
        # Первый раз сохраняем как новый урок.
        #

        if self._lesson_directory is None:

            self._save_as()

            return

        #
        # ids
        #

        ids_path = self._lesson_directory / "ids"

        with ids_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            for passport in self._lesson:

                file.write(
                    f"{passport.id}\n"
                )

        #
        # manifest
        #

        manifest = self._lesson_directory / "manifest"

        with manifest.open(
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                f"{self._lesson_directory.name}\n"
            )

            file.write(
                f"Count={len(self._lesson)}\n"
            )

        QMessageBox.information(
            self,
            "Saved",
            "Lesson has been updated.",
        )


    def _save_as(
        self,
    ) -> None:
        """
        Save lesson as...
        """

        name, ok = QInputDialog.getText(
            self,
            "Save lesson",
            "Lesson name:",
        )

        if not ok:
            return

        name = name.strip()

        if not name:
            return

        lessons_dir = DATASET_ROOT / "lessons"

        lessons_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        lesson_dir = lessons_dir / name

        self._lesson_directory = lesson_dir

        if lesson_dir.exists():

            QMessageBox.warning(
                self,
                "Lesson exists",
                f'Lesson "{name}" already exists.',
            )

            return

        lesson_dir.mkdir()

        #
        # ids
        #

        ids_path = lesson_dir / "ids"

        with ids_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            for passport in self._lesson:

                file.write(
                    f"{passport.id}\n"
                )

        #
        # manifest
        #

        manifest = lesson_dir / "manifest"

        with manifest.open(
            "w",
            encoding="utf-8",
        ) as file:

            file.write(f"{name}\n")
            file.write(f"Count={len(self._lesson)}\n")

        self._lesson_directory = lesson_dir

        print(self._lesson_directory)
        
        QMessageBox.information(
            self,
            "Saved",
            f'Lesson "{name}" has been saved.',
        )