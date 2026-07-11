"""
core/dataset/html_loader.py

Загрузка HTML-кэша страниц nonograms.ru.
"""

from pathlib import Path
import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}


def download_html(url: str, save_path: Path, overwrite: bool = False) -> bool:
    """
    Скачать HTML-страницу.

    Parameters
    ----------
    url
        URL страницы.

    save_path
        Куда сохранить html.

    overwrite
        Перезаписывать существующий файл.

    Returns
    -------
    bool

        True  — файл скачан.

        False — файл уже существовал.
    """

    if save_path.exists() and not overwrite:
        return False

    save_path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20,
    )

    response.raise_for_status()

    save_path.write_text(
        response.text,
        encoding="utf-8",
    )

    return True
