from ...colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE
from ...components.shapes import Rectangle
import pygame

def create_show_words(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.9 * state.display.get_height()
    button_text = ''
    buffer_height = 0.0625 * state.display.get_height() + 10

    shape = Rectangle(
        x=buffer, y=buffer_height, w=width, h=height,
        font_color=COLOR_ORANGE,
        text=button_text
    )
    
    if state.show_guessed_words:
        shape.draw(state.display, color=COLOR_BLACK)

        guessed_words_start_pos = buffer, buffer_height
        menu_y = guessed_words_start_pos[1]
        arrow_dimensions = (width * 1.75) * .05
        arrow_offset_x = buffer + width - (arrow_dimensions * .5)
        arrow_start_pos = arrow_offset_x, buffer_height + 5

        arrow_up_pos = (arrow_start_pos[0] + arrow_dimensions - (arrow_dimensions * 2),
                        arrow_start_pos[1] + (arrow_dimensions * 3))

        arrow_down_pos = arrow_up_pos[0], (arrow_start_pos[1] + (width) - arrow_dimensions)

        # Define the arrow button rectangles
        arrow_up_rect = pygame.Rect(arrow_up_pos[0], arrow_up_pos[1] - arrow_dimensions,
                                         arrow_dimensions, arrow_dimensions)
        arrow_down_rect = pygame.Rect(arrow_down_pos[0], arrow_down_pos[1], arrow_dimensions, arrow_dimensions)

        input_box_font_size = state.display.get_width() * .05
        # Calculate the number of columns based on the width of the display area
        col_width = (input_box_font_size * max(len(word) for word in state.puzzle_stats.wordList)) * 1.75
        guessed_words_column_count = int(max(1, (shape.shape.size[0]) // col_width))
        arrow_color = None

        if state.scroll_position == 0:
           arrow_color = COLOR_BLACK
        else:
           arrow_color = COLOR_WHITE
        
        font = pygame.font.SysFont(None, int(input_box_font_size))

        # Draw up arrow
        pygame.draw.polygon(state.display, arrow_color, (
            arrow_up_pos, (arrow_up_pos[0] + arrow_dimensions, arrow_up_pos[1]),
            (arrow_up_pos[0] + arrow_dimensions // 2, arrow_up_pos[1] - arrow_dimensions)
        ))

        # Draw the words
        for word_column in range(guessed_words_column_count):
            word_column_x = guessed_words_start_pos[0] + word_column * col_width
            for i in range(len(state.puzzle_stats.guesses)):
                if i % guessed_words_column_count == word_column:
                    word_y = menu_y + ((i //guessed_words_column_count) * 30) - (
                                state.scroll_position * 30)
                    if word_y >= guessed_words_start_pos[1] and word_y + 30 <= guessed_words_start_pos[
                        1] + (state.display.get_height() * .90):
                        word = font.render(state.puzzle_stats.guesses[i], True, COLOR_ORANGE)
                        state.display.blit(word, (word_column_x + 10, word_y + 10))
                        arrow_color = COLOR_BLACK
                    else:
                        arrow_color = COLOR_WHITE
        
        # Draw down arrow
        pygame.draw.polygon(state.display, arrow_color, (
            arrow_down_pos,
            (arrow_down_pos[0] + arrow_dimensions, arrow_down_pos[1]),
            (arrow_down_pos[0] + arrow_dimensions // 2,
             arrow_down_pos[1] + arrow_dimensions)
        ))