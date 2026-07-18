"""
inspect_html.py

Inspect downloaded HTML page.
"""

from __future__ import annotations

from core.dataset.html_parser import load_html
from core.dataset.paths import get_html_path


SOURCE = "nonograms"
PAGE_ID = 73190


def main() -> None:

    html_path = get_html_path(
        SOURCE,
        PAGE_ID,
    )

    soup = load_html(html_path)

    print("=" * 60)
    print("HTML")
    print("=" * 60)

    print()

    print(soup.title.string)

    scripts = soup.find_all("script")

    print(f"Scripts: {len(scripts)}")

    for i, script in enumerate(scripts):
        print(
            f"{i:02d}: {len(script.get_text())} chars"
        )


if __name__ == "__main__":
    main()
