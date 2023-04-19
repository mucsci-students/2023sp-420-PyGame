from dataclasses import dataclass
from PyGame_Project.MVC.Model.model_puzzle import PuzzleStats
from .components.pop_ups import LeavePopup, SavePopup, GiveUpPopup

import pygame


@dataclass
class State:
    pygame.init()
    # display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    start_animation_time = pygame.time.get_ticks()
    puzzle_stats = PuzzleStats()
    # leave_popup = LeavePopup(display)
    # save_popup = SavePopup(display)
    # give_up_popup = GiveUpPopup(display)
    active_popup = None
    elapsed_animation_time = 0
    animation_progress = 0

    surrounding_hexagons = []
    buttons = {}

    is_animating: bool = False
    first_run: bool = True
    can_guess: bool = True
    running: bool = True

    required_letter = ''
    current_puzzle = ''
    current_guess = ''