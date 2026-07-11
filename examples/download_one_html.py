"""
download_one_html.py

Пример загрузки одной HTML-страницы с сайта nonograms.ru.

Скрипт:

1. читает коллекцию паспортов;
2. выбирает первый черно-белый (BW) кроссворд;
3. скачивает HTML;
4. сохраняет страницу в HTML-кэш.
"""

from core.dataset.html_loader import download_html
from core.dataset.passport_reader import read_passports
from core.dataset.paths import (
    WORKBOOK,
    get_html_path,
)


def main() -> None:

    passports = read_passports(WORKBOOK)

    # Берем первый BW-кроссворд
    passport = next(
        p for p in passports
        if p.color_type == "BW"
    )

    html_path = get_html_path(
        passport.source,
        passport.page_id,
    )

    print(f"Worksheet : {passport.worksheet_name}")
    print(f"URL       : {passport.url}")
    print(f"Save to   : {html_path}")

    download_html(
        passport.url,
        html_path,
    )

    print()
    print("Download completed successfully.")


if __name__ == "__main__":
    main()
