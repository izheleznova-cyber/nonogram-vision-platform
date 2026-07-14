"""
student_gui.py

Run Student GUI.
"""

from __future__ import annotations

import sys

from pathlib import Path

from PyQt6.QtWidgets import QApplication

from client.student.gui import StudentGui

from core.dataset.paths import CACHE_DIR
from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode

from core.game.session import GameSession
from core.game.settings import LessonSettings

from core.puzzle.renderer import render_puzzle


PAGE_ID = 1039


def main() -> None:

    #
    # QApplication
    #

    app = QApplication(sys.argv)

    #
    # Load puzzle
    #

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    #
    # Temporary PNG
    #

    output = (
        Path(__file__).resolve().parents[2]
        / "output"
        / "renders"
        / f"render_{PAGE_ID}.png"
    )

    render_puzzle(
        puzzle,
        output,
    )

    #
    # Create lesson session
    #

    settings = LessonSettings()

    session = GameSession(
        puzzle=puzzle,
        settings=settings,
    )

    #
    # GUI
    #

    window = StudentGui()

    window.set_session(session)

    # window.board.load_image(output)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
