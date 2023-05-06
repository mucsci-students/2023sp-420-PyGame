import pygame, os
from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle


def create_rank_display(state):
    button_text = ''
    buffer = state.display.get_width() / 10
    width = buffer * 8
    state_height = state.display.get_height()
    height = 0.75 * state_height
    spacer = state_height * .01
    highscore_title_height = .125 * state_height + 5
    puzzle_description_height = (.0625 * state_height) + spacer

    y_offset = highscore_title_height + puzzle_description_height

    font_color = COLOR_ORANGE

    shape = Rectangle(
        x=buffer, y=y_offset, w=width, h=height,
        font_color=font_color,
        text=button_text
    )

    # Calculate total rows that can be displayed at once
    displayable_rows = 10

    # Adjust the font size based on the available height for the rows
    font_height = height / displayable_rows
    input_box_font_size = int(font_height * 0.8)
    font = pygame.font.SysFont(None, input_box_font_size)

    # Calculate total possible columns
    column_width = width / 3
    displayable_columns = 3

    # Calculate total needed rows to display all guesses.
    total_rows = len(state.all_scores)

    shape.draw(state.display, color=COLOR_BLACK)
    show_rank = buffer, y_offset
    menu_y = show_rank[1]

    if len(state.all_scores) % displayable_columns != 0:
        total_rows += 1

    # Draw headers
    headers = ["Rank", "Name", "Score"]
    for col in range(displayable_columns):
        header = headers[col]
        header_render = font.render(header, True, COLOR_ORANGE)
        text_rect = header_render.get_rect(center=(buffer + col * column_width + column_width / 2, y_offset +
                                                   header_render.get_height()))
        state.display.blit(header_render, text_rect)

    # Draw the words
    for i in range(displayable_rows):
        word_y = y_offset + (header_render.get_height() + spacer) + (i * font_height) - (state.scroll_position * font_height)

        if word_y >= show_rank[1] and word_y + font_height <= show_rank[1] + (state.display.get_height() * .75):
            for col in range(displayable_columns):
                index = state.scroll_position + i
                if index < len(state.edited_scores):
                    word = str(state.edited_scores[index][col])  # Convert the rank (integer) to a string
                    word_render = font.render(word, True, COLOR_ORANGE)
                    text_rect = word_render.get_rect(
                        center=(buffer + col * column_width + column_width / 2, word_y + header_render.get_height() + spacer))
                    state.display.blit(word_render, text_rect)

    # Set scroll cutoff
    state.max_scroll_position = max(0, total_rows - displayable_rows)
