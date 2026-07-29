from core.dataset.lesson_loader import load_lesson
from core.dataset.paths import DATASET_ROOT


def main():

    lesson = load_lesson(
        DATASET_ROOT / "lessons" / "lesson01_build"
    )

    print("=" * 60)
    print(lesson.name)
    print("=" * 60)

    print()

    print(f"Puzzles: {len(lesson.puzzle_ids)}")

    print()

    for puzzle_id in lesson.puzzle_ids:
        print(puzzle_id)


if __name__ == "__main__":
    main()
