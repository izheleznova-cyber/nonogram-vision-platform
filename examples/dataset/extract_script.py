"""
extract_script.py

Извлекает встроенный JavaScript с данными кроссворда
из HTML-страницы и сохраняет его отдельно.

Используется для исследования структуры JavaScript
перед написанием html_parser.py.
"""

from bs4 import BeautifulSoup

from core.dataset.paths import (
    CACHE_DIR,
    get_html_path,
)


SOURCE = "nonograms"
PAGE_ID = 1039


def main() -> None:

    html_path = get_html_path(
        SOURCE,
        PAGE_ID,
    )

    print(f"Reading: {html_path}")

    html = html_path.read_text(
        encoding="utf-8",
    )

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    scripts = soup.find_all("script")

    target_script = None

    for script in scripts:

        text = script.get_text()

        if "var d=" in text or "var d =" in text:

            target_script = text
            break

    if target_script is None:

        print("Embedded puzzle script not found.")
        return

    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = CACHE_DIR / f"{PAGE_ID}_script.js"

    output_file.write_text(
        target_script,
        encoding="utf-8",
    )

    print()
    print("JavaScript extracted successfully.")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()
