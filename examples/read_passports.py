from core.dataset.paths import WORKBOOK
from core.dataset.passport_reader import read_passports


passports = read_passports(WORKBOOK)

print(f"Всего паспортов: {len(passports)}")

for passport in passports[:5]:
    print(passport)
