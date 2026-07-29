from core.dataset.lesson_builder import build_lesson
from core.dataset.passport_reader import read_passports
from core.dataset.paths import DATASET_ROOT
from core.dataset.paths import WORKBOOK


def main():

    records = read_passports(WORKBOOK)

    lesson = build_lesson(
        records=records,
        lesson_dir=DATASET_ROOT / "lessons" / "lesson01_build",
        name="lesson01_build",
        title="Первые шаги",
        max_width=10,
        max_height=10,
    )

    print(lesson.name)
    print(len(lesson.puzzle_ids))


if __name__ == "__main__":
    main()
