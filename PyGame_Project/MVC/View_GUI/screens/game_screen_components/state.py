from PyGame_Project.MVC.Model.model_puzzle import PuzzleStats
from dataclasses import dataclass
import pygame


@dataclass
class State:
    pygame.init()
    puzzle_stats = PuzzleStats()

    running: bool = True
    
    display = None
    start_animation_time = pygame.time.get_ticks()

    save_popup = None
    back_popup = None
    leave_popup = None
    give_up_popup = None
    highscore_popup = None

    guess_state = None
    active_popup = None
    current_guess_state = None

    scroll_position = 0
    animation_progress = 0
    max_scroll_position = 0
    animation_duration = 900
    elapsed_animation_time = 0

    total_rows = 0
    column_width = 0
    displayable_rows = 0
    displayable_columns = 0

    buttons = {}
    word_list = []
    surrounding_hexagons = []

    can_guess: bool = True
    first_run: bool = True
    is_animating: bool = False
    show_guessed_words: bool = False
    correct_guess_timer: bool = False
    incorrect_guess_timer: bool = False

    current_guess = ''
    current_puzzle = ''
    required_letter = ''
