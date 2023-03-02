#imports
import pygame, sys
from pygame.locals import *
clock = pygame.time.Clock()

#settings
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption('New Game')
font_title = pygame.font.SysFont(None, 50)
font = pygame.font.SysFont(None, 30)
user_text = ''
 
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
    while True:
 
        screen.fill(('white'))
        draw_text('NEW GAME OPTIONS', font_title, ('black'), screen, 100, 70)
 
        mx, my = pygame.mouse.get_pos()

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
    running = True
    while running:
        screen.fill('white')
       
        draw_text('RANDOM GAME', font, ('black'), screen, 200, 150)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)

# function is called when the "START FROM KEY" button is clicked on
def key_screen():
    running = True
    while running:
        screen.fill('white')
        draw_text('PLEASE ENTER KEY', font, ('black'), screen, 200, 200)

        mx, my = pygame.mouse.get_pos()
        
        #creating buttons
        save = pygame.Rect(170, 450, 110, 50)
        clear = pygame.Rect(320, 450, 110, 50)
      
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
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)

# function is called when the "START FROM A CODE" button is clicked on
def code_screen():
    running = True
    while running:
        screen.fill('white')
        draw_text('PLEASE ENTER CODE', font, ('black'), screen, 180, 200)

        mx, my = pygame.mouse.get_pos()
        
        #creating buttons
        save = pygame.Rect(170, 450, 110, 50)
        clear = pygame.Rect(320, 450, 110, 50)
      
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
                if event.key == K_ESCAPE:
                    running = False
      
        pygame.display.update()
        clock.tick(60)
      
load_menu()