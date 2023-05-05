from PyGame_Project.MVC.View_GUI.screens.game_screen_components.pop_ups import LeavePopup, SavePopup, GiveUpPopup, BackPopup, HighScorePopup
from PyGame_Project.MVC.View_GUI.screens.game_screen_components.center import create_center
from PyGame_Project.MVC.View_GUI.screens.game_screen_components.footer import create_footer
from PyGame_Project.MVC.View_GUI.screens.game_screen_components.header import create_header
from PyGame_Project.MVC.View_GUI.screens.game_screen_components.state import State
from PyGame_Project.MVC.View_GUI.screens.effects.game_events import wire_events, GuessState
from PyGame_Project.MVC.Model.model_puzzle import PuzzleStats
import pygame
import os


def build_main_screen():
    pygame.init()
    state = State()
    state.guess_state = GuessState
    state.puzzle_stats = PuzzleStats()
    # state.puzzle_stats.clear()
    pygame.display.set_caption('PyGame - Spelling Bee')
    state.required_letter = state.puzzle_stats.required_letter.upper()

    current_puzzle = state.puzzle_stats.pangram.replace(state.puzzle_stats.required_letter, '', 1)
    state.current_puzzle = current_puzzle.upper()

    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/mvc/view_gui/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()
    fps = pygame.time.Clock()
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        
    state.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    state.start_animation_time = pygame.time.get_ticks()
    state.save_popup = SavePopup(state)
    state.back_popup = BackPopup(state)
    state.leave_popup = LeavePopup(state)
    state.give_up_popup = GiveUpPopup(state)
    state.highscore_popup = HighScorePopup(state)

    word_list = []
    for word in state.puzzle_stats.current_word_list:
        word_list.append(word[0])
    state.word_list = word_list

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))
        if state.active_popup is None or not state.active_popup.active:
            create_header(state)
            create_footer(state)
            create_center(state)

        wire_events(state)
        if state.first_run:
            state.current_guess = ''

        pygame.display.update()
