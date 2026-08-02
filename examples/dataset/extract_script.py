"""
extract_script.py

Extract embedded JavaScript (var d)
from downloaded HTML pages and save
it into cache/.

Can be executed repeatedly.
Already extracted scripts are skipped.
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from core.dataset.paths import (
    CACHE_DIR,
    WORKBOOK,
    get_html_path,
)
from core.dataset.passport_reader import read_passports


def main() -> None:

    passports = read_passports(WORKBOOK)

    print("=" * 60)
    print("EXTRACT JAVASCRIPT")
    print("=" * 60)
    print()

    print(f"Passports: {len(passports)}")
    print()

    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    created = 0
    cached = 0
    missing = 0

    for passport in passports:

        html_path = get_html_path(
            passport.source,
            passport.page_id,
        )

        #
        # HTML not downloaded.
        #
        if not html_path.exists():
            print(f"HTML missing : {passport.page_id}")
            missing += 1
            continue

        output_file = CACHE_DIR / f"{passport.page_id}_script.js"

        #
        # Script already exists.
        #
        if output_file.exists():
            cached += 1
            continue

        print(f"Reading: {html_path}")

        html = html_path.read_text(
            encoding="utf-8",
        )

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        target_script = None

        for script in soup.find_all("script"):

            text = script.get_text()

            if "var d=" in text or "var d =" in text:
                target_script = text
                break

        if target_script is None:
            print(f"Script not found: {passport.page_id}")
            continue

        output_file.write_text(
            target_script,
            encoding="utf-8",
        )

        created += 1

        print(f"Saved: {output_file}")

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)
    print()

    print(f"Passports        : {len(passports)}")
    print(f"Created scripts  : {created}")
    print(f"Already cached   : {cached}")
    print(f"Missing HTML     : {missing}")


if __name__ == "__main__":
    main()