from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE, COLOR_NEON_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Hexagon, Rectangle
buttons = ['New Game', 'Load Game', 'Help', 'High Scores', 'Exit']


def create_middle(state):

    hex_initial_pos = state.display.get_height() / 3
    spacer = state.display.get_width() * .01

    left_x_offset = hex_initial_pos - spacer * 3
    right_x_offset = hex_initial_pos + spacer * 3

    height = 0.0625 * state.display.get_height()
    height_offset = height * .5

    total_height = 5 * height + 4 * spacer
    start_y = (state.display.get_height() - total_height) / 2 - height
    y_pos_offset = spacer + (height * 2)

    width = state.display.get_width() / 3

    for i in range(5):
        button_x = left_x_offset
        if i % 2 == 1:
            button_x = right_x_offset
        button_y = start_y + i * (y_pos_offset if i > 0 else 0)

        hex_button = draw_button(state, '', button_x, button_y, height)

        rec = Rectangle(
            x=button_x + height + spacer, y=button_y - height_offset, w=width, h=height,
            font_color=COLOR_NEON_ORANGE,
            text=buttons[i]
        )
        rec.draw(state.display, COLOR_BLACK)

        if rec.is_hover():
            rec.change_colors(state.display, COLOR_ORANGE, COLOR_ORANGE, rec.text)

        if rec.is_hover() or hex_button.is_hover():
            state.buttons[rec.text] = True
        else:
            state.buttons[rec.text] = False


def draw_button(state, text, x, y, w):
    hexagon = Hexagon(x, y, w, w, text)
    hexagon.draw(state.display, COLOR_ORANGE, COLOR_BLACK, COLOR_NEON_ORANGE)
    hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)
    return hexagon
