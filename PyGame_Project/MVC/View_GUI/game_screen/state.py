from dataclasses import dataclass
from Model.model_puzzle import PuzzleStats
from .components.pop_ups import LeavePopup, SavePopup, GiveUpPopup

import pygame

@dataclass
class State:
    pygame.init()
    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    start_animation_time = pygame.time.get_ticks()
    give_up_popup = GiveUpPopup(display)
    leave_popup = LeavePopup(display)
    save_popup = SavePopup(display)
    puzzle_stats = PuzzleStats()
    active_popup = None
    guess_state = None

    elapsed_animation_time = 0
    max_scroll_position = 0
    animation_progress = 0
    scroll_position = 0

    displayable_columns = 0
    displayable_rows = 0
    column_width = 0
    total_rows = 0

    surrounding_hexagons = []
    buttons = {}

    show_guessed_words: bool = False
    is_animating: bool = False
    first_run: bool = True
    can_guess: bool = True
    running: bool = True

    required_letter = ''
    current_puzzle = ''
    current_guess = ''
