from PyGame_Project.MVC.View_GUI.screens.highscore_components.high_score_screen import build_high_score_screen
from ..game_screen_components.center.game import update_hexagon_positions
from PyGame_Project.MVC.View_GUI.hints_gui import hint_screen
from PyGame_Project.MVC.Model.imageGen import generateImage
from enum import Enum
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
                if state.correct_guess_timer:
                    reset_timer(state)
                    clicked_clear(state)
                elif state.incorrect_guess_timer:
                    reset_timer(state)

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


def clicked_hints():
    hint_screen()


def clicked_share():
    generateImage('')


def clicked_clear(state):
    state.current_guess = ''


def clicked_show_words(state):
    state.show_guessed_words = not state.show_guessed_words


def clicked_score(state):
    build_high_score_screen(state.required_letter, state.puzzle_stats.pangram, 'this makes it not work')


def clicked_save(state):
    state.active_popup = state.save_popup
    state.active_popup.show()


def clicked_give_up(state):
    state.active_popup = state.give_up_popup
    state.active_popup.show()


def clicked_go_back(state):
    state.active_popup = state.leave_popup
    state.active_popup.show()


def clicked_leave(state):
    state.active_popup = state.leave_popup
    state.active_popup.is_quitting = True
    state.active_popup.show()


def clicked_shuffle(state):
    if not state.is_animating:
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        state.is_animating = True
        state.start_animation_time = pygame.time.get_ticks()
        state.elapsed_animation_time = 0


def clicked_submit(state):
    if state.puzzle_stats.get_check_guess(state.current_guess) == 0:
        state.current_guess_state = GuessState.CORRECT
        pygame.event.set_blocked(pygame.KEYDOWN)
        state.correct_guess_timer = True
        if len(state.current_guess) == 4:
            state.current_guess = f'+ {state.puzzle_stats.get_word_points(state.current_guess)} point!'
        else:
            state.current_guess = f'+ {state.puzzle_stats.get_word_points(state.current_guess)} points!'
    else:
        state.current_guess_state = GuessState.INCORRECT
        state.incorrect_guess_timer = True

    state.start_animation_time = pygame.time.get_ticks()


def handle_scroll(state, event):
    if event == 4:
        state.scroll_position = max(0, state.scroll_position - 1)
    else:
        state.scroll_position = min(state.max_scroll_position, state.scroll_position + 1)


def reset_timer(state):
    state.current_guess_state = GuessState.NEUTRAL
    if state.correct_guess_timer:
        state.current_guess = ''
    state.incorrect_guess_timer = False
    state.correct_guess_timer = False
    pygame.event.set_allowed(pygame.KEYDOWN)


def handle_button_press(state, event):
    if not (event.button == 4 or event.button == 5):
        for key in state.buttons:
            # Only process button actions when not showing guessed words, and a button is hovered.
            if not state.show_guessed_words and state.buttons[key]:
                if key.strip().casefold() == "Save".casefold():
                    clicked_save(state)
                elif key.strip().casefold() == "Clear".casefold():
                    clicked_clear(state)
                elif key.strip().casefold() == "Hints".casefold():
                    clicked_hints()
                elif key.strip().casefold() == "Share".casefold():
                    clicked_share()
                elif key.strip().casefold() == "Scores".casefold():
                    clicked_score(state)
                elif key.strip().casefold() == "Submit".casefold():
                    clicked_submit(state)
                elif key.strip().casefold() == "Shuffle".casefold():
                    clicked_shuffle(state)
                elif key.strip().casefold() == "Give Up".casefold():
                    clicked_give_up(state)
                elif key.strip().casefold() == "Leave Game".casefold():
                    clicked_go_back(state)

                elif key.strip() in state.puzzle_stats.pangram.upper() and state.can_guess:
                    state.current_guess += key.upper()
            
            # Process these whenever.
            if key.strip() == "Toggle Guessed Words" and state.buttons[key]:
                clicked_show_words(state)
            elif key.strip().casefold() == "Up".casefold() and state.buttons[key]:
                handle_scroll(state, 4)
            elif key.strip().casefold() == "Down".casefold() and state.buttons[key]:
                handle_scroll(state, 5)
