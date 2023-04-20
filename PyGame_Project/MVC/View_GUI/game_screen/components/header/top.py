from ...colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE
from ..shapes import Rectangle


def create_top(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.0625 * state.display.get_height()

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=COLOR_ORANGE,
        text='Show Guessed Words'
    )
    shape.draw(state.display, color=COLOR_BLACK)

    if shape.is_hover():
        shape.change_colors(state.display, COLOR_WHITE, COLOR_ORANGE, 'Show Guessed Words')
