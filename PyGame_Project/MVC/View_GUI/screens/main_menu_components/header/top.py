from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle


def create_top(state):
    buffer = state.display.get_width() / 10
    width = buffer * 8
    height = .125 * state.display.get_height()

    shape = Rectangle(
        x=buffer, y=5, w=width, h=height,
        font_color=COLOR_ORANGE,
        text="Spelling Bee by PyGame"
    )
    shape.draw(state.display, color=COLOR_BLACK)
