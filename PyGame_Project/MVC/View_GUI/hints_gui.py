import pygame, os, math
from PyGame_Project.MVC.Model.model_puzzle import *

def hint_screen():

    PuzzleStats().generate_hints()

    # initializes pygame
    pygame.init()

    # create window dimensions, and minimum window dimensions (when window is resized)
    winX, winY = 800, 600
    minX, minY = 800, 600
    window = pygame.display.set_mode((winX, winY), pygame.RESIZABLE)

    # set window name and icon
    pygame.display.set_caption("Hints")
   
    # set visual text and font
    font = pygame.font.SysFont(None, 21)
    table_font = pygame.font.SysFont("couriernew", 16)


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
    intro_text = ["Click an option to see each hint."]

    # strings shown in window for each hint when clicked on 

    # Pangram Hint
    puzzle = PuzzleStats()
    pangramStr = (f" -> Center letter is {puzzle.shuffled_puzzle[0].upper()}; Remaining letters are: {puzzle.shuffled_puzzle[1:7].upper()}")
    totalStats = (f" -> Words {len(puzzle.current_word_list)}; Points: {puzzle.total_points}")
    rem_words = len(puzzle.current_word_list) - len(puzzle.guesses)
    rem_points = puzzle.total_points - puzzle.score
    remStats = (f" -> Remaining Words: {rem_words}; Remaining Points: {rem_points}")
    pangram_overview = [
        "Pangrams: Shows general statistics for puzzle",
        "",
        pangramStr,
        totalStats,
        remStats
    ]


    # Matrix Hint

    # prints reference matrix to terminal
    matrix_list = ["Hint Matrix: ", ""]
    [matrix_list.append(''.join(['{:4}'.format(item) for item in row])) for row in PuzzleStats().hints.two_d_array]

    two_letter_dict = PuzzleStats().hints.two_letter_dict
    two_letter_str = ["Two Letter List: ", ""]
    count = 0
    row = ""
    for key in two_letter_dict:
        row = row + (f"{key.upper()} - {two_letter_dict[key]}")
        if count == 2:
            two_letter_str.append(row) 
            count = 0
            row = ""
        else:
            if len(str(two_letter_dict[key])) == 1:
                row = row + "      "
            else:
                row = row + "     "
            count += 1
    two_letter_str.append(row) 

    # sets the updated text to new_text, to funnel all possible informational texts into one variable
    new_text = intro_text

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
        window.blit(font.render("Pangram", 1, ("black")), (36, 63))
        window.blit(font.render("Matrix", 1, ("black")), (49, 188))
        window.blit(font.render("Two Letter", 1, ("black")), (35, 313))




    # when resizing window, text should be wrapped so that all text is visible to the user (not going outside the window)
    def wrap_text():
        #wordList = info_text.split() # splits the intro string into a list of words (the list will change when a button is pressed)
        """        
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
        """

        for i, line in enumerate(new_text):
            text_surface = table_font.render(line, 1, pygame.Color('black'))
            text_padX = 150  # set the x position to the left padding
            text_padY = 50 + i * (table_font.get_linesize())  # add padding and spacing between each line
            window.blit(text_surface, (text_padX, text_padY))





    # *** ACTIVE HELP LOOP ***
    running = True
    while running:
        clock.tick(fps)

        events = pygame.event.get()

        for event in events:

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
                    new_text = pangram_overview
                elif pygame.draw.polygon(window, ("white"), [(x, y + 125) for x, y in hex_points]).collidepoint(event.pos):
                    new_text = matrix_list
                elif pygame.draw.polygon(window, ("white"), [(x, y + 250) for x, y in hex_points]).collidepoint(event.pos):
                    new_text = two_letter_str
                elif pygame.draw.polygon(window, ("white"), arrow_rect_vertices).collidepoint(event.pos):
                    running = False

        add_elements()
        wrap_text()

        
        # update display
        pygame.display.update()

    # when running is False, reset the window size to the gui_main_menu window size
    window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    return
    pygame.quit()
