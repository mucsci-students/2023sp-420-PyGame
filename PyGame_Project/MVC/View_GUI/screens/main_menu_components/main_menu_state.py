from dataclasses import dataclass
import pygame


@dataclass
class MainMenuState:
    running: bool = True

    pygame.init()
    buttons = {}

    max_scroll_position = 0
    scroll_position = 0

    display = None
    font = None
