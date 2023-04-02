import os
import sys

from model_puzzle import *

## prints the start up "Loading" screen
def print_start_screen():
    startingScreen = f"""
          \             /
           \   o ^ o   /            
            \ (     ) /
 ____________(%%%%%%%)____________      
(     /   /  )%%%%%%%(  \   \     )          
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)        
            /(       )\ 
          /   (%%%%%)   \ 
               (%%%) 
                 !                      
    Spelling Bee Game by PyGame
      """
    print (startingScreen)

"""
Prints the Current Puzzle menu, using current passed stats.

Parameters: 2
    Puzzle Stats; class
    requiredLetter; str
    Remaining Letters; list
"""
def print_current_puzzle():
    puzzle = PuzzleStats()
    
    prettyGuesses = get_pretty_guesses(puzzle.guesses)
    # variables to store each letter 

    req = puzzle.shuffled_puzzle[0]
    fir = puzzle.shuffled_puzzle[3]
    sec = puzzle.shuffled_puzzle[1]
    thi = puzzle.shuffled_puzzle[2]
    fou = puzzle.shuffled_puzzle[4]
    fif = puzzle.shuffled_puzzle[5]
    six = puzzle.shuffled_puzzle[6]

    currentProgress = f"""
    Puzzle:
        Rank: {puzzle.get_rank()}   
        Score: {puzzle.score} / {puzzle.total_points} 
        Words Guessed: {prettyGuesses}
        
                ,---.
               /     \\
          ,---<   {fir}   >---.
         /     \     /     \\
         "  {sec}  ">---<"  {thi}  "
         \     /     \     /
          >---<   {req}   >---<
         /     \     /     \\
         "  {fou}  ">---<"  {fif}  "
         \     /     \     /
          `---<   {six}   >---'
               \     /
                "---"

               Commands
         ---------------------
          /help      /shuffle 
          /back      /showall 
          /share     /savegame 
          /exit      /hints
        
        """
    print(currentProgress)

"""
Turns players list of valid guesses into a string with the last 4 entered words

One paramater:
    guesses, LIST

Returns a string of four last entered guesses
"""
def get_pretty_guesses(guesses):
    prettyGuesses = ""
    counter = 0
    ## If the list length is longer than 3, string has last four entered words
    if len(guesses) > 3:
        while counter != -4:
            counter = counter - 1
            prettyGuesses = prettyGuesses + guesses[counter] + " "

    ## Else; string has all words entered so far
    else:
        for guess in guesses:
            prettyGuesses = prettyGuesses + guess + " "
    return prettyGuesses

## prints the main start up menu
def print_main_menu():
    mainMenu = f"""
Main Menu
    /newgame
    /loadgame
    /startfromkey
    /startsharedgame
    /help
    /exit
"""
    print(mainMenu)

## Promtps user if he wants to exit the game or not
def print_exit():
    exit = f"""
Confirm exit?
Y
N
"""
    print(exit)

## Promtps user if he wants to save the game or not
def print_game_save():
    gameSave = f"""

Save Game?
Y
N
"""
    print(gameSave)

## Promtps user if he wants to load the game or not
def print_load_game():
    load = f"""
    
Load Game?
Y
N
"""
    print(load)

## prints screen shwoing all avaiable saves, prompting for input
def print_load_options():
    print("All Saved Games:")
    for option in get_load_options():
        print("-- " + option.replace(".json",""))
    print("\n(Type just the name in):")
    print("\nSelect Game to load:")

## prints string for when you select start puzzle from Base
def print_base_input():
    print("Enter a panagram with seven unique letters: ")

## prints outcome for players guesses to active puzzle
def print_guess_outcome(outcome):
    if(outcome == 69420):
        print_game_over()
        return False
    elif(outcome != 0):
        print("\n\tWrong!")
        ## Prints detailed explanation as to why guess is wrong
        get_detailed_response(outcome)
        return True
    else:
        print("\n\tCorrect!")
        return True

## prints the generic help screen including game instructions
def print_help():
    help = f"""

Instructions

~ Create words using letters from the hive and try to get the maximum score. 
~ Words must have at least four unique letters and include the center letter in brackets.
~ All optional letters will be surrounding the required center letter.   
~ Letters can be used more than once. 
~ Words with hyphens, proper nouns, vulgarities, and especially obscure words are not in the word list. 
~ Score points to increase your rating.
~ 4-letter words are worth 1 point each.
~ Longer words earn 1 point per letter. 
~ Each puzzle includes at least one “pangram” which uses every letter, which are worth double points.

Main Menu Commands:
/newgame          Loads a new game
/loadgame         Loads a saved game
/startfromkey     Enter a 7 letter key to start a new puzzle
/startsharedgame  Copies the key to your clipboard
/help             Get instructions and commands 
/exit             Exits the program

In-Game Commands:
/help             Get instructions and commands
/back             Go back to the main menu screen
/share            Shows a sharable key (usable for CLI and GUI)
/exit             Exits the program
/shuffle          Shuffles the outer letters of the hive
/showall          Prints a list of correct guessed words
/savegame         Saves the current state of the game
/hints            Shows the hint matrix and a two-letter list

Press the space key to continue...
""" 
    print(help)

