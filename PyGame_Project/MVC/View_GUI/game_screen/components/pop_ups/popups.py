import pygame, sys
from pygame import *


min_width = 800
min_height = 600

class Popup:
    def __init__(self, screen, message, on_yes, on_no, show_input=True, input_prompt="Enter your input:"):
        self.screen = screen
        self.message = message
        self.on_yes = on_yes
        self.on_no = on_no
        self.show_input = show_input
        self.input_prompt = input_prompt
        self.font = pygame.font.Font(None, 36)
        self.active = False
        self.text_input = ""
        self.input_box = None
        self.yes_button = None
        self.no_button = None
        self.setup_ui()

    def setup_ui(self):
        screen_width, screen_height = self.screen.get_size()

        # Semi-transparent background
        self.background = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        self.background.fill((100, 100, 100, 128))

        # Popup size based on screen size
        popup_width, popup_height = int(screen_width * 0.6), int(screen_height * 0.4)
        self.popup_rect = pygame.Rect(0, 0, popup_width, popup_height)
        self.popup_rect.center = self.screen.get_rect().center

        font_size = int((popup_height * .15))
        self.font = pygame.font.Font(None, font_size)

        # Message
        self.message_surface = self.font.render(self.message, True, (255, 255, 255))
        self.message_rect = self.message_surface.get_rect(center=(self.popup_rect.centerx, self.popup_rect.top +
                                                                  popup_height * .1))

        # Input prompt
        self.input_prompt_surface = self.font.render(self.input_prompt, True, (255, 255, 255))
        self.input_prompt_rect = self.input_prompt_surface.get_rect(
            center=(self.popup_rect.centerx, self.popup_rect.top + popup_height * .3))

        # Input box
        input_box_width, input_box_height = int(popup_width * 0.8), int(popup_width * 0.1)
        self.input_box = pygame.Rect(0, 0, input_box_width, input_box_height)
        self.input_box.center = (self.popup_rect.centerx, self.popup_rect.top + 150)

        # Buttons
        button_width, button_height = input_box_width * .33, input_box_height * .75
        self.yes_button = pygame.Rect(0, 0, button_width, button_height)
        self.yes_button.center = (self.input_box.center[0] - button_width, self.input_box.center[1] +
                                  (button_height * 1.25))

        self.no_button = pygame.Rect(0, 0, button_width, button_height)
        self.no_button.center = (self.input_box.center[0] + button_width, self.input_box.center[1] +
                                 (button_height * 1.25))

    def handle_event(self, event, state):
        if event.type == MOUSEBUTTONUP:
            if self.yes_button.collidepoint(event.pos):
                self.on_yes(self.text_input)
            elif self.no_button.collidepoint(event.pos):
                self.on_no()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text_input = self.text_input[:-1]
            else:
                self.text_input += event.unicode
        elif event.type == pygame.VIDEORESIZE:
            if event.w < min_width:
                width = min_width
            else:
                width = event.w

            if event.h < min_height:
                height = min_height
            else:
                height = event.h

            state.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            self.setup_ui()
            self.draw()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # Draw popup rectangle
        pygame.draw.rect(self.screen, (50, 50, 50), self.popup_rect)

        # Draw message
        self.screen.blit(self.message_surface, self.message_rect)

        if self.show_input:
            self.screen.blit(self.input_prompt_surface, self.input_prompt_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
            input_text_surface = self.font.render(self.text_input, True, (255, 255, 255))
            input_text_rect = input_text_surface.get_rect(x=self.input_box.x + 10, centery=self.input_box.centery)
            self.screen.blit(input_text_surface, input_text_rect)

        # Draw buttons
        pygame.draw.rect(self.screen, (0, 128, 0), self.yes_button)
        pygame.draw.rect(self.screen, (128, 0, 0), self.no_button)

        yes_text_surface = self.font.render("Yes", True, (255, 255, 255))
        yes_text_rect = yes_text_surface.get_rect(center=self.yes_button.center)
        self.screen.blit(yes_text_surface, yes_text_rect)

        no_text_surface = self.font.render("No", True, (255, 255, 255))
        no_text_rect = no_text_surface.get_rect(center=self.no_button.center)
        self.screen.blit(no_text_surface, no_text_rect)

        self.setup_ui()

    def show(self):
        self.active = True

    def hide(self):
        self.active = False


class SavePopup(Popup):
    def __init__(self, screen):
        self.message = "Would you like to save your game?"
        self.confirmation_bool = False
        self.finished_saving = False
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False, input_prompt='')

    def on_yes(self, input_text):
        if not self.show_input:
            self.show_input = True
            self.input_prompt = "Please enter a filename:"
            self.message = ''

    def on_no(self):
        self.__init__(self.screen)



class LeavePopup(Popup):
    def __init__(self, screen):
        message = "Are you sure you want to leave the game?"
        super().__init__(screen, message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self, input_text=None):
        print("Exiting the game")
        pygame.quit()
        sys.exit()

    def on_no(self):
        self.__init__(self.screen)


class GiveUpPopup(Popup):
    def __init__(self, screen):
        self.message = "Are you sure you want to give up?"
        self.confirmation_bool = False
        self.finished_saving = False
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False, input_prompt='')

    def on_yes(self, input_text):
        if not self.show_input:
            self.show_input = True
            self.input_prompt = "Please enter your name for the highscores:"
            self.message = ''

    def on_no(self):
        self.__init__(self.screen)
