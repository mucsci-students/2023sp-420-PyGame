import pygame
import math

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the polygon points
shuffle_letter_hex_points = [
    (200, 150),  # top-left
    (320, 90),  # top-right
    (380, 220),  # bottom-right
    (320, 350),  # bottom
    (200, 290),  # bottom-left
    (140, 220),  # top-middle
]

# Create a surface for the polygon
polygon_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
pygame.draw.polygon(polygon_surface, BLACK, shuffle_letter_hex_points)

# Define the button area
button_points = [
    (200, 200),  # top-left
    (320, 120),  # top-right
    (360, 220),  # right
    (320, 320),  # bottom-right
    (200, 240),  # bottom-left
    (160, 140),  # left
]
def is_in_hexagon(point):
    """
    Check if the given point is inside the hexagon defined by button_points.
    """
    num_points = len(button_points)
    inside = False
    j = num_points - 1
    for i in range(num_points):
        if (
            (button_points[i][1] < point[1] and button_points[j][1] >= point[1]
            or button_points[j][1] < point[1] and button_points[i][1] >= point[1])
            and (button_points[i][0] <= point[0] or button_points[j][0] <= point[0])):
            if (button_points[i][0] + (point[1] - button_points[i][1]) / (button_points[j][1] - button_points[i][1]) * (button_points[j][0] - button_points[i][0]) < point[0]):
                inside = not inside
        j = i
    return inside

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse was clicked inside the hexagon
            if is_in_hexagon(event.pos) and pygame.Surface.get_at(polygon_surface, event.pos) != (0, 0, 0, 0):
                print("Button clicked!")

    # Draw the polygon surface to the screen
    screen.blit(polygon_surface, (0, 0))

    # Draw the button area to the screen
    pygame.draw.polygon(screen, WHITE, button_points, 2)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
