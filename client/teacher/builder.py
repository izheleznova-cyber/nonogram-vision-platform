"""
Lesson builder.
"""

from __future__ import annotations
from .widgets.filters_widget import FiltersWidget
from core.dataset.passport_database import PassportDatabase

from core.lesson.query import LessonQuery

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

        self.candidate_list.clear()

        for passport in passports:

            self.candidate_list.addItem(
                f"{passport.id:10}   {passport.title}"
            )