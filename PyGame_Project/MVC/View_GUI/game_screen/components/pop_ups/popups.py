import pygame, sys, re
from pygame import *


min_width = 800
min_height = 600

class Popup:
    def __init__(self, screen, message, on_yes, on_no, show_input=True):
        self.screen = screen
        self.message = message
        self.on_yes = on_yes
        self.on_no = on_no
        self.show_input = show_input
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

        font_size = screen_width * .05
        self.font = pygame.font.SysFont(None, int(font_size))

        # Message
        wrapped_message = self.wrap_text(self.message, self.font, self.popup_rect.width * 0.8)
        self.message_surfaces = [self.font.render(line, True, (255, 255, 255)) for line in wrapped_message]
        self.message_rects = [surface.get_rect() for surface in self.message_surfaces]
        for i, rect in enumerate(self.message_rects):
            rect.center = (self.popup_rect.centerx, self.popup_rect.top + popup_height * .1 + i * self.font.get_height())


        # Input box
        input_box_width, input_box_height = int(popup_width * 0.8), int(popup_width * 0.1)
        self.input_box = pygame.Rect(0, 0, input_box_width, input_box_height)
        self.input_box.center = (self.popup_rect.centerx, self.popup_rect.centery)

        # Buttons
        button_width, button_height = input_box_width * .33, input_box_height * .75
        self.yes_button = pygame.Rect(0, 0, button_width, button_height)
        self.yes_button.center = (self.input_box.center[0] - button_width, self.popup_rect.bottom - button_height * 1.5)

        self.no_button = pygame.Rect(0, 0, button_width, button_height)
        self.no_button.center = (self.input_box.center[0] + button_width, self.popup_rect.bottom - button_height * 1.5)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # Draw popup rectangle
        pygame.draw.rect(self.screen, (50, 50, 50), self.popup_rect)

        # Draw message
        for i, message_surface in enumerate(self.message_surfaces):
            self.screen.blit(message_surface, self.message_rects[i])

        if self.show_input:
            pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
            input_text_surface = self.font.render(self.text_input, True, (255, 255, 255))
            input_text_rect = input_text_surface.get_rect()

            # Center the text within the input box
            input_text_rect.center = self.input_box.center
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

    
    def handle_event(self, event, state):
        if event.type == MOUSEBUTTONUP:
            if self.yes_button.collidepoint(event.pos):
                self.on_yes()
            elif self.no_button.collidepoint(event.pos):
                self.on_no()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text_input = self.text_input[:-1]
            
            elif self.show_input: 
                if isinstance(self, SavePopup):
                    if not self.check_string(event.unicode):
                        temp_text_input = self.text_input + event.unicode
                        temp_text_surface = self.font.render(temp_text_input, True, (255, 255, 255))
                        if temp_text_surface.get_width() < self.input_box.width - 20:
                            self.text_input += event.unicode
                
                elif isinstance(self, GiveUpPopup) and len(self.text_input) + 1 < 4:
                    self.text_input += event.unicode

            elif event.key == K_RETURN:
                self.on_yes()

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

    def wrap_text(self, text, font, max_width):
        lines = []
        words = text.split(' ')
        current_line = ''

        for word in words:
            test_line = current_line + word + ' '
            test_width, _ = font.size(test_line)

            if test_width < max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + ' '

        lines.append(current_line.strip())
        return lines
    
    @staticmethod
    def check_string(string):
        pattern = r'[\\/:*?"<>|]'
        if re.search(pattern, string):
            return True
        return False
        
    def show(self):
        self.active = True

    def hide(self):
        self.active = False


class SavePopup(Popup):
    def __init__(self, screen, puzzle_stats):
        self.puzzle_stats = puzzle_stats
        self.message = "Would you like to save your game?"
        self.confirmation_bool = False
        self.finished_saving = False
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self):
        print("In on_yes()")
        if not self.show_input:
            self.show_input = True
            self.message = "Please enter a filename:"
        elif self.show_input and not self.finished_saving:
            check_file_name()
            

    def on_no(self):
        self.__init__(self.screen, self.puzzle_stats)
    
    def check_file_name(self):
        if not self.puzzle_stats.get_check_file(self.text_input):
            self.message = "Game saved successfully!"
            self.puzzle_stats.get_save_game(self.text_input)
            self.finished_saving = True
            self.setup_ui()
            self.draw()
        if self.finished_saving:
            pygame.time.wait(1500)
            self.on_no()


class LeavePopup(Popup):
    def __init__(self, screen):
        self.message = "Are you sure you want to leave the game?"
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self, input_text=None):
        print("Exiting the game")
        pygame.quit()
        sys.exit()

    def on_no(self):
        self.__init__(self.screen)


class GiveUpPopup(Popup):
    def __init__(self, screen, puzzle_stats):
        self.puzzle_stats = puzzle_stats
        self.message = "Are you sure you want to give up?"
        self.confirmation_bool = False
        self.name_check = False
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self):
        if not self.show_input:
            self.show_input = True
            self.confirmation_bool = True
            self.message = "Enter a three character name for the highscores."

        elif self.confirmation_bool:
            print("This would call the highscore screen.")
            # Call highscore screen.
            pass

    def on_no(self):
        self.__init__(self.screen, self.puzzle_stats)

