from dataclasses import dataclass
from PyGame_Project.MVC.Model.model_puzzle import PuzzleStats
import pygame


@dataclass
class State:
    pygame.init()
    puzzle_stats = PuzzleStats()
    running: bool = True
    
    display = None
    start_animation_time = pygame.time.get_ticks()
    give_up_popup = None
    save_popup = None
    leave_popup = None
    back_popup = None
    current_guess_state = None

    active_popup = None
    guess_state = None

    elapsed_animation_time = 0
    max_scroll_position = 0
    animation_progress = 0
    animation_duration = 900
    scroll_position = 0

    displayable_columns = 0
    displayable_rows = 0
    column_width = 0
    total_rows = 0

    surrounding_hexagons = []
    word_list = []
    buttons = {}

    incorrect_guess_timer: bool = False
    correct_guess_timer: bool = False
    show_guessed_words: bool = False
    is_animating: bool = False
    first_run: bool = True
    can_guess: bool = True

    required_letter = ''
    current_puzzle = ''
    current_guess = ''
