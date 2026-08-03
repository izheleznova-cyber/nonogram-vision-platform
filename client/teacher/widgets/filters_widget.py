"""
Lesson builder filters.
"""

from __future__ import annotations
from core.dataset.passport_database import PassportDatabase

from core.lesson.query import LessonQuery 

from PyQt6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGroupBox,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class FiltersWidget(QWidget):
    """
    Filter panel for Lesson Builder.
    """

    def __init__(self) -> None:
        super().__init__()

        self._create_widgets()

        self._build_layout()

        


    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_database(
        self,
        database: PassportDatabase,
    ) -> None:
        """
        Attach passport database to filters.
        """

        self.database = database

        self._fill_filters()


    def query(self) -> LessonQuery:
        """
        Return current search query.
        """

        category = self.category.currentText()

        if category == "Any":
            category = None

        difficulty = self.difficulty.currentText()

        if difficulty == "Any":
            difficulty = None
        else:
            difficulty = int(difficulty)

        color = self.color.currentText()

        if color == "Any":
            color = None

        return LessonQuery(
            max_width=self.max_width.value(),
            max_height=self.max_height.value(),
            category=category,
            difficulty=difficulty,
            color=color,
        )


    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _fill_filters(self) -> None:
        """
        Fill filter controls from database.
        """

        if self.database is None:
            return

        #
        # Category
        #

        self.category.clear()

        self.category.addItem(
            "Any"
        )

        for value in self.database.values(
            "category"
        ):
            self.category.addItem(
                str(value)
            )

        #
        # Difficulty
        #

        self.difficulty.clear()

        self.difficulty.addItem(
            "Any"
        )

        for value in self.database.values(
            "difficulty"
        ):
            self.difficulty.addItem(
                str(value)
            )

        #
        # Color
        #

        self.color.clear()

        self.color.addItem(
            "Any"
        )

        for value in self.database.values(
            "color"
        ):
            self.color.addItem(
                str(value)
            )

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------
 
    def _create_widgets(self) -> None:

        self.max_width = QSpinBox()
        self.max_width.setRange(1, 100)
        self.max_width.setValue(10)

        self.max_height = QSpinBox()
        self.max_height.setRange(1, 100)
        self.max_height.setValue(10)

        self.category = QComboBox()
        self.category.addItem("Any")

        self.difficulty = QComboBox()
        self.difficulty.addItem("Any")

        self.color = QComboBox()
        self.color.addItem("Any")

        self.find_button = QPushButton(
            "Find"
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(self) -> None:

        form = QFormLayout()

        form.addRow(
            "Maximum width",
            self.max_width,
        )

        form.addRow(
            "Maximum height",
            self.max_height,
        )

        form.addRow(
            "Category",
            self.category,
        )

        form.addRow(
            "Difficulty",
            self.difficulty,
        )

        form.addRow(
            "Color",
            self.color,
        )

        layout = QVBoxLayout(self)

        layout.addLayout(form)

        layout.addStretch()

        layout.addWidget(
            self.find_button
        )

