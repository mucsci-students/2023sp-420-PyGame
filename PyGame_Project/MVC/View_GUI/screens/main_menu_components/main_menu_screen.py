from PyGame_Project.MVC.View_GUI.screens.main_menu_components.main_menu_state import MainMenuState
from PyGame_Project.MVC.View_GUI.screens.main_menu_components.center import build_center
from PyGame_Project.MVC.View_GUI.screens.main_menu_components.header import build_top
from PyGame_Project.MVC.View_GUI.screens.highscore_components.high_score_screen import build_high_score_screen
from PyGame_Project.MVC.View_GUI.newgame import start_new_game
from PyGame_Project.MVC.View_GUI.loadgame import start_load
from PyGame_Project.MVC.View_GUI.helpgui import start_help
from PyGame_Project.MVC.View_GUI.screens.main_menu_components.footer import *
import pygame, os, sys, math

minimum_width = 800
minimum_height = 600


def build_main_menu_screen():
    pygame.init()
    state = MainMenuState()

    pygame.display.set_caption('Main Menu')
    state.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/MVC/View_GUI/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()
    fps = pygame.time.Clock()

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))

        build_top(state)
        build_center(state)
        main_menu_events(state)

        pygame.display.update()


def main_menu_events(state):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            state.running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            handle_button_press(state, event)

        if event.type == pygame.VIDEORESIZE:
            handle_screen_resize(state, event)


def handle_screen_resize(state, event):
    if event.w < minimum_width:
        width = minimum_width
    else:
        width = event.w

    if event.h < minimum_height:
        height = minimum_height
    else:
        height = event.h

    state.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def handle_button_press(state, event):
    if not (event.button == 4 or event.button == 5):
        for key in state.buttons:
            print(key)
            if key.strip().casefold() == 'New Game'.casefold() and state.buttons[key]:
                start_new_game()
            elif key.strip().casefold() == 'Load Game'.casefold() and state.buttons[key]:
                start_load()
            elif key.strip().casefold() == 'Help'.casefold() and state.buttons[key]:
                start_help()
            elif key.strip().casefold() == 'High Scores'.casefold() and state.buttons[key]:
                build_high_score_screen('s', 'efdoras', 'bob', 0)
            elif key.strip().casefold() == 'Exit'.casefold() and state.buttons[key]:
                clicked_leave(state)


def clicked_leave(state):
    state.running = False
