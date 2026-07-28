"""
Extract JavaScript from the reference HTML pages.
"""

from __future__ import annotations

from core.dataset.builder import build_reference_dataset
from core.dataset.html_parser import (
    load_html,
    find_puzzle_script,
)
from core.dataset.passport_reader import read_passports
from core.dataset.paths import (
    WORKBOOK,
    CACHE_DIR,
    get_html_path,
)


def main() -> None:

    passports = read_passports(WORKBOOK)

    dataset = build_reference_dataset(passports)

    print("=" * 60)
    print("EXTRACT REFERENCE SCRIPTS")
    print("=" * 60)
    print()

    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    for passport in dataset:

        html_path = get_html_path(
            passport.source,
            passport.page_id,
        )

        print(f"Processing {passport.page_id}...")

        soup = load_html(html_path)

        script = find_puzzle_script(soup)

        script_path = (
            CACHE_DIR
            / f"{passport.page_id}_script.js"
        )

        script_path.write_text(
            script.get_text(),
            encoding="utf-8",
        )

        print(
            f"Saved {script_path.name}"
        )

    print()
    print(f"Total: {len(dataset)}")


if __name__ == "__main__":
    main()
