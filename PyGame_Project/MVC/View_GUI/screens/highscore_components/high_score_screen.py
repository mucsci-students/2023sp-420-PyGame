from PyGame_Project.MVC.Model.Database.model_highscores import insert_or_update_score, get_scores_for_puzzle
from PyGame_Project.MVC.View_GUI.screens.highscore_components.highscore_state import HighScoreState
from PyGame_Project.MVC.View_GUI.screens.highscore_components.header import create_header
from PyGame_Project.MVC.View_GUI.screens.highscore_components.center import create_center
from PyGame_Project.MVC.Model.imageGen import generateImage

import pygame, os, sys, math

minimum_width = 800
minimum_height = 600


def build_high_score_screen(required_letter='', pangram='', name='', score=0):

    state = HighScoreState()
    state.player_name = name
    pygame.display.set_caption('High Scores')
    state.display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    insert_or_update_score(name, required_letter, pangram, score)
    state.all_scores = get_scores_for_puzzle(required_letter, pangram)

    state.required_letter = required_letter
    state.current_puzzle = pangram

    i = 1
    for score in state.all_scores:
        state.edited_scores.append((i, score[0], score[1]))
        i += 1

    image_file_path = os.path.join(os.getcwd(), "PyGame_Project/MVC/View_GUI/helpicons")
    bg_img = pygame.image.load(os.path.join(image_file_path, "Background_Image.png")).convert()

    fps = pygame.time.Clock()

    while state.running:
        fps.tick(60)
        state.display.blit(bg_img, (0, 0))
        create_header(state)
        create_center(state)

        high_score_events(state)
        pygame.display.update()


def high_score_events(state):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            state.running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            handle_button_press(state, event)

        if event.type == pygame.VIDEORESIZE:
            handle_screen_resize(state, event)

        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button == 5):
            handle_scroll(state, event.button)


def handle_screen_resize(state, event):
    if event.w < minimum_width:
        width = minimum_width
    else:
        width = event.w

    if event.h < minimum_height:
        height = minimum_height
    else:
        height = event.h

    state.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)


def handle_scroll(state, event):
    if event == 4:
        state.scroll_position = max(0, state.scroll_position - 1)
    else:
        state.scroll_position = min(state.max_scroll_position, state.scroll_position + 1)


def handle_button_press(state, event):
    if not (event.button == 4 or event.button == 5):
        for key in state.buttons:
            if key.strip().casefold() == 'Leave'.casefold() and state.buttons[key]:
                clicked_leave(state)
            elif key.strip().casefold() == 'Share'.casefold() and state.buttons[key]:
                generateImage(state.player_name)


def clicked_leave(state):
    state.running = False


def clicked_share(state):
    pass


# load start screen
def start_hs(player_name, req_letter, pangram, player_score):
    clock = pygame.time.Clock()

    # settings
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    pygame.display.set_caption('Load A Game')
    font_title = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont("couriernew", 30)

    # create hexagon points (NOT the lines between the points)
    hex_radius = 60 # change this for bigger hexagons, considered midpoint
    hex_points = []
    for i in range(6):
        hex_angle = (math.pi / 180) * (60 * i) # converts from degrees to radians
        hex_x = hex_radius * math.cos(hex_angle) + 70 # the + 70 changes x position
        hex_y = hex_radius * math.sin(hex_angle) + 70
        hex_points.append((hex_x, hex_y))

    # create back arrow points
    arrow_vertices = [(10, 15), (5, 20), (10, 25), (5, 20), (22, 20), (5, 20), (10, 25)]
    arrow_rect_vertices = [(0, 0), (0, 25), (30, 25), (30, 0)]
    
    # function that writes text onto the screen and buttons
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # variable to check for clicking status
    click = False
    
    # main function
    def hs_menu(player_name, req_letter, pangram, player_score):
        # from shapes import Rectangle, Hexagon
        
        while True:
            # creates screen and titles
            screen.fill(('white'))
            draw_text('HIGH SCORES', font_title, ('black'), screen, 180, 50)

            insert_or_update_score(player_name, req_letter, pangram, player_score)

            all_scores = get_scores_for_puzzle(req_letter, pangram)


            y_axis = 100
            rank_num = 1
            for score in all_scores:
                if rank_num == 10:
                    hs_line = (f"{rank_num}    {score[0]}     {score[1]}")
                else:
                    hs_line = (f"{rank_num}     {score[0]}     {score[1]}")

                draw_text(hs_line, font, ('black'), screen, 160, y_axis)
                rank_num += 1
                y_axis += 30
                if rank_num > 10:
                    break
    
            mx, my = pygame.mouse.get_pos()

            # creating buttons
            share = pygame.draw.polygon(screen, ('black'), [(hex_x + 225, hex_y + 450) for hex_x, hex_y in hex_points], 3)

            # defining statements when clicked on
            if share.collidepoint((mx, my)):
                if click:
                    generateImage(player_name)

        
            # draws the back arrow in the window
            pygame.draw.polygon(screen, ("black"), arrow_vertices, 0)
            pygame.draw.polygon(screen, ("white"), arrow_rect_vertices, 1)
    
            # writing text over buttons
            draw_text('SHARE', font, ('black'), screen, 250, 505)
           
            # commands that lead to actions
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONUP:
                    generateImage(player_name)
                    if share.collidepoint(event.pos):
                        print("here")

            pygame.display.update()
            clock.tick(60)
        
    hs_menu(player_name, req_letter, pangram, player_score)
