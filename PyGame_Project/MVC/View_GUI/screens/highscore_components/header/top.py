from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle, Hexagon


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


def create_back_button(state):
        left_x_offset = (state.display.get_width() / 6) * .33
        right_x_offset = state.display.get_width() - left_x_offset
        height = 0.0625 * state.display.get_height()
        spacer = left_x_offset * 2.3
        y_pos = state.display.get_height() - height * 1.5
        y_pos_offset = y_pos - left_x_offset * 1.65
        save_x_pos = left_x_offset

        back_hex = Hexagon(save_x_pos, y_pos, spacer, height, 'Leave')

        back_hex.draw(state.display, COLOR_ORANGE, COLOR_BLACK, COLOR_BLACK)

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
