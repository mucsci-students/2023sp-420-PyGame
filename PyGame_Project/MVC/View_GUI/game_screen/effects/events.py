from enum import Enum
from ..components.center.game import update_hexagon_positions
from model_puzzle import *
from hints_gui import *
import pygame

class GuessState(Enum):
    CORRECT = 1
    INCORRECT = 2
    NEUTRAL = 3


min_width = 800
min_height = 600


def wire_events(state):

    if state.correct_guess_timer or state.incorrect_guess_timer:
        if pygame.time.get_ticks() - state.start_animation_time >= state.animation_duration:
            print('We actually got in here')
            reset_timer(state)

    if state.active_popup is not None:
        if state.active_popup.active:
            state.active_popup.draw()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            clicked_leave(state)

        if state.active_popup is None or not state.active_popup.active:
            if state.show_guessed_words:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                    handle_scroll(state, event.button)

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                    handle_scroll(state, event.button)

            if event.type == pygame.MOUSEBUTTONUP:
                handle_button_press(state, event)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    state.current_guess = state.current_guess[:-1]
                
                elif event.unicode.isalpha() and event.unicode.upper() in state.puzzle_stats.pangram.upper() and state.can_guess:
                    state.current_guess += event.unicode.upper()

                elif event.key == pygame.K_RETURN:
                    if len(state.current_guess) > 3:
                        clicked_submit(state)
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LCTRL]:
                    if event.key == pygame.K_BACKSPACE:
                        state.current_guess = ''

        elif state.active_popup.active:
            state.active_popup.handle_event(event, state)
        
        if event.type == pygame.VIDEORESIZE:
            if event.w < min_width:
                width = min_width
            else:
                width = event.w

            if event.h < min_height:
                height = min_height
            else:
                height = event.h

            state.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            state.scroll_position = 0
            update_hexagon_positions(state)


def clicked_shuffle(state):
    if not state.is_animating:
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        state.is_animating = True
        state.start_animation_time = pygame.time.get_ticks()
        state.elapsed_animation_time = 0


def clicked_save(state):
    state.active_popup = state.save_popup
    state.active_popup.show()


def clicked_give_up(state):
    state.active_popup = state.give_up_popup
    state.active_popup.show()


def clicked_leave(state):
    state.active_popup = state.leave_popup
    state.active_popup.show()


def clicked_hints():
    hint_screen()


def clicked_go_back(state):
    state.active_popup = state.back_popup
    if state.active_popup.show():
        state.running = False
        


def reset_timer(state):
    state.current_guess_state = GuessState.NEUTRAL
    if state.correct_guess_timer:
        state.current_guess = ''
    state.incorrect_guess_timer = False
    state.correct_guess_timer = False


def clicked_submit(state):
    if state.puzzle_stats.get_check_guess(state.current_guess) == 0:
        state.current_guess_state = GuessState.CORRECT
        state.correct_guess_timer = True
        if len(state.current_guess) == 4:
                state.current_guess = f'+ {state.puzzle_stats.get_word_points(state.current_guess)} point!'
        else:
                state.current_guess= f'+ {state.puzzle_stats.get_word_points(state.current_guess)} points!'
    else:
        state.current_guess_state = GuessState.INCORRECT
        state.incorrect_guess_timer = True
    
    state.start_animation_time = pygame.time.get_ticks()
    print(state.start_animation_time)


def clicked_clear(state):
    state.current_guess = ''

def clicked_show_words(state):
    state.show_guessed_words = not state.show_guessed_words

def handle_scroll(state, event):
    if event == 4:
        state.scroll_position = max(0, state.scroll_position - 1)
    else:
        state.scroll_position = min(state.max_scroll_position, state.scroll_position + 1)

def handle_button_press(state, event):
    if not (event.button == 4 or event.button == 5):
        for key in state.buttons:
            # Only process button actions when not showing the guessed words.
            if not state.show_guessed_words:
                if key.strip().casefold() == "Shuffle".casefold() and state.buttons[key]:
                    clicked_shuffle(state)
                elif key.strip().casefold() == "Submit".casefold() and state.buttons[key]:
                    clicked_submit(state)
                elif key.strip().casefold() == "Clear".casefold() and state.buttons[key]:
                    clicked_clear(state)
                elif key.strip().casefold() == "Give Up".casefold() and state.buttons[key]:
                    clicked_give_up(state)
                elif key.strip().casefold() == "Save".casefold() and state.buttons[key]:
                    clicked_save(state)
                elif key.strip().casefold() == "Hints".casefold() and state.buttons[key]:
                    clicked_hints()
                elif key.strip().casefold() == "Leave Game".casefold() and state.buttons[key]:
                    clicked_leave(state)
                elif key.strip() in state.puzzle_stats.pangram.upper() and state.buttons[key] and state.can_guess:
                    state.current_guess += key.upper()
            
            # Process these whenever.
            if key.strip() == "Toggle Guessed Words" and state.buttons[key]:
                clicked_show_words(state)
            elif key.strip().casefold() == "Up".casefold() and state.buttons[key]:
                    handle_scroll(state, 4)
            elif key.strip().casefold() == "Down".casefold() and state.buttons[key]:
                    handle_scroll(state, 5)
