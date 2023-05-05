from PyGame_Project.MVC.View_GUI.screens.game_screen_components.main_screen import build_main_screen
from PyGame_Project.MVC.Controller.controller_universal import prep_new_game

import pygame
import sys


minimum_width = 800
minimum_height = 600


def new_game_menu_events(state):

    if state.active_popup is not None:
        if state.active_popup.active:
            state.active_popup.draw()
            if state.active_popup == state.shared_game_popup:
                if state.active_popup.confirmation_bool:
                    state.active_popup.on_no()
                    state.active_popup = None
                    build_main_screen()

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
                if key.strip().casefold() == 'Random'.casefold():
                    clicked_random()
                elif key.strip().casefold() == 'Base Word'.casefold():
                    clicked_base_word(state)
                elif key.strip().casefold() == 'Shared'.casefold():
                    clicked_shared(state)
                elif key.strip().casefold() == 'Back'.casefold():
                    clicked_back(state)


def clicked_random():
    prep_new_game()
    build_main_screen()


def clicked_base_word(state):
    state.active_popup = state.shared_game_popup
    state.active_popup.show()


def clicked_shared(state):
    state.shared_game_popup.is_shared_game = True
    state.active_popup = state.shared_game_popup
    state.active_popup.show()


def clicked_back(state):
    state.current_active_screen = state.active_screen.MAIN_MENU
