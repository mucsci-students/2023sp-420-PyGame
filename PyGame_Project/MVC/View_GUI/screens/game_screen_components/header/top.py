from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE, COLOR_INVALID_COLOR, COLOR_VALID_COLOR
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle


def create_top(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.0625 * state.display.get_height()

    if state.current_guess_state == state.guess_state.INCORRECT:
        font_color = COLOR_INVALID_COLOR
    elif state.current_guess_state == state.guess_state.CORRECT:
        font_color = COLOR_VALID_COLOR
    else:
        font_color = COLOR_ORANGE

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=font_color,
        text="Toggle Guessed Words"
    )
    shape.draw(state.display, color=COLOR_BLACK)
    state.buttons[shape.text] = shape.is_hover()

    if shape.is_hover():
        shape.change_colors(state.display, COLOR_WHITE, COLOR_ORANGE, "Toggle Guessed Words")
