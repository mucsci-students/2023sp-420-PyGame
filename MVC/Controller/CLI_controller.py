### Main Menu CLI

import sys
import os
import time

from model_PuzzleStats import PuzzleStats
from model_puzzle import Puzzle
from model_shuffleLetters import ShuffleKey
from controller_universal import *
from View import *

### ------------Global Var--------------- ###

puzzle = Puzzle()
puzzle_stats = PuzzleStats(-1,"")


### ------------MAIN CLI Controller--------------- ###

# auto completes the command name when the TAB key is pressed
def tab_completion(typed_string, command_set):
  # checks to see if the current input can be autocompleted
  if len(typed_string) == 0 or not typed_string.startswith('/'):
    return typed_string, ''
  
  # gets the correct command set, depending on if the user is on the Main Menu or the Active Game screen
  if command_set == 1:
    commands = ['/newgame', '/loadgame', '/startfromkey', '/startsharedgame', '/help', '/exit']
  elif command_set == 2:
    commands = ['/help', '/back', '/share', '/exit', '/shuffle', '/showall', '/savegame', '/refresh']

  # finds commands that match what the user started to type
  matches = [c for c in commands if c.startswith(typed_string)]

  # split the command up, output the split variables
  if len(matches) == 1:
    typed_string, _, ending_letters = matches[0].partition(typed_string)
    return typed_string, ending_letters

  # if there was more than one command match, return as if no command was found (do nothing)
  return typed_string, ''


# Collects information about what the user types into the window
def user_input(command_set):
  # initialize an empty list to store the typed letters
  typed_letters = []

  # wait for keyboard events until enter/return key is pressed
  while True:
    key = get_os_name()
    # if the enter/return key is pressed, return the full typed string; else, figure out the key pressed
    if key == '\r' or key == '\n':
      return ''.join(typed_letters).lower()
    elif key is not None:
      on_key_press(key, typed_letters, command_set)


# Figures out information about the key pressed
def on_key_press(key, typed_letters, command_num):
  # if the tab key is pressed (tab completion)
  if key == '\t':
    typed_string, ending_string = tab_completion(''.join(typed_letters), command_num)
    if ending_string:
      typed_letters.extend(ending_string)
    typed_string = ''.join(typed_letters)

  # if the backspace key is pressed (unix = \xf7; win = \x08)
  elif key == '\x7f' or key == '\x08':
    typed_letters and typed_letters.pop()
    print("\033[K", end="")
    typed_string = ''.join(typed_letters)
  
  # if a single alpha character or '/' is pressed (like: /, a, b; not like: shift, backspace)
  elif key.isalpha() or key == '/':
    typed_letters.append(key)
    typed_string = ''.join(typed_letters)

  # if the key pressed is not tab, backspace, single alpha char, or '/'
  else:
    return

  # outputs the final string after the last key is pressed to the console
  print(typed_string, end='\r')


# Figures out the OS name to use correct keyboard for inputting text
def get_os_name():
  # if the current os is windows
  if os.name == 'nt':
    import msvcrt
    key = msvcrt.getch()
    # delete and arrow keys return a character, so exclude them as usable characters for os keyboard
    if key == b'\x00' or key == b'\xe0':
      # read the next character to discard escape sequence
      msvcrt.getch()
      return None
    return key.decode('utf-8', 'ignore')
  
  # if the current os is unix-based
  else:
    import tty
    import termios
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
      tty.setraw(sys.stdin.fileno())
      char = sys.stdin.read(1)
      # delete and arrow keys return a character, so exclude them as usable characters for os keyboard
      if char == '\x1b':
        # read and discard next two characters of escape sequence
        sys.stdin.read(2)
        return None
    finally:
      termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
    return char


# Checks to see if the space key was pressed
# "Press the space key to continue.."
def space_out():
  key = get_os_name()
  while True:
    if key == ' ':
      break


# starts the cli main menu
def main_menu_handler():
  command_set = 1
  while (True):
    cls()
    print_start_screen()
    print_main_menu()
    print("Select a command.")
    userInput = user_input(command_set).lower()
    main_response(userInput)


# handles users input from the main menu
def main_response(userInput):
  match userInput:
    case "/newgame":
      start_new_game()

    case "/loadgame":
      load_save_game()
          
    case "/startfromkey":
      keyStart()

    case "/startsharedgame":
      start_shared_game()

    case "/help":
      cls()
      print_help()
      space_out()
        
    case "/exit":
      cls()
      print_exit()
      exit_game()

    case _:
      print("Command Not Recognized")
      time.sleep(1)


