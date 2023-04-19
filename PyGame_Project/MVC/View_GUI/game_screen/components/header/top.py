from ...colors import COLOR_BLACK, COLOR_ORANGE, COLOR_WHITE
from ..shapes import Rectangle


def create_top(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.0625 * state.display.get_height()

    if state.show_active:
        top_text = 'Hide Guessed Words'
    else:
        top_text = 'Show Guessed Words'

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=COLOR_ORANGE,
        text=top_text
    )
    shape.draw(state.display, color=COLOR_BLACK)
    state.buttons[shape.text] = shape.is_hover()

    if shape.is_hover():
        shape.change_colors(state.display, COLOR_WHITE, COLOR_ORANGE, top_text)


def create_show_words(state):

    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = 0.9 * state.display.get_height()
    button_text = ''

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=COLOR_ORANGE,
        text=button_text
    )
    shape.draw(state.display, color=COLOR_BLACK)
    state.buttons[shape.text] = shape.is_hover()

#  def draw_guessed_words(self):
#         words_background_rect = pygame.Rect((self.top_puzzle_section[0] - (self.radius * 4.5),
#                                              self.top_puzzle_section[1] + self.control_height),
#                                             (self.control_width * 1.75, self.game_window_height * .9))
#         self.draw_rectangle_button(words_background_rect.topleft, words_background_rect, "", self.SHOW_WORDS_HOVER)

#         guessed_words_start_pos = words_background_rect.topleft
#         menu_y = guessed_words_start_pos[1]
#         arrow_dimensions = (self.control_width * 1.75) * .05
#         arrow_offset_x = words_background_rect.topright[0] - (arrow_dimensions * .5)
#         arrow_start_pos = arrow_offset_x, words_background_rect.topright[1]

#         arrow_up_pos = (arrow_start_pos[0] + arrow_dimensions - (arrow_dimensions * 2),
#                         arrow_start_pos[1] + (arrow_dimensions * 3))

#         arrow_down_pos = arrow_up_pos[0], (arrow_start_pos[1] + (self.radius * 2) - arrow_dimensions)

#         # Define the arrow button rectangles
#         self.arrow_up_rect = pygame.Rect(arrow_up_pos[0], arrow_up_pos[1] - arrow_dimensions,
#                                          arrow_dimensions, arrow_dimensions)
#         self.arrow_down_rect = pygame.Rect(arrow_down_pos[0], arrow_down_pos[1], arrow_dimensions, arrow_dimensions)

#         # Calculate the number of columns based on the width of the display area
#         col_width = (self.input_box_font_size * max(len(word) for word in self.all_possible_words)) * .75
#         self.guessed_words_column_count = int(max(1, (words_background_rect.size[0]) // col_width))

#         if self.scroll_position == 0:
#             self.UP_ARROW_COLOR = self.colors.LIGHT_GRAY
#         else:
#             self.UP_ARROW_COLOR = self.colors.BLACK

#         # Draw up arrow
#         pygame.draw.polygon(self.game_window, self.UP_ARROW_COLOR, (
#             arrow_up_pos, (arrow_up_pos[0] + arrow_dimensions, arrow_up_pos[1]),
#             (arrow_up_pos[0] + arrow_dimensions // 2, arrow_up_pos[1] - arrow_dimensions)
#         ))

#         # Draw down arrow
#         pygame.draw.polygon(self.game_window, self.DOWN_ARROW_COLOR, (
#             arrow_down_pos,
#             (arrow_down_pos[0] + arrow_dimensions, arrow_down_pos[1]),
#             (arrow_down_pos[0] + arrow_dimensions // 2,
#              arrow_down_pos[1] + arrow_dimensions)
#         ))

#         # Draw the words
#         for word_column in range(self.guessed_words_column_count):
#             word_column_x = guessed_words_start_pos[0] + word_column * col_width
#             for i in range(len(self.correctly_guessed_words)):
#                 if i % self.guessed_words_column_count == word_column:
#                     word_y = menu_y + ((i // self.guessed_words_column_count) * 30) - (
#                                 self.scroll_position * 30)
#                     if word_y >= guessed_words_start_pos[1] and word_y + 30 <= guessed_words_start_pos[
#                         1] + (self.game_window_height * .90):
#                         word = self.input_box_font.render(self.correctly_guessed_words[i], True, self.colors.NEON_ORANGE)
#                         self.game_window.blit(word, (word_column_x + 10, word_y + 10))
#                         self.DOWN_ARROW_COLOR = self.colors.LIGHT_GRAY
#                     else:
#                         self.DOWN_ARROW_COLOR = self.colors.BLACK