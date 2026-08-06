"""
Example: create a lesson rubric.
"""

from core.lesson.criterion import Criterion
from core.lesson.rubric import Rubric


def main() -> None:
    rubric = Rubric(
        criteria=[
            Criterion(
                id="accuracy",
                title="Solution accuracy",
                weight=0.7,
            ),
            Criterion(
                id="time",
                title="Completion time",
                weight=0.2,
            ),
            Criterion(
                id="hypothesis",
                title="Hypothesis quality",
                weight=0.1,
            ),
        ]
    )

    print(rubric)

    print()

    print("Criteria")

    for criterion in rubric.criteria:
        print(
            f"{criterion.id:12} "
            f"{criterion.title:24} "
            f"{criterion.weight:.1f}"
        )


if __name__ == "__main__":
    main()
