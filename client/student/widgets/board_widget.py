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
from core.game.session import GameSession
from core.puzzle.layout import (
    Layout,
    calculate_layout,
)
from core.puzzle.player import (
    PlayerBoard,
    FILLED,
    CROSSED,
)

from core.game.completed_hints import (
    completed_row_hints,
    completed_column_hints,
)

from PyQt6.QtWidgets import QWidget, QMessageBox

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
        #
        # Current game session
        #
        self._session: GameSession | None = None
        
        self._completed_row_hints = []
        self._completed_column_hints = [] 


        self._layout: Layout | None = None

        self.setMinimumSize(
            900,
            700,
        )
        #
        # View scale
        #
        self.scale = 1.0

        #
        # Incorrect cells after last check
        #
        self._errors: set[tuple[int, int]] = set()
        self._completed_row_hints: list[list[bool]] = []
        self._completed_column_hints: list[list[bool]] = []

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # Temporary compatibility
    # ---------------------------------------------------------
        # Позиция мыши для подсветки
        self._hover_row = -1
        self._hover_col = -1
        
        # Включить отслеживание движения мыши
        self.setMouseTracking(True)

        # Completion state
        self._is_completed = False


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

    def _after_move(self) -> None:
        """
        Update widget after player move.
        """
        was_completed = self._is_completed
        self._is_completed = self._check_completed()
        
        self.update_completed_hints()
        
        # Show message only once when completed
        if self._is_completed and not was_completed:
            self._show_completion_message()
        
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

        if self._session is None:
            return

        if event.button() == Qt.MouseButton.LeftButton:

            self._session.left_click(
                row,
                col,
            )
            
            self._after_move()

        elif event.button() == Qt.MouseButton.RightButton:

            self._session.right_click(
                row,
                col,
            )

            self._after_move()

        self.update()

    # ---------------------------------------------------------
    # Painting
    # ---------------------------------------------------------

    def mouseMoveEvent(
        self,
        event: QMouseEvent,
    ) -> None:
        """
        Track mouse position for hint highlighting.
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
        
        # Проверяем, находится ли курсор над игровым полем
        if x < left or y < top:
            # Мышь вне поля - сбрасываем подсветку
            if self._hover_row != -1 or self._hover_col != -1:
                self._hover_row = -1
                self._hover_col = -1
                self.update()
            return
        
        col = int((x - left) // cell)
        row = int((y - top) // cell)
        
        # Проверяем границы
        if row < 0 or row >= self._puzzle.height:
            row = -1
        if col < 0 or col >= self._puzzle.width:
            col = -1
        
        # Обновляем только если позиция изменилась
        if self._hover_row != row or self._hover_col != col:
            self._hover_row = row
            self._hover_col = col
            self.update()
    
    def leaveEvent(
        self,
        event,
    ) -> None:
        """
        Clear highlight when mouse leaves widget.
        """
        if self._hover_row != -1 or self._hover_col != -1:
            self._hover_row = -1
            self._hover_col = -1
            self.update()
    # === КОНЕЦ ВСТАВКИ ===

    # -
    # Painting
    # -
    


    def paintEvent(
        self,
        event,
    ) -> None:
         
        painter = QPainter(self)
        
        painter.fillRect(
            self.rect(),
            QColor(240, 240, 240),
        )

        painter.setPen(Qt.GlobalColor.red)
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))

        painter.drawText(
            20,
            20,
            "PREVIEW",
        )

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

        self._draw_player(painter)

        # Highlighted hints (NEW)
        if self.scale >= 0.75:
            self._draw_highlighted_hints(painter)

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

            completed = (
                self._completed_row_hints[row]
                if self._session is not None
                else [False] * len(hints)
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

                #
                # Strike completed hint
                #
                if completed[index]:

                    line_y = y + cell // 2

                    painter.drawLine(
                        cell_left + 2,
                        line_y,
                        cell_left + cell - 2,
                        line_y,
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
            
            completed = (
                self._completed_column_hints[col]
                if self._session is not None
                else [False] * len(hints)
            )


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

                #
                # Strike completed hint
                #
                if completed[index]:

                    line_y = cell_top + cell // 2

                    painter.drawLine(
                        x + 2,
                        line_y,
                        x + cell - 2,
                        line_y,
                    )

    def _draw_highlighted_hints(
        self,
        painter: QPainter,
    ) -> None:
        """
        Highlight row and column hints under cursor.
        """
        if self._hover_row < 0 and self._hover_col < 0:
            return
        
        if self._layout is None:
            return
        
        layout = self._layout
        cell = layout.cell_size
        
        # Цвет подсветки
        highlight_color = QColor(255, 255, 150, 100)  # Полупрозрачный желтый
        
        # Подсветка строки подсказок
        if self._hover_row >= 0:
            left = layout.puzzle_x - layout.left_hint_cells * cell
            y = layout.puzzle_y + self._hover_row * cell
            
            painter.fillRect(
                left,
                y,
                layout.left_hint_cells * cell,
                cell,
                highlight_color,
            )
        
        # Подсветка столбца подсказок
        if self._hover_col >= 0:
            top = layout.puzzle_y - layout.top_hint_cells * cell
            x = layout.puzzle_x + self._hover_col * cell
            
            painter.fillRect(
                x,
                top,
                cell,
                layout.top_hint_cells * cell,
                highlight_color,
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

    def set_session(
        self,
        session: GameSession,
    ) -> None:
        """
        Connect current game session.
        """

        self._session = session

        self._completed_row_hints = [
            [False] * len(hints)
            for hints in session.puzzle.row_hints
        ]

        self._completed_column_hints = [
            [False] * len(hints)
            for hints in session.puzzle.column_hints
        ]

        self._puzzle = session.puzzle

        self._player = session.board

        self._update_layout()

        self._update_widget_size()

        self.update_completed_hints()
        
        self.update()

        
    def update_completed_hints(self) -> None:
        """
        Update completed row and column hints.
        """
        if self._session is None:
            return
        puzzle = self._session.puzzle
        board = self._session.board
        self._completed_row_hints = [
            completed_row_hints(
                puzzle,
                board,
                row,
            )
            for row in range(puzzle.height)
        ]
        self._completed_column_hints = [
            completed_column_hints(
                puzzle,
                board,
                col,
            )
            for col in range(puzzle.width)
        ]

    # === ВСТАВИТЬ ЗДЕСЬ ===
    def _check_completed(
        self,
    ) -> bool:
        """
        Check if puzzle is fully solved.
        """
        if self._session is None:
            return False
        
        puzzle = self._session.puzzle
        board = self._session.board
        
        for row in range(puzzle.height):
            for col in range(puzzle.width):
                expected = puzzle.matrix[row][col]
                actual = board.state(row, col)
                
                # Если клетка должна быть заполнена, но пуста или зачёркнута
                if expected != 0 and actual != FILLED:
                    return False
                
                # Если клетка должна быть пустой, но заполнена
                if expected == 0 and actual == FILLED:
                    return False
        
        return True

    def _show_completion_message(
        self,
    ) -> None:
        """
        Show completion congratulation.
        """
        from PyQt6.QtWidgets import QMessageBox
        
        msg = QMessageBox()
        msg.setWindowTitle("Completed!")
        msg.setText("🎉 Completed!")
        msg.setInformativeText(
            "Congratulations! You have successfully solved the puzzle!"
        )
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    

    def _draw_player(
        self,
        painter: QPainter,
    ) -> None:

        if self._layout is None:
            return

        if self._player is None:
            return

        layout = self._layout
        cell = layout.cell_size

        for row in range(self._player.height):

            for col in range(self._player.width):

                state = self._player.state(
                    row,
                    col,
                )

                x = layout.puzzle_x + col * cell
                y = layout.puzzle_y + row * cell

                if state == FILLED:

                    margin = 2

                    painter.fillRect(
                        x + margin,
                        y + margin,
                        cell - 2 * margin,
                        cell - 2 * margin,
                        Qt.GlobalColor.black,
                    )

                elif state == CROSSED:

                    pen = QPen(
                        Qt.GlobalColor.darkGray,
                        2,
                    )

                    painter.setPen(pen)

                    painter.drawLine(
                        x + 3,
                        y + 3,
                        x + cell - 3,
                        y + cell - 3,
                    )

                    painter.drawLine(
                        x + 3,
                        y + cell - 3,
                        x + cell - 3,
                        y + 3,
                    )

    def check(
        self,
    ) -> list[tuple[int, int]]:
        """
        Compare current player board
        with the correct puzzle solution.
        """

        errors = []

        for row in range(self.puzzle.height):

            for col in range(self.puzzle.width):

                #
                # Expected puzzle state

                #

                expected_color = self.puzzle.matrix[row][col]

                expected_filled = expected_color != 0


                player_filled = (
                    self.board.state(row, col) == FILLED
                )

                if expected_filled != player_filled:

                    errors.append(
                        (row, col)
                    )
                #
                # Player state
                #

                current = (
                    self.board.state(row, col) == FILLED
                )

                if expected != current:

                    errors.append(
                        (row, col)
                    )

        self.check_count += 1

        self.last_check_time = time.time()

        return errors

    def set_errors(
        self,
        errors: list[tuple[int, int]],
    ) -> None:
        """
        Show incorrect cells.
        """

        self._errors = set(errors)

        self.update()