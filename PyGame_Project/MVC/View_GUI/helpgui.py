import pygame, os, math
# from PyGame_Project.MVC.View_GUI.screens.main_menu_components.main_menu_screen import *


def start_help():

    # initializes pygame
    pygame.init()

    # create window dimensions, and minimum window dimensions (when window is resized)
    winX, winY = 750, 400
    minX, minY = 700, 400
    window = pygame.display.set_mode((winX, winY), pygame.RESIZABLE)

    # set window name and icon
    pygame.display.set_caption("Help")
    image_dir = os.path.join(os.getcwd(), "PyGame_Project/MVC/View_GUI/helpicons")
    icon = pygame.image.load(os.path.join(image_dir, 'clubpenguin4.jpg'))
    pygame.display.set_icon(icon)

    # set visual text and font
    hex_font = pygame.font.SysFont(None, 21)
    font = pygame.font.SysFont("couriernew", 16)

    # create hexagon points (NOT the lines between the points)
    hex_radius = 50 # change this for bigger hexagons, considered midpoint
    hex_points = []
    for i in range(6):
        hex_angle = (math.pi / 180) * (60 * i) # converts from degrees to radians
        hex_x = hex_radius * math.cos(hex_angle) + 70 # the + 70 changes x position
        hex_y = hex_radius * math.sin(hex_angle) + 70
        hex_points.append((hex_x, hex_y))

    # create back arrow points
    arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
    arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]

    # text shown in window before a hexagonal button is clicked
    intro_text = "Click an option for more information."

    # text shown in window when "How to Play" button is clicked
    htp_text = """
    How to Play:
    *** ***
    ~ Create words using letters from the hive, move up the ranks, and try to get the maximum score ***
    ~ You must use only the letters in the hive to create words ***
    ~ Each word much use the required letter in the center of the hive ***
    ~ Words must be at least four letters long ***
    ~ Letters can be used more than once in a single guess ***
    ~ Guesses cannot contain hyphens, proper nouns, vulgarities, or obscure words ***
    ~ Each puzzle includes at least one "pangram", which uses all seven given letters at least once
    """

    # text shown in window when "Point System" button is clicked
    ptsys_text = """
    Point System:
    *** ***
    ~ 4-letter words are worth 1 point each. ***
    ~ If the entered word is longer than 4 letters then you get a point for the word's character length ***
    ~ Each puzzle includes at least one “pangram” which uses every letter at least once. ***
    ~ Words guesses that use all seven given letters will earn an extra 7 points, plus the word's character length
    """

    # text shown in window when "Rank System" Button is clicked
    ranks_text = """
    Rank System:
    *** ***
    Every puzzle has 10 ranks that will progress and change based on the percentage that the puzzle is completed.
    *** ***
     0% - Beginner    ***
     2% - Good Start  ***
     5% - Moving Up   ***
     8% - Good        ***
     15% - Solid      ***
     25% - Nice       ***
     40% - Great      ***
     50% - Amazing    ***
     70% - Genius     ***
    100% - Queen Bee  
    """

    # sets the updated text to new_text, to funnel all possible informational texts into one variable
    new_text = intro_text
    show_text = font.render(intro_text, 1, ("black"))

    # for frame limiter
    fps = 60
    clock = pygame.time.Clock()

    # window fill, draw hexagons, draw back arrow, write hexagon text
    def add_elements():
        
        # make window background white
        window.fill("white")
        
        # draw hexagons in the window
        pygame.draw.polygon(window, ("black"), hex_points, 3)
        pygame.draw.polygon(window, ("black"), [(hex_x, hex_y + 125) for hex_x, hex_y in hex_points], 3)
        pygame.draw.polygon(window, ("black"), [(hex_x, hex_y + 250) for hex_x, hex_y in hex_points], 3)

        # draw the back arrow in the window
        pygame.draw.polygon(window, ("black"), arrow_vertices, 0)
        pygame.draw.polygon(window, ("white"), arrow_rect_vertices, 1)

        # write the text on top of the hexagons
        window.blit(hex_font.render("How to Play", 1, ("black")), (32, 63))
        window.blit(hex_font.render("Points", 1, ("black")), (50, 188))
        window.blit(hex_font.render("Ranks", 1, ("black")), (50, 313))

    # when resizing window, text should be wrapped so that all text is visible to the user (not going outside the window)
    def wrap_text(info_text):
        wordList = info_text.split() # splits the intro string into a list of words (the list will change when a button is pressed)
        lines = []
        curr_line = "" # current line that is able to fit within the current window-space

        max_text_line = window.get_width() - 200
        lines.clear()
        curr_line = ""

        for word in wordList:
            if word == "***":
                lines.append(curr_line)
                curr_line = ""
                continue

            if font.size(curr_line + word)[0] < max_text_line:
                curr_line += f"{word} "
            else:
                lines.append(curr_line)
                curr_line = f"{word} "
        lines.append(curr_line)
        
        for i, line in enumerate(lines):
            text_surface = font.render(line, 1, pygame.Color('black'))
            text_padX = 150  # set the x position to the left padding
            text_padY = 50 + i * (font.get_linesize())  # add padding and spacing between each line
            window.blit(text_surface, (text_padX, text_padY))

    # *** ACTIVE HELP LOOP ***
    running = True
    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            print("here")

            # if the user exits the window
            if event.type == pygame.QUIT:
                running = False
            
            # if the window is resized
            if event.type == pygame.VIDEORESIZE:
                if event.w < minX and event.h < minY:
                    window = pygame.display.set_mode((minX, minY), pygame.RESIZABLE)
                elif event.w < minX:
                    window = pygame.display.set_mode((minX, event.h), pygame.RESIZABLE)
                elif event.h < minY:
                    window = pygame.display.set_mode((event.w, minY), pygame.RESIZABLE)
                else:
                    window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
            # if the user left-clicks on a hexagon
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.draw.polygon(window, ("white"), hex_points).collidepoint(event.pos):
                    new_text = htp_text
                elif pygame.draw.polygon(window, ("white"), [(x, y + 125) for x, y in hex_points]).collidepoint(event.pos):
                    new_text = ptsys_text
                elif pygame.draw.polygon(window, ("white"), [(x, y + 250) for x, y in hex_points]).collidepoint(event.pos):
                    new_text = ranks_text
                elif pygame.draw.polygon(window, ("white"), arrow_rect_vertices).collidepoint(event.pos):
                    running = False

        add_elements()
        wrap_text(new_text)
        
        # update display
        pygame.display.update()

    # when running is False, reset the window size to the gui_main_menu window size
    window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    return
    pygame.quit()
