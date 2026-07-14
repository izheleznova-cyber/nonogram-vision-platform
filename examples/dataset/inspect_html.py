"""
inspect_html.py

Исследование HTML-страницы nonograms.ru.

Скрипт НЕ парсит кроссворд.

Он помогает понять структуру HTML перед написанием
html_parser.py.
"""

from bs4 import BeautifulSoup

from core.dataset.paths import get_html_path


SOURCE = "nonograms"
PAGE_ID =  1039


def main() -> None:

    html_path = get_html_path(
        SOURCE,
        PAGE_ID,
    )

    print("=" * 60)
    print("HTML INSPECTION")
    print("=" * 60)
    print()

    print(f"File : {html_path}")
    print()

    html = html_path.read_text(
        encoding="utf-8",
    )

    print(f"HTML size : {len(html):,} characters")
    print()

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    scripts = soup.find_all("script")

    print(f"Scripts found : {len(scripts)}")
    print()

    print("-" * 60)

    for i, script in enumerate(scripts):

        text = script.get_text().strip()

        print("-" * 60)
        print(f"[{i:02}] {len(text):7} characters")

        if script.get("src"):
            print(f"src : {script['src']}")

        elif text:
            preview = text.replace("\n", " ")
            preview = preview[:200]

            print(preview)

        else:
            print("(empty)")

    print("-" * 60)


if __name__ == "__main__":
    main()