## prints the nice message when the puzzle is completed
def print_game_over():
    gameOver = f"""
          \             /
           \   o ^ o   /            
            \ (     ) /
 ____________(%%%%%%%)____________      
(     /   /  )%%%%%%%(  \   \     )          
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)        
            /(       )\ 
          /   (%%%%%)   \ 
               (%%%) 
                 !
              Congrats!
      You Completed the Puzzle                      
      """
    print(gameOver)

## Prints all the players correct word guesses 
## Layout: four coulmns and N amount of rows depending on the list size
def print_all_guesses(stats):
    print("\n\t WORDS CORRECTLY GUESSED:")
    prettyGuesses = "\t\t"
    counter = 0
    for guess in stats.guesses:
        counter += 1
        prettyGuesses = prettyGuesses + guess + ", "
        if(counter == 4):
            prettyGuesses = prettyGuesses + "\n\t\t"
            counter = 0
    print(prettyGuesses)
    print("\t Press the space key to continue...")

## Returns a list of all save files able to load (load options)
def get_load_options():
    save_path = ''
    for path in sys.path:
        if "Saves" in path:
            save_path = path
            break
    options = os.listdir(save_path)
    return options

## prints a detatiled "Invalid Guess" given a passed value from print_guess_outcome()
"""
    All Possible Outcome Values: 
        0: Word was valid & updated player stats *Checked in print_guess_outcome*
        1: Word was invalid (not a word in pangram list)
        False: Word was not prev. guessed
        100: Word needs to be 4 or more letters in length
        200: Word needs to contain the required letter
        300: Word can only contain letters from pangram
        69420: Player guessed all words. Game over *Checked in print_guess_outcome*
"""
def get_detailed_response(outcome):
    ## "Error return value" matches to a relevant message *Prints in CLI*

    ## Checks the bool value
    if type(outcome) == bool:
        print("\n\t... Guessed word was already used ...")
        return 
    
    ## Checks int values
    match outcome:
        case 1:
            print("\n\t... Input is not in the Scrabble Dictionary ...")
        case 100:
            print("\n\t... Input is shorter than four letters ...")
        case 200:
            print("\n\t... Input does not contain the required letter ...")
        case 300:
            print("\n\t... Input has non-given letters ...")
    
def print_shared_key_input():
    print("Enter a shared game key: ")

## prints out the sharable key
def print_shared_key_output(key):
    print("\n\tYour Share Key is: " + str(key))
    print("\n\tPress the space key to continue...")

def print_hint():
    print("\n\t\t--------- HINTS ---------\n\n")
    print_hint_pangram()
    print_hint_matrix()
    Print_hint_two_Let_Dict()
    print("\n\t  ... Press the space key to continue ...")

def print_hint_pangram():
    puzzle = PuzzleStats()
    print("\tPangram Over-view: \n")
    print(f"\t -> Center letter is {puzzle.shuffled_puzzle[0].upper()}; Remaining letters are: {puzzle.shuffled_puzzle[1:7].upper()}")
    print(f"\t -> Words: {len(puzzle.current_word_list)}; Points: {puzzle.total_points}")
    rem_words = len(puzzle.current_word_list) - len(puzzle.guesses)
    rem_points = puzzle.total_points - puzzle.score
    print(f"\t -> Remaining Words: {rem_words}; Remaining Points: {rem_points}")


def print_hint_matrix():
    print("\n\n\tHint Matrix: \n")
    print("\t\t", end = "")

    ## prints the first row, then puts a space after
    print('\n\t\t'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in PuzzleStats().hints.two_d_array[0:1]]))
   
    print("\n\t\t", end = "")

    ## prints the remaining matrix (by row)
    print('\n\t\t'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in PuzzleStats().hints.two_d_array[1:]]))
    

def Print_hint_two_Let_Dict():
    print("\n\n\tTwo Letter List: \n")

    two_letter_dict = PuzzleStats().hints.two_letter_dict
    two_letter_str = ""
    count = 0
    for key in two_letter_dict:
        two_letter_str = two_letter_str + (f"\t\t{key.upper()} - {two_letter_dict[key]}")
        if count == 1:
            two_letter_str = two_letter_str + "\n"
            count = 0   
        else:
            two_letter_str = two_letter_str + "\t"
            count += 1

    print (two_letter_str)