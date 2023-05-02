from PyGame_Project.MVC.View_GUI.screens.game_screen_components.main_screen import build_main_screen
from PyGame_Project.MVC.Controller.controller_universal import prep_game_from_load

import pygame
import sys


minimum_width = 800
minimum_height = 600


def load_game_menu_events(state):
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

        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button == 5):
            handle_scroll(state, event.button)


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


def handle_scroll(state, event):
    if event == 4:
        state.scroll_position = max(0, state.scroll_position - 1)
    else:
        state.scroll_position = min(state.max_scroll_position, state.scroll_position + 1)


def handle_button_press(state, event):
    if not (event.button == 4 or event.button == 5):
        for key in state.buttons:
            if state.buttons[key]:
                if key.strip().casefold() == 'Back'.casefold():
                    clicked_back(state)
                else:
                    clicked_load(state, key)


def clicked_back(state):
    state.current_active_screen = state.active_screen.MAIN_MENU


def clicked_load(state, text):
    file_name = text[:-5]
    print(file_name)
    check_file = prep_game_from_load(file_name)
    if not check_file == 1:
        build_main_screen()
