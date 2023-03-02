#imports
import pygame, sys

from pygame.locals import *
from gui_main_game import Game
from controller_universal import *
from pygame.locals import *

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
    
            screen.fill(('white'))
            draw_text('NEW GAME OPTIONS', font_title, ('black'), screen, 100, 70)
    
            mx, my = pygame.mouse.get_pos()
            active = False

            #creating buttons
            random = pygame.Rect(150, 150, 260, 50)
            key = pygame.Rect(150, 280, 260, 50)
            code = pygame.Rect(150, 410, 260, 50)

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
            pygame.draw.rect(screen, ('black'), random)
            pygame.draw.rect(screen, ('black'), key)
            pygame.draw.rect(screen, ('black'), code)
    
            #writing text over button
            draw_text('START FROM RANDOM', font, ('white'), screen, 166, 170)
            draw_text('START FROM A KEY', font, ('white'), screen, 180, 300)
            draw_text('START FROM A CODE', font, ('white'), screen, 175, 431)

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
    
    # function is called when the "START FROM RANDOM" button is clicked on
    def random_screen():
        puzzle, puzzle_stats = prep_new_game()
        game = Game(puzzle, puzzle_stats)
        game.run()
 
    # function is called when the "START FROM KEY" button is clicked on
    def key_screen():
        running = True
        user_text = ''
        error_msg = ''
        while running:
            screen.fill('white')
            draw_text('PLEASE ENTER KEY', font, ('black'), screen, 200, 200)
            draw_text(error_msg, font, ('red'), screen, 200, 375)

            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            save = pygame.Rect(170, 450, 110, 50)
            clear = pygame.Rect(320, 450, 110, 50)
        
            input= pygame.Rect(240, 300, 110, 40)

            if save.collidepoint((mx, my)):
                if click:
                    exist_screen()
            if clear.collidepoint((mx, my)):
                if click:
                    exist_screen()
            pygame.draw.rect(screen, ('green'), save)
            pygame.draw.rect(screen, ('red'), clear)  
    
            #writing text over button
            draw_text('START', font, ('black'), screen, 195, 470)
            draw_text('CLEAR', font, ('black'), screen, 340, 470)


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
        while running:
            screen.fill('white')
            draw_text('PLEASE ENTER CODE', font, ('black'), screen, 180, 200)
            draw_text(error_msg, font, ('red'), screen, 200, 375)

            mx, my = pygame.mouse.get_pos()
            
            #creating buttons
            save = pygame.Rect(170, 450, 110, 50)
            clear = pygame.Rect(320, 450, 110, 50)
            input = pygame.Rect(240, 300, 110, 40)
            
        
            if save.collidepoint((mx, my)):
                if click:
                    exist_screen()
            if clear.collidepoint((mx, my)):
                if click:
                    exist_screen()
                
            pygame.draw.rect(screen, ('green'), save)
            pygame.draw.rect(screen, ('red'), clear)  
    
            #writing text over button
            draw_text('START', font, ('black'), screen, 195, 470)
            draw_text('CLEAR', font, ('black'), screen, 340, 470)
        
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
        
            text_surface = font.render(user_text,True,(0,0,0))  
            screen.blit(text_surface,(input.x + 5,input.y + 5))

            input.w = max(150,text_surface.get_width() + 10)

            pygame.display.update()
            clock.tick(60)
        
    def start_from_key(key):    
        prep_value = prep_game_with_key(key)

        if type(prep_value) == int:
            return 1

        game = Game(prep_value[0], prep_value[1])
        game.run()

    def start_from_share(shared_key):    
        puzzle, puzzle_stats = prep_game_from_share(shared_key)

        if type(prep_value) == int:
            return 1

        game = Game(puzzle, puzzle_stats)
        game.run(prep_value)

    load_game()