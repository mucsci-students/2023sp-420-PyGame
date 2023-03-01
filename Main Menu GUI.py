import pygame

pygame.init()

# Set up the display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Main Menu PYGAME')

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Define the box dimensions and positions
BOX_WIDTH = 150
BOX_HEIGHT = 50
BOX_SPACING = 20
BOX_X = (WINDOW_WIDTH - BOX_WIDTH) / 2
BOX_Y_START = (WINDOW_HEIGHT - (BOX_HEIGHT * 4 + BOX_SPACING * 3)) / 2
NEW_GAME_BOX_Y = BOX_Y_START
LOAD_GAME_BOX_Y = NEW_GAME_BOX_Y + BOX_HEIGHT + BOX_SPACING
HELP_BOX_Y = LOAD_GAME_BOX_Y + BOX_HEIGHT + BOX_SPACING
EXIT_BOX_Y = HELP_BOX_Y + BOX_HEIGHT + BOX_SPACING

# Define the text for each box
HEADER_TEXT = 'SPELLING BEE BY PYGAME'
NEW_GAME_TEXT = 'New Game'
LOAD_GAME_TEXT = 'Load Game'
HELP_TEXT = 'Help / How to Play'
EXIT_TEXT = 'Exit'

# Define the font for the text
FONT_SIZE = 30
FONT = pygame.font.Font(None, FONT_SIZE)

# Draw the boxes and text on the screen
def draw_boxes():
    global new_game_box, load_game_box, help_box, exit_box
    new_game_box = pygame.draw.rect(DISPLAY_SURFACE, GRAY, (BOX_X, NEW_GAME_BOX_Y, BOX_WIDTH, BOX_HEIGHT))
    load_game_box = pygame.draw.rect(DISPLAY_SURFACE, GRAY, (BOX_X, LOAD_GAME_BOX_Y, BOX_WIDTH, BOX_HEIGHT))
    help_box = pygame.draw.rect(DISPLAY_SURFACE, GRAY, (BOX_X, HELP_BOX_Y, BOX_WIDTH, BOX_HEIGHT))
    exit_box = pygame.draw.rect(DISPLAY_SURFACE, GRAY, (BOX_X, EXIT_BOX_Y, BOX_WIDTH, BOX_HEIGHT))

    title_text_surface = FONT.render(HEADER_TEXT, True, WHITE)
    title_text_rect = title_text_surface.get_rect(center=((WINDOW_WIDTH/2), BOX_Y_START/2))
    DISPLAY_SURFACE.blit(title_text_surface, title_text_rect)

    new_game_text_surface = FONT.render(NEW_GAME_TEXT, True, WHITE)
    new_game_text_rect = new_game_text_surface.get_rect(center=new_game_box.center)
    DISPLAY_SURFACE.blit(new_game_text_surface, new_game_text_rect)

    load_game_text_surface = FONT.render(LOAD_GAME_TEXT, True, WHITE)
    load_game_text_rect = load_game_text_surface.get_rect(center=load_game_box.center)
    DISPLAY_SURFACE.blit(load_game_text_surface, load_game_text_rect)

    help_text_surface = FONT.render(HELP_TEXT, True, WHITE)
    help_text_rect = help_text_surface.get_rect(center=help_box.center)
    DISPLAY_SURFACE.blit(help_text_surface, help_text_rect)

    exit_text_surface = FONT.render(EXIT_TEXT, True, WHITE)
    exit_text_rect = exit_text_surface.get_rect(center=exit_box.center)
    DISPLAY_SURFACE.blit(exit_text_surface, exit_text_rect)

# Main game loop
def main():
    global new_game_box, load_game_box, help_box, exit_box, WINDOW_HEIGHT, WINDOW_WIDTH
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if new_game_box.collidepoint(mouse_pos):
                    print('Run New Game')
                elif load_game_box.collidepoint(mouse_pos):
                    print('Run Load Game')
                elif help_box.collidepoint(mouse_pos):
                    print('Help clicked')
                elif exit_box.collidepoint(mouse_pos):
                    running = False
                
            elif event.type == pygame.VIDEORESIZE:  
                w, h = pygame.display.get_surface().get_size()
                WINDOW_WIDTH = w
                WINDOW_HEIGHT = h
        # Draw the screen
            DISPLAY_SURFACE.fill(BLACK)
            draw_boxes()
            pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()