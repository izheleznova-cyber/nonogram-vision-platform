"""
student_gui.py

Run Student GUI.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from client.student.gui import StudentGui


def main() -> None:

    app = QApplication(sys.argv)

    window = StudentGui()

    image = (
        Path(__file__).resolve().parents[2]
        / "output"
        / "renders"
        / "render_1039.png"
    )

    window.board.load_image(image)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()