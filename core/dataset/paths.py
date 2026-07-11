"""
paths.py

Единое описание структуры проекта и датасета.

Проект предполагает следующую структуру каталогов:

cv-projects/
│
├── nonogram-vision-platform/
│
└── nonogram-dataset/
    ├── source/
    ├── html/
    ├── json/
    ├── cache/
    ├── preview/
    └── backups/

Все остальные модули должны использовать пути только
через этот файл.
"""

from pathlib import Path


# =============================================================================
# Project
# =============================================================================

#: Корень репозитория nonogram-vision-platform
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# =============================================================================
# Dataset
# =============================================================================

#: Корень датасета
DATASET_ROOT = PROJECT_ROOT.parent / "nonogram-dataset"


# =============================================================================
# Source data
# =============================================================================

SOURCE_DIR = DATASET_ROOT / "source"

WORKBOOK = SOURCE_DIR / "nonogram_passports.xlsm"

IMAGES_DIR = SOURCE_DIR / "images"


# =============================================================================
# HTML cache
# =============================================================================

HTML_DIR = DATASET_ROOT / "html"

NONOGRAMS_HTML_DIR = HTML_DIR / "nonograms"

NONOGRAMS2_HTML_DIR = HTML_DIR / "nonograms2"


# =============================================================================
# JSON database
# =============================================================================

JSON_DIR = DATASET_ROOT / "json"

BW_JSON_DIR = JSON_DIR / "bw"

COLOR_JSON_DIR = JSON_DIR / "color"


# =============================================================================
# Other directories
# =============================================================================

CACHE_DIR = DATASET_ROOT / "cache"

PREVIEW_DIR = DATASET_ROOT / "preview"

BACKUPS_DIR = DATASET_ROOT / "backups"


# =============================================================================
# Helper functions
# =============================================================================

def get_html_path(source: str, page_id: int) -> Path:
    """
    Возвращает путь к HTML-файлу кроссворда.

    Parameters
    ----------
    source : str
        Источник ("nonograms" или "nonograms2").

    page_id : int
        Идентификатор страницы.

    Returns
    -------
    Path
        Полный путь к HTML-файлу.

    Examples
    --------
    >>> get_html_path("nonograms", 16323)
    .../html/nonograms/16323.html

    >>> get_html_path("nonograms2", 14596)
    .../html/nonograms2/14596.html
    """

    if source == "nonograms":
        folder = NONOGRAMS_HTML_DIR

    elif source == "nonograms2":
        folder = NONOGRAMS2_HTML_DIR

    else:
        raise ValueError(
            f"Unknown source: {source}"
        )

    return folder / f"{page_id}.html"
