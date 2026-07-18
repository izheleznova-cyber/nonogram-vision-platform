"""
download_html.py

Download HTML page for one nonogram from the passport.
"""

from __future__ import annotations

from core.dataset.html_loader import download_html
from core.dataset.passport_reader import read_passports
from core.dataset.paths import get_html_path


PASSPORT_INDEX = 0


def main() -> None:
    passports = read_passports()

    passport = passports[PASSPORT_INDEX]

    save_path = get_html_path(
        source=passport.source,
        page_id=passport.page_id,
    )

    downloaded = download_html(
        url=passport.url,
        save_path=save_path,
    )

    print()
    print(f"Worksheet : {passport.worksheet_name}")
    print(f"URL       : {passport.url}")
    print(f"HTML      : {save_path}")

    if downloaded:
        print("Status    : downloaded")
    else:
        print("Status    : already exists")


if __name__ == "__main__":
    main()
