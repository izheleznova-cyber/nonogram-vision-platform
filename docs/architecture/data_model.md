# Data Model

Версия: 1.0

Документ описывает внутреннюю модель данных проекта.

Любой источник данных (Excel, HTML, PNG, JSON)
должен преобразовываться в PuzzleModel.

Ни один алгоритм не должен работать напрямую
с Excel или HTML.

PuzzleModel
                   /           \
                  /             \
                 /               \
        PuzzleGeometry     PuzzleMetadata


 PuzzleGeometry

| Поле      | Тип             | Обязательное | Источник      |
| --------- | --------------- | ------------ | ------------- |
| width     | int             | Да           | HTML / Vision |
| height    | int             | Да           | HTML / Vision |
| row_hints | list[list[int]] | Да           | HTML / Vision |
| col_hints | list[list[int]] | Да           | HTML / Vision |
| solution  | list[list[int]] | Да           | HTML / Vision |

PuzzleMetadata

| Поле              | Тип       | Обязательное | Источник |
| ----------------- | --------- | ------------ | -------- |
| id                | int       | Да           | URL      |
| source            | str       | Да           | URL      |
| title             | str       | Да           | Excel    |
| author_title      | str       | Нет          | Excel    |
| category          | str       | Нет          | Excel    |
| subcategory       | str       | Нет          | Excel    |
| synonyms          | list[str] | Нет          | Excel    |
| recognition_level | int       | Нет          | Excel    |
| difficulty        | int       | Нет          | Excel    |
| difficulty_reason | str       | Нет          | Excel    |
| emotion           | str       | Нет          | Excel    |
| minimal_detail    | bool      | Нет          | Excel    |
| density           | float     | Нет          | Авто     |
| occlusion         | bool      | Нет          | Эксперт  |
| perspective       | bool      | Нет          | Эксперт  |
| has_face          | bool      | Нет          | Эксперт  |
| color_type        | str       | Да           | Excel    |


PassportRecord

Это объект,который возвращает   passport_reader.py

Он содержит только то,  что хранится в Excel. 
| Поле           | Тип            |
| -------------- | -------------- |
| url            | str            |
| worksheet_name | str            |
| metadata       | PuzzleMetadata |

HTMLRecord

Получается после загрузки страницы.

Поле	Тип
url	str
html	str

PuzzleModel

Самая главная сущность.

PuzzleModel
Поле
geometry
metadata



Data Pipeline
Excel
        │
        ▼
PassportRecord
        │
        ▼
HTML Loader
        │
        ▼
HTMLRecord
        │
        ▼
HTML Parser
        │
        ▼
PuzzleModel
        │
        ▼
JSON Writer
        │
        ▼
JSON


Vision Pipeline
PNG
 │
 ▼
Image
 │
 ▼
Grid
 │
 ▼
PuzzleGeometry
 │
 ▼
PuzzleModel






Источники данных 
| Источник | Что содержит  |
| -------- | ------------- |
| Excel    | Метаданные    |
| HTML     | Геометрию     |
| PNG      | Изображение   |
| JSON     | Полную модель |


Инварианты проекта 
1. Геометрия никогда не содержит экспертной информации.

2. Метаданные никогда не содержат геометрии.

3. Любой источник данных должен преобразовываться в PuzzleModel.

4. GUI работает только с PuzzleModel.

5. Алгоритмы Computer Vision работают только с PuzzleGeometry.

6. Excel никогда не используется как рабочая база данных.

7. JSON является рабочим форматом хранения.
