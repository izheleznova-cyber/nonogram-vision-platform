"""
Example: Lesson Designer.
"""

import sys

from PyQt6.QtWidgets import QApplication

from client.teacher.designer import LessonDesigner


def main() -> None:

    app = QApplication(sys.argv)

    window = LessonDesigner()
    window.resize(1200, 700)

    #
    # Temporary test
    #
    window._load_lesson()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()