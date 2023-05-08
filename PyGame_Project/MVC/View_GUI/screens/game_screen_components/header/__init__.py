from .top import create_top
from .guessed_words import create_show_words, create_arrows
from .leave_button import create_leave_button
from .score import create_score


def create_header(state):
    create_top(state)
    create_show_words(state)
    create_arrows(state)

    if not state.show_guessed_words:
        create_leave_button(state)
        create_score(state)
    
