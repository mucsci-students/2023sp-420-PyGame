#imports
import pygame, sys, os
from pygame.locals import *
from gui_main_game import Game

from controller_universal import *

def start_load():
    clock = pygame.time.Clock()

    #settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('Load A Game')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 30)
    
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
        save_path = ''
        for path in sys.path:
            if "\Saves" in path:
                save_path = path
                break 

        options = os.listdir(save_path)
        option_count = len(options)
        curr_count = 0
        if not option_count > 0:
            error_msg = '!!! No Files Found !!!'
            file_name = ''
        else: 
            error_msg = ''
            file_name = str(options[curr_count].replace(".json",""))

        while True:
            screen.fill(('white'))
            draw_text('GAME FILES', font_title, ('black'), screen, 200, 100)
            draw_text(file_name, font_title, ('black'), screen, 200, 250)
            draw_text(error_msg, font_title, ('red'), screen, 125, 250)
    
            mx, my = pygame.mouse.get_pos()

            #creating buttons
            load = pygame.Rect(235, 532, 120, 50)
            prev = pygame.Rect(40, 532, 120, 50)
            next = pygame.Rect(425, 532, 120, 50)

            #defining functions when clicked on
            if load.collidepoint((mx, my)):
                if click:
                    load_game(file_name) ## load button / function call

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
                
            pygame.draw.rect(screen, ('black'), load)
            pygame.draw.rect(screen, ('black'), prev)
            pygame.draw.rect(screen, ('black'), next)
    
            #writing text over button
            draw_text('LOAD', font, ('white'), screen, 265, 550)
            draw_text('PREV', font, ('white'), screen, 60, 550)
            draw_text('NEXT', font, ('white'), screen, 450, 550)

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

        if type(prep_value) == int:
            return 1
        running = True
        while running:
            screen.fill('white')
    
            draw_text('ARE YOU SURE?', font, ('black'), screen, 220, 150)
                    
            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            yes = pygame.Rect(190, 280, 60, 50)
            no = pygame.Rect(355, 280, 60, 50)
            pygame.draw.rect(screen, ('red'), yes)
            pygame.draw.rect(screen, ('green'), no)  
    
            #writing text over button
            draw_text('YES', font, ('black'), screen, 200, 300)
            draw_text('NO', font, ('black'), screen, 370, 300)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if yes.collidepoint((mx, my)):
                        game = Game(prep_value[0], prep_value[1])
                        game.run()
                    if no.collidepoint((mx, my)):
                        print(f'loadgame.py - def load_game(file_name): This function does not exist.')
        
            pygame.display.update()
            clock.tick(60)
        
    load_menu()