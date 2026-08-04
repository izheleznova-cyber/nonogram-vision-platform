"""
Generate preview cache for every puzzle.
"""

from pathlib import Path

from core.dataset.passport_database import PassportDatabase
from core.dataset.paths import PREVIEW_DIR

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import get_html_path

from core.puzzle.renderer import render_png


database = PassportDatabase()

PREVIEW_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

for passport in database.records:

    print(passport.id)

    html_path = get_html_path(
        passport.source,
        passport.page_id,
    )

    d = load_d(html_path)

    puzzle = decode(d)

    output = PREVIEW_DIR / f"{passport.id}.png"

    render_puzzle(
        puzzle,
        output,
        preview=True,
        cell_size=4,
    )
