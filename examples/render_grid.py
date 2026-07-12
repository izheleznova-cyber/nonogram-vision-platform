"""
Render empty grid.
"""

from core.dataset.d_decoder import decode
from core.dataset.d_parser import parse_d
from core.dataset.html_loader import load_html
from core.puzzle.layout import calculate_layout
from core.puzzle.renderer import render_grid


html = load_html(4466)

d = parse_d(html)

puzzle = decode(d)

layout = calculate_layout(puzzle)

image = render_grid(
    puzzle,
    layout,
)

image.save("grid.png")

print("Saved grid.png")
