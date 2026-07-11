"""
nonograms_url.py

Вспомогательные функции для работы с URL сайта nonograms.ru.

Модуль отвечает только за разбор URL и получение
идентифицирующей информации.

Например:

https://www.nonograms.ru/nonograms/i/16323

↓

source  = "nonograms"
page_id = 16323
"""

from urllib.parse import urlparse


def get_source(url: str) -> str:
    """
    Возвращает источник кроссворда.

    Parameters
    ----------
    url : str
        URL страницы nonograms.ru.

    Returns
    -------
    str
        "nonograms" или "nonograms2"

    Examples
    --------
    >>> get_source("https://www.nonograms.ru/nonograms/i/16323")
    'nonograms'

    >>> get_source("https://www.nonograms.ru/nonograms2/i/14596")
    'nonograms2'
    """

    parts = urlparse(url).path.split("/")

    return parts[1]


def get_page_id(url: str) -> int:
    """
    Возвращает числовой идентификатор страницы.

    Parameters
    ----------
    url : str
        URL страницы nonograms.ru.

    Returns
    -------
    int
        Идентификатор страницы.

    Examples
    --------
    >>> get_page_id("https://www.nonograms.ru/nonograms/i/16323")
    16323

    >>> get_page_id("https://www.nonograms.ru/nonograms2/i/14596")
    14596
    """

    return int(url.rstrip("/").split("/")[-1])
