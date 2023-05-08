from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE, COLOR_NEON_ORANGE
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
    back_x_pos = (state.display.get_width() / 6)
    share_x_pos = (state.display.get_width() / 6 * 5)
    height = 0.062 * state.display.get_height()
    y_pos = (.125 * state.display.get_height() + 5) - height

    back_text = 'Leave'
    share_text = 'Share'

    back_hex = Hexagon(back_x_pos, y_pos, height, height, back_text)
    share_hex = Hexagon(share_x_pos, y_pos, height, height, share_text)

    back_hex.draw(state.display, COLOR_ORANGE, COLOR_BLACK, COLOR_NEON_ORANGE)
    back_hex.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)

    share_hex.draw(state.display, COLOR_ORANGE, COLOR_BLACK, COLOR_NEON_ORANGE)
    share_hex.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)

    state.buttons[back_text] = back_hex.is_hover()
    state.buttons[share_text] = share_hex.is_hover()


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
