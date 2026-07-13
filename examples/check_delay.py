"""
check_delay.py

Test lesson checking rules.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.game.settings import LessonSettings
from core.game.session import GameSession
from core.game.checker import (
    can_check,
    register_check,
    checks_left,
)

PAGE_ID = 1039


def main():

    data = load_d(
        CACHE_DIR / f"{PAGE_ID}_script.js"
    )

    puzzle = decode(data)

    settings = LessonSettings(
        check_delay=5,
        max_checks=3,
    )

    session = GameSession(
        puzzle=puzzle,
        settings=settings,
    )

    print()

    print("First check")

    allowed, message = can_check(session)

    print(allowed, message)

    if allowed:
        register_check(session)

    print(
        "Checks left:",
        checks_left(session),
    )

    print()

    print("Second check immediately")

    allowed, message = can_check(session)

    print(allowed, message)

    print(
        "Checks left:",
        checks_left(session),
    )


if __name__ == "__main__":
    main()
