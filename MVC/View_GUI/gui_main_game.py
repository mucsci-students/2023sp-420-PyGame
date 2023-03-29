import pygame, os, random
from model_puzzle import *


class Game:
    def __init__(self):
        pygame.init()
        self.puzzle_stats = None

        self.colors = Colors()
        self.button_dict = {}
        self.letter_dict = {}
        self.all_possible_words = []
        self.correctly_guessed_words = []

        self.puzzle_letter_center_position = []
        self.top_puzzle_section = (0, 0)
        self.bottom_puzzle_section = (0, 0)

        self.game_window_minimum_width = 800
        self.game_window_minimum_height = 600

        # Define an absolute minimum value for width and height.
        self.game_window_width = self.game_window_minimum_width
        self.game_window_height = self.game_window_minimum_height
        self.game_window = pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)

        # Find the x,y coordinate for the middle of the game window.
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2
        self.radius = min(self.game_window_width, self.game_window_height) // 8

        self.control_height = int(self.radius * .5)
        self.control_width = self.radius * 5

        # Set the name and icon for the window.
        pygame.display.set_caption("Main Game")
        image_file_path = os.path.join(os.getcwd(), "mvc/view_gui/helpicons")
        pygame.display.window_position = (0, 0)

        self.background_image = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()

        # Get and use a copy of the background image to avoid distortion when resizing.
        self.scaled_background_image = self.background_image

        # Set up the colors
        self.HOVER_COLOR = self.colors.ORANGE
        self.SUBMIT_BUTTON = self.colors.BLACK
        self.SUBMIT_HOVER = self.colors.ORANGE
        self.HEXAGON_HOVER = self.colors.BLACK
        self.SHUFFLE_HOVER = self.colors.ORANGE
        self.SHOW_WORDS_HOVER = self.colors.ORANGE
        self.UP_ARROW_COLOR = self.colors.LIGHT_GRAY
        self.DOWN_ARROW_COLOR = self.colors.LIGHT_GRAY

        self.input_box_max_length = 0
        print(self.all_possible_words)

        # Set up variables to control the scroll wheel
        self.scroll_position = 0
        self.scroll_direction = 0
        self.max_input_length = 0

        # Set up puzzle letter font
        self.puzzle_letter_font_size = int(self.game_window_width * .15)
        self.puzzle_letter_font = pygame.font.SysFont(None, self.puzzle_letter_font_size)

        # Set up show guessed words button font
        self.guessed_word_button_font_size = int(self.game_window_width * .07)
        self.guessed_word_button_font = pygame.font.SysFont(None, self.guessed_word_button_font_size)

        # Set up input box and smaller button font
        self.input_box_font_size = int(self.game_window_width * .01)
        self.input_box_font = pygame.font.SysFont(None, self.input_box_font_size)

        print(f'input font: {self.input_box_font_size}')
        print(f'guessed word: {self.guessed_word_button_font_size}')

        # Set up the timer
        self.bad_timer_active = False
        self.good_timer_active = False
        self.timer_duration = 900  # in milliseconds
        self.timer_start_time = 0

        self.show_words_rect = None
        self.arrow_up_rect = None
        self.arrow_down_rect = None
        self.exit_button_rect = None
        self.guessed_words_column_count = 1

        # self.character_width, self.character_height = self.input_box_font.size(self.puzzle_stats.shuffled_puzzle[0])
        self.character_width, self.character_height = self.guessed_word_button_font.size('i')
        print(f'char width: {self.character_width}')
        print(f'char height: {self.character_height}')

        self.clock = pygame.time.Clock()
        self.input_box_text = ''
        self.show_words_text = "Show Guessed Words"

        self.running = True
        self.show_words_box_visible = False
        self.set_puzzle()

    def set_puzzle(self):
        self.puzzle_stats = PuzzleStats()

        # Define the letters to display
        self.puzzle_stats.shuffled_puzzle = self.puzzle_stats.shuffled_puzzle.upper()

        for word in self.puzzle_stats.current_word_list:
            self.all_possible_words.append(word[0])
            if len(word[0]) > self.input_box_max_length:
                self.input_box_max_length = len(word[0])
        self.input_box_max_length += 10
        print(self.input_box_max_length)
        print(self.all_possible_words)

    def calculate_puzzle_position(self):
        self.puzzle_letter_center_position = [
            (self.center_x, self.center_y),                                     # Center
            (self.center_x, self.center_y - 2 * self.radius),                   # Top Middle
            (self.center_x + 2 * self.radius, self.center_y - self.radius),     # Top Right
            (self.center_x + 2 * self.radius, self.center_y + self.radius),     # Bottom right
            (self.center_x, self.center_y + 2 * self.radius),                   # Bottom Middle
            (self.center_x - 2 * self.radius, self.center_y + self.radius),     # Bottom Left
            (self.center_x - 2 * self.radius, self.center_y - self.radius)      # Top Left
        ]

        # Determine the (x,y) coordinates for the section above and below the main puzzle.
        self.top_puzzle_section = (self.center_x, self.puzzle_letter_center_position[1][1] - (self.radius * 1.75))
        self.bottom_puzzle_section = (self.center_x, self.puzzle_letter_center_position[4][1] + self.radius)

    # Calculate the scale and position of elements on screen based on game_window size.
    def calculate_scale(self):
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2
        self.radius = min(self.game_window_width, self.game_window_height) // 8
        self.control_width = self.radius * 5
        self.control_height = self.radius * .5
        # Get the width and height of a character in the current puzzle
        self.character_width, self.character_height = self.input_box_font.size(self.puzzle_stats.pangram[0])
        self.scale_font()
        self.calculate_puzzle_position()

    def draw_game(self):
        show_words_box_x_offset = self.top_puzzle_section[0] - (self.radius * 4.5)
        input_box_x_offset = self.bottom_puzzle_section[0] - (self.radius * 2.5)

        show_words_pos = show_words_box_x_offset, self.top_puzzle_section[1]
        exit_game_pos = show_words_pos[0], show_words_pos[1] + self.control_height
        input_box_pos = input_box_x_offset, self.bottom_puzzle_section[1]

        shuffle_position = input_box_pos[0] - self.radius, input_box_pos[1]
        save_position = shuffle_position[0] - (self.radius * 1.25), input_box_pos[1]
        submit_position = input_box_pos[0] + self.control_width + self.radius, input_box_pos[1]
        hint_position = submit_position[0] + (self.radius * 1.25), submit_position[1]

        self.draw_hex_button(shuffle_position, "Shuffle")
        self.draw_hex_button(save_position, "Save")
        self.draw_hex_button(submit_position, "Submit")
        self.draw_hex_button(hint_position, "Hints")

        input_box_rect = pygame.Rect(input_box_pos, (self.control_width, self.control_height))
        self.show_words_rect = pygame.Rect(show_words_pos, (self.control_width * 1.75, self.control_height))
        self.exit_button_rect = pygame.Rect(exit_game_pos, (self.control_width * .66, self.control_height))

        self.draw_rectangle_button(input_box_pos, input_box_rect,
                                   self.input_box_text, self.colors.WHITE)
        self.draw_rectangle_button(show_words_pos, self.show_words_rect,
                                   self.show_words_text, self.SHOW_WORDS_HOVER)

        if self.show_words_box_visible:
            self.draw_guessed_words()
        elif not self.show_words_box_visible:
            self.draw_rank((show_words_pos[0] + (self.control_width * 1.75), show_words_pos[1] + self.control_height))
            self.draw_rectangle_button(exit_game_pos, self.exit_button_rect,
                                       "Leave Game", self.colors.ORANGE)

    def draw_gradient(self, box, pos):
        box_surface = pygame.Surface(box.size, pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (180, 13, 100, 0), box)
        gradient = pygame.Rect((0, 0), box.size)
        gradient_surface = pygame.Surface(box.size)
        gradient_surface.set_alpha(150)
        pygame.draw.rect(gradient_surface, (0, 0, 0), gradient)
        gradient_surface.blit(box_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.game_window.blit(gradient_surface, pos)

    def draw_hexagon(self):
        self.calculate_scale()
        for i, pos in enumerate(self.puzzle_letter_center_position):
            letter = self.puzzle_stats.shuffled_puzzle[i]
            hex_points = [
                (pos[0] - self.radius, pos[1]),
                (pos[0] - self.radius * 0.5, pos[1] - self.radius * 0.866),
                (pos[0] + self.radius * 0.5, pos[1] - self.radius * 0.866),
                (pos[0] + self.radius, pos[1]),
                (pos[0] + self.radius * 0.5, pos[1] + self.radius * 0.866),
                (pos[0] - self.radius * 0.5, pos[1] + self.radius * 0.866)
            ]

            # Check if the mouse cursor is inside the hexagon
            if self.point_inside_polygon(pygame.mouse.get_pos(), hex_points) and not self.show_words_box_visible:
                self.HEXAGON_HOVER = self.HOVER_COLOR
                self.letter_dict[letter] = True
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, hex_points)
                pygame.draw.polygon(self.game_window, self.colors.BLACK, hex_points, 6)
            else:
                self.HEXAGON_HOVER = self.colors.NEON_ORANGE
                self.letter_dict[letter] = False
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, hex_points)
                pygame.draw.polygon(self.game_window, self.colors.BLACK, hex_points, 6)

            letter_text = self.puzzle_letter_font.render(letter, True, self.colors.BLACK)
            letter_text_rect = letter_text.get_rect(center=pos)
            self.game_window.blit(letter_text, letter_text_rect)

    def draw_rectangle_button(self, position, button_rectangle, text, color):
        rect = pygame.draw.rect(self.game_window, self.colors.BLACK, button_rectangle, 2)
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = self.colors.WHITE

        if self.bad_timer_active:
            color = self.colors.INVALID_COLOR
            # Randomly modify the position of the text within a certain range
            button_rectangle.center = (button_rectangle.centerx + random.randint(-5, 5),
                                       button_rectangle.centery + random.randint(-5, 5))
        elif self.good_timer_active:
            color = self.colors.VALID_COLOR

        input_surface = self.input_box_font.render(text, True, color)
        # Center the input text within the input box rectangle
        input_rect = input_surface.get_rect()
        input_rect.center = button_rectangle.center
        self.draw_gradient(button_rectangle, position)
        self.game_window.blit(input_surface, input_rect)

    def draw_hex_button(self, position, text):
        hex_pos = HexagonButton(position[0], position[1], self.radius).draw_hexagonal_button()
        if self.good_timer_active:
            self.SUBMIT_HOVER = self.colors.VALID_COLOR
        elif self.bad_timer_active:
            self.SUBMIT_HOVER = self.colors.INVALID_COLOR

        if self.point_inside_polygon(pygame.mouse.get_pos(), hex_pos) and not self.show_words_box_visible:
            self.SUBMIT_HOVER = self.colors.WHITE
            self.button_dict[text] = True
        else:
            self.SUBMIT_HOVER = self.colors.BLACK
            self.button_dict[text] = False
        pygame.draw.polygon(self.game_window, self.colors.ORANGE, hex_pos)
        button = pygame.draw.polygon(self.game_window, self.SUBMIT_HOVER, hex_pos, 4)
        render_text = self.input_box_font.render(text, True, self.SUBMIT_BUTTON)
        text_rect = render_text.get_rect(center=button.center)
        self.game_window.blit(render_text, text_rect)

    @staticmethod
    def point_inside_polygon(mouse_point, hex_points):
        mouse_x, mouse_y = mouse_point
        num_points = len(hex_points)
        inside_hex = False
        start_x_pos, start_y_pos = hex_points[0]
        for i in range(num_points + 1):
            end_x_pos, end_y_pos = hex_points[i % num_points]
            if mouse_y > min(start_y_pos, end_y_pos):
                if mouse_y <= max(start_y_pos, end_y_pos):
                    if mouse_x <= max(start_x_pos, end_x_pos):
                        if start_y_pos != end_y_pos:
                            x_intercept = (mouse_y - start_y_pos) * (end_x_pos - start_x_pos) / (end_y_pos - start_y_pos) + start_x_pos
                            if start_x_pos == end_x_pos or mouse_x <= x_intercept:
                                inside_hex = not inside_hex
            start_x_pos, start_y_pos = end_x_pos, end_y_pos
        return inside_hex

    def draw_rank(self, pos):
        rank_width = self.control_width * .66
        rank_pos = pos[0] - rank_width, pos[1]
        rank_text = f'{self.puzzle_stats.get_rank()}: {self.puzzle_stats.score} / {self.puzzle_stats.total_points}'
        rank_box_rect = pygame.Rect(rank_pos, (rank_width, self.control_height))
        input_surface = self.input_box_font.render(rank_text, True, self.colors.NEON_ORANGE)
        # Center the input text within the input box rectangle
        input_rect = input_surface.get_rect()
        input_rect.center = rank_box_rect.center
        self.draw_gradient(rank_box_rect, rank_pos)
        self.game_window.blit(input_surface, input_rect)

    def draw_guessed_words(self):
        words_background_rect = pygame.Rect((self.top_puzzle_section[0] - (self.radius * 4.5),
                                             self.top_puzzle_section[1] + self.control_height),
                                            (self.control_width * 1.75, self.game_window_height * .9))
        self.draw_rectangle_button(words_background_rect.topleft, words_background_rect, "", self.SHOW_WORDS_HOVER)

        guessed_words_start_pos = words_background_rect.topleft
        menu_y = guessed_words_start_pos[1]
        arrow_dimensions = (self.control_width * 1.75) * .05
        arrow_offset_x = words_background_rect.topright[0] - (arrow_dimensions * .5)
        arrow_start_pos = arrow_offset_x, words_background_rect.topright[1]

        arrow_up_pos = (arrow_start_pos[0] + arrow_dimensions - (arrow_dimensions * 2),
                        arrow_start_pos[1] + (arrow_dimensions * 3))

        arrow_down_pos = arrow_up_pos[0], (arrow_start_pos[1] + (self.radius * 2) - arrow_dimensions)

        # Define the arrow button rectangles
        self.arrow_up_rect = pygame.Rect(arrow_up_pos[0], arrow_up_pos[1] - arrow_dimensions,
                                         arrow_dimensions, arrow_dimensions)
        self.arrow_down_rect = pygame.Rect(arrow_down_pos[0], arrow_down_pos[1], arrow_dimensions, arrow_dimensions)

        # Calculate the number of columns based on the width of the display area
        col_width = (self.input_box_font_size * max(len(word) for word in self.all_possible_words)) * .75
        self.guessed_words_column_count = int(max(1, (words_background_rect.size[0]) // col_width))

        if self.scroll_position == 0:
            self.UP_ARROW_COLOR = self.colors.LIGHT_GRAY
        else:
            self.UP_ARROW_COLOR = self.colors.BLACK

        # Draw up arrow
        pygame.draw.polygon(self.game_window, self.UP_ARROW_COLOR, (
            arrow_up_pos, (arrow_up_pos[0] + arrow_dimensions, arrow_up_pos[1]),
            (arrow_up_pos[0] + arrow_dimensions // 2, arrow_up_pos[1] - arrow_dimensions)
        ))

        # Draw down arrow
        pygame.draw.polygon(self.game_window, self.DOWN_ARROW_COLOR, (
            arrow_down_pos,
            (arrow_down_pos[0] + arrow_dimensions, arrow_down_pos[1]),
            (arrow_down_pos[0] + arrow_dimensions // 2,
             arrow_down_pos[1] + arrow_dimensions)
        ))

        # Draw the words
        for word_column in range(self.guessed_words_column_count):
            word_column_x = guessed_words_start_pos[0] + word_column * col_width
            for i in range(len(self.correctly_guessed_words)):
                if i % self.guessed_words_column_count == word_column:
                    word_y = menu_y + ((i // self.guessed_words_column_count) * 30) - (
                                self.scroll_position * 30)
                    if word_y >= guessed_words_start_pos[1] and word_y + 30 <= guessed_words_start_pos[
                        1] + (self.game_window_height * .90):
                        word = self.input_box_font.render(self.correctly_guessed_words[i], True, self.colors.NEON_ORANGE)
                        self.game_window.blit(word, (word_column_x + 10, word_y + 10))
                        self.DOWN_ARROW_COLOR = self.colors.LIGHT_GRAY
                    else:
                        self.DOWN_ARROW_COLOR = self.colors.BLACK

    def handle_guess_visuals(self):
        if (self.puzzle_stats.get_check_guess(self.input_box_text)) == 0:
            self.correctly_guessed_words = self.puzzle_stats.guesses
            self.SUBMIT_BUTTON = self.colors.VALID_COLOR
            self.SUBMIT_HOVER = self.colors.VALID_COLOR
            self.SHUFFLE_HOVER = self.colors.VALID_COLOR

            self.good_timer_active = True
            self.timer_start_time = pygame.time.get_ticks()
            if len(self.input_box_text) == 4:
                self.input_box_text = f'+ {self.puzzle_stats.get_word_points(self.input_box_text)} point!'
            else:
                self.input_box_text = f'+ {self.puzzle_stats.get_word_points(self.input_box_text)} points!'
        else:
            self.SUBMIT_BUTTON = self.colors.INVALID_COLOR
            self.SUBMIT_HOVER = self.colors.INVALID_COLOR
            self.SHUFFLE_HOVER = self.colors.INVALID_COLOR
            self.bad_timer_active = True
            self.timer_start_time = pygame.time.get_ticks()

    def scale_font(self):
        text_height = int(self.radius * .5)
        # Set new puzzle font size
        self.puzzle_letter_font_size = int(self.radius * 1.5)
        self.puzzle_letter_font = pygame.font.SysFont(None, self.puzzle_letter_font_size)

        if self.good_timer_active:
            # Set new input box font size
            self.input_box_font_size = int(text_height * .85)
            self.input_box_font = pygame.font.SysFont(None, self.input_box_font_size)
        else:
            # Set new input box font size
            self.input_box_font_size = int(text_height * .75)
            self.input_box_font = pygame.font.SysFont(None, self.input_box_font_size)

        # Set new show guessed words font size
        self.guessed_word_button_font_size = int((text_height * 1.75) * .05)
        self.guessed_word_button_font = pygame.font.SysFont(None, self.guessed_word_button_font_size)

    def handle_save_visuals(self):
        pass
        # semi_transparent_color = (0, 0, 0, 160)
        #
        # message_box_width = (self.radius * 5)
        # message_box_height = self.input_box_height
        # message_box_x = (self.game_window_width - message_box_width) // 2
        # message_box_y = (self.game_window_height - message_box_height) // 2 - 100
        # message_box_rectangle = pygame.Rect(message_box_x, message_box_y, message_box_width, message_box_height)

        # file_input_width = self.control_width
        # file_input_height = self.input_box_height * 1.1
        # file_input_x = (self.game_window_width - file_input_width) // 2
        # file_input_y = (self.game_window_height - file_input_height) // 2 + 100
        # file_input_rectangle = pygame.Rect(file_input_x, file_input_y, file_input_width, file_input_height)
        #
        # message_text_surface = self.input_box_font.render(f'Enter filename: ', True, self.colors.NEON_ORANGE)
        #
        # hide_background_surface = pygame.Surface((self.game_window_width, self.game_window_height), pygame.SRCALPHA)
        # message_display = pygame.Surface((message_box_width, message_box_height), pygame.SRCALPHA)
        # message_display.fill(semi_transparent_color)
        # hide_background_surface.fill(semi_transparent_color)
        #
        # # Create a Font object
        # font = pygame.font.SysFont(None, 32)
        #
        # message_text_rect = message_text_surface.get_rect(center=message_box_rectangle.center)
        # self.game_window.blit(hide_background_surface, (0, 0))
        # self.game_window.blit(message_display, (message_box_x, message_box_y))
        # self.game_window.blit(message_text_surface, (message_text_rect))
        #
        # input_text = ''
        # while True:
        #     event = pygame.event.wait()
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RETURN:
        #             if input_text != '':
        #                 print(
        #                     f'gui_main_game.py - def handle_save_visuals(): Save has not implemented required letter.')
        #                 # self.puzzle_stats.get_save_game(self.puzzle_stats, input_text)
        #                 break
        #         elif event.key == pygame.K_BACKSPACE:
        #             input_text = input_text[:-1]
        #         elif event.unicode.isalpha():
        #             input_text += event.unicode
        #         elif event.key == pygame.K_ESCAPE:
        #             break
        #
        #     pygame.draw.rect(self.game_window, self.colors.WHITE, file_input_rectangle)
        #     # Render the text as a Surface and blit it onto the text display
        #     text_surface = font.render(input_text, True, (0, 0, 0))
        #     self.game_window.blit(text_surface, (file_input_x, file_input_y))
        #     pygame.display.update()

    # Draw all screen elements
    def draw_screen(self):
        self.draw_hexagon()
        self.draw_game()

    def run(self):
        loading = True

        while self.running:
            if self.show_words_box_visible:
                self.show_words_text = "Hide Guessed Words"
            else:
                self.show_words_text = "Show Guessed Words"
            # Set frame rate to 60
            self.clock.tick(60)
            # Fill the background
            self.game_window.blit(self.scaled_background_image, (0, 0))
            self.draw_screen()

            if self.puzzle_stats.check_progress():
                self.running = False

            if self.bad_timer_active:
                # Check if the timer has expired
                if pygame.time.get_ticks() - self.timer_start_time >= self.timer_duration:
                    # Stop the timer after the specified duration has passed
                    self.bad_timer_active = False
                    self.SUBMIT_HOVER = self.colors.BLACK
                    self.SHUFFLE_HOVER = self.colors.BLACK
                    self.SUBMIT_BUTTON = self.colors.BLACK

            if self.good_timer_active:
                if pygame.time.get_ticks() - self.timer_start_time >= self.timer_duration:
                    # Stop the timer after the specified duration has passed
                    self.good_timer_active = False
                    self.input_box_text = ''
                    self.SUBMIT_HOVER = self.colors.BLACK
                    self.SHUFFLE_HOVER = self.colors.BLACK
                    self.SUBMIT_BUTTON = self.colors.BLACK

            # Handle events
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                #
                # If user resized game_window, set new dimensions
                elif event.type == pygame.VIDEORESIZE:
                    # Set screen to minimum allowed width if resized too small
                    if event.w < self.game_window_minimum_width:
                        self.game_window_width = self.game_window_minimum_width
                    else:
                        self.game_window_width = event.w

                    # Set screen to minimum allowed height if resized too small
                    if event.h < self.game_window_minimum_height:
                        self.game_window_height = self.game_window_minimum_height
                    else:
                        self.game_window_height = event.h
                    self.calculate_scale()
                #
                    pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)
                    self.scaled_background_image = pygame.transform.scale(
                        self.background_image, (self.game_window_width, self.game_window_height)).convert()
                #

                # Check if the user has clicked the up or down arrow
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.show_words_box_visible:
                    if self.arrow_up_rect.collidepoint(event.pos):
                        self.scroll_direction = -1
                    elif self.arrow_down_rect.collidepoint(event.pos):
                        self.scroll_direction = 1

                # Mouse scroll up with guessed words visible
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and self.show_words_box_visible:
                    self.scroll_position = max(0, self.scroll_position - 1)
                    # Redraw words to account for new scroll position.

                # Mouse scroll down with guessed words visible
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and self.show_words_box_visible:
                    self.scroll_position = min(len(self.correctly_guessed_words) - 1, self.scroll_position + 1)

                # If user released left click on mouse.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if loading:
                        pygame.time.wait(800)
                        loading = False
                    else:
                        self.scroll_direction = 0
                        for text in self.button_dict:
                            if text == "Shuffle":
                                if self.button_dict[text]:
                                    self.puzzle_stats.ShuffleKey()
                                    self.puzzle_stats.shuffled_puzzle = self.puzzle_stats.shuffled_puzzle.upper()
                            elif text == "Submit":
                                if self.button_dict[text]:
                                    self.handle_guess_visuals()
                            elif text == "Save":
                                if self.button_dict[text]:
                                    self.handle_save_visuals()
                            elif text == "Hints":
                                if self.button_dict[text]:
                                    pass
                                    # self.handle_save_visuals()

                        # If user clicked on "Show Words".
                        if self.show_words_rect.collidepoint(event.pos):
                            self.show_words_box_visible = not self.show_words_box_visible

                        elif self.exit_button_rect.collidepoint(event.pos):
                            self.running = False

                        for letter in self.letter_dict:
                            if self.letter_dict[letter] and len(self.input_box_text) < self.input_box_max_length:
                                self.input_box_text += letter

                # Handle key events
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    print(key, "key was pressed")
                    # Check if the backspace key was pressed
                    if event.key == pygame.K_BACKSPACE:
                        self.input_box_text = self.input_box_text[:-1]
                    # Check if a letter key was pressed
                    elif event.unicode.isalpha() and event.unicode in self.puzzle_stats.pangram:
                        if len(self.input_box_text) < self.input_box_max_length:
                            self.input_box_text += event.unicode.upper()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN and not self.good_timer_active:
                        if self.input_box_text != '':
                            self.handle_guess_visuals()

            self.scroll_position = max(0, min((len(self.correctly_guessed_words) // self.guessed_words_column_count) - 15,
                                              self.scroll_position + self.scroll_direction))
            pygame.display.update()


class Button:
    def __init__(self, x_coordinate, y_coordinate, radius):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius
        self.control_height = int(radius * .5)


class HexagonButton(Button):
    def __init__(self, x_coordinate, y_coordinate, radius):
        super().__init__(x_coordinate, y_coordinate, radius)
        self.hex_points = []

    def draw_hexagonal_button(self):
        hex_points = [
            (self.x_coordinate, self.y_coordinate - (self.radius * .25)),
            (self.x_coordinate + self.control_height, self.y_coordinate),
            (
             self.x_coordinate + self.control_height, self.y_coordinate + self.control_height),
            (self.x_coordinate, self.y_coordinate + (self.radius * .75)),
            (self.x_coordinate - self.control_height, self.y_coordinate + self.control_height),
            (self.x_coordinate - self.control_height, self.y_coordinate),
        ]
        self.hex_points = hex_points

        return self.hex_points


class Colors:
    def __init__(self):
        # Set up the colors
        self.WHITE = (255, 255, 255)  # White
        self.BLACK = (0, 0, 0)  # Black
        self.ORANGE = (255, 189, 49)  # Orange
        self.NEON_ORANGE = (255, 85, 0)  # Obnoxious Orange
        self.GRAY = (224, 224, 224)
        self.LIGHT_GRAY = (155, 155, 155)  # Light Gray
        self.VALID_COLOR = (68, 214, 44)  # Green
        self.INVALID_COLOR = (255, 0, 0)  # Red
        self.GAME_BACKGROUND = (255, 30, 231)  # Bright Pink
        self.BUTTON_BACKGROUND = (186, 100, 65)
