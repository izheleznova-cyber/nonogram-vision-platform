"""
test_nonograms_url.py

Тесты для функций разбора URL сайта nonograms.ru.
"""

from core.dataset.nonograms_url import (
    get_page_id,
    get_source,
)


def test_get_source_nonograms():
    url = "https://www.nonograms.ru/nonograms/i/16323"

    assert get_source(url) == "nonograms"


def test_get_source_nonograms2():
    url = "https://www.nonograms.ru/nonograms2/i/14596"

    assert get_source(url) == "nonograms2"


def test_get_page_id_nonograms():
    url = "https://www.nonograms.ru/nonograms/i/16323"

    assert get_page_id(url) == 16323


def test_get_page_id_nonograms2():
    url = "https://www.nonograms.ru/nonograms2/i/14596"

    assert get_page_id(url) == 14596
