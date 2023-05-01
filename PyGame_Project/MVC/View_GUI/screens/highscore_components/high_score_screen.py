from PyGame_Project.MVC.Model.Database.model_highscores import insert_or_update_score, get_scores_for_puzzle
from PyGame_Project.MVC.View_GUI.screens.highscore_components.highscore_state import HighScoreState
from PyGame_Project.MVC.View_GUI.screens.highscore_components.header import create_header
from PyGame_Project.MVC.View_GUI.screens.highscore_components.center import create_center
from PyGame_Project.MVC.Model.imageGen import generateImage
import pygame
import random
import sys
import os

minimum_width = 800
minimum_height = 600


def build_high_score_screen(required_letter='', pangram='', name='', score=0):

    state = HighScoreState()
    state.player_name = name
    pygame.display.set_caption('High Scores')
    state.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    if len(name) <= 3:
        insert_or_update_score(name, required_letter, pangram, score)

    state.all_scores = get_scores_for_puzzle(required_letter, pangram)

    state.required_letter = required_letter
    state.current_puzzle = ''.join(random.sample(pangram, len(pangram)))

    i = 1
    for score in state.all_scores:
        state.edited_scores.append((i, score[0], score[1]))
        i += 1

    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/MVC/View_GUI/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()

    fps = pygame.time.Clock()

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))
        create_header(state)
        create_center(state)

        high_score_events(state)
        pygame.display.update()


def high_score_events(state):
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
            if key.strip().casefold() == 'Leave'.casefold() and state.buttons[key]:
                clicked_leave(state)
            elif key.strip().casefold() == 'Share'.casefold() and state.buttons[key]:
                clicked_share(state)


def clicked_leave(state):
    state.running = False


def clicked_share(state):
    generateImage(state.player_name)


