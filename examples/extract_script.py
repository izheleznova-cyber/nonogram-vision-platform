"""
Extract puzzle JavaScript from downloaded HTML.
"""

from __future__ import annotations

from core.dataset.html_parser import (
    load_html,
    find_puzzle_script,
)
from core.dataset.paths import (
    CACHE_DIR,
    get_html_path,
)

SOURCE = "nonograms"
PAGE_ID = 73190


def main() -> None:

    html_path = get_html_path(
        source=SOURCE,
        page_id=PAGE_ID,
    )

    soup = load_html(html_path)

    script = find_puzzle_script(soup)

    save_path = CACHE_DIR / f"{PAGE_ID}_script.js"

    save_path.write_text(
        script.get_text(),
        encoding="utf-8",
    )

    print()
    print(f"HTML   : {html_path}")
    print(f"Script : {save_path}")


if __name__ == "__main__":
    main()
