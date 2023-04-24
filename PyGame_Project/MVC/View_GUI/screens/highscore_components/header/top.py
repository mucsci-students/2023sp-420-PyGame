from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle


def create_top(state):
    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = .125 * state.display.get_height()

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=COLOR_ORANGE,
        text="HIGH SCORES"
    )
    shape.draw(state.display, color=COLOR_BLACK)


def create_description(state):
    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.0625 * state.display.get_height()
    spacer = state.display.get_height() * .01
    y_offset = .125 * state.display.get_height() + spacer

    shape = Rectangle(
        x=buffer, y=y_offset, w=width, h=height,
        font_color=COLOR_ORANGE,
        text=f'Required Letter: {state.required_letter.upper()},  Puzzle Letters: {state.current_puzzle.upper()}'
    )

    shape.draw(state.display, color=COLOR_BLACK)
