from PyGame_Project.MVC.View_GUI.screens.effects.colors import COLOR_BLACK, COLOR_NEON_ORANGE
from PyGame_Project.MVC.View_GUI.screens.effects.shapes import Rectangle


def create_score(state):
    buffer = state.display.get_width() / 10
    width = buffer * 3
    height = 0.0625 * state.display.get_height()
    x = buffer * 6
    y = height + 10

    shape = Rectangle(
        x=x, y=y, w=width, h=height,
        font_color=COLOR_NEON_ORANGE,
        text=f'{state.puzzle_stats.get_rank()}: {state.puzzle_stats.score} / {state.puzzle_stats.total_points}'
    )
    shape.draw(state.display, COLOR_BLACK)