# when user wants to load a saved game
def load_save_game():
  global puzzle_stats
  print_load_options()
  file_name = user_input(0)
  print_load_game()
  answer = user_input(0).lower()
  match answer:
    case "y":
      start_game_with_key_from_load(puzzle_stats.LoadGame(file_name))
    case "n":
      cls()
      return

    case _: # if any other command not in the list is entered, then this output will be returned
      print("Command Not Recognized")

# when user wants to load a game with a key
def keyStart():
  check_value = 1
  while(check_value == 1):
    cls()
    print_base_input()
    key = user_input(0).lower()
    
    check_value = start_game_with_key(key)
    
    if check_value == 1:
    # Turn into custom error call to Output.py with key
      cls()
      print("Invalid word, not a valid pangram. Return to main menu? Y/N \n")
      response = user_input(0).lower()
      if(response == "y"):
        main_menu_handler()

# function to save game
def saveGamePrompt():
    global puzzle_stats
    global puzzle

    while(True):
      print("Enter title to save game as:")
      userInput = user_input(0).lower() #asks user for an input
      cls()
      puzzle_stats.get_save_game(puzzle, userInput)
      print(f"{userInput} has been saved.")
      return

#Loops thru the active game screens
def activeGameLoop():
  loop = True
  while (loop):
    cls()
    loop = activeGame()

# when an active game is in play
def activeGame():
  global puzzle
  global puzzle_stats
  command_set = 2

  print_current_puzzle(puzzle_stats)
  print("Enter your guess.")
  userInput = user_input(command_set).lower() #asks user for input to match
  if (userInput == ""):
    return True
  elif (userInput[0] != "/"):
    outcome = print_guess_outcome(puzzle_stats.get_check_guess(userInput, puzzle))
    time.sleep(1)
    return outcome
  else:
    return active_game_commands(userInput)

# handles users inputed commands from the active game screen
def active_game_commands(userInput):
  match userInput:
    case "/help":
      cls()
      print_help()
      space_out()

      return True

    case "/shuffle":
      puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
      return True

    case "/savegame":
      print(f"Enter filename: ")
      file_name = user_input(0).lower()
      cls()
      save_current_game(file_name)
      return True
    
    case "/showall":
      print_all_guesses(puzzle_stats)
      space_out()
      
      return True
    
    case "/back":
      print_game_save()
      if(user_input(0).lower() == "y"):
        print(f"Enter filename: ")
        file_name = user_input(0).lower()
        cls()
        save_current_game(file_name)
      return False

    case "/share":
      cls()
      print_shared_key_output(puzzle.encode_puzzle_key())
      space_out()

      return True

    case "/exit":
      cls()
      print_exit()
      return exit_game()
    
    case "/refresh":
      return True

    case _:
      print("Command Not Recognized")
      time.sleep(1)
      return True

# starts a new game from randomly selected puzzle
def start_new_game():
  global puzzle
  global puzzle_stats
  puzzle, puzzle_stats = prep_new_game()
  activeGameLoop()

# Start game from base
def start_game_with_key(key):
  global puzzle
  global puzzle_stats
  prep_value = prep_game_with_key(key)

  if type(prep_value) == int:
    return 1
  
  puzzle, puzzle_stats = prep_value
  activeGameLoop()

# start game from a saved .json file
def start_game_with_key_from_load(save_info):
  global puzzle
  global puzzle_stats
  print(save_info)

  if save_info != 1:
    activeGameLoop()
  
  # prep_value = prep_game_from_load(save_info)
  # if type(prep_value) == int:
  #   return 1

  # puzzle = prep_value
    

# creates a save file (saves current game)
def save_current_game(filename):
  global puzzle
  global puzzle_stats
  puzzle_stats.get_save_game(puzzle, filename)

# closes the CLI
def exit_game():
  answer = user_input(0).lower()

  match answer:
    case "y": 
      cls()
      sys.exit()

    case "n":
      return True

    case _:
      print("Command not recognized")
        #should proceed with exiting. if !running game
      return True

# Function to clear the console after a user input is taken in 
def cls():
  os.system("cls" if os.name=="nt" else "clear") # now, to clear the screen

# Start a game from a shared key
def start_shared_game():
  global puzzle
  global puzzle_stats

  cls()
  print_shared_key_input()
  shared_key = user_input(0).lower()
  
  prep_value = prep_game_from_share(shared_key)
  
  if type(prep_value) == int:
    cls()
    print("Invalid Code Input.")
    print("\nPress the space key to try again...")
    print("Press 'n' to quit to main menu...")

    while True:
      key = get_os_name()
      if key == ' ':
        return start_shared_game()
      elif key == 'n':
        return True

  puzzle = prep_value
  activeGameLoop()

  
