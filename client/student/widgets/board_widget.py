"""
Interactive board widget.

Step 1:
Draw empty grid using QPainter.
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QFont,
)
from PyQt6.QtWidgets import QWidget
from core.puzzle.layout import (
    Layout,
    calculate_layout,
)


class BoardWidget(QWidget):
    """
    Interactive puzzle board.

    First version:
    only draws an empty grid.
    """

    CELL_SIZE = 20

    def __init__(self):

        super().__init__()

        #
        # Current puzzle
        #
        self._puzzle = None
        #
        # Current zoom
        #

        self.scale = 1.0
        #
        # Current player board
        #
        self._player = None
        self._layout: Layout | None = None
        self.setMinimumSize(
            900,
            700,
        )
        #
        # View scale
        #
        self.scale = 1.0

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # Temporary compatibility
    # ---------------------------------------------------------

    def load_image(
        self,
        image,
    ) -> None:
        """
        Temporary stub.

        Needed so existing examples
        continue to run.
        """
        self.update()

    def set_puzzle(
        self,
        puzzle,
    ) -> None:
        """
        Set current puzzle.
        """

        self._puzzle = puzzle

        if puzzle is not None:
            self._layout = calculate_layout(puzzle)

            print(
                self._layout
            )

        else:
            self._layout = None

        self.update()

    def set_player(
        self,
        player,
    ) -> None:
        """
        Set current player board.
        """

        self._player = player

        self.update()

    def refresh(
        self,
    ) -> None:
        """
        Refresh board.
        """

        self.update()

    # ---------------------------------------------------------
    # Painting
    # ---------------------------------------------------------

    def paintEvent(
        self,
        event,
    ) -> None:

        painter = QPainter(self)

        painter.fillRect(
            self.rect(),
            Qt.GlobalColor.white,
        )

        self._draw_grid(painter)
        self._draw_row_hints(painter)
        self._draw_column_hints(painter)

    # ---------------------------------------------------------
    # Grid
    # ---------------------------------------------------------

    def _draw_grid(
        self,
        painter: QPainter,
    ) -> None:

        if self._layout is None:
            return

        layout = self._layout

        cell = int(
            layout.cell_size * self.scale
        )

        left = layout.puzzle_x
        top = layout.puzzle_y

        columns = self._puzzle.width
        rows = self._puzzle.height
        
        
        thin_pen = QPen(
            QColor(190, 190, 190)
        )
        thin_pen.setWidth(1)

        thick_pen = QPen(
            Qt.GlobalColor.black
        )
        thick_pen.setWidth(2)

        #
        # Vertical lines
        #

        for col in range(columns + 1):

            x = left + col * cell

            if col % 5 == 0:
                painter.setPen(thick_pen)
            else:
                painter.setPen(thin_pen)

            painter.drawLine(
                x,
                top,
                x,
                top + rows * cell,
            )
        #
        # Horizontal lines
        #

        for row in range(rows + 1):

            y = top + row * cell

            if row % 5 == 0:
                painter.setPen(thick_pen)
            else:
                painter.setPen(thin_pen)

            painter.drawLine(
                left,
                y,
                left + columns * cell,
                y,
            )


    def _draw_row_hints(
        self,
        painter: QPainter,
    ) -> None:
        """
        Draw left row hints.
        """

        if self._layout is None:
            return

        if self._puzzle is None:
            return

        layout = self._layout

        cell = int(
            layout.cell_size * self.scale
        )

        #
        # Левая граница области подсказок
        #
        left = (
            layout.puzzle_x
            - layout.left_hint_cells * cell
        )

        # font = QFont()
        # font.setPointSize(9)
        # font.setBold(True)

        # painter.setFont(font)
        self._prepare_hint_painter(painter)

        metrics = painter.fontMetrics()

        for row, hints in enumerate(self._puzzle.row_hints):

            y = (
                layout.puzzle_y
                + row * cell
            )

            hint_count = len(hints)

            start_cell = (
                layout.left_hint_cells
                - hint_count
            )

            for index, (length, color) in enumerate(hints):

                cell_left = (
                    left
                    + (start_cell + index) * cell
                )

                text = str(length)

                text_height = metrics.height()

                painter.drawText(
                    cell_left + 2,
                    y + (cell + text_height) // 2 - 4,
                    text,
                )
    def _draw_column_hints(
        self,
        painter: QPainter,
    ) -> None:
        """
        Draw top column hints.
        """

        if self._layout is None:
            return

        if self._puzzle is None:
            return

        layout = self._layout

        cell = int(
            layout.cell_size * self.scale
        )

        #
        # Верхняя граница области подсказок
        #
        top = (
            layout.puzzle_y
            - layout.top_hint_cells * cell
        )

        # font = QFont()
        # font.setPointSize(9)
        # font.setBold(True)

        # painter.setFont(font)
        # painter.setPen(Qt.GlobalColor.black)
        self._prepare_hint_painter(painter)

        metrics = painter.fontMetrics()

        for col, hints in enumerate(self._puzzle.column_hints):

            #
            # Левая координата столбца
            #
            x = (
                layout.puzzle_x
                + col * cell
            )

            hint_count = len(hints)

            #
            # Первая занятая ячейка
            #
            start_cell = (
                layout.top_hint_cells
                - hint_count
            )

            for index, (length, color) in enumerate(hints):

                #
                # Верхняя координата текущей ячейки
                #
                cell_top = (
                    top
                    + (start_cell + index) * cell
                )

                text = str(length)

                rect = metrics.boundingRect(text)

                text_width = rect.width()

                painter.drawText(
                    x + (cell - text_width) // 2,
                    cell_top + (cell + metrics.ascent()) // 2,
                    text,
                )

    def _hint_font(self) -> QFont:
        """
        Font used for row and column hints.
        """

        font = QFont()

        font.setPointSize(9)

        # Пока без жирного
        font.setBold(False)

        return font

    def _prepare_hint_painter(
        self,
        painter: QPainter,
    ) -> None:
        """
        Configure painter for hint rendering.
        """

        painter.setFont(
            self._hint_font()
        )

        painter.setPen(
            QColor(60, 60, 60)
        )

    def zoom_in(self) -> None:

        if self.scale < 3.0:
            self.scale *= 1.25
            self.update()


    def zoom_out(self) -> None:

        if self.scale > 0.4:
            self.scale /= 1.25
            self.update()


    def zoom_reset(self) -> None:

        self.scale = 1.0
        self.update()

    # ---------------------------------------------------------
    # Zoom
    # ---------------------------------------------------------

    def zoom_in(
        self,
    ) -> None:
        """
        Increase board scale.
        """

        if self.scale < 3.0:

            self.scale *= 1.25

            print(
                f"Zoom: {self.scale:.2f}"
            )

            self.update()


    def zoom_out(
        self,
    ) -> None:
        """
        Decrease board scale.
        """

        if self.scale > 0.4:

            self.scale /= 1.25

            print(
                f"Zoom: {self.scale:.2f}"
            )

            self.update()