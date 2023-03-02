import pygame

# initializes pygame
pygame.init()

# button class, used to click and show different texts in the window
class Button:
    # initializes the button, creates rectangle, sets pivot
    def __init__(self, x, y, icon_name):
        self.img = icon_name
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # reacts to the button being pressed (or not being pressed)
    def draw(self, word_list_name):
        cursor_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(cursor_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                assign_list(word_list_name)
                wrap_text()
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        window.blit(self.img, (self.rect.x, self.rect.y))


# images of different help buttons
htp_icon = pygame.image.load("helpicons/htp_icon.png")
htp_icon = pygame.transform.scale(htp_icon, (100,55))
ptsys_icon = pygame.image.load("helpicons/ptsys_icon.png")
ptsys_icon = pygame.transform.scale(ptsys_icon, (100,55))
ranks_icon = pygame.image.load("helpicons/ranks_icon.png")
ranks_icon = pygame.transform.scale(ranks_icon, (100,55))

# creates different buttons to be pressed
button_htp = Button(10, 30, htp_icon)
button_ptsys = Button(10, 130, ptsys_icon)
button_ranks = Button(10, 230, ranks_icon)

# create window dimensions, and minimum window dimensions (when window is resized)
winX, winY = 600, 375
minX, minY = 400, 350
window = pygame.display.set_mode((winX, winY), pygame.RESIZABLE)

# set window name and icon
pygame.display.set_caption("Help")
icon = pygame.image.load("helpicons/clubpenguin4.jpg")
pygame.display.set_icon(icon)

# set visual text and font 
font = pygame.font.SysFont("None", 21)

# text shown in window before a button is clicked
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
~ Words guesses that use all seven given letters will earn double amount of points
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

# different word lists for each section (used for text wrapping)
htp_word_list = htp_text.split()
ptsys_word_list = ptsys_text.split()
ranks_word_list = ranks_text.split()

# other variables (used for text wrapping)
wordList = intro_text.split() # splits the intro string into a list of words (the list will change when a button is pressed)
lines = [] # list of all words that can fit on a line within the current window-space
curr_line = "" # current line that is able to fit within the current window-space

# padding for adding text in window (used for text wrapping and adding elements to the window)
paddingX = 130  # blank space from top left corner, accounting for where buttons are
paddingY = 20 # blank space from top left corner

# for frame limiter
fps = 60


################################### FUNCTIONS ###################################


# main function called when help button is clicked (through main menu or active puzzle)
def main_help():
    global window

    wrap_text()
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                if event.w < minX and event.h < minY:
                    window = pygame.display.set_mode((minX, minY), pygame.RESIZABLE)
                elif event.w < minX:
                    window = pygame.display.set_mode((minX, event.h), pygame.RESIZABLE)
                elif event.h < minY:
                    window = pygame.display.set_mode((event.w, minY), pygame.RESIZABLE)
                else:
                    window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                wrap_text()

        add_window_elements()
        pygame.display.update()


# adds the background color, buttons, and (wrapped) text on the screen
def add_window_elements():
    window.fill((0,128,128))

    button_htp.draw(htp_word_list)
    button_ptsys.draw(ptsys_word_list)
    button_ranks.draw(ranks_word_list)

    for i, line in enumerate(lines):
            text_surface = font.render(line, 1, pygame.Color('white'))
            text_padX = paddingX  # set the x position to the left padding
            text_padY = paddingY + i * (font.get_linesize())  # add padding and spacing between each line
            window.blit(text_surface, (text_padX, text_padY))


# creates lines of text, so that the maximum amount of words can fit in the visible window-space (left-to-right)
def wrap_text():
    global lines
    global curr_line

    max_text_line = window.get_width() - (paddingX - 50) * 2
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


# assigns the correct word list, depending on which button is pressed (accessed through Button class)
def assign_list(name):
    global wordList

    if name == htp_word_list:
        wordList = htp_word_list
    elif name == ptsys_word_list:
        wordList = ptsys_word_list
    elif name == ranks_word_list:
        wordList = ranks_word_list


# when help button is clicked/accessed
if __name__ == "__main__":
    main_help()