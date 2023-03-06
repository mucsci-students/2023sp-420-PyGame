import pygame, os, math
from gui_main_game import *

def leave_game_options(winX, winY):
    pygame.init()

    # create window dimensions, and minimum window dimensions (when window is resized)

    window = pygame.display.set_mode((400, 300), pygame.RESIZABLE)

    # set window name and icon
    pygame.display.set_caption("Help")
    image_dir = os.path.join(os.getcwd(), "mvc/view_gui/helpicons")
    icon = pygame.image.load(os.path.join(image_dir, 'clubpenguin4.jpg'))
    pygame.display.set_icon(icon)

    # set visual text and font
    font = pygame.font.Font(None, 21)
    prompt_font = pygame.font.Font(None, 40)

    # create hexagon points (NOT the lines between the points)
    hex_radius = 40 # change this for bigger hexagons, considered midpoint
    hex_points = []
    for i in range(6):
        hex_angle = (math.pi / 180) * (60 * i) # converts from degrees to radians
        hex_x = hex_radius * math.cos(hex_angle) + 70 # the + 70 changes x position
        hex_y = hex_radius * math.sin(hex_angle) + 70
        hex_points.append((hex_x, hex_y))

    # create back arrow points
    arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
    arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

    running_here = True
    while running_here:
        for event in pygame.event.get():

            # if the user exits the window
            if event.type == pygame.QUIT:
                running_here = False

            # if the window is resized
            if event.type == pygame.VIDEORESIZE:
                if event.w != minX and event.h != minY:
                    window = pygame.display.set_mode((minX, minY), pygame.RESIZABLE)

            # if the user clicks on a hexagon/arrow
            if event.type == pygame.MOUSEBUTTONDOWN:
                # user wants to leave game (sets running to False) and save game (calls save function)
                if pygame.draw.polygon(window, ("white"), [(hex_x + 60, hex_y + 125) for hex_x, hex_y in hex_points]).collidepoint(event.pos):
                    print("YES")
                    window = pygame.display.set_mode((winX, winY))
                    return True, True
                # user wants to leave game (sets running to False) and NOT save game (does not call save function)
                elif pygame.draw.polygon(window, ("white"), [(hex_x + 200, hex_y + 125) for hex_x, hex_y in hex_points]).collidepoint(event.pos):
                    print("NO")
                    window = pygame.display.set_mode((600, 600))
                    return False, False
                # user DOES NOT want to leave game (keeps running set to True, does not call save function) (back arrow)
                elif pygame.draw.polygon(window, ("white"), arrow_rect_vertices).collidepoint(event.pos):
                    return True, False

        window.fill("white")

        # draw the back arrow in the window
        pygame.draw.polygon(window, ("black"), arrow_vertices, 0)
        pygame.draw.polygon(window, ("white"), arrow_rect_vertices, 1)

        # draw the YES/NO hexagons in the window
        pygame.draw.polygon(window, ("black"), [(hex_x + 60, hex_y + 125) for hex_x, hex_y in hex_points], 3)
        pygame.draw.polygon(window, ("black"), [(hex_x + 200, hex_y + 125) for hex_x, hex_y in hex_points], 3)

        # write SAVE GAME? prompt
        window.blit(prompt_font.render("SAVE GAME?", 1, ("black")), (110, 55))

        # write YES or NO on top of hexagons
        window.blit(font.render("YES", 1, ("black")), (117, 187))
        window.blit(font.render("NO", 1, ("black")), (260, 187))

        # update display
        pygame.display.update()

    return
    pygame.quit()

leave_game_options()