### Main Menu CLI

import sys

from PuzzleStats import PuzzleStats
from puzzle import Puzzle
from shuffleLetters import ShuffleKey
from Output import *

puzzle = Puzzle()
puzzle_stats = PuzzleStats(-1,"")


###------------MAIN MENU SCREEN---------------

def main_menu_handler():
    print_start_screen()
    
    while (True):
      print_main_menu()
      userInput = (input("Select Your Option\n")).lower() # User should select from the options listed
      match userInput:
        case "/newgame":
          start_new_game()
        
        case "/loadgame":
          load_save_game()
              
        case "/start from key":
          keyStart()

        case "/help":
          print(help)
            
        case "/exit":
          print_exit()
          answer = input().lower()
          exit_game(answer)

        case "_":
          print('Command Not Recognized')


###-----CLEAN UP FOR MAIN MENU------

# when user wants to load a saved game
def load_save_game():
  global puzzle_stats
  print_load_options()
  file_name = input()
  print_load_game()
  answer = input()
  match answer:
    case "/y":
      start_game_with_key(puzzle_stats.LoadGame(file_name))
    case "/n":
      return

    case _: # if any other command not in the list is entered, then this output will be returned
      print('Command Not Recognized')

# when user wants to load a game with a key
def keyStart():
  global puzzle
  loop = 1
  while(loop == 1):
    print_base_input()
    key = input().lower()
    puzzle = puzzle.generate_puzzle_from_base(key)
    if (puzzle == 0):
      loop = 0
    else:
      response = input("Invalid word. Exit? y/n").lower()
      if(response == "y"):
        main_menu_handler()


# function to save game
def saveGamePrompt():
    global puzzle_stats
    global puzzle

    while(True):
      print('Enter title to save game as:')
      userInput = input().lower() #asks user for an input
      puzzle_stats.get_save_game(puzzle, userInput)
      print(f'{userInput} has been saved.')
      return

###------------ACTIVE GAME SCREEN---------------
#Loops thru the active game screens
def activeGameLoop():
  loop = True

  while (loop):
    loop = activeGame()

# when an active game is in play
def activeGame():
  global puzzle
  global puzzle_stats
  print_current_puzzle(puzzle_stats)
  userInput = input("Enter your guess. \n").lower() #asks user for input to match
  
  if (userInput == ""):
    return True
  elif (userInput[0] != "/"):
    print_guess_outcome(puzzle_stats.get_check_guess(userInput, puzzle))
    return True
  else:
    match userInput:
      case "/help":
        print_help()
        return True

      case "/newgame":
        start_new_game()

      case "/shuffle":
        puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram)
        return True

      case "/savegame":
        print(f'Enter filename: ')
        file_name = input().lower()
        save_current_game(file_name)
        return True

      case "/share":
        # myList = ["a","b","c","d","e","f","g"] #temporary example of a list
        print(f'Coming Soon.')
        return True

      case "/exit":
        print_exit()
        answer = input().lower()
        return exit_game(answer)

      case _:
        print('Command not recognized')
        return True

def start_new_game():
  global puzzle
  global puzzle_stats
  puzzle = Puzzle()
  puzzle.generate_random_puzzle()
  shuffled_puzzle = ShuffleKey(puzzle.pangram)
  puzzle_stats = PuzzleStats(puzzle.total_points, shuffled_puzzle)
  activeGameLoop()

def start_game_with_key(key):
  global puzzle
  global puzzle_stats
  puzzle = Puzzle()
  puzzle.generate_puzzle_from_base(key)
  puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram)
  puzzle_stats.maxScore = puzzle.total_points
  activeGameLoop()

def save_current_game(filename):
  global puzzle
  global puzzle_stats
  puzzle_stats.get_save_game(puzzle, filename)

def exit_game(answer):
  match answer:
    case "/y": 
      sys.exit()

    case "/n":
      return True

    case _:
      print('Command not recognized')
        #should proceed with exiting. if !running game
      return True

main_menu_handler()
