"""
Example: create an educational asset.
"""

from core.lesson.asset import Asset


def main() -> None:
    asset = Asset(
        id="IMG000005",
        type="Nonogram",
        passport="passports/IMG000005.json",
    )

    print(asset)

    print()

    print("Fields")
    print(f"id        : {asset.id}")
    print(f"type      : {asset.type}")
    print(f"passport  : {asset.passport}")


if __name__ == "__main__":
    main()
