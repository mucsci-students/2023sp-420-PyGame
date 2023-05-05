from dataclasses import dataclass
import pygame


@dataclass
class MainMenuState:

    running: bool = True

    active_popup = None
    highscore_popup = None
    shared_game_popup = None

    active_screen = None
    current_active_screen = None

    saved_games = None

    pygame.init()
    buttons = {}

    scroll_position = 0
    max_scroll_position = 0

    font = None
    display = None
