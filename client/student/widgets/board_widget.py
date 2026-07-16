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
    QMouseEvent,
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

    BASE_CELL_SIZE = 20
    MIN_SCALE = 0.25
    MAX_SCALE = 3.0

    def __init__(self):

        super().__init__()

        #
        # Current puzzle
        #
        self._puzzle = None
        #
        # Current zoom
        #
        # Rendering sizes
        #
        self._hint_cell = 20

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
            self._update_layout()

            self._update_widget_size()

            self.update()
            
            self._update_widget_size()
            self.update()

            if self._layout is not None:

                self.resize(
                    self._layout.image_width,
                    self._layout.image_height,
                )
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
    # Mouse
    # ---------------------------------------------------------

    def mousePressEvent(
        self,
        event: QMouseEvent,
    ) -> None:
        """
        Handle mouse click.

        Commit 1:
        Only determine the clicked cell.
        """

        if self._layout is None:
            return

        if self._puzzle is None:
            return

        x = event.position().x()
        y = event.position().y()

        left = self._layout.puzzle_x
        top = self._layout.puzzle_y

        cell = self._layout.cell_size

        #
        # Outside puzzle
        #

        if x < left or y < top:
            return

        col = int((x - left) // cell)
        row = int((y - top) // cell)

        if row < 0 or row >= self._puzzle.height:
            return

        if col < 0 or col >= self._puzzle.width:
            return

        print(
            f"Clicked cell: row={row}, col={col}"
        )


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

        #
        # Grid
        #

        self._draw_grid(painter)

        #
        # Hints and coordinates
        #

        if self.scale >= 0.75:

            self._draw_row_hints(painter)

            self._draw_column_hints(painter)

            self._draw_coordinates(painter)

        #
        # Player board
        #

        # self._draw_player(painter)
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

        cell = layout.cell_size

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

        cell = layout.cell_size

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

        cell = layout.cell_size

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

    def zoom_in(self):

        if self._board_cell < 50:

            self._board_cell += 2

            self._board_cell = max(
                5,
                int(20 * self.scale)
            )

            self._update_layout()

            self.update()

    def zoom_out(self):

        if self._board_cell > 8:

            self._board_cell -= 2

            self._board_cell = max(
                5,
                int(20 * self.scale)
            )

            self._update_layout()

            self.update()


    def zoom_reset(self):

        self.scale = 1.0

        self._update_layout()

        self._update_widget_size()

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

        if self.scale < self.MAX_SCALE:

            self.scale *= 1.25

            self._update_layout()

            self._update_widget_size()

            self.update()

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

        if self.scale > self.MIN_SCALE:

            self.scale /= 1.25

            self._update_layout()

            self._update_widget_size()

            self.update()

            print(
                f"Zoom: {self.scale:.2f}"
            )

            self.update()

    def _update_layout(self):

        if self._puzzle is None:
            return

        cell_size = max(
            5,
            int(self.BASE_CELL_SIZE * self.scale),
        )

        self._layout = calculate_layout(
            self._puzzle,
            cell_size=self._current_cell_size(),
        )

    def _update_widget_size(self):

        if self._layout is None:
            return

        self.resize(
            self._layout.image_width,
            self._layout.image_height,
        )


    def _draw_coordinates(
        self,
        painter: QPainter,
    ) -> None:
        """
        Draw coordinates every 5 cells.
        """

        if self._layout is None:
            return

        layout = self._layout

        cell = layout.cell_size

        left = layout.puzzle_x
        top = layout.puzzle_y

        width = self._puzzle.width
        height = self._puzzle.height

        painter.setPen(Qt.GlobalColor.black)

        font = painter.font()
        font.setPointSize(9)

        painter.setFont(font)

        #
        # Bottom coordinates
        #

        y = (
            top
            + layout.puzzle_height
            + 18
        )

        for col in range(5, width + 1, 5):

            x = (
                left
                + (col - 1) * cell
                + cell // 2
            )

            painter.drawText(
                x - 8,
                y,
                str(col),
            )

        #
        # Right coordinates
        #

        x = (
            left
            + layout.puzzle_width
            + 8
        )

        for row in range(5, height + 1, 5):

            y = (
                top
                + (row - 1) * cell
                + cell // 2
                + 5
            )

            painter.drawText(
                x,
                y,
                str(row),
            )

    def _current_cell_size(self) -> int:
        """
        Current board cell size in pixels.
        """

        return max(
            5,
            int(self.BASE_CELL_SIZE * self.scale),
        )