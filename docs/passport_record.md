PassportRecord

Это объект, который представляет один лист Excel.

Он не содержит HTML.

Он не содержит PuzzleGeometry.

Он содержит только информацию, необходимую для дальнейшего конвейера.

Поля

Например

Поле	Тип	Откуда берётся
worksheet_name	str	Excel
url	str	B2
source	str	вычисляется
page_id	int	вычисляется
color_type	str	K21
metadata	PuzzleMetadata	Excel
Инварианты

Например

url обязательно существует

page_id всегда > 0

source всегда
    nonograms
или
    nonograms2

metadata никогда не None
Что умеет PassportRecord

Ничего.

Это просто контейнер данных.
