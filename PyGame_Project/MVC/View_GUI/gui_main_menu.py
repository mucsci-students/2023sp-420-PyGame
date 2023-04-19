import pygame
from PyGame_Project.MVC.View_GUI.newgame import *
from PyGame_Project.MVC.View_GUI.loadgame import *
from PyGame_Project.MVC.View_GUI.helpgui import *

def start_gui():
    pygame.init()

    # Set up the display window
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Main Menu')

    # Define some colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Define the box dimensions and positions
    BOX_WIDTH = 250
    BOX_HEIGHT = 50
    BOX_SPACING = 80
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
    HELP_TEXT = 'Help'
    EXIT_TEXT = 'Exit'

    # Define the font for the text
    FONT_SIZE = 30
    FONT = pygame.font.Font(None, FONT_SIZE)

    # Draw the boxes and text on the screen
    def draw_boxes():
        global new_game_box, load_game_box, help_box, exit_box
        half_width = BOX_WIDTH // 2
        half_height = BOX_HEIGHT // 2
        
        '''hexagon_points = [
            (BOX_X + half_width, NEW_GAME_BOX_Y),
            (BOX_X + BOX_WIDTH, NEW_GAME_BOX_Y + half_height),
            (BOX_X + BOX_WIDTH, NEW_GAME_BOX_Y + half_height + BOX_HEIGHT),
            (BOX_X + half_width, NEW_GAME_BOX_Y + BOX_HEIGHT + BOX_HEIGHT // 2),
            (BOX_X, NEW_GAME_BOX_Y + half_height + BOX_HEIGHT),
            (BOX_X, NEW_GAME_BOX_Y + half_height)
        ]'''
            # create hexagon points (NOT the lines between the points)
        hex_radius = 70 # change this for bigger hexagons, considered midpoint
        hexagon_points = []
        for i in range(6):
            hex_angle = (math.pi / 180) * (60 * i) # converts from degrees to radians
            hex_x = hex_radius * math.cos(hex_angle) + 300 # the + changes x position
            hex_y = hex_radius * math.sin(hex_angle) + 120 # the + changes y position
            hexagon_points.append((hex_x, hex_y))

        
        
        new_game_box = pygame.draw.polygon(DISPLAY_SURFACE, GRAY, hexagon_points)
        load_game_box = pygame.draw.polygon(DISPLAY_SURFACE, GRAY, [tuple(map(sum, zip(point, (0, BOX_HEIGHT + BOX_SPACING)) )) for point in hexagon_points])
        help_box = pygame.draw.polygon(DISPLAY_SURFACE, GRAY, [tuple(map(sum, zip(point, (0, 2 * BOX_HEIGHT + 2 * BOX_SPACING)) )) for point in hexagon_points])
        exit_box = pygame.draw.polygon(DISPLAY_SURFACE, GRAY, [tuple(map(sum, zip(point, (0, 3 * BOX_HEIGHT + 3 * BOX_SPACING)) )) for point in hexagon_points])

        title_text_surface = FONT.render(HEADER_TEXT, True, BLACK)
        title_text_rect = title_text_surface.get_rect(center=((WINDOW_WIDTH/2), BOX_Y_START/2))
        DISPLAY_SURFACE.blit(title_text_surface, title_text_rect)

        new_game_text_surface = FONT.render(NEW_GAME_TEXT, True, BLACK)
        new_game_text_rect = new_game_text_surface.get_rect(center=new_game_box.center)
        DISPLAY_SURFACE.blit(new_game_text_surface, new_game_text_rect)

        load_game_text_surface = FONT.render(LOAD_GAME_TEXT, True, BLACK)
        load_game_text_rect = load_game_text_surface.get_rect(center=load_game_box.center)
        DISPLAY_SURFACE.blit(load_game_text_surface, load_game_text_rect)

        help_text_surface = FONT.render(HELP_TEXT, True, BLACK)
        help_text_rect = help_text_surface.get_rect(center=help_box.center)
        DISPLAY_SURFACE.blit(help_text_surface, help_text_rect)

        exit_text_surface = FONT.render(EXIT_TEXT, True, BLACK)
        exit_text_rect = exit_text_surface.get_rect(center=exit_box.center)
        DISPLAY_SURFACE.blit(exit_text_surface, exit_text_rect)

    # Main game loop
    def main_menu():
        global new_game_box, load_game_box, help_box, exit_box, WINDOW_HEIGHT, WINDOW_WIDTH
        running = True

        while running:
            # Handle events
            pygame.display.set_caption('Main Menu')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if new_game_box.collidepoint(mouse_pos):
                        start_new_game()
                        
                    elif load_game_box.collidepoint(mouse_pos):
                        start_load()
                        
                    elif help_box.collidepoint(mouse_pos):
                        start_help()
                        
                    elif exit_box.collidepoint(mouse_pos):
                        running = False
                    
                elif event.type == pygame.VIDEORESIZE:  
                    w, h = pygame.display.get_surface().get_size()
                    WINDOW_WIDTH = w
                    WINDOW_HEIGHT = h
            # Draw the screen
            DISPLAY_SURFACE.fill(WHITE)
            draw_boxes()
            pygame.display.update()

        
        pygame.quit()
    main_menu()
