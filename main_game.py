import pygame
from puzzle import Puzzle

class Game:
    def __init__(self):
        pygame.init()
        self.puzzle = Puzzle()
        self.puzzle.generate_random_puzzle()

        # Set up the main game game_window
        self.game_window_minimum_width, self.game_window_minimum_height = 800, 600
        self.game_window_width, self.game_window_height = self.game_window_minimum_width, self.game_window_minimum_height
        self.game_window = pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Main Game")

        # Define the radius and center position of the hexagon
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2

        # Set up the colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.INPUT_BACKGROUND = (155, 155, 155)     # Gray
        self.HOVER_COLOR = (0, 255, 255, 150)       # Cyan
        self.VALID_COLOR = (68, 214, 44)            # Green
        self.INVALID_COLOR = (255, 0, 0)            # Red
        self.GAME_BACKGROUND = (255, 30, 231)       # Bright Pink
        self.SHOW_WORDS_HOVER = self.BLACK
        self.HEXAGON_HOVER = self.BLACK

        # Define the letters to display
        self.letters = self.puzzle.pangram.upper()
        self.current_word_list = [word[0] for word in self.puzzle.current_word_list]
        self.guessed_word_list = self.current_word_list
        
        print(self.guessed_word_list)
        print(self.puzzle.pangram)
        print(len(self.guessed_word_list))

        # Set up the scroll variables
        self.scroll_position = 0
        self.scroll_direction = 0

        # Set up the font
        self.font_size = 30
        self.font = pygame.font.SysFont(None, self.font_size)
        self.character_width, self.character_height = self.font.size('i')

        self.show_words_box_visible = False
        self.input_box_text = ''

        self.clock = pygame.time.Clock()
        self.running = True

    # Calculate the scale and position of elements on screen based on game_window size.
    def calculate_scale(self):
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2
        self.radius = min(self.game_window_width, self.game_window_height) // 8
        self.positions = [
            (self.center_x, self.center_y),                                             # Center
            (self.center_x, self.center_y - 2 * self.radius),                           # Top Middle
            (self.center_x + 2 * self.radius * 0.866, self.center_y - self.radius),     # Top Right
            (self.center_x + 2 * self.radius * 0.866, self.center_y + self.radius),     # Bottom right
            (self.center_x, self.center_y + 2 * self.radius),                           # Bottom Middle
            (self.center_x - 2 * self.radius * 0.866, self.center_y + self.radius),     # Bottom Left
            (self.center_x - 2 * self.radius * 0.866, self.center_y - self.radius)      # Top Left
        ]

        # Calculate position of the input box and dropdown menu.
        self.input_box_pos = (self.positions[5][0] - self.radius, self.positions[4][1] + self.radius)
        self.show_words_pos = (self.positions[5][0] - (self.radius * 3), self.positions[1][1] - self.radius * 1.75)

        # Calculate the size of the input box
        self.input_box_width = (self.radius * 5) + (self.radius * .5)
        self.input_box_height = int(0.08 * self.game_window_height)

        self.shuffle_button_pos = (self.input_box_pos[0] + self.input_box_width + self.radius, self.input_box_pos[1])
        self.shuffle_button_rectangle = pygame.Rect(self.shuffle_button_pos, (self.radius, self.radius))

        # Calculate the size of the "Show Words" button
        self.guessed_words_button_width = self.input_box_width * 1.75
        self.guessed_words_button_height = int(0.06 * self.game_window_height)
        self.guessed_words_button_text = self.font.render("Show Guessed Words", True, self.SHOW_WORDS_HOVER)

        # Calculate the size of the dropdown window
        self.guessed_words_background_width = self.guessed_words_button_width
        self.guessed_words_background_height = self.game_window_height * .90
        
        # Set up the arrow buttons
        self.arrow_width = self.guessed_words_background_width * .05
        self.arrow_height = self.guessed_words_background_height * .05
        self.arrow_up_x = self.show_words_pos[0] + self.guessed_words_background_width - (self.arrow_height * 2)
        self.arrow_up_y = self.show_words_pos[1] + (self.arrow_height * 3)
        self.arrow_down_x = self.arrow_up_x
        self.arrow_down_y =  self.show_words_pos[1] + self.guessed_words_background_height

        # Define the arrow button rectangles
        self.arrow_up_rectangle = pygame.Rect(self.arrow_up_x, self.arrow_up_y - self.arrow_height, self.arrow_width,  self.arrow_height)
        self.arrow_down_rectangle = pygame.Rect(self.arrow_down_x, self.arrow_down_y, self.arrow_width, self.arrow_height)

        # Calculate the number of columns based on the width of the display area
        self.word_width = self.font_size * max(len(word) for word in self.guessed_word_list)
        self.col_width = self.word_width + 5  # add some padding
        self.guessed_words_column_count = int(max(1, self.guessed_words_background_width // self.col_width))
        self.guessed_words_list_rows = len(self.guessed_word_list) // self.guessed_words_column_count + (len(self.guessed_word_list) % self.guessed_words_column_count != 0)
        
        # Give calculated values to pygame.Rect to draw the input box.
        self.input_box_rectangle = pygame.Rect(self.input_box_pos, (self.input_box_width, self.input_box_height))
        self.guessed_words_button = pygame.Rect(self.show_words_pos, (self.guessed_words_button_width, self.guessed_words_button_height))
        
        self.guessed_words_background_rectangle = pygame.Rect(self.show_words_pos[0], self.show_words_pos[1] + self.guessed_words_button_height, self.guessed_words_background_width, self.guessed_words_background_height)
        # Center the "Show Words" text
        self.guessed_words_text_rectangle = self.guessed_words_button_text.get_rect()
        self.guessed_words_text_rectangle.centerx = self.guessed_words_button.centerx
        self.guessed_words_text_rectangle.centery = self.guessed_words_button.centery
    
        self.menu_y = self.show_words_pos[1] + 10
        # If we have a puzzle
        if self.letters:
            # Get the width and height of a character in the current puzzle
            self.character_width, self.character_height = self.font.size(self.letters[0])
            # Divide the width of the box and the width of a puzzle character to determine max possible characters.
            self.input_box_max_length = max(int(self.input_box_width / self.character_width), 15)
        else:
            print("self.letters is null or empty.")


    def draw_hexagon(self):
        self.calculate_scale()

        # Draw the letters and hexagons
        for i, pos in enumerate(self.positions):
            letter = self.letters[i]
            points = [
                (pos[0] - self.radius, pos[1]),
                (pos[0] - self.radius * 0.5, pos[1] - self.radius * 0.866),
                (pos[0] + self.radius * 0.5, pos[1] - self.radius * 0.866),
                (pos[0] + self.radius, pos[1]),
                (pos[0] + self.radius * 0.5, pos[1] + self.radius * 0.866),
                (pos[0] - self.radius * 0.5, pos[1] + self.radius * 0.866)
            ]

            # Check if the mouse cursor is inside the hexagon
            hex_pos = (pos[0] - self.radius, pos[1] - self.radius * 0.866)
            hex_rect = pygame.Rect(hex_pos, (self.radius * 2, self.radius * 1.732))
            
            if hex_rect.collidepoint(pygame.mouse.get_pos()):
                self.HEXAGON_HOVER = self.HOVER_COLOR
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, points)
            else:
                self.HEXAGON_HOVER = self.WHITE
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, points, 4)

            letter_text = self.font.render(letter, True, self.BLACK)
            letter_text_rect = letter_text.get_rect(center=pos)
            self.game_window.blit(letter_text, letter_text_rect)

    def draw_input_box(self):
        # Draw the input box rectangle
        pygame.draw.rect(self.game_window, self.WHITE, self.input_box_rectangle, 0)
        # Make a burder around the input box.
        pygame.draw.rect(self.game_window, self.BLACK, self.input_box_rectangle, 2)

        # Render the input box text onto a separate surface
        input_surface = self.font.render(self.input_box_text, True, self.WHITE)

        # Loop over the characters in the input box text and modify their colors
        for i, char in enumerate(self.input_box_text):
            char_color = self.VALID_COLOR if char in self.letters else self.INVALID_COLOR
            char_surface = self.font.render(char, True, char_color)
            input_surface.blit(char_surface, (i * self.character_width + .1, 0))

        # Center the input text within the input box rectangle
        input_rect = input_surface.get_rect()
        input_rect.center = self.input_box_rectangle.center

        # Blit the modified surface onto the main surface
        self.game_window.blit(input_surface, input_rect)

    def draw_shuffle_button(self):
        pygame.draw.rect(self.game_window, self.WHITE, self.shuffle_button_rectangle)
    
    def draw_guessed_words_botton(self):
        pygame.draw.rect(self.game_window, self.WHITE, self.guessed_words_button)
        self.game_window.blit(self.guessed_words_button_text, (self.guessed_words_text_rectangle))
        
        if self.show_words_box_visible:
            self.guessed_words_button_text = self.font.render("Hide guessed words", True, self.SHOW_WORDS_HOVER)     
        
        else:
            self.guessed_words_button_text = self.font.render("Show guessed words", True, self.SHOW_WORDS_HOVER)

    def draw_guessed_words(self): 
        # Draw the dropdown box if it's visible
        if self.show_words_box_visible:
            # Draw the up and down arrows
            pygame.draw.rect(self.game_window, self.WHITE, self.guessed_words_background_rectangle)
            if self.scroll_position == 0:
                pygame.draw.polygon(self.game_window, self.INPUT_BACKGROUND, [[self.arrow_up_x, self.arrow_up_y], [self.arrow_up_x + self.arrow_width, self.arrow_up_y], [self.arrow_up_x + self.arrow_width // 2, self.arrow_up_y - self.arrow_height]])
            else:
                pygame.draw.polygon(self.game_window, self.BLACK, [[self.arrow_up_x, self.arrow_up_y], [self.arrow_up_x + self.arrow_width, self.arrow_up_y], [self.arrow_up_x + self.arrow_width // 2, self.arrow_up_y - self.arrow_height]])
    
            # Draw the words
            for word_column in range(self.guessed_words_column_count):
                word_column_x = self.show_words_pos[0] + word_column * self.col_width
                for i in range(len(self.guessed_word_list)):
                    if i % self.guessed_words_column_count == word_column:
                        word_y = self.menu_y + ((i // self.guessed_words_column_count) * 30) - (self.scroll_position * 30)
                        if word_y >= self.show_words_pos[1] and word_y + 30 <= self.show_words_pos[1] + self.guessed_words_background_height:
                            word = self.font.render(self.guessed_word_list[i], True, self.BLACK)
                            self.game_window.blit(word, (word_column_x + 10, word_y + self.guessed_words_button_height))
                            pygame.draw.polygon(self.game_window, self.INPUT_BACKGROUND, [[self.arrow_down_x, self.arrow_down_y], [self.arrow_down_x + self.arrow_width, self.arrow_down_y], [self.arrow_down_x + self.arrow_width // 2, self.arrow_down_y + self.arrow_height]])
                        else:
                            pygame.draw.polygon(self.game_window, self.BLACK, [[self.arrow_down_x, self.arrow_down_y], [self.arrow_down_x + self.arrow_width, self.arrow_down_y], [self.arrow_down_x + self.arrow_width // 2, self.arrow_down_y + self.arrow_height]])

    def check_input_text_color(self):
        # Set the color for the current character
        for character in self.input_box_text:
            if character in self.letters:
                guess_color = self.VALID_COLOR
                print("Is valid")
            else:
                guess_color = self.INVALID_COLOR
                print("Invalid")
            return guess_color

    # Draw all screen elements
    def draw_screen(self):
        self.draw_hexagon()
        self.draw_input_box()
        self.draw_shuffle_button()
        self.draw_guessed_words_botton()
        self.draw_guessed_words()

    def run(self):
        while self.running:
            # Limit framerate
            self.clock.tick(60)
            
            # Fill the background
            self.game_window.fill(self.GAME_BACKGROUND)
            self.draw_screen()

            # Handle events
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                
                # If user resized game_window, set new dimensions
                elif event.type == pygame.VIDEORESIZE:
                    if event.w < self.game_window_minimum_width:
                        self.game_window_width = self.game_window_minimum_width
                    else:
                        self.game_window_width = event.w

                    if event.h < self.game_window_minimum_height:
                       self.game_window_height = self.game_window_minimum_height
                    else:
                        self.game_window_height = event.h

                    self.game_window = pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)
                    pygame.display.set_caption("Main Game")
                
                if event.type == pygame.MOUSEMOTION:
                    # Change the button color when hovered
                    if self.guessed_words_button.collidepoint(event.pos):
                        self.SHOW_WORDS_HOVER = self.HOVER_COLOR
                    else:
                        self.SHOW_WORDS_HOVER = self.BLACK

                        # Check if the user has scrolled the mouse wheel
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and self.show_words_box_visible:
                    print("Scrolled up!")
                    self.scroll_position = max(0, self.scroll_position - 1)
                    self.draw_guessed_words()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and self.show_words_box_visible:
                    print("Scrolled down!")
                    self.scroll_position = min(len(self.guessed_word_list) - 1, self.scroll_position + 1)
                    print(self.scroll_position)
                    self.draw_guessed_words()

                # Check if the user has clicked the up or down arrow
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.arrow_up_rectangle.collidepoint(event.pos):
                        self.scroll_direction = -1
                    elif self.arrow_down_rectangle.collidepoint(event.pos):
                        self.scroll_direction = 1

                # If user released left click on mouse.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.scroll_direction = 0
                    if self.guessed_words_button.collidepoint(event.pos):
                        self.show_words_box_visible = not self.show_words_box_visible

                    # Check if the click is inside the hexagons
                    for i, pos in enumerate(self.positions):
                        hex_pos = (pos[0] - self.radius, pos[1] - self.radius * 0.866)
                        hex_rect = pygame.Rect(hex_pos, (self.radius * 2, self.radius * 1.732))
                        
                        # If user clicked on a letter and can type
                        if hex_rect.collidepoint(event.pos):
                            # Update current string in the input box.
                            self.input_box_text += self.letters[i]

                # Handle key events
                elif event.type == pygame.KEYDOWN:
                    # Check if the backspace key was pressed
                    if event.key == pygame.K_BACKSPACE:
                        self.input_box_text = self.input_box_text[:-1]
                    # Check if a letter key was pressed
                    elif event.unicode.isalpha():
                        self.input_box_text += event.unicode.upper()
                    # elif event.key == pygame.K_KP_ENTER:
                        # Check if current string is valid word in word list.
                self.scroll_position = max(0, min((len(self.guessed_word_list) // self.guessed_words_column_count) - 15, self.scroll_position + self.scroll_direction))
                self.draw_guessed_words()
            # Update the screen
            self.draw_guessed_words()
            pygame.display.update()
        
        pygame.quit()

game = Game()
game.run()
