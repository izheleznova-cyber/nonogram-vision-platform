"""
Download HTML pages for the reference dataset.
"""

from __future__ import annotations

from core.dataset.builder import build_reference_dataset
from core.dataset.html_loader import download_html
from core.dataset.passport_reader import read_passports
from core.dataset.paths import WORKBOOK
from core.dataset.paths import get_html_path


def main() -> None:

    passports = read_passports(WORKBOOK)

    dataset = build_reference_dataset(passports)

    print("=" * 60)
    print("DOWNLOAD REFERENCE HTML")
    print("=" * 60)
    print()

    for passport in dataset:

        save_path = get_html_path(
            passport.source,
            passport.page_id,
        )

        print(f"Downloading {passport.page_id}...")

        downloaded = download_html(
            passport.url,
            save_path,
        )

        status = "Downloaded" if downloaded else "Cached"

        print(f"{status:10} {save_path}")

    print()
    print(f"Total: {len(dataset)}")


if __name__ == "__main__":
    main()