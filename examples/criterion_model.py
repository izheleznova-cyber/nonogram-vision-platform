"""
Example: create a lesson assessment criterion.
"""

from core.lesson.criterion import Criterion


def main() -> None:
    criterion = Criterion(
        id="accuracy",
        title="Solution accuracy",
        weight=0.7,
    )

    print(criterion)

    print()

    print("Fields")
    print(f"id     : {criterion.id}")
    print(f"title  : {criterion.title}")
    print(f"weight : {criterion.weight}")


if __name__ == "__main__":
    main()
