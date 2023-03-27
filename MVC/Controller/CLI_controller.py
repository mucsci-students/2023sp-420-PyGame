### Main Menu CLI

import sys
import os
import time
import keyboard

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
  
  commands = []

  if command_set == 1:
    commands = ['/newgame', '/loadgame', '/startfromkey', '/startsharedgame', '/help', '/exit']
  elif command_set == 2:
    commands = ['/help', '/back', '/share', '/exit', '/shuffle', '/showall', '/savegame', '/refresh']

  matches = [c for c in commands if c.startswith(typed_string)]

  if len(matches) == 1:
    old_string = typed_string
    typed_string = matches[0]
    inputted_part, removed_part, ending_letters = typed_string.partition(old_string)
    return typed_string, ending_letters
  else:
    return typed_string, ''


def user_input(command_set):
    # initialize an empty list to store the typed letters
    typed_letters = []

    # listens to key presses
    keyboard.on_press(lambda event: on_key_press(event, typed_letters, command_set))
    
    # wait for keyboard events until Enter key is pressed
    while True:
        event = keyboard.read_event()
        if event.name == 'enter':
            typed_string = ''.join(typed_letters)
            typed_letters.clear()
            keyboard.unhook_all()
            return typed_string.lower()
            


def on_key_press(event, typed_letters, command_num):
    # if the tab key is pressed
    if event.name == 'tab':
        ending_string = ""
        typed_string = ''.join(typed_letters)
        typed_string, ending_string = tab_completion(typed_string, command_num)
        
        if ending_string != '':
          typed_letters.append(ending_string)

        print(typed_string, end = '\r')

    # if the enter key is pressed
    elif event.name == 'enter':
        typed_string = ''
        return False

    # if the backspace key is pressed
    elif event.name == 'backspace':
        if typed_letters:
            typed_letters.pop()
            print("\033[K", end = "")
    
    # if a single alpha character or "/" is pressed (like: /, a, b; not like: shift, backspace)
    elif (event.name.isalpha() and len(event.name) == 1) or event.name == '/':
        typed_letters.append(event.name)

    # combine the letters into a word, print on screen
    typed_string = ''.join(typed_letters)
    print(typed_string, end = '\r')
    return True



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

      # user must press space to exit help screen
      while True:
        event = keyboard.read_event()
        if event.name == 'space':
          break
        
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
  # count = -1
  # for i in puzzle.pangram:
  #   ++count
  #   if puzzle.pangram[i] == puzzle.required_letter:
  #     puzzle[0] == puzzle[count]


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

      # user must press space to exit help screen
      while True:
        event = keyboard.read_event()
        if event.name == 'space':
          break

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
      
      # user must press space to exit help screen
      while True:
        event = keyboard.read_event()
        if event.name == 'space':
          break
      
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
      
      # user must press space to exit help screen
      while True:
        event = keyboard.read_event()
        if event.name == 'space':
          break

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
      event = keyboard.read_event()
      if event.name == 'space':
        return start_shared_game()
      elif event.name == 'n':
        return True

  puzzle = prep_value
  activeGameLoop()

  
