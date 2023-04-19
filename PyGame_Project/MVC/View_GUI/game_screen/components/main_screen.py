import pygame, os

from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.View_GUI.hints_gui import *

from ..effects.events import wire_events
from ..state import State
from .header import create_header
from .center import create_center
from .footer import create_footer


def build_main_screen():
    pygame.init()
    state = State()
    pygame.display.set_caption('New Game')
    state.puzzle_stats = PuzzleStats()
    state.required_letter = state.puzzle_stats.required_letter.upper()
    current_puzzle = state.puzzle_stats.pangram.replace(state.puzzle_stats.required_letter, '', 1)
    state.current_puzzle = current_puzzle.upper()
    print(current_puzzle)
    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/mvc/view_gui/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()
    fps = pygame.time.Clock()

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))
        if state.active_popup is None or not state.active_popup.active:
            create_header(state)
            create_footer(state)
            create_center(state)

        wire_events(state)
        pygame.display.update()