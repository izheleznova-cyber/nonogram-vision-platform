from core.puzzle.player import PlayerBoard


def print_board(board: PlayerBoard) -> None:
    """
    Print player board.
    """

    symbols = {
        0: ".",
        1: "#",
        2: "X",
    }

    for row in board.cells:
        print(
            " ".join(
                symbols[cell]
                for cell in row
            )
        )


def main():

    board = PlayerBoard.create(
        width=8,
        height=6,
    )

    print("=" * 40)
    print("EMPTY")
    print("=" * 40)

    print_board(board)

    board.fill(1, 2)
    board.fill(1, 3)

    board.cross(4, 5)

    board.fill(0, 0)

    print()

    print("=" * 40)
    print("AFTER MOVES")
    print("=" * 40)

    print_board(board)

    board.clear(1, 2)

    print()

    print("=" * 40)
    print("AFTER CLEAR")
    print("=" * 40)

    print_board(board)


if __name__ == "__main__":
    main()
