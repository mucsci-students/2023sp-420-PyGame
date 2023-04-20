# imports
import pygame, sys, os, math
from pygame.locals import *
from PyGame_Project.MVC.Model.Database.model_highscores import *
from PyGame_Project.MVC.Model.imageGen import *
from PyGame_Project.MVC.View_GUI.gui_main_menu import *

# load start screen
def start_hs(player_name, req_letter, pangram, player_score):
    clock = pygame.time.Clock()

    # settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('Load A Game')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont("couriernew", 30)
    

    # create hexagon points (NOT the lines between the points)
    hex_radius = 60 # change this for bigger hexagons, considered midpoint
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
    def hs_menu(player_name, req_letter, pangram, player_score):
        
        while True:
            # creates screen and titles
            screen.fill(('white'))
            draw_text('HIGH SCORES', font_title, ('black'), screen, 180, 50)

            insert_or_update_score(player_name, req_letter, pangram, player_score)

            all_scores = get_scores_for_puzzle(req_letter, pangram)


            y_axis = 100
            rank_num = 1
            for score in all_scores:
                if rank_num == 10:
                    hs_line = (f"{rank_num}    {score[0]}     {score[1]}")
                else:
                    hs_line = (f"{rank_num}     {score[0]}     {score[1]}")
                draw_text(hs_line, font, ('black'), screen, 160, y_axis)
                rank_num += 1
                y_axis += 30
                if rank_num > 10:
                    break
    
            mx, my = pygame.mouse.get_pos()

            # creating buttons
            share = pygame.draw.polygon(screen, ('black'), [(hex_x + 225, hex_y + 450) for hex_x, hex_y in hex_points], 3)
        

            # defining statements when clicked on
            if share.collidepoint((mx, my)):
                if click:
                    generateImage(player_name)

        
            # draws the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)
    
            # writing text over buttons
            draw_text('SHARE', font, ('black'), screen, 250, 505)
           
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                    if pygame.draw.polygon(screen, ("white"), arrow_rect_vertices).collidepoint(event.pos):
                        start_gui()
                    elif share.collidepoint(event.pos):
                        generateImage(player_name)

            pygame.display.update()
            clock.tick(60)
        
    hs_menu(player_name, req_letter, pangram, player_score)
