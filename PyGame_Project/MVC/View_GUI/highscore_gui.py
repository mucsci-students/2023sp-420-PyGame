# imports
import pygame, sys,math
from pygame.locals import *
from gui_main_game import Game
from controller_universal import *

# starting highscore screen
def highscore():
    clock = pygame.time.Clock()

    #settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('High Scores')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 30)
    smallfont = pygame.font.SysFont(None, 20)

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
    def load_highscore():
        while True:
            
            # creates screen and title
            screen.fill(('white'))
            draw_text('HIGH SCORES', font_title, ('black'), screen, 190, 70)
    
            # gets mouse position
            mx, my = pygame.mouse.get_pos()
            active = False

            #creating buttons
            view = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 200) for hex_x, hex_y in hex_points], 3)
            enter = pygame.draw.polygon(screen, ('black'), [(hex_x + 230, hex_y + 390) for hex_x, hex_y in hex_points], 3)

            #defining functions when clicked on
            if view.collidepoint((mx, my)):
                if click:
                    view_screen()
            if enter.collidepoint((mx, my)):
                if click:
                    enter_screen()
            if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(mx,my):
                if click:
                    return

            # draw the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)

            # writing text over button
            draw_text('VIEW', font, ('black'), screen, 272, 260)
            draw_text('ENTER', font, ('black'), screen, 265, 455)

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
    
    # function is called when the "VIEW" button is clicked on, and displays the top 10 high scores
    def view_screen():
        running = True

        # create back arrow points
        arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
        arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

        # creates screen and title
        while running:
            screen.fill('white')
            draw_text('TOP TEN HIGH SCORES', font, ('black'), screen, 200, 50)

            mx, my = pygame.mouse.get_pos()
 
    
            # draw the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)

            #writing text over button
            draw_text('HIGH SCORE 1', font, ('black'), screen, 240, 120)
            draw_text('HIGH SCORE 2', font, ('black'), screen, 240, 160)
            draw_text('HIGH SCORE 3', font, ('black'), screen, 240, 200)
            draw_text('HIGH SCORE 4', font, ('black'), screen, 240, 240)
            draw_text('HIGH SCORE 5', font, ('black'), screen, 240, 280)
            draw_text('HIGH SCORE 6', font, ('black'), screen, 240, 320)
            draw_text('HIGH SCORE 7', font, ('black'), screen, 240, 360)
            draw_text('HIGH SCORE 8', font, ('black'), screen, 240, 400)
            draw_text('HIGH SCORE 9', font, ('black'), screen, 240, 440)
            draw_text('HIGH SCORE 10', font, ('black'), screen, 240, 480)

            # defining statements when clickd on 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False  
               
            pygame.display.update()
            clock.tick(60)

    # function is called when the "ENTER" button is clicked on and allows for a player to save their score
    def enter_screen():
        running = True
        user_text = ''
        error_msg = ''

        # create back arrow points
        arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
        arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

        # creates screen and title
        while running:
            screen.fill('white')
            draw_text('PLEASE ENTER LETTERS', font, ('black'), screen, 175, 150)
            draw_text('REQUIRED LETTER', smallfont, ('black'), screen, 160, 250)
            draw_text('REST OF LETTERS', smallfont, ('black'), screen, 320, 250)
            draw_text(error_msg, font, ('red'), screen, 165, 375)

            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            save = pygame.Rect(170, 450, 110, 50)
            clear = pygame.Rect(320, 450, 110, 50)
            required = pygame.Rect(209, 300, 40, 40)
            rest = pygame.Rect(320, 300, 110, 40)
            
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
                        enter_screen(user_text)
                        error_msg = "Incorrect Letter Combination"

                    if clear.collidepoint(pygame.mouse.get_pos()):
                        user_text = ""
                    
            # draws rectangle input with a border            
            pygame.draw.rect(screen,('black'), rest, 2)
            pygame.draw.rect(screen,('black'), required, 2)
        
            #creates surface
            text_surface = font.render(user_text,True,(0,0,0))  
            screen.blit(text_surface,(rest.x + 5,rest.y + 5))
            
            rest.w = max(150,text_surface.get_width() + 10)

            pygame.display.update()
            clock.tick(60)

    load_highscore()
