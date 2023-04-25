# imports
import pygame, sys,math
from pygame.locals import *
from PyGame_Project.MVC.View_GUI.gui_main_game import Game
from PyGame_Project.MVC.View_GUI.game_screen.components.main_screen import build_main_screen
from PyGame_Project.MVC.Controller.controller_universal import *
from pygame.locals import *

# starting new game screen
def start_new_game():
    clock = pygame.time.Clock()

    #settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('New Game')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 30)


    # create hexagon points (NOT the lines between the points)
    hex_radius = 70 # change this for bigger hexagons, considered midpoint
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
    def load_game():
        while True:
            
            # creates screen and title
            screen.fill(('white'))
            draw_text('START GAME FROM:', font_title, ('black'), screen, 130, 70)
    
            # gets mouse position
            mx, my = pygame.mouse.get_pos()
            active = False

            #creating buttons
            random = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 150) for hex_x, hex_y in hex_points], 3)
            key = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 300) for hex_x, hex_y in hex_points], 3)
            code = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 450) for hex_x, hex_y in hex_points], 3)

            #defining functions when clicked on
            if random.collidepoint((mx, my)):
                if click:
                    random_screen()
            if key.collidepoint((mx, my)):
                if click:
                    key_screen()
            if code.collidepoint((mx, my)):
                if click:
                    code_screen()
            if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(mx,my):
                if click:
                    return

            # draw the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)

            # writing text over button
            draw_text('RANDOM', font, ('black'), screen, 257, 213)
            draw_text('BASE', font, ('black'), screen, 270, 362)
            draw_text('SHARED', font, ('black'), screen, 260, 513)

            # defining statements when clicked on 
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
    
    # function is called when the "START FROM RANDOM" button is clicked on
    def random_screen():
        prep_new_game()
        build_main_screen()

 
    # function is called when the "START FROM KEY" button is clicked on
    def key_screen():
        running = True
        user_text = ''
        error_msg = ''
    
        # create back arrow points
        arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
        arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

        # creates screen and title
        while running:
            screen.fill('white')
            draw_text('PLEASE ENTER KEY', font, ('black'), screen, 200, 200)
            draw_text(error_msg, font, ('red'), screen, 200, 375)

            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            save = pygame.Rect(170, 450, 110, 50)
            clear = pygame.Rect(320, 450, 110, 50)
            input= pygame.Rect(240, 300, 110, 40)

            # defining if statements when buttons are clicked on 
            if save.collidepoint((mx, my)):
                if click:
                    print(f'newgame.py - def key_screen(): save does not exist.')
            if clear.collidepoint((mx, my)):
                if click:
                    print(f'newgame.py - def key_screen(): Does not exist.')
            if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(mx,my):
                if click:
                    return

            # draws green and red buttons
            pygame.draw.rect(screen, ('green'), save)
            pygame.draw.rect(screen, ('red'), clear)  
    
            # draw the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)

            #writing text over button
            draw_text('START', font, ('black'), screen, 195, 470)
            draw_text('CLEAR', font, ('black'), screen, 340, 470)

            # defining statements when clickd on 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.unicode.isalpha():
                        user_text += event.unicode  

                    if event.key == K_ESCAPE:
                        running = False  
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if save.collidepoint(pygame.mouse.get_pos()):
                        start_from_key(user_text)
                        error_msg = "!!! You don't have the right amount of unique character !!!"

                    if clear.collidepoint(pygame.mouse.get_pos()):
                        user_text = ""    
                    

            # draws rectangle input with a border            
            pygame.draw.rect(screen,('black'), input, 2)

            # creates surface 
            text_surface = font.render(user_text,True,(0,0,0))  
            screen.blit(text_surface,(input.x + 5,input.y + 5))

            input.w = max(150,text_surface.get_width() + 10)
        
            pygame.display.update()
            clock.tick(60)

    # function is called when the "START FROM A CODE" button is clicked on
    def code_screen():
        running = True
        user_text = ''
        error_msg = ''

        # create back arrow points
        arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
        arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

        # creates screen and title
        while running:
            screen.fill('white')
            draw_text('PLEASE ENTER CODE', font, ('black'), screen, 180, 200)
            draw_text(error_msg, font, ('red'), screen, 200, 375)

            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            save = pygame.Rect(170, 450, 110, 50)
            clear = pygame.Rect(320, 450, 110, 50)
            input = pygame.Rect(240, 300, 110, 40)
            
            # defining statements when clicked on 
            if save.collidepoint((mx, my)):
                if click:
                    print(f'Does not exist')
            if clear.collidepoint((mx, my)):
                if click:
                    print(f'Does not exist')
            if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(mx,my):
                if click:
                    return
                
            # draws the green and button buttons
            pygame.draw.rect(screen, ('green'), save)
            pygame.draw.rect(screen, ('red'), clear)  
    
            # draw the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)

            #writing text over button
            draw_text('START', font, ('black'), screen, 195, 470)
            draw_text('CLEAR', font, ('black'), screen, 340, 470)
        
            # definining statements when clicked on 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode  

                    if event.key == K_ESCAPE:
                        running = False 
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if save.collidepoint(pygame.mouse.get_pos()):
                        start_from_share(user_text)
                        error_msg = "!!! Incorrect Code !!!"

                    if clear.collidepoint(pygame.mouse.get_pos()):
                        user_text = ""
                    
            # draws rectangle input with a border            
            pygame.draw.rect(screen,('black'), input, 2)
        
            #creates surface
            text_surface = font.render(user_text,True,(0,0,0))  
            screen.blit(text_surface,(input.x + 5,input.y + 5))

            input.w = max(150,text_surface.get_width() + 10)

            pygame.display.update()
            clock.tick(60)

    # function start from key   
    def start_from_key(key):    
        prep_value = prep_game_with_key(key)

        if prep_value == 1:
            return 1
        build_main_screen()
        # game = Game()
        # game.run()
    
    #function start from share
    def start_from_share(shared_key):    
        prep_value = prep_game_from_share(shared_key)

        if prep_value == 1:
            return 1

        build_main_screen()
        # game = Game()
        # game.run()

    load_game()
