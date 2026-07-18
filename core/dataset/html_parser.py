"""
html_parser.py

Utilities for parsing downloaded HTML pages.
"""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import Tag


def load_html(html_path: Path) -> BeautifulSoup:
    """
    Load HTML file and return BeautifulSoup object.
    """

    html = html_path.read_text(
        encoding="utf-8",
    )

    return BeautifulSoup(
        html,
        "html.parser",
    )


def find_puzzle_script(soup: BeautifulSoup) -> Tag:
    """
    Return the <script> element containing puzzle data.

    Raises
    ------
    ValueError
        If no puzzle script is found.
    """

    for script in soup.find_all("script"):

        text = script.get_text()

        if "var d" in text:
            return script

    raise ValueError(
        "Puzzle script not found."
    )