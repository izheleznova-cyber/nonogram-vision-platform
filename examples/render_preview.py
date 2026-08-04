"""
Generate preview cache for every puzzle.
"""

from core.dataset.passport_database import PassportDatabase
from core.dataset.paths import (
    CACHE_DIR,
    PREVIEW_DIR,
)

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode

from core.puzzle.renderer import render_puzzle


def main() -> None:
    """
    Generate preview PNG for every passport.
    """

    database = PassportDatabase()

    PREVIEW_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print()
    print("============================================")
    print("BUILD PREVIEW CACHE")
    print("============================================")
    print()

    for passport in database.records:

        print(f"{passport.id}  {passport.title}")

        #
        # Cached JavaScript
        #
        script = CACHE_DIR / f"{passport.page_id}_script.js"

        if not script.exists():

            print(f"  missing: {script.name}")
            continue

        #
        # Decode puzzle
        #
        data = load_d(script)

        puzzle = decode(data)

        #
        # Output PNG
        #
        output = PREVIEW_DIR / f"{passport.id}.png"

        render_puzzle(
            puzzle,
            output,
            preview=True,
            cell_size=4,
        )

    print()
    print("Done.")


if __name__ == "__main__":
    main()
