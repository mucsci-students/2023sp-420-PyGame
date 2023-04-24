import pygame, sys, re
from pygame import *
from PyGame_Project.MVC.View_GUI.screens.highscore_components.high_score_screen import build_high_score_screen

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
        self.no_button_text = "No"
        self.yes_button_text = "Yes"
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

        yes_text_surface = self.font.render(self.yes_button_text, True, (255, 255, 255))
        yes_text_rect = yes_text_surface.get_rect(center=self.yes_button.center)
        self.screen.blit(yes_text_surface, yes_text_rect)

        no_text_surface = self.font.render(self.no_button_text, True, (255, 255, 255))
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
            elif event.key == K_RETURN:
                self.on_yes()

            elif self.show_input: 
                if isinstance(self, GiveUpPopup) and len(self.text_input) + 1 < 4:
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
        if isinstance(self, SavePopup):
            if self.finished_saving:
                self.setup_ui()
                self.draw()
                self.on_no()

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
    def check_character_is_allowed(string):
        allowed_char_pattern = r'[A-Za-z0-9_!@#$%^&*()\-=+\[\]{};,. ]'
        if re.search(allowed_char_pattern, string):
            return True
        return False
    
    @staticmethod
    def check_windows_reserved_name(string):
        reserved_names = re.compile(r'^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$', re.IGNORECASE)
        if not re.search(reserved_names, string):
            return True
        return False
        
    def show(self):
        self.active = True

    def hide(self):
        self.active = False
    
    def update_screen(self):
        self.setup_ui()
        self.draw()
        pygame.display.update()


class SavePopup(Popup):
    def __init__(self, state):
        self.puzzle_stats = state.puzzle_stats
        self.state = state
        self.message = "Would you like to save your game?"
        self.confirmation_bool = False
        self.finished_saving = False
        self.chose_encryption_option = False
        self.user_choice = False
        super().__init__(screen, self.message, self.on_yes, self.on_no, show_input=False)

    def on_no(self):
        if not self.chose_encryption_option:
            self.chose_encryption_option = True
            self.show_input = True
            self.message = "Please enter a filename:"
            self.yes_button_text = "Enter"
            self.no_button_text = "Cancel"
        else:
            self.message = "Returning to game..."
            self.update_screen()
            pygame.time.wait(1000)
            self.__init__(self.screen, self.puzzle_stats)

    def on_yes(self):
        if not self.chose_encryption_option:
            self.chose_encryption_option = True
            self.user_choice = True
            self.message = "Would you like to make your game shareable?"
            self.yes_button_text = "Yes"
            self.no_button_text = "No"
        
        # User chose they wanted to save their game
        elif not self.show_input and self.chose_encryption_option:
            self.show_input = True
            self.message = "Please enter a filename:"
            self.yes_button_text = "Enter"
            self.no_button_text = "Cancel"
        
        elif self.show_input:
            self.check_file_name()

        self.update_screen()
    
    def check_file_name(self):
        if self.check_windows_reserved_name(self.text_input):
            if (not self.puzzle_stats.get_check_file(self.text_input) and not self.confirmation_bool) or self.confirmation_bool:
                self.message = "Game saved successfully!"
                self.puzzle_stats.get_save_game(self.text_input, self.user_choice)
                self.finished_saving = True
            else:
                self.message = "File already exists. Overwrite?"
                self.yes_button_text = "Yes"
                self.no_button_text = "Cancel"
                self.confirmation_bool = True
        else:
            self.message = "Filename not allowed."
        
        self.update_screen()

    def handle_event(self, event, state):
        if event.type == MOUSEBUTTONUP:
            if self.yes_button.collidepoint(event.pos):
                self.on_yes()
            elif self.no_button.collidepoint(event.pos):
                self.on_no()
        
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text_input = self.text_input[:-1]
            elif event.key == K_RETURN:
                self.on_yes()
            
            elif self.show_input: 
                if self.check_character_is_allowed(event.unicode):
                    temp_text_input = self.text_input + event.unicode
                    temp_text_surface = self.font.render(temp_text_input, True, (255, 255, 255))
                    if temp_text_surface.get_width() < self.input_box.width - 20:
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
            self.update_screen()
        
        if self.finished_saving:
            self.on_no()


class LeavePopup(Popup):
    def __init__(self, state):
        self.state = state
        self.message = "Are you sure you want to leave the game?"
        super().__init__(state.display, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self, input_text=None):
        pygame.quit()
        sys.exit()

    def on_no(self):
        self.__init__(self.state)


class GiveUpPopup(Popup):
    def __init__(self, state):
        self.state = state
        self.puzzle_stats = state.puzzle_stats
        self.message = "Are you sure you want to give up?"
        self.confirmation_bool = False
        self.name_check = False
        super().__init__(state.display, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self):
        if not self.show_input:
            self.show_input = True
            self.confirmation_bool = True
            self.message = "Enter a three character name for the highscores."
            self.yes_button_text = "Confirm"
            self.no_button_text = "Cancel"
            self.update_screen()

        elif self.confirmation_bool:
            self.state.running = False
            build_high_score_screen(self.puzzle_stats.required_letter, self.puzzle_stats.pangram, self.text_input,
                                    self.puzzle_stats.score)
            # start_hs(self.text_input, self.puzzle_stats.required_letter, self.puzzle_stats.pangram, self.puzzle_stats.score)

    def on_no(self):
        self.__init__(self.state)


class BackPopup(Popup):
    def __init__(self, state):
        self.state = state
        self.message = "Are you sure you want to leave the game?"
        super().__init__(state.display, self.message, self.on_yes, self.on_no, show_input=False)

    def on_yes(self, input_text=None):
        return True

    def on_no(self):
        self.__init__(self.state)
