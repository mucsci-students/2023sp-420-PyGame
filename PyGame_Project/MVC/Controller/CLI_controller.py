### Main Menu CLI

import sys
import os
import time

from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *
from PyGame_Project.MVC.View_CLI.View import *
from PyGame_Project.MVC.Model.Database.model_highscores import *
from PyGame_Project.MVC.Model.imageGen import *


### ------------MAIN CLI Controller--------------- ###

# auto completes the command name when the TAB key is pressed
def tab_completion(typed_string, command_set):
  # checks to see if the current input can be autocompleted
  if len(typed_string) == 0 or not typed_string.startswith('/'):
    return typed_string, ''
  
  # gets the correct command set, depending on if the user is on the Main Menu or the Active Game screen
  if command_set == 1:
    commands = ['/newgame', '/loadgame', '/startfromkey', '/startsharedgame', '/highscores', '/help', '/exit']
  elif command_set == 2:
    commands = ['/help', '/back', '/share', '/exit', '/shuffle', '/showall', '/savegame', '/hints', '/giveup', '/highscores']

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
      return ''.join(typed_letters)
    elif key is not None:
      on_key_press(key, typed_letters, command_set)


# Figures out information about the key pressed
def on_key_press(key, typed_letters, command_num):
  # when a user types (most cases)
  if command_num != 3:

    # if the user is entering a save filename
    if command_num == 4 and key in ["/", "\\", ":", "\"", "<", ">", "|"]:
        return

    # if the tab key is pressed (tab completion)
    if key == '\t':
      typed_string, ending_string = tab_completion(''.join(typed_letters).lower(), command_num)
      if ending_string:
        typed_letters.extend(ending_string)
      typed_string = ''.join(typed_letters)

    # if the backspace key is pressed (unix = \xf7; win = \x08)
    elif key == '\x7f' or key == '\x08':
      typed_letters and typed_letters.pop()
      print("\033[K", end="")
      typed_string = ''.join(typed_letters)

    # allows all keys to be pressed (as opposed to commented out elif and else statement)
    else:
      typed_letters.append(key)
      typed_string = ''.join(typed_letters)
  
  # if the user is entering a high score (limit of 3 letters)
  else:
    # if the backspace key is pressed (unix = \xf7; win = \x08)
    if key == '\x7f' or key == '\x08':
      typed_letters and typed_letters.pop()
      print("\033[K", end="")
      typed_string = ''.join(typed_letters)
    elif len(typed_letters) == 3:
      return
    else:
      typed_letters.append(key)
      typed_string = ''.join(typed_letters)
  
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
  while True:
    key = get_os_name()
    if key == ' ':
      break
    

### ------------MAIN CLI Controller--------------- ###


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
      cls()
      load_save_game()
          
    case "/startfromkey":
      keyStart()

    case "/startsharedgame":
      start_shared_game()

    case "/highscores":
      high_score_lookup()

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
  ## all load options
  print_load_options()
  file_name = user_input(4)

  ## user confirmation 
  print_load_game()
  answer = user_input(0).lower()
  match answer:
    case "y":
      if (start_game_with_key_from_load(file_name) == 1):
        print("Was unable to load the file")
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
    while(True):
      print("Enter title to save game as:")
      userInput = user_input(4)  #asks user for an input
      print(userInput)
      input()
      cls()
      PuzzleStats().get_save_game(userInput)
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
  print_current_puzzle()
  print("Enter your guess.")
  userInput = user_input(2).lower() #asks user for input to match
  if (userInput == ""):
    return True
  elif (userInput[0] != "/"):
    outcome = print_guess_outcome(PuzzleStats().get_check_guess(userInput))
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
      PuzzleStats().ShuffleKey()
      return True

    case "/savegame":
      cls()
      print(f"Enter filename: ")
      file_name = user_input(4)
      cls()
      save_current_game(file_name)
      return True
    
    case "/showall":
      print_all_guesses(PuzzleStats())
      space_out()
      return True
    
    case "/back":
      print_game_save()
      if(user_input(0).lower() == "y"):
        print(f"Enter filename: ")
        file_name = user_input(4)
        cls()
        save_current_game(file_name)
      PuzzleStats().clear()
      return False

    case "/share":
      cls()
      print_shared_key_output(PuzzleStats().encode_puzzle_key())
      space_out()

      return True

    case "/exit":
      cls()
      print_exit()
      return exit_game()
    
    case "/hints":
      cls()
      PuzzleStats().generate_hints()
      print_hint()
      space_out()
      return True
    
    case "/giveup":
      cls()
      print_giveup_confirmation()
      if give_up() != 2:
        PuzzleStats().clear()
        return False
      cls()
      return True
    
    case "/highscores":
      cls()
      high_score_current_puzzle()
      space_out()
      return True

    case _:
      print("Command Not Recognized")
      time.sleep(1)
      return True

