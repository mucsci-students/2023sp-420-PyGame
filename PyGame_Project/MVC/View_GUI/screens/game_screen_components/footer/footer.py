from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle, Hexagon
from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_NEON_ORANGE, COLOR_ORANGE, COLOR_INVALID_COLOR, COLOR_VALID_COLOR


def create_input_box(state):
    x_buffer = state.display.get_width() / 4
    width = x_buffer * 2
    height = 0.0625 * state.display.get_height()
    y_buffer = state.display.get_height() - (height * 2)

    if state.current_guess_state == state.guess_state.INCORRECT:
        font_color = COLOR_INVALID_COLOR
    elif state.current_guess_state == state.guess_state.CORRECT:
        font_color = COLOR_VALID_COLOR
    else:
        font_color = COLOR_ORANGE

    shape = Rectangle(
        x=x_buffer, y=y_buffer, w=width, h=height,
        font_color=font_color,
        text=state.current_guess
    )

    if len(state.current_guess) <= shape.grad_surface.get_width() // shape.font.size(state.current_guess)[1]:
        state.can_guess = True
    else:
        state.can_guess = False

    shape.draw(state.display, COLOR_BLACK)


def create_buttons(state):
    left_x_offset = (state.display.get_width() / 6) * .33
    right_x_offset = state.display.get_width() - left_x_offset
    height = 0.0625 * state.display.get_height()
    spacer = left_x_offset * 2.3
    y_pos = state.display.get_height() - (height * 3.5)
    # y_pos_top_offset = y_pos - left_x_offset * 1.65
    # y_pos_bottom_offset = y_pos + left_x_offset * 1.65
    y_pos_top_offset = y_pos - (height * 2)
    y_pos_bottom_offset = y_pos + (height * 2)

    save_x_pos = left_x_offset
    clear_x_pos = right_x_offset
    giveup_x_pos = left_x_offset + (spacer * .5)
    shuffle_x_pos = save_x_pos + spacer
    submit_x_pos = clear_x_pos - spacer
    hints_x_pos = clear_x_pos - (spacer * .5)

    draw_button(state, " Save ", save_x_pos, y_pos)
    draw_button(state, " Give Up ", giveup_x_pos, y_pos_top_offset)
    draw_button(state, " Shuffle ", shuffle_x_pos, y_pos)
    draw_button(state, " Submit ", submit_x_pos, y_pos)
    draw_button(state, " Hints ", hints_x_pos, y_pos_top_offset)
    draw_button(state, " Clear ", clear_x_pos, y_pos)
    draw_button(state, " Scores ", giveup_x_pos, y_pos_bottom_offset)
    draw_button(state, " Share ", hints_x_pos, y_pos_bottom_offset)


def draw_button(state, text, x, y):
    width = (state.display.get_width() / 6) * .33
    hexagon = Hexagon(x, y, width, width, text)
    hexagon.draw(state.display, COLOR_ORANGE, COLOR_BLACK, COLOR_NEON_ORANGE)
    hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)
    state.buttons[text] = hexagon.is_hover()
