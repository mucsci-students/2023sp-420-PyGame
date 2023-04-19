from ..footer.footer import create_input_box, create_buttons


def create_footer(state):
    if not state.show_guessed_words:
        create_input_box(state)
        create_buttons(state)
