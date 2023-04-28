from .game import create_game


def create_center(state):
    if not state.show_guessed_words:
        create_game(state)
