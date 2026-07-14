"""
download_test_page.py

Загрузка произвольной страницы nonograms.ru.

Используется для исследования структуры HTML.
Не зависит от Excel и PassportReader.
"""

from core.dataset.html_loader import download_html
from core.dataset.paths import get_html_path


# ------------------------------------------------------------
# Исследуемая страница
# ------------------------------------------------------------

SOURCE = "nonograms"
PAGE_ID = 1039


def main() -> None:

    url = (
        f"https://www.nonograms.ru/"
        f"{SOURCE}/i/{PAGE_ID}"
    )

    html_path = get_html_path(
        SOURCE,
        PAGE_ID,
    )

    print("=" * 60)
    print("DOWNLOAD TEST PAGE")
    print("=" * 60)

    print(f"URL      : {url}")
    print(f"Save to  : {html_path}")
    print()

    download_html(
        url,
        html_path,
    )

    print("Download completed successfully.")


if __name__ == "__main__":
    main()
