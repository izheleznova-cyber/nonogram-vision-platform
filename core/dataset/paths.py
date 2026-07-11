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
