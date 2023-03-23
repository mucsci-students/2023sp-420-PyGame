### Main Menu CLI

import sys, os, time

from model_PuzzleStats import PuzzleStats
from model_puzzle import Puzzle
from model_shuffleLetters import ShuffleKey
from controller_universal import *
from View import *


## ----------- Function Block for Main Menu ----------- ##
""" 
Start the game / main menu
"""
def main_menu_handler():
  while (True):
    cls()

    ## Print start of game (Bee Pic & Main Menu)
    print_start_screen()
    print_main_menu()


    userInput = (input("Select Your Option\n")).lower() 
    ## Input gets passed to a function that will determin what menu to go to next
    main_response(userInput)

""" 
Handles users input from the main menu
Will send to the menu coresponding to the input, if comand not valid will
  """
def main_response(userInput):

  match userInput:
    ## when any menu gets returned it will restart the main menu loop
    case "/newgame":
      start_game_from_random()

    case "/loadgame":
      load_save_game()
          
    case "/gamefromkey":
      game_from_base()

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


## ----------- Function Block for Active Game ----------- ##
""" 
Start the game screen (playable section) 
Loop ends when:
  - the player enters /back
  - the all words are entered (total points collected)
"""
def activeGameLoop():
  loop = True
  while (loop):
    cls()
    loop = activeGame()

""" 
Displays the current puzzle screen, also retrieves players input for guesses
Returns:
  False : if you run /back or if the game is completed
"""
def activeGame():
  ## Prints the puzzle and updated players stats
  print_current_puzzle()

  #asks user for input to match
  userInput = input("Enter your guess. ").lower() 

  if (userInput == ""):
    ## Base Case: Check blank input
    return True
  
  elif (userInput[0] != "/"):
    ## if it donest start with "/" its a guess
    outcome = print_guess_outcome(puzzle_stats.get_check_guess(userInput))
    time.sleep(.5)
    return outcome
  
  else:
    ## Else means its a command so we pas it to a fucntion to determin what that command is and call it
    return active_game_commands(userInput)

"""  
Handles command options for the game (active puzzle) screen and calls the apropiote actions/functions
"""
def active_game_commands(userInput):
  match userInput:
    case "/help":
      print_help()
      input()
      return True

    case "/shuffle":
      puzzle_stats.shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
      return True

    case "/savegame":
      save_game()
    
    case "/showall":
      print_all_guesses(PuzzleStats)
      input()
      return True
    
    case "/back":
      ## Checks if player wants to save before leaving
      print_game_save()

      ## If YES (Y): call the start for saving the game
      if(input().lower() == "y"):
        save_game()
      
      return False

    case "/share":
      print_shared_key_output(puzzle.encode_puzzle_key())
      input()
      return True

    case "/exit":
      print_exit()
      answer = input().lower()
      cls()
      return exit_game(answer)
    
    case "/refresh":
      ## Just to even out the CLI :) 
      return True

    case _:
      ## Handle incomplete commands
      input("Command not recognized, press any key to continue...")
      return True

""" 
Start of the Save command 
  - Asks for user input for filename
  - Then passes it to the back-end save funtion
"""
def save_game():
  print("Enter title to save game as:")
  file_name = input().lower()
  cls()
  puzzle_stats.get_save_game(file_name)


## ----------- Function Block for Random Game ----------- ##
"""  
Starts the game off with a random puzzle and stats cleared
"""
def start_game_from_random():
  ## From Universal File, generates puzzle and stats
  prep_new_game()

  activeGameLoop()


## ----------- Function Block for Load Game ----------- ##
"""  
Prompts for the players input for the file to be loaded
"""
def load_save_game():
  ## Print all save games found in the saves directory & prompts for files name to load
  print_load_options()
  file_name = input()

  ## User Confirmation 
  print_load_game()
  answer = input()

  match answer:
    case "y":
      ## If unalbe to load corectly, will diplay message
      if (prep_game_from_load(file_name) == 1):
        print("Was unalbe to Load the File")

    case "n":
      cls()
    
    # if any other command not in the list is entered, then this output will be returned
    case _:       
      print("Command Not Recognized")

"""  
Generates the puzzle and player stats from the load file
  - returns 1 if there was a problem generating the puzzle and stats
"""
def start_game_from_load(file_name):
  ## From Universal Controller
  prep_value = prep_game_from_load(file_name)

  ## Checks to see if a puzzle was loaded correctly 
  if type(prep_value) == int:
    return 1

  activeGameLoop()


## ----------- Function Block for Starting Game from Key ----------- ##
"""  
Handles the strt of loading game from a inputed key 
- Loops until a useful key is given
"""
def game_from_base():
  check_value = 1

  ## Will loop through until a valid option is given
  while(check_value == 1):
    print_base_input()

    key = input().lower()
    cls()

    """  
    Calls the functinon to check if the inputed key can be used then calls active game if it is valid
    """
    check_value = start_game_with_key(key)
    
    ## Checks if the user would like to go back to the main menu
    if check_value == 1:
      response = input("Invalid option. Return to main menu? Y/N \n").lower()
      if(response == "y"):
        main_menu_handler()

"""  
Gets the game ready for the inputed key
Returns:
  - 1: if the puzzle was unable to generate

"""
def start_game_with_base(key):
  ## From uUniversal Controller
  prep_value = prep_game_with_base(key)

  ## Checks to see if it was able to generate properly 
  if type(prep_value) == int:
    return 1
  
  activeGameLoop()


## ----------- Function Block for Starting Game from Shared Key ----------- ##
"""  
Promts for a shared key, If the key is valid start the game, otherwise start again
"""
def start_shared_game():
  global puzzle
  global puzzle_stats
  cls()
  print_shared_key_input()
  shared_key = input().lower()
  
  prep_value = prep_game_from_share(shared_key)
  
  if type(prep_value) == int:
    ## Input was invalid ask what they want to do next
    print("Invalid Code Input, Press any key to continue...")
    print("Press 'N' to quit to main menu...")
    user_input = input()

    ## Handles the input
    if user_input.lower() == 'n':
      main_menu_handler()
    return start_shared_game()

  ## Base Everything passed, start game screen
  activeGameLoop()

## ----------- Function Block for OTHER ----------- ##
""" 
Function to clear the console after a user input is taken in 
  - Works for both Mac and Win
""" 
def cls():
  os.system("cls" if os.name=="nt" else "clear") # now, to clear the screen

"""  
Closes the terminal
  - Works for both Mac and Win
"""
def exit_game(answer):
  match answer:
    case "y": 
      sys.exit()

    case "n":
      return True

    case _:
      ## Base Case: Player doenst enter Y or N, assume No
      return True




