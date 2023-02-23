import pygame

class Game:
    def __init__(self):
        pygame.init()

        # Set up the window
        self.window_width, self.window_height = 1000, 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Main Game")

        # Define the center position of the hexagon
        self.center_x, self.center_y = self.window_width // 2, self.window_height // 2
        
        # Define the radius of the hexagon
        self.radius = 100

        # Set up the colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.INPUT_BACKGROUND = (200, 200, 200)
        self.HOVER_COLOR = (0, 255, 255)

        # Define the letters to display
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        # Set up the font
        self.font = pygame.font.SysFont(None, 30)
        self.character_width, self.character_height = self.font.size(self.letters[0])

        # Set up the input box
        self.input_box_text = ''
        self.is_input_box_active = False
        self.input_box_width = int(0.4 * self.window_width)
        self.input_box_height = int(0.08 * self.window_height)
        self.input_box_max_length = len(self.letters)
        self.user_can_type = True

        self.clock = pygame.time.Clock()
        self.running = True

    # Calculate the scale and position of elements on screen based on window size.
    def calculate_scale(self):
        self.center_x, self.center_y = self.window_width // 2, self.window_height // 2
        self.radius = min(self.window_width, self.window_height) // 8
        self.positions = [
            (self.center_x, self.center_y),
            (self.center_x, self.center_y - 2 * self.radius),
            (self.center_x + 2 * self.radius * 0.866, self.center_y - self.radius),
            (self.center_x + 2 * self.radius * 0.866, self.center_y + self.radius),
            (self.center_x, self.center_y + 2 * self.radius),
            (self.center_x - 2 * self.radius * 0.866, self.center_y + self.radius),
            (self.center_x - 2 * self.radius * 0.866, self.center_y - self.radius)
        ]

        # Calculate position of the input box
        self.input_box_pos = (self.positions[5][0] - self.radius, self.positions[4][1] + self.radius)
        
        # Calculate the size of the input box
        self.input_box_width = (self.radius * 5) + (self.radius * .5)
        self.input_box_height = int(0.08 * self.window_height)
        
        # Give calculated values to pygame.Rect to draw the input box.
        self.input_box_rectangle = pygame.Rect(self.input_box_pos, (self.input_box_width, self.input_box_height))
        
        # If we have a puzzle
        if self.letters:
            # Get the width and height of a character in the current puzzle
            self.character_width, self.character_height = self.font.size(self.letters[0])
            # Divide the width of the box and the width of a puzzle character to determine max possible characters.
            self.input_box_max_length = int(self.input_box_width / self.character_width)
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
                pygame.draw.polygon(self.window, self.HOVER_COLOR, points)
            else:
                pygame.draw.polygon(self.window, self.WHITE, points, 2)

            letter_text = self.font.render(letter, True, self.BLACK)
            letter_text_rect = letter_text.get_rect(center=pos)
            self.window.blit(letter_text, letter_text_rect)

    def draw_input_box(self):
        # Draw the input box rectangle
        color = self.INPUT_BACKGROUND if self.is_input_box_active else self.WHITE
        pygame.draw.rect(self.window, color, self.input_box_rectangle, 0)
        pygame.draw.rect(self.window, self.BLACK, self.input_box_rectangle, 2)

        # Draw the input text area
        text_surface = self.font.render(self.input_box_text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = self.input_box_rectangle.center
        self.window.blit(text_surface, text_rect)

        # Check length of string current in the input box
        if(len(self.input_box_text) < self.input_box_max_length):
            # If less than max length, user can type
            self.user_can_type = True
        else:
            # If greater than or equal to max length, user cannot type
            self.user_can_type = False

    # Draw all screen elements
    def draw_screen(self):
        self.draw_hexagon()
        self.draw_input_box()

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, 1, self.WHITE)
        return fps_text

    def run(self):
        while self.running:
            # Limit framerate
            self.clock.tick(60)
            
            # Fill the background
            self.window.fill((255, 30, 231))
            self.draw_screen()

            # Handle events
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                
                # If user resized window, set new dimensions
                elif event.type == pygame.VIDEORESIZE:
                    self.window_width, self.window_height = event.size

                # If user released left click on mouse.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    # Check if the click is inside the hexagons
                    for i, pos in enumerate(self.positions):
                        hex_pos = (pos[0] - self.radius, pos[1] - self.radius * 0.866)
                        hex_rect = pygame.Rect(hex_pos, (self.radius * 2, self.radius * 1.732))
                        
                        # If user clicked on a letter and can type
                        if hex_rect.collidepoint(event.pos) and self.user_can_type:
                            # Update current string in the input box.
                            self.input_box_text += self.letters[i]
                            self.is_input_box_active = True
                        else:
                            self.is_input_box_active = False

                # Handle key events
                elif event.type == pygame.KEYDOWN:
                    # Check if the backspace key was pressed
                    if event.key == pygame.K_BACKSPACE:
                        self.input_box_text = self.input_box_text[:-1]
                    # Check if a letter key was pressed
                    elif event.unicode.isalpha() and self.user_can_type:
                        self.input_box_text += event.unicode
                        
                    # elif event.key == pygame.K_KP_ENTER:
                        # Check if current string is valid word in word list.

            # Update the screen
            pygame.display.update()

        pygame.quit()

game = Game()
game.run()
