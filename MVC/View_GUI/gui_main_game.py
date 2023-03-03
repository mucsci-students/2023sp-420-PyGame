import pygame, os, random
import platform
import win32api     # Needed for Windows
# import AppKit       # Needed for macOS
import subprocess   # Need for Linux

from model_shuffleLetters import *
from model_puzzle import *
from model_PuzzleStats import *

class Game:
    def __init__(self, puzzle, puzzle_stats):
            
        self.puzzle = puzzle
        self.puzzle_stats = puzzle_stats
        print(f'gui_main_game.py - def__init__(): puzzle.pangram is: {puzzle.pangram}')
        print(f'gui_main_game.py - def__init__(): puzzle.required_letter is: {puzzle.required_letter}')

        pygame.init()

        self.setup_screen()
        pygame.display.set_caption("Main Game")
        self.image_file_path = os.path.join(os.getcwd(), "mvc/view_gui/helpicons")
        self.background_image = pygame.image.load(os.path.join(self.image_file_path, "Background_Image.png")).convert()
        self.scaled_background_image = self.background_image
        
        self.game_window = pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)
        if pygame.display.get_init():
            pygame.display.window_position = (0,0)
        
        # Define the radius and center position of the hexagon
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2

        # Set up the colors
        self.WHITE = (255, 255, 255)                # White
        self.BLACK = (0, 0, 0)                      # Black
        self.ORANGE = (255, 189, 49)                # Orange
        self.NEON_ORANGE = (255, 85, 0)             # Obnoxious Orange
        self.ARROW_COLOR = (155, 155, 155)          # Light Gray
        self.INPUT_BACKGROUND = (224, 224, 224)     # Gray
        self.VALID_COLOR = (68, 214, 44)            # Green
        self.INVALID_COLOR = (255, 0, 0)            # Red
        self.GAME_BACKGROUND = (255, 30, 231)       # Bright Pink
        self.HOVER_COLOR = self.ORANGE              # Changes while running
        self.SHOW_WORDS_HOVER = self.WHITE          # Changes while running
        self.HEXAGON_HOVER = self.BLACK             # Changes while running
        self.SHUFFLE_HOVER = self.ORANGE            # Changes while running
        self.SUBMIT_HOVER = self.ORANGE             # Changes while running
        self.SUBMIT_BUTTON = self.BLACK
        self.BUTTON_BACKGROUND = (186,100,65)
        self.SCORE = self.NEON_ORANGE
        self.SAVE_BUTTON = self.BLACK
        self.SAVE_HOVER = self.ORANGE
        # Define the letters to display
        self.puzzle_stats.shuffled_puzzle = self.puzzle_stats.shuffled_puzzle.upper()
        
        self.current_word_list = []
        self.guessed_word_list = []
        # self.guessed_word_list = self.puzzle_stats.guesses

        self.input_box_max_length = 0

        for word in self.puzzle.current_word_list:
            self.current_word_list.append(word[0])
            if len(word[0]) > self.input_box_max_length:
                self.input_box_max_length = len(word[0])
    
    
        print(self.current_word_list)

        # Set up the scroll variables
        self.scroll_position = 0
        self.scroll_direction = 0

        print(self.input_box_max_length)

        # Set up puzzle letter font
        self.puzzle_letter_font_size = int(self.game_window_width * .15)
        print(self.puzzle_letter_font_size)  
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

        # self.character_width, self.character_height = self.input_box_font.size(self.puzzle_stats.shuffled_puzzle[0])
        self.character_width, self.character_height = self.guessed_word_button_font.size('i')
        print(f'char width: {self.character_width}')
        print(f'char height: {self.character_height}')
        
        self.clock = pygame.time.Clock()
        self.input_box_text = ''
        
        self.running = True
        self.backspace_down = False
        self.show_words_box_visible = False
        

    # Get the size of the primary monitor based on the operating system        
    def setup_screen(self):
        # Set up the main game game_window
        self.game_window_minimum_width, self.game_window_minimum_height = 800, 600

        # Get the size of the primary monitor on Windows
        if platform.system() == "Windows":
            self.game_window_width = win32api.GetSystemMetrics(0) // 2
            self.game_window_height = win32api.GetSystemMetrics(1) // 2
        
        # Get the size of the primary monitor on macOS
        elif platform.system() == "Darwin":
            screen_size = AppKit.NSScreen.mainScreen().frame().size
            self.game_window_width = win32api.GetSystemMetrics(0) // 2
            self.game_window_height = win32api.GetSystemMetrics(1) // 2
        
        # Get the size of the primary monitor on Linux
        elif platform.system() == "Linux":
            output = subprocess.check_output(["xrandr"]).decode("utf-8")
            primary_line = [line for line in output.splitlines() if " primary " in line][0]
            screen_size = primary_line.split()[3]
            self.game_window_width, self.game_window_height = map(int, screen_size.split("x")) // 2
        
        # Minimum size
        else:
            self.game_window_width = self.game_window_minimum_width
            self.game_window_height = self.game_window_minimum_height

    
    # Calculate the scale and position of elements on screen based on game_window size.
    def calculate_scale(self):
        self.center_x, self.center_y = self.game_window_width // 2, self.game_window_height // 2
        self.radius = min(self.game_window_width, self.game_window_height) // 8
        self.puzzle_letter_center_position = [
            (self.center_x, self.center_y),                                             # Center
            (self.center_x, self.center_y - 2 * self.radius),                           # Top Middle
            (self.center_x + 2 * self.radius * 0.866, self.center_y - self.radius),     # Top Right
            (self.center_x + 2 * self.radius * 0.866, self.center_y + self.radius),     # Bottom right
            (self.center_x, self.center_y + 2 * self.radius),                           # Bottom Middle
            (self.center_x - 2 * self.radius * 0.866, self.center_y + self.radius),     # Bottom Left
            (self.center_x - 2 * self.radius * 0.866, self.center_y - self.radius)      # Top Left
        ]

        # Calculate position of the input box and dropdown menu.
        self.input_box_pos = (self.puzzle_letter_center_position[5][0] - self.radius, self.puzzle_letter_center_position[4][1] + self.radius)
        self.show_words_pos = (self.puzzle_letter_center_position[5][0] - (self.radius * 3), self.puzzle_letter_center_position[1][1] - (self.radius * 1.75))

        # Calculate the size of the input box
        self.input_box_width = (self.radius * 5) + (self.radius * .5)
        self.input_box_height = int(self.radius * .5)

        # Calculate the size of the "Show Words" button
        self.guessed_words_button_width = self.input_box_width * 1.75
        self.guessed_words_button_height = int(0.06 * self.game_window_height)
        self.guessed_words_button_text = self.guessed_word_button_font.render("Show Guessed Words", True, self.SHOW_WORDS_HOVER)

        # Calculate the size of the dropdown window
        self.guessed_words_background_width = self.guessed_words_button_width
        self.guessed_words_background_height = self.game_window_height * .90
      
        # Set up the arrow buttons
        self.arrow_width = self.guessed_words_background_width * .05
        self.arrow_height = self.guessed_words_background_height * .05
        self.arrow_up_x = self.show_words_pos[0] + self.guessed_words_background_width - (self.arrow_height * 2)
        self.arrow_up_y = self.show_words_pos[1] + (self.arrow_height * 3)
        self.arrow_down_x = self.arrow_up_x
        self.arrow_down_y =  self.show_words_pos[1] + self.guessed_words_background_height - self.arrow_height

        # Define the arrow button rectangles
        self.arrow_up_rectangle = pygame.Rect(self.arrow_up_x, self.arrow_up_y - self.arrow_height, self.arrow_width,  self.arrow_height)
        self.arrow_down_rectangle = pygame.Rect(self.arrow_down_x, self.arrow_down_y, self.arrow_width, self.arrow_height)
       
        # Calculate the number of columns based on the width of the display area
        self.word_width = self.input_box_font_size * max(len(word) for word in self.current_word_list)
        self.col_width = self.word_width + 5

        self.guessed_words_column_count = int(max(1, self.guessed_words_background_width // self.col_width))
        self.guessed_words_list_rows = len(self.current_word_list) // self.guessed_words_column_count + (len(self.current_word_list) % self.guessed_words_column_count != 0)
        
        # Give calculated values to pygame.Rect to draw the input box.
        self.input_box_rectangle = pygame.Rect(self.input_box_pos, (self.input_box_width, self.input_box_height))
        self.guessed_words_button = pygame.Rect(self.show_words_pos, (self.guessed_words_button_width, self.guessed_words_button_height))

        self.guessed_words_background_rectangle = pygame.Rect(self.show_words_pos[0], self.show_words_pos[1] + self.guessed_words_button_height, self.guessed_words_background_width, self.guessed_words_background_height)
        
        # Center the "Show Words" text
        self.guessed_words_text_rectangle = self.guessed_words_button_text.get_rect()
        self.guessed_words_text_rectangle.centerx = self.guessed_words_button.centerx
        self.guessed_words_text_rectangle.centery = self.guessed_words_button.centery

        self.draw_gradient(self.input_box_rectangle, self.input_box_pos)
        self.draw_gradient(self.guessed_words_button, self.show_words_pos)
        if self.show_words_box_visible:
            self.draw_gradient(self.guessed_words_background_rectangle, self.show_words_pos)
        
        self.menu_y = self.show_words_pos[1] + 5
        
        # Get the width and height of a character in the current puzzle
        self.character_width, self.character_height = self.input_box_font.size(self.puzzle.pangram[0])
        # Divide the width of the box and the width of a puzzle character to determine max possible characters.


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
        # Draw the letters and hexagons
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
            hex_pos = (pos[0] - self.radius, pos[1] - self.radius * 0.866)
            hex_rect = pygame.Rect(hex_pos, (self.radius * 2, self.radius * 1.732))
            
            if hex_rect.collidepoint(pygame.mouse.get_pos()) and not self.show_words_box_visible:
                self.HEXAGON_HOVER = self.HOVER_COLOR
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, hex_points)
            else:
                self.HEXAGON_HOVER = self.BLACK
                pygame.draw.polygon(self.game_window, self.HEXAGON_HOVER, hex_points, 6)

            letter_text = self.puzzle_letter_font.render(letter, True, self.BLACK)
            letter_text_rect = letter_text.get_rect(center=pos)
            self.game_window.blit(letter_text, letter_text_rect)


    def draw_input_box(self):
        # Draw the input box rectangle and a fancy border.
        pygame.draw.rect(self.game_window, self.BLACK, self.input_box_rectangle, 2)

        # Variable storing the rendered font
        input_surface = self.input_box_font.render(self.input_box_text, True, self.INPUT_BACKGROUND)
        
        # Center the input text within the input box rectangle
        input_rect = input_surface.get_rect()
        if self.bad_timer_active:
            # Randomly modify the position of the text within a certain range
            self.input_box_rectangle.center = (self.input_box_rectangle.centerx + random.randint(-5, 5), self.input_box_rectangle.centery + random.randint(-5, 5))
        
        input_rect.center = self.input_box_rectangle.center

        # Put the text on the rect
        self.game_window.blit(input_surface, input_rect)


    def draw_shuffle_button(self):
        # Set the (x,y) values of the shuffle letters button to be to the right of the input box.
        self.shuffle_button_pos = (self.input_box_pos[0] - self.radius, self.input_box_pos[1])
        self.save_button_pos = (self.input_box_pos[0] - (self.radius * 2), self.input_box_pos[1])
        
        shuffle_letter_hex_points = [
            (self.shuffle_button_pos[0], self.shuffle_button_pos[1] - (self.input_box_height * .5)),                                 
            (self.shuffle_button_pos[0] + (self.input_box_height), self.input_box_rectangle.y),     
            (self.shuffle_button_pos[0] + (self.input_box_height), self.input_box_rectangle.y + (self.input_box_height)),
            (self.shuffle_button_pos[0], self.shuffle_button_pos[1] + (self.input_box_height * 1.5)),
            (self.shuffle_button_pos[0] - (self.input_box_height), self.input_box_rectangle.y + self.input_box_height),    
            (self.shuffle_button_pos[0] - (self.input_box_height), self.input_box_rectangle.y),   
        ]

        save_letter_hex_points = []
        for i in shuffle_letter_hex_points:
            new_x = (i[0] - (self.radius * 2), i[1])
            save_letter_hex_points.append(new_x)

        self.shuffle_button = pygame.draw.polygon(self.game_window, self.SHUFFLE_HOVER, shuffle_letter_hex_points, 4)
        self.save_button = pygame.draw.polygon(self.game_window, self.SAVE_HOVER, save_letter_hex_points, 4)
        shuffle_text = self.input_box_font.render("Shuffle", True, self.SUBMIT_BUTTON)
        shuffle_text_rect = shuffle_text.get_rect(center=self.shuffle_button.center)
        save_text = self.input_box_font.render("  Save", True, self.SAVE_BUTTON)
        save_text_rect = shuffle_text.get_rect(center=self.save_button.center)

        self.game_window.blit(save_text, save_text_rect)
        self.game_window.blit(shuffle_text, shuffle_text_rect)


    def draw_submit_button(self):
        # Set the (x,y) values of the shuffle letters button to be to the right of the input box.
        self.submit_button_pos = (self.input_box_pos[0] + self.input_box_width + self.radius, self.input_box_pos[1])
        
        submit_guess_hex_points = [
            (self.submit_button_pos[0], self.submit_button_pos[1] - (self.input_box_height * .5)),                                 
            (self.submit_button_pos[0] + (self.input_box_height), self.input_box_rectangle.y),     
            (self.submit_button_pos[0] + (self.input_box_height), self.input_box_rectangle.y + (self.input_box_height)),
            (self.submit_button_pos[0], self.submit_button_pos[1] + (self.input_box_height * 1.5)),
            (self.submit_button_pos[0] - (self.input_box_height), self.input_box_rectangle.y + self.input_box_height),    
            (self.submit_button_pos[0] - (self.input_box_height), self.input_box_rectangle.y),   
        ]

        self.submit_button = pygame.draw.polygon(self.game_window, self.SUBMIT_HOVER, submit_guess_hex_points, 4)
        submit_text = self.input_box_font.render("Submit", True, self.SUBMIT_BUTTON)
        submit_text_rect = submit_text.get_rect(center=self.submit_button.center)
        self.game_window.blit(submit_text, submit_text_rect)
    

    def draw_guessed_words_button(self):
        pygame.draw.rect(self.game_window, self.BLACK, self.guessed_words_button, 2)
        self.game_window.blit(self.guessed_words_button_text, (self.guessed_words_text_rectangle))
        
        if self.show_words_box_visible:
            self.guessed_words_button_text = self.guessed_word_button_font.render("Hide guessed words", True, self.BLACK)     
        else:
            self.guessed_words_button_text = self.guessed_word_button_font.render("Show guessed words", True, self.BLACK)

    def draw_rank(self):
        if not self.show_words_box_visible:
            self.rank_width = self.guessed_words_button.right - (self.puzzle_letter_center_position[2][0] - self.radius)
            self.rank_height = self.guessed_words_button_height
            self.rank_pos = self.puzzle_letter_center_position[2][0] - self.radius + 1, self.guessed_words_button.centery + (self.guessed_words_button_height * .5) + 1
            self.rank_rectangle = pygame.Rect(self.rank_pos, (self.rank_width, self.rank_height))
            pygame.draw.rect(self.game_window, self.BLACK, self.rank_rectangle, 2)

            self.rank_text = self.guessed_word_button_font.render(f'{self.puzzle_stats.get_rank()}: {self.puzzle_stats.score} / {self.puzzle_stats.maxScore}', True, self.SCORE)
            
            self.rank_text_x = (self.rank_width - self.rank_text.get_width()) // 2  
            self.rank_text_y = (self.rank_height - self.rank_text.get_height()) // 2
            self.rank_surface = pygame.Surface((self.rank_width, self.rank_height), pygame.SRCALPHA)
            self.draw_gradient(self.rank_rectangle, self.rank_pos)
            self.rank_surface.blit(self.rank_text, (self.rank_text_x, self.rank_text_y))
            self.game_window.blit(self.rank_surface, (self.rank_pos))



    def draw_guessed_words(self):
        # Draw the dropdown box if it's visible
        if self.show_words_box_visible:
            # Draw the up and down arrows
            if self.scroll_position == 0:
                pygame.draw.polygon(self.game_window, self.ARROW_COLOR, [[self.arrow_up_x, self.arrow_up_y], [self.arrow_up_x + self.arrow_width, self.arrow_up_y], [self.arrow_up_x + self.arrow_width // 2, self.arrow_up_y - self.arrow_height]])
            else:
                pygame.draw.polygon(self.game_window, self.BLACK, [[self.arrow_up_x, self.arrow_up_y], [self.arrow_up_x + self.arrow_width, self.arrow_up_y], [self.arrow_up_x + self.arrow_width // 2, self.arrow_up_y - self.arrow_height]])

            # Draw the words
            for word_column in range(self.guessed_words_column_count):
                word_column_x = self.show_words_pos[0] + word_column * self.col_width
                for i in range(len(self.guessed_word_list)):
                    if i % self.guessed_words_column_count == word_column:
                        word_y = self.menu_y + ((i // self.guessed_words_column_count) * 30) - (self.scroll_position * 30)
                        if word_y >= self.show_words_pos[1] and word_y + 30 <= self.show_words_pos[1] + self.guessed_words_background_height:
                            word = self.input_box_font.render(self.guessed_word_list[i], True, self.NEON_ORANGE)
                            print(self.guessed_word_list[i])
                            self.game_window.blit(word, (word_column_x + 10, word_y + self.guessed_words_button_height))
                            pygame.draw.polygon(self.game_window, self.ARROW_COLOR, [[self.arrow_down_x, self.arrow_down_y], [self.arrow_down_x + self.arrow_width, self.arrow_down_y], [self.arrow_down_x + self.arrow_width // 2, self.arrow_down_y + self.arrow_height]])
                        else:
                            pygame.draw.polygon(self.game_window, self.BLACK, [[self.arrow_down_x, self.arrow_down_y], [self.arrow_down_x + self.arrow_width, self.arrow_down_y], [self.arrow_down_x + self.arrow_width // 2, self.arrow_down_y + self.arrow_height]])

    
    def handle_guess_visuals(self):
        if (self.puzzle_stats.get_check_guess(self.input_box_text, self.puzzle)) == 0:
            self.guessed_word_list = self.puzzle_stats.guesses
            self.INPUT_BACKGROUND = self.WHITE
            self.SUBMIT_BUTTON = self.VALID_COLOR
            self.SUBMIT_HOVER = self.VALID_COLOR
            self.SHUFFLE_HOVER = self.VALID_COLOR
            self.SAVE_HOVER = self.VALID_COLOR
            self.SAVE_BUTTON = self.VALID_COLOR
            self.INPUT_BACKGROUND = self.VALID_COLOR
            self.SCORE = self.VALID_COLOR
            
            self.good_timer_active = True
            self.timer_start_time = pygame.time.get_ticks()
            if len(self.input_box_text) == 4:
                self.input_box_text = f'+ {self.puzzle_stats.get_word_points(self.input_box_text)} point!'
            else:
                self.input_box_text = f'+ {self.puzzle_stats.get_word_points(self.input_box_text)} points!'
        else:
            self.SUBMIT_BUTTON = self.INVALID_COLOR
            self.SUBMIT_HOVER = self.INVALID_COLOR
            self.SHUFFLE_HOVER = self.INVALID_COLOR
            self.INPUT_BACKGROUND = self.INVALID_COLOR
            self.SAVE_HOVER = self.INVALID_COLOR
            self.SAVE_BUTTON = self.INVALID_COLOR
            self.bad_timer_active = True
            self.timer_start_time = pygame.time.get_ticks()


    def scale_font(self):
        # Set new puzzle font size
        self.puzzle_letter_font_size = int(self.radius * 1.5)        
        self.puzzle_letter_font = pygame.font.SysFont(None, self.puzzle_letter_font_size)
        
        if self.good_timer_active:
            # Set new input box font size
            self.input_box_font_size = int(self.input_box_height * .80)        
            self.input_box_font = pygame.font.SysFont(None, self.input_box_font_size)
        else:
            # Set new input box font size
            self.input_box_font_size = int(self.input_box_height * .75)        
            self.input_box_font = pygame.font.SysFont(None, self.input_box_font_size)

        # Set new show guessed words font size
        self.guessed_word_button_font_size = int(self.guessed_words_button_width * .05)
        self.guessed_word_button_font = pygame.font.SysFont(None, self.guessed_word_button_font_size)  


    def handle_save_visuals(self):
        background_surface = pygame.Surface((self.game_window_width, self.game_window_height), pygame.SRCALPHA)
        background_surface.fill((0, 0, 0, 128))



        # while True:
        #     self.game_window.blit(background_surface, (0, 0))
        #     pygame.display.update()
        #     event = pygame.event.wait()
        #     if event.type == KEYDOWN:
        #         if event.key == K_RETURN:
        #             break
        #         elif event.key == K_BACKSPACE:
        #             input_text = input_text[:-1]
        #         else:
        #             input_text += event.unicode

        #     # Render the text as a Surface and blit it onto the text display
        #     text_surface = font.render(input_text, True, (0, 0, 0))
        #     self.game_window.blit(background_surface, (0, 0))
        #     pygame.draw.rect(self.game_window, input_box_color, input_box_rect)
        #     self.game_window.blit(text_surface, (text_display_x, text_display_y))
        #     pygame.draw.rect(screen, text_display_color, text_display_rect)
        #     pygame.display.update()
   
        # self.puzzle_stats.get_save_game()
        


    # Draw all screen elements
    def draw_screen(self):
        self.draw_hexagon()
        self.draw_input_box()
        self.draw_submit_button()
        self.draw_shuffle_button()
        self.draw_guessed_words_button()
        self.draw_guessed_words()
        self.draw_rank()
        self.scale_font()

    def run(self):
        pygame.time.wait(500)

        while self.running:
            # Limit framerate
            self.clock.tick(60)
            
            # Fill the background
            self.game_window.blit(self.scaled_background_image, (0,0))
            self.draw_screen()
            if self.bad_timer_active:
                # Check if the timer has expired
                if pygame.time.get_ticks() - self.timer_start_time >= self.timer_duration:
                    # Stop the timer after the specified duration has passed
                    self.bad_timer_active = False
                    self.INPUT_BACKGROUND = self.WHITE
                    self.SUBMIT_HOVER = self.BLACK
                    self.SHUFFLE_HOVER = self.BLACK
                    self.SUBMIT_BUTTON = self.BLACK
                    self.SAVE_HOVER = self.BLACK
                    self.SAVE_BUTTON = self.BLACK
            
            if self.good_timer_active:
                 if pygame.time.get_ticks() - self.timer_start_time >= self.timer_duration:
                    # Stop the timer after the specified duration has passed
                    self.good_timer_active = False
                    self.input_box_text = ''
                    self.SCORE = self.NEON_ORANGE
                    self.INPUT_BACKGROUND = self.WHITE
                    self.SUBMIT_HOVER = self.BLACK
                    self.SHUFFLE_HOVER = self.BLACK
                    self.SUBMIT_BUTTON = self.BLACK
                    self.SAVE_HOVER = self.BLACK
                    self.SAVE_BUTTON = self.BLACK

    
            # Handle events
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                
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

                    self.game_window = pygame.display.set_mode((self.game_window_width, self.game_window_height), pygame.RESIZABLE)
                    self.scaled_background_image = pygame.transform.scale(self.background_image, (self.game_window_width, self.game_window_height)).convert()
                
                if event.type == pygame.MOUSEMOTION:
                    # Change the button color when hovered
                    if self.guessed_words_button.collidepoint(event.pos):
                        self.SHOW_WORDS_HOVER = self.NEON_ORANGE
                    else:
                        self.SHOW_WORDS_HOVER = self.ORANGE
                    
                    if self.shuffle_button.collidepoint(event.pos) and not self.show_words_box_visible and not self.bad_timer_active:
                        self.SHUFFLE_HOVER = self.ORANGE
                    else:
                        self.SHUFFLE_HOVER = self.BLACK

                    if self.save_button.collidepoint(event.pos) and not self.show_words_box_visible and not self.bad_timer_active:
                        self.SAVE_HOVER = self.ORANGE
                    else:
                        self.SAVE_HOVER = self.BLACK
                    
                    if self.submit_button.collidepoint(event.pos) and not self.show_words_box_visible and not self.bad_timer_active:
                        self.SUBMIT_HOVER = self.ORANGE
                    else:
                        self.SUBMIT_HOVER = self.BLACK
                    
                # Check if the user has clicked the up or down arrow
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.show_words_box_visible:
                    if self.arrow_up_rectangle.collidepoint(event.pos):
                        self.scroll_direction = -1
                    elif self.arrow_down_rectangle.collidepoint(event.pos):
                        self.scroll_direction = 1

                # Mouse scroll up with guessed words visible
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and self.show_words_box_visible:
                    self.scroll_position = max(0, self.scroll_position - 1)
                    # Redraw words to account for new scroll position.
                    self.draw_guessed_words()

                # Mouse scroll down with guessed words visible
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and self.show_words_box_visible:
                    self.scroll_position = min(len(self.guessed_word_list) - 1, self.scroll_position + 1)
                    # Redraw words to account for new scroll position.
                    self.draw_guessed_words()

                # If user released left click on mouse.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.scroll_direction = 0
                    # If user clicked on "Show Words".
                    if self.guessed_words_button.collidepoint(event.pos):
                        self.show_words_box_visible = not self.show_words_box_visible
                    
                    # If user clicked on "Shuffle".
                    elif self.shuffle_button.collidepoint(event.pos) and not self.show_words_box_visible:
                        # Calls shuffle_letters
                        self.puzzle_stats.shuffled_puzzle = ShuffleKey(self.puzzle.pangram, self.puzzle.required_letter)
                        self.puzzle_stats.shuffled_puzzle = self.puzzle_stats.shuffled_puzzle.upper()

                    # If user clicked on "Submit".
                    elif self.submit_button.collidepoint(event.pos) and not self.show_words_box_visible:
                        self.handle_guess_visuals()
                    
                    # If user clicked on "Save".
                    elif self.save_button.collidepoint(event.pos) and not self.show_words_box_visible:
                        self.handle_save_visuals()

                    # Check if user clicked inside a hex related to a letter.
                    for i, pos in enumerate(self.puzzle_letter_center_position):
                        hex_pos = (pos[0] - self.radius, pos[1] - self.radius * 0.866)
                        hex_rect = pygame.Rect(hex_pos, (self.radius * 2, self.radius * 1.732))
                        
                        # If user did click on a letter:
                        if hex_rect.collidepoint(event.pos):
                            # Update current string with clicked letter.
                            self.input_box_text += self.puzzle_stats.shuffled_puzzle[i]

                # Handle key events
                elif event.type == pygame.KEYDOWN:
                    key=pygame.key.name(event.key)
                    print (key, "Key is pressed")
                    # Check if the backspace key was pressed
                    if event.key == pygame.K_BACKSPACE:
                        self.backspace_down = True
                    
                    # Check if a letter key was pressed
                    elif event.unicode.isalpha() and event.unicode in self.puzzle.pangram:
                        if len(self.input_box_text) < self.input_box_max_length:
                            self.backspace_down = False
                            self.input_box_text += event.unicode.upper()
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        self.backspace_down = False
                    
                    if event.key == pygame.K_RETURN and not self.good_timer_active:
                        if self.input_box_text != '':
                            self.handle_guess_visuals()
                
            if self.backspace_down:
                self.input_box_text = self.input_box_text[:-1]

            self.scroll_position = max(0, min((len(self.guessed_word_list) // self.guessed_words_column_count) - 15, self.scroll_position + self.scroll_direction))
            self.draw_guessed_words()
            pygame.display.update()
        pygame.quit()
