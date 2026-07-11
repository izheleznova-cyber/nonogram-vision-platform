from dataclasses import dataclass


@dataclass
class PassportRecord:
    worksheet_name: str
    url: str
    source: str
    page_id: int
    color_type: str
