from PyGame_Project.MVC.View_GUI.screens.main_menu_components.main_menu_state import MainMenuState
from PyGame_Project.MVC.View_GUI.screens.game_screen_components.pop_ups import HighScorePopup
from PyGame_Project.MVC.View_GUI.screens.main_menu_components.center import build_center
from PyGame_Project.MVC.View_GUI.screens.main_menu_components.header import build_top
from PyGame_Project.MVC.View_GUI.newgame import start_new_game
from PyGame_Project.MVC.View_GUI.loadgame import start_load
from PyGame_Project.MVC.View_GUI.helpgui import start_help
import pygame
import os
import sys

minimum_width = 800
minimum_height = 600


def build_main_menu_screen():
    pygame.init()
    state = MainMenuState()

    pygame.display.set_caption('Main Menu')
    state.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    state.highscore_popup = HighScorePopup(state)

    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/MVC/View_GUI/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()
    fps = pygame.time.Clock()

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))

        if state.active_popup is None or not state.active_popup.active:
            build_top(state)
            build_center(state)

        main_menu_events(state)
        pygame.display.update()


def main_menu_events(state):

    if state.active_popup is not None:
        if state.active_popup.active:
            state.active_popup.draw()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            state.running = False
            pygame.quit()
            sys.exit()

        if state.active_popup is None or not state.active_popup.active:
            if event.type == pygame.MOUSEBUTTONUP:
                handle_button_press(state, event)

        elif state.active_popup.active:
            state.active_popup.handle_event(event, state)

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
            if state.buttons[key]:
                if key.strip().casefold() == 'Help'.casefold():
                    start_help()
                elif key.strip().casefold() == 'Exit'.casefold():
                    clicked_leave(state)
                elif key.strip().casefold() == 'New Game'.casefold():
                    start_new_game()
                elif key.strip().casefold() == 'Load Game'.casefold():
                    start_load()
                elif key.strip().casefold() == 'High Scores'.casefold():
                    clicked_high_score(state)


def clicked_leave(state):
    state.running = False


def clicked_high_score(state):
    state.active_popup = state.highscore_popup
    state.active_popup.show()
