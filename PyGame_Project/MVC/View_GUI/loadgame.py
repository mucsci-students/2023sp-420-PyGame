# imports
import pygame, math
from pygame.locals import *
from PyGame_Project.MVC.View_GUI.screens.main_game_screen_components.main_screen import build_main_screen
from PyGame_Project.MVC.Controller.controller_universal import *

# load start screen
def start_load():
    clock = pygame.time.Clock()

    # settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('Load A Game')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 30)

    # create hexagon points (NOT the lines between the points)
    hex_radius = 50 # change this for bigger hexagons, considered midpoint
    hex_points = []
    for i in range(6):
        hex_angle = (math.pi / 180) * (60 * i) # converts from degrees to radians
        hex_x = hex_radius * math.cos(hex_angle) + 70 # the + 70 changes x position
        hex_y = hex_radius * math.sin(hex_angle) + 70
        hex_points.append((hex_x, hex_y))

    # create back arrow points
    arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
    arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]
    
    # function that writes text onto the screen and buttons
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # variable to check for clicking status
    click = False
    
    # main function
    def load_menu():
        options = []
        for file in os.listdir(os.getcwd()):
            if ".json" in file:
                options.append(file)

        option_count = len(options)
        curr_count = 0
        if not option_count > 0:
            error_msg = '!!! No Files Found !!!'
            file_name = ''
        else: 
            error_msg = ''
            file_name = str(options[curr_count].replace(".json",""))

        while True:
            # creates screen and titles
            screen.fill(('white'))
            draw_text('GAME FILES', font_title, ('black'), screen, 200, 100)
            draw_text(file_name, font_title, ('black'), screen, 200, 250)
            draw_text(error_msg, font_title, ('red'), screen, 125, 250)
    
            mx, my = pygame.mouse.get_pos()

            # creating buttons
            load = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 450) for hex_x, hex_y in hex_points], 3)
            prev = pygame.draw.polygon(screen, ('black'), [(hex_x + 50, hex_y + 450) for hex_x, hex_y in hex_points], 3)
            next = pygame.draw.polygon(screen, ('black'), [(hex_x + 400, hex_y + 450) for hex_x, hex_y in hex_points], 3)

            # defining statements when clicked on
            if load.collidepoint((mx, my)):
                if click:
                    load_game(file_name) # load button / function call

            if prev.collidepoint((mx, my)):
                if click:
                    if  option_count > 0:
                        if curr_count == 0:
                            curr_count = option_count
                        curr_count = curr_count - 1
                        file_name = str(options[curr_count].replace(".json",""))

            if next.collidepoint((mx, my)):
                if click:
                    if option_count > 0:
                        if curr_count == option_count - 1:
                            curr_count = -1
                        curr_count = curr_count + 1
                        file_name = str(options[curr_count].replace(".json",""))

            # if statement for back arrow    
            if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(mx,my):
                if click:
                    return

            # draws the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)
    
            # writing text over buttons
            draw_text('LOAD', font, ('black'), screen, 270, 513)
            draw_text('PREV', font, ('black'), screen, 92, 513)
            draw_text('NEXT', font, ('black'), screen, 442, 513)

            # commands that lead to actions
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                

            pygame.display.update()
            clock.tick(60)
    
    # function is called when the "LOAD" button is clicked on
    def load_game(file_name):

        print(f'loadgame.py - def load_game(file_name): Selected filename is: {file_name}')
        spacer = 0 
        prep_value = prep_game_from_load(file_name)
        print(prep_value)

        if prep_value == 1:
            return 1
        running = True
        while running:
            screen.fill('white')

            # prints out title
            draw_text('ARE YOU SURE?', font, ('black'), screen, 220, 150)

            #gets mouse position        
            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            yes = pygame.Rect(190, 280, 60, 50)
            no = pygame.Rect(355, 280, 60, 50)
            pygame.draw.rect(screen, ('green'), yes)
            pygame.draw.rect(screen, ('red'), no)  
    
            #writing text over button
            draw_text('YES', font, ('black'), screen, 200, 300)
            draw_text('NO', font, ('black'), screen, 370, 300)

            # functions called when clicked on
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if yes.collidepoint((mx, my)):
                        build_main_screen()
                        running = False
                    if no.collidepoint((mx, my)):
                        return
                    
            # updates the screen
            pygame.display.update()
            clock.tick(60)
        
    load_menu()
