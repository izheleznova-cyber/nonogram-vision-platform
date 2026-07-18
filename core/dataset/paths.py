"""
paths.py

Единое описание структуры проекта и датасета.

Структура:

cv-projects/
│
├── nonogram-vision-platform/
│
└── nonogram-dataset/
    ├── source/
    ├── html/
    │   ├── nonograms/
    │   └── nonograms2/
    ├── json/
    │   ├── bw/
    │   └── color/
    ├── cache/
    ├── preview/
    └── backups/
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
# Source
# =============================================================================

SOURCE_DIR = DATASET_ROOT / "source"

WORKBOOK = SOURCE_DIR / "nonogram_passports.xlsm"

IMAGES_DIR = SOURCE_DIR / "images"


# =============================================================================
# HTML
# =============================================================================

HTML_DIR = DATASET_ROOT / "html"

NONOGRAMS_HTML_DIR = HTML_DIR / "nonograms"

NONOGRAMS2_HTML_DIR = HTML_DIR / "nonograms2"


# =============================================================================
# JSON
# =============================================================================

JSON_DIR = DATASET_ROOT / "json"

BW_JSON_DIR = JSON_DIR / "bw"

COLOR_JSON_DIR = JSON_DIR / "color"


# =============================================================================
# Other folders
# =============================================================================

CACHE_DIR = DATASET_ROOT / "cache"

PREVIEW_DIR = DATASET_ROOT / "preview"

BACKUPS_DIR = DATASET_ROOT / "backups"


# =============================================================================
# Helpers
# =============================================================================

def get_html_path(source: str, page_id: int) -> Path:
    """
    Возвращает путь к HTML-файлу кроссворда.

    Parameters
    ----------
    source
        "nonograms" или "nonograms2"

    page_id
        Идентификатор страницы.

    Returns
    -------
    Path
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