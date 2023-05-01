from dataclasses import dataclass
import pygame


@dataclass
class MainMenuState:
    running: bool = True

    active_popup = None
    highscore_popup = None

    pygame.init()
    buttons = {}

    max_scroll_position = 0
    scroll_position = 0

    display = None
    font = None
