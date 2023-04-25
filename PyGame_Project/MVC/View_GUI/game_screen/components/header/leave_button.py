from ...colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE, COLOR_INVALID_COLOR, COLOR_VALID_COLOR
from ...components.shapes import Rectangle


def create_leave_button(state):
    buffer = state.display.get_width() / 10
    width = buffer * 3
    height = 0.0625 * state.display.get_height()
    y = height + 10

    if state.current_guess_state == state.guess_state.INCORRECT:
        font_color = COLOR_INVALID_COLOR
    elif state.current_guess_state == state.guess_state.CORRECT:
        font_color = COLOR_VALID_COLOR
    else:
        font_color = COLOR_ORANGE

    shape = Rectangle(
        x=buffer, y=y, w=width, h=height,
        font_color=font_color,
        text='Leave Game'
    )
    
    shape.draw(state.display, color=COLOR_BLACK)
    state.buttons['Leave Game'] = shape.is_hover()

    if shape.is_hover():
        shape.change_colors(state.display, COLOR_WHITE, COLOR_ORANGE, 'Leave Game')
