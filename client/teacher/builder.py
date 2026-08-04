"""
Lesson builder.
"""

from __future__ import annotations
from .widgets.filters_widget import FiltersWidget
from core.dataset.passport_database import PassportDatabase

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
            "Save lesson"
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