# starts a new game from randomly selected puzzle
def start_new_game():
  prep_new_game()
  activeGameLoop()

# Start game from base
def start_game_with_key(key):
  prep_value = prep_game_with_key(key)
 
  if prep_value == 1:
    return 1
  
  activeGameLoop()

# start game from a saved .json file
def start_game_with_key_from_load(file_name):
  ## From Universal Controller
  prep_value = prep_game_from_load(file_name)

  ## Checks to see if a puzzle was loaded correctly 
  if prep_value == 1:
    return 1

  activeGameLoop()
    
# creates a save file (saves current game)
def save_current_game(filename):
  PuzzleStats().get_save_game(filename)

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
  cls()
  print_shared_key_input()
  shared_key = user_input(0).lower()
  
  prep_value = prep_game_from_share(shared_key)
  
  if prep_value == 1:
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
  
  activeGameLoop()


# for when the user considers giving up their current puzzle
def give_up():
  answer = user_input(0).lower()
  match answer:
    # you gave up!
    case "y":
      print_enter_name()
      player_name = user_input(3)
      all_letters = PuzzleStats().pangram
      req_letter = PuzzleStats().required_letter
      player_score = PuzzleStats().score
      insert_or_update_score(player_name, req_letter, all_letters, player_score)

      # prints the high score table
      cls()
      print_pangram_stats(req_letter, all_letters)
      high_score_current_puzzle()
      space_out()

      # asks to generate image
      cls()
      print_generate_image()
      answer = user_input(0).lower()
      match answer:
        case "y":
          generate_new_image(player_name)
        
        case _:
          print("Image not saved..")
          time.sleep(1)

      return 1
    
    # you didn't give up!
    case _:
      return 2


# for when the user wants to search for a high score with their selected pangram and required letter
# accessed through the MAIN MENU
def high_score_lookup():
  while True:
    cls()
    print("Enter the pangram (including the required letter):")
    all_letters = user_input(0).lower()
    if len(set(all_letters)) != 7:
      print("Pangram does not contain 7 unique letters, try again.")
      time.sleep(1)
    else:
      break

  while True:
    cls()
    print(f"\n\tPangram: {all_letters}")
    print("\nEnter the required letter:")
    req_letter = user_input(0).lower()
    if len(req_letter) != 1 or req_letter not in all_letters:
      print("Required letter should be 1 letter within the above pangram.")
      time.sleep(1.5)
    else:
      cls()
      print_pangram_stats(req_letter, all_letters)
      break
  
  print_high_scores(req_letter, set(all_letters))
  space_out()


# for when the user wants to see the high scores for the current puzzle they're playing
# accessed through an ACTIVE PUZZLE
def high_score_current_puzzle():
  all_letters = PuzzleStats().pangram
  req_letter = PuzzleStats().required_letter
  print_high_scores(req_letter, all_letters)

# for when the user wants to generate an image for the current puzzle
def generate_new_image(player_name):
  generateImage(player_name)
  print("Image Saved!")
  time.sleep(1)