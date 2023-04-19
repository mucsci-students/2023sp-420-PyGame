import math, random, pygame, os

from ...components.shapes import Hexagon
from ...colors import COLOR_BLACK, COLOR_NEON_ORANGE, COLOR_ORANGE
from ..header import create_header
from ..footer import create_footer


def create_game(state):
    if not state.is_animating:
        x = state.display.get_width() // 2
        y = state.display.get_height() // 2
        spacing = x * .04
        hex_size = min(state.display.get_width(), state.display.get_height()) // 9
        center_x, center_y = state.display.get_width() // 2, state.display.get_height() // 2
        center_hexagon = Hexagon(x, y, hex_size, hex_size, state.required_letter)
        hex_positions = _get_hex_positions(center_x, center_y, hex_size, spacing)
        if state.first_run:
            state.first_run = False
            state.surrounding_hexagons = [Hexagon(pos[0], pos[1], hex_size, hex_size, letter) for pos, letter in
                                          zip(hex_positions, state.current_puzzle)]
        for hexagon in state.surrounding_hexagons:
            hexagon.draw(state.display, COLOR_NEON_ORANGE, COLOR_BLACK, COLOR_ORANGE)
            hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 6)
            state.buttons[hexagon.text] = hexagon.is_hover()

        center_hexagon.draw(state.display, COLOR_NEON_ORANGE, COLOR_BLACK, COLOR_ORANGE)
        center_hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 6)
        state.buttons[center_hexagon.text] = center_hexagon.is_hover()
    else:
        start_animation(state)


def _get_hex_positions(center_x, center_y, size, spacing=0):
    hex_positions = []
    for index in range(6):
        angle = 30 + 60 * index
        radians = math.radians(angle)
        new_x = center_x + (size * math.sqrt(3) + spacing) * math.cos(radians)
        new_y = center_y + (size * math.sqrt(3) + spacing) * math.sin(radians)
        hex_positions.append((new_x, new_y))
    return hex_positions


def lerp(start, end, t):
    return start + (end - start) * t


def start_animation(state):
    x = state.display.get_width() // 2
    y = state.display.get_height() // 2
    hex_size = min(state.display.get_width(), state.display.get_height()) // 9
    center_hexagon = Hexagon(x, y, hex_size, hex_size, state.required_letter)
    shuffled_hexagons = shuffle_hexagons(state.surrounding_hexagons.copy(), hex_size, state)
    animate_hexagons(state, state.display, state.surrounding_hexagons, shuffled_hexagons, center_hexagon, hex_size, 600)
    state.surrounding_hexagons = shuffled_hexagons
    center_hexagon.draw(state.display, COLOR_NEON_ORANGE, COLOR_BLACK, COLOR_ORANGE)
    center_hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 6)
    state.is_animating = False
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)


def animate_hexagons(state, surface, start_hexagons, end_hexagons, center_hexagon, hex_size, duration):
    start_time = pygame.time.get_ticks()
    elapsed_time = 0
    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/mvc/view_gui/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()
    fps = pygame.time.Clock()

    while elapsed_time < duration:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))
        create_header(state)
        create_footer(state)
        elapsed_time = pygame.time.get_ticks() - start_time
        t = min(1, elapsed_time / duration)

        center_hexagon.draw(surface, COLOR_NEON_ORANGE, COLOR_BLACK, COLOR_ORANGE)
        center_hexagon.draw(surface, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)
        for start_hex, end_hex in zip(start_hexagons, end_hexagons):
            x = lerp(start_hex.center[0], end_hex.center[0], t)
            y = lerp(start_hex.center[1], end_hex.center[1], t)
            hexagon = Hexagon(x, y, hex_size, hex_size, start_hex.text)
            hexagon.draw(state.display, COLOR_NEON_ORANGE, COLOR_BLACK, COLOR_ORANGE)
            hexagon.draw(state.display, COLOR_BLACK, COLOR_BLACK, COLOR_BLACK, 3)

        pygame.display.flip()


def shuffle_hexagons(hexagons, size, state):
    hex_positions = [hexagon.center for hexagon in hexagons]
    hex_text = [hexagon.text for hexagon in hexagons]

    # Shuffle the positions, but keep the text in the same order
    random.shuffle(hex_positions)

    # Combine the shuffled positions with the original text
    shuffled_hexagons = [Hexagon(pos[0], pos[1], size, size, text) for pos, text in zip(hex_positions, hex_text)]
    return shuffled_hexagons


def update_hexagon_positions(state):
    x = state.display.get_width() // 2
    spacing = x * .04
    hex_size = min(state.display.get_width(), state.display.get_height()) // 9
    center_x, center_y = state.display.get_width() // 2, state.display.get_height() // 2

    hex_positions = _get_hex_positions(center_x, center_y, hex_size, spacing)

    state.surrounding_hexagons = [Hexagon(pos[0], pos[1], hex_size, hex_size, old_hex.text) for pos, old_hex in
                                  zip(hex_positions, state.surrounding_hexagons)]
