from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle
import pygame


def create_arrows(state):
    x_buffer = state.display.get_width() / 10
    y_buffer = state.display.get_height() + 10
    
    guessed_words_width = x_buffer * 8
    guessed_words_height = y_buffer * .9
    
    arrow_dimensions = guessed_words_width * .05

    arrow_up_y_pos =  (0.0625 * y_buffer) + arrow_dimensions
    arrow_down_y_pos = guessed_words_height - arrow_dimensions
    
    arrow_x_pos = x_buffer + guessed_words_width - (arrow_dimensions * 1.5)    
    
    up_arrow = Rectangle(
        x=arrow_x_pos, y=arrow_up_y_pos, w=arrow_dimensions, h=arrow_dimensions,
        font_color=COLOR_ORANGE,
        text='Up'
    )

    down_arrow = Rectangle(
        x=arrow_x_pos, y=arrow_down_y_pos, w=arrow_dimensions, h=arrow_dimensions,
        font_color=COLOR_ORANGE,
        text='Down'
    )

    if state.show_guessed_words:

        if state.scroll_position == 0:
            pygame.draw.polygon(state.display, COLOR_BLACK, (up_arrow.shape.midtop, up_arrow.shape.bottomleft, up_arrow.shape.bottomright,))
        else:
            pygame.draw.polygon(state.display, COLOR_WHITE, (up_arrow.shape.midtop, up_arrow.shape.bottomleft, up_arrow.shape.bottomright,))
        
        if state.scroll_position + state.displayable_rows >= state.total_rows:
            pygame.draw.polygon(state.display, COLOR_BLACK, (down_arrow.shape.topleft, down_arrow.shape.topright, down_arrow.shape.midbottom))
        else:
            pygame.draw.polygon(state.display, COLOR_WHITE, (down_arrow.shape.topleft, down_arrow.shape.topright, down_arrow.shape.midbottom))

        state.buttons[up_arrow.text] = up_arrow.is_hover()
        state.buttons[down_arrow.text] = down_arrow.is_hover()


def create_show_words(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.9 * state.display.get_height()
    button_text = ''
    buffer_height = 0.0625 * state.display.get_height() + 10

    font_color = COLOR_ORANGE

    shape = Rectangle(
        x=buffer, y=buffer_height, w=width, h=height,
        font_color=font_color,
        text=button_text
    )
    
    if state.show_guessed_words:
        input_box_font_size = state.display.get_width() * .05
        font = pygame.font.SysFont(None, int(input_box_font_size))
        font_height = font.get_height() + 10
        
        # Calculate total possible columns
        state.column_width = width // max(len(word) for word in state.puzzle_stats.current_word_list) + input_box_font_size + 35
        state.displayable_columns = int(max(1, (shape.shape.size[0]) // state.column_width))
        
        # Calculate total rows that can be displayed at once
        state.displayable_rows = int((state.display.get_height() * .90) // font_height)
        
        # Calculate total needed rows to display all guesses.
        state.total_rows = len(state.puzzle_stats.guesses) // state.displayable_columns

        
        shape.draw(state.display, color=COLOR_BLACK)
        guessed_words_start_pos = buffer, buffer_height
        menu_y = guessed_words_start_pos[1]

        if len(state.puzzle_stats.guesses) % state.displayable_columns != 0:
            state.total_rows += 1

        # Draw the words
        for word_column in range(state.displayable_columns):
            word_column_x = guessed_words_start_pos[0] + word_column * state.column_width
            for i in range(len(state.puzzle_stats.guesses)):
                if i % state.displayable_columns == word_column:
                    word_y = menu_y + ((i // state.displayable_columns) * font_height) - (
                        state.scroll_position * font_height)
                    if word_y >= guessed_words_start_pos[1] and word_y + font_height <= guessed_words_start_pos[
                        1] + (state.display.get_height() * .90):
                        word = font.render(state.puzzle_stats.guesses[i], True, COLOR_ORANGE)
                        state.display.blit(word, (word_column_x + 10, word_y + 10))
     
        # Set scroll cutoff
        state.max_scroll_position = max(0, state.total_rows - state.displayable_rows)
