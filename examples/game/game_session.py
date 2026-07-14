"""
game_session.py

Example of a complete game session.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.game.settings import LessonSettings
from core.game.session import GameSession


PAGE_ID = 1039


def print_actions(session: GameSession) -> None:
    """
    Print action history.
    """

    print()

    print("=" * 60)
    print("ACTIONS")
    print("=" * 60)

    if not session.actions:
        print("No actions.")
        return

    for action in session.actions:

        print(
            f"{action.action:6s}"
            f"  row={action.row:2d}"
            f"  col={action.column:2d}"
        )


def print_predictions(session: GameSession) -> None:
    """
    Print prediction history.
    """

    print()

    print("=" * 60)
    print("PREDICTIONS")
    print("=" * 60)

    if not session.predictions:
        print("No predictions.")
        return

    for prediction in session.predictions:

        print(
            f"{prediction.progress * 100:6.1f}%"
            f"   {prediction.text}"
        )


def main():

    print("=" * 60)
    print("GAME SESSION")
    print("=" * 60)

    #
    # Load puzzle
    #

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    #
    # Create lesson settings
    #

    settings = LessonSettings()

    #
    # Start session
    #

    session = GameSession(
        puzzle=puzzle,
        settings=settings,
    )

    print()

    print("Puzzle size:")

    print(
        f"{puzzle.width} x {puzzle.height}"
    )

    print()

    print(
        f"Filled cells in solution: "
        f"{session.solution_cells()}"
    )

    #
    # Simulate several moves
    #

    session.fill(0, 0)
    session.fill(0, 1)

    session.cross(3, 5)

    session.fill(8, 10)

    session.clear(0, 1)

    #
    # Student hypotheses
    #

    session.add_prediction(
        "Птица"
    )

    session.fill(15, 18)

    session.fill(15, 19)

    session.fill(15, 20)

    session.add_prediction(
        "Вертолет"
    )

    #
    # Statistics
    #

    print()

    print("=" * 60)
    print("STATISTICS")
    print("=" * 60)

    print(
        f"Player filled cells : "
        f"{session.filled_cells()}"
    )

    print(
        f"Solution filled cells: "
        f"{session.solution_cells()}"
    )

    print(
        f"Progress: "
        f"{session.progress() * 100:.2f}%"
    )

    print(
        f"Elapsed time: "
        f"{session.elapsed_time():.2f} s"
    )

    print_actions(session)

    print_predictions(session)


if __name__ == "__main__":
    main()
