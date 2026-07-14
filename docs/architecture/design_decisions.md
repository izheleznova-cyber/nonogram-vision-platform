DD-001
Датасет хранится вне репозитория.

Причина:
репозиторий должен содержать только код. 

DD-002
Имя HTML-файла вычисляется автоматически из URL.

Причина:

исляемые данные.

DD-003
Geometry отделена от Metadata.

Причина:
геометрия и экспертная разметка развиваются независимо.

Renderer architecture

render_puzzle()
    ├── _draw_grid()
    ├── _draw_row_hints()
    ├── _draw_column_hints()
    └── _draw_cells()

Layout is responsible only for geometry.
Renderer performs no layout calculations.
