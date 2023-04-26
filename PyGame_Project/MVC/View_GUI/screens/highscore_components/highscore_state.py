from dataclasses import dataclass
from PyGame_Project.MVC.Model.model_puzzle import PuzzleStats
import pygame


@dataclass
class HighScoreState:
    running: bool = True

    pygame.init()
    buttons = {}

    all_scores = []
    edited_scores = []

    column_width = 0
    displayable_columns = 0
    displayable_rows = 0
    total_rows = 0

    max_scroll_position = 0
    scroll_position = 0

    required_letter = ''
    current_puzzle = ''
    player_name = ''

    display = None
    font = None
