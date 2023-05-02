from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE, COLOR_NEON_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Hexagon, Rectangle


def create_middle(state, all_button_text):
    spacer = state.display.get_width() * .01
    hex_initial_pos = state.display.get_height() / 3

    left_x_offset = hex_initial_pos - spacer * 3
    right_x_offset = hex_initial_pos + spacer * 3

    button_height = 0.0625 * state.display.get_height()

    button_gap = button_height * .5
    next_button_y_pos = spacer + (button_height * 2)

    # Calculate the total height of the button group
    num_rows = (len(all_button_text) + 1) // 2
    total_height = num_rows * (button_height + spacer)

    # Header height
    header_height_offset = (.125 * state.display.get_height()) + 5

    # Remaining screen height after accounting for the header
    remaining_screen_height = state.display.get_height() + header_height_offset

    # Compute the starting y-coordinate for the first button, placing the middle button at the center
    middle_button_index = len(all_button_text) // 2
    start_y = (remaining_screen_height - total_height) / 2 + header_height_offset - middle_button_index * next_button_y_pos - button_gap

    width = state.display.get_width() / 3

    for i in range(len(all_button_text)):
        button_x = left_x_offset
        if i % 2 == 1:
            button_x = right_x_offset
        button_y = start_y + i * next_button_y_pos

        hex_button = draw_button(state, '', button_x, button_y, button_height)

        rec = Rectangle(
            x=button_x + button_height + spacer, y=button_y - button_gap, w=width, h=button_height,
            font_color=COLOR_NEON_ORANGE,
            text=all_button_text[i]
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
