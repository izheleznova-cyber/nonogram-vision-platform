from core.puzzle.player import PlayerBoard
from core.puzzle.player import EMPTY


def main():

    board = PlayerBoard.create(
        width=5,
        height=4,
    )

    print("=" * 40)
    print("PLAYER BOARD")
    print("=" * 40)

    print(f"Width : {board.width}")
    print(f"Height: {board.height}")

    print()

    print("Cells:")

    for row in board.cells:
        print(row)

    print()

    #
    # Simple checks
    #

    assert board.width == 5
    assert board.height == 4

    assert len(board.cells) == 4

    assert len(board.cells[0]) == 5

    for row in board.cells:
        assert all(cell == EMPTY for cell in row)

    print("OK")



if __name__ == "__main__":
    main()
