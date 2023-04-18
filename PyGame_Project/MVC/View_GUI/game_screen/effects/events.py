from ..components.center.game import update_hexagon_positions
from model_puzzle import *
from hints_gui import *
import pygame

min_width = 800
min_height = 600


def wire_events(state):
    if state.active_popup is not None:
        if state.active_popup.active:
            state.active_popup.draw()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            clicked_leave(state)

        if state.active_popup is None or not state.active_popup.active:
            if event.type == pygame.MOUSEBUTTONUP:
                for key in state.buttons:
                    if key.strip() == "Shuffle" and state.buttons[key]:
                        clicked_shuffle(state)
                    elif key.strip() == "Submit" and state.buttons[key]:
                        clicked_submit(state)
                    elif key.strip() == "Clear" and state.buttons[key]:
                        clicked_clear(state)
                    elif key.strip() == "Give Up" and state.buttons[key]:
                        clicked_give_up(state)
                    elif key.strip() == "Save" and state.buttons[key]:
                        clicked_save(state)
                    elif key.strip() == "Hints" and state.buttons[key]:
                        clicked_hints()
                    elif key.strip() == "Leave Game" and state.buttons[key]:
                        clicked_leave(state)
                    elif key.strip() in state.puzzle_stats.pangram.upper() and state.buttons[key] and state.can_guess:
                        state.current_guess += key.upper()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    state.current_guess = state.current_guess[:-1]
                
                elif event.unicode.isalpha() and event.unicode.upper() in state.puzzle_stats.pangram.upper() and state.can_guess:
                    state.current_guess += event.unicode.upper()

                elif event.key == pygame.K_RETURN:
                    print("Pressed return")
                    if len(state.current_guess) > 3:
                        clicked_submit(state)
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LCTRL]:
                    if event.key == pygame.K_BACKSPACE:
                        state.current_guess = ''

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
                update_hexagon_positions(state)

        elif state.active_popup.active:
            state.active_popup.handle_event(event, state)


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
    state.leave_popup.show()


def clicked_hints():
    hint_screen()
    pass


def clicked_submit(state):
    if state.puzzle_stats.get_check_guess(state.current_guess) == 0:
        print("Good")
        if len(state.current_guess) == 4:
                state.current_guess = f'+ {state.puzzle_stats.get_word_points(state.current_guess)} point!'
        else:
                state.current_guess= f'+ {state.puzzle_stats.get_word_points(state.current_guess)} points!'
    else:
        print("Bad")

def clicked_clear(state):
    state.current_guess = ''
