from .vertical_buttons import create_middle
main_menu_buttons = ['New Game', 'Load Game', 'Help', 'High Scores', 'Exit']
new_game_buttons = ['Random', 'Base Word', 'Shared', 'Back']


def build_center(state):
    if state.current_active_screen is state.active_screen.MAIN_MENU:
        create_middle(state, main_menu_buttons)
    elif state.current_active_screen is state.current_active_screen.NEW_GAME:
        create_middle(state, new_game_buttons)
    elif state.current_active_screen is state.current_active_screen.LOAD_GAME:
        create_middle(state, state.saved_games)
