### Main Menu CLI

import sys
import os
import time

from PuzzleStats import PuzzleStats
from puzzle import Puzzle
from shuffleLetters import ShuffleKey
from Output import *

puzzle = Puzzle()
puzzle_stats = PuzzleStats(-1,"")


###------------MAIN MENU SCREEN---------------

def main_menu_handler():
    while (True):
      cls()
      print_start_screen()
      print_main_menu()
      userInput = (input("Select Your Option\n")).lower() # User should select from the options listed
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
          print_help()
          input()
            
        case "/exit":
          print_exit()
          answer = input().lower()
          cls()
          exit_game(answer)

        case _:
          print("Command Not Recognized")
          time.sleep(1)


###-----CLEAN UP FOR MAIN MENU------

# when user wants to load a saved game
def load_save_game():
  global puzzle_stats
  print_load_options()
  file_name = input()
  print_load_game()
  answer = input()
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
    print_base_input()
    key = input().lower()
    cls()
    check_value = start_game_with_key(key)
    
    # Turn into custom error call to Output.py with key
    response = input("Invalid word, not a valid pangram. Return to main menu? Y/N \n").lower()
    if(response == "y"):
      main_menu_handler()


# function to save game
def saveGamePrompt():
    global puzzle_stats
    global puzzle

    while(True):
      print("Enter title to save game as:")
      userInput = input().lower() #asks user for an input
      cls()
      puzzle_stats.get_save_game(puzzle, userInput)
      print(f"{userInput} has been saved.")
      return

###------------ACTIVE GAME SCREEN---------------
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
  print_current_puzzle(puzzle_stats)
  userInput = input("Enter your guess. ").lower() #asks user for input to match
  if (userInput == ""):
    return True
  elif (userInput[0] != "/"):
    outcome = print_guess_outcome(puzzle_stats.get_check_guess(userInput, puzzle))
    time.sleep(.5)
    return outcome
  else:
    match userInput:
      case "/help":
        print_help()
        input()
        return True

      case "/shuffle":
        puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
        return True

      case "/savegame":
        print(f"Enter filename: ")
        file_name = input().lower()
        cls()
        save_current_game(file_name)
        return True
      
      case "/showall":
        print_all_guesses(puzzle_stats)
        input()
        return True
      
      case "/back":
        print_game_save()
        if(input().lower() == "y"):
          print(f"Enter filename: ")
          file_name = input().lower()
          cls()
          save_current_game(file_name)
        return False

      case "/share":
        print(puzzle.encode_puzzle_key())
        input("Press any key to continue...")
        return True

      case "/exit":
        print_exit()
        answer = input().lower()
        cls()
        return exit_game(answer)
      
      case "/refresh":
        return True

      case _:
        input("Command not recognized, press any key to continue...")
        return True

def start_new_game():
  global puzzle
  global puzzle_stats
  puzzle = Puzzle()
  puzzle.generate_random_puzzle()
  shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
  puzzle_stats = PuzzleStats(puzzle.total_points, shuffled_puzzle)
  activeGameLoop()

def start_game_with_key(key):
  global puzzle
  global puzzle_stats
  puzzle = Puzzle()
  if(puzzle.generate_puzzle_from_base(key) == 1):
    return 1

  shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
  puzzle_stats = PuzzleStats(puzzle.total_points, shuffled_puzzle)
  # puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
  # puzzle_stats.maxScore = puzzle.total_points
  activeGameLoop()

def start_game_with_key_from_load(save_info):
  global puzzle
  global puzzle_stats
  puzzle = Puzzle()
  if(puzzle.generate_puzzle_from_load(save_info[0], save_info[1]) == 1):
    return 1

  ShuffleKey(puzzle.pangram, puzzle.required_letter)
  activeGameLoop()

def save_current_game(filename):
  global puzzle
  global puzzle_stats
  puzzle_stats.get_save_game(puzzle, filename)

def exit_game(answer):
  match answer:
    case "y": 
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

def start_shared_game():
  global puzzle
  global puzzle_stats
  print_shared_key_input()
  shared_key = input().lower()
  decoded_key = puzzle.decode_puzzle_key(shared_key)
  puzzle = Puzzle()
  
  if(puzzle.generate_puzzle_from_shared(decoded_key[1:], decoded_key[0]) == 1):
    return 1

  puzzle_stats = PuzzleStats(puzzle.total_points, ShuffleKey(puzzle.pangram, puzzle.required_letter))
  puzzle_stats.score = 0
  puzzle_stats.guesses = []
  activeGameLoop()

  

main_menu_handler()
