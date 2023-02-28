#imports
import pygame, sys
from pygame.locals import *
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
    while True:
 
        screen.fill(('white'))
        draw_text('GAME FILES', font_title, ('black'), screen, 200, 100)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        load = pygame.Rect(235, 532, 120, 50)
        rename = pygame.Rect(40, 532, 120, 50)
        delete = pygame.Rect(425, 532, 120, 50)

        #defining functions when clicked on
        if load.collidepoint((mx, my)):
            if click:
                exist_screen()
        if rename.collidepoint((mx, my)):
            if click:
                rename_screen()
        if delete.collidepoint((mx, my)):
            if click:
                delete_screen()
        pygame.draw.rect(screen, ('black'), load)
        pygame.draw.rect(screen, ('black'), rename)
        pygame.draw.rect(screen, ('black'), delete)
 
        #writing text over button
        draw_text('LOAD', font, ('white'), screen, 265, 550)
        draw_text('RENAME', font, ('white'), screen, 60, 550)
        draw_text('DELETE', font, ('white'), screen, 450, 550)

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
def exist_screen():
    running = True
    while running:
        screen.fill('white')
       
        draw_text('Puzzle', font_title, ('black'), screen, 200, 150)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)

# function is called when the "RENAME" button is clicked on
def rename_screen():
    running = True
    while running:
        screen.fill('white')
        draw_text('PLEASE ENTER NEW NAME', font, ('black'), screen, 170, 150)

        mx, my = pygame.mouse.get_pos()
        
        #creating buttons
        save = pygame.Rect(170, 450, 110, 50)
        clear = pygame.Rect(350, 450, 110, 50)
      
        if save.collidepoint((mx, my)):
          if click:
            exist_screen()
        if clear.collidepoint((mx, my)):
          if click:
            exist_screen()
        pygame.draw.rect(screen, ('green'), save)
        pygame.draw.rect(screen, ('red'), clear)  
  
        #writing text over button
        draw_text('SAVE', font, ('black'), screen, 190, 470)
        draw_text('CLEAR', font, ('black'), screen, 370, 470)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        clock.tick(60)

# function is called when the "DELETE" button is clicked on
def delete_screen():
    running = True
    while running:
        screen.fill('white')
 
        draw_text('ARE YOU SURE?', font, ('black'), screen, 220, 150)
                
        mx, my = pygame.mouse.get_pos()
        
        #creating buttons
        yes = pygame.Rect(190, 280, 60, 50)
        no = pygame.Rect(355, 280, 60, 50)
      
        if yes.collidepoint((mx, my)):
          if click:
            exist_screen()
        if no.collidepoint((mx, my)):
          if click:
            exist_screen()
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
       
        pygame.display.update()
        clock.tick(60)
      
load_menu()