import os

from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Model.Database.model_highscores import *

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
    print(startingScreen)

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
         /     \     /     \\                         Puzzle Commands
         "  {sec}   >---<   {thi}  "              ______________________________________
         \     /     \     /                          
          >---<   {req}   >---<                /shuffle    /highscores    /help 
         /     \     /     \\               /hints      /sharekey      /commands
         "  {fou}  ">---<   {fif}  "               /showall    /shareimage    /mainmenu
         \     /     \     /               /savegame   /giveup        /exit
          `---<   {six}   >---'
               \     /
                "---"
        
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
             Main Menu Commands
      ________________________________
      
       /newgame           /highscores
       /loadgame          /help
       /startfromkey      /commands
       /startsharedgame   /exit
   
"""
    print(mainMenu)

## Prompts user if they want to exit the game or not from the main menu
def print_exit_menu():
    exit_m = f"""
Are you sure you want to exit? (Y/N)"""
    print(exit_m)


## Prompts user if they want to exit the game or not from their active puzzle
def print_exit_puzzle():
    exit_p = f"""
Are you sure you want to exit? (Any unsaved puzzle progress will be lost!) (Y/N)"""
    print(exit_p)

## Prompts user if he wants to save the game or not
def print_game_save():
    gameSave = f"""

Save Game? (Y/N)"""
    print(gameSave)

## not used
## Prompts user if he wants to load the game or not
def print_load_game():
    load = f"""
    
Load Game? (Y/N)"""
    
    print(load)

## prints screen shwoing all avaiable saves, prompting for input
def print_load_options():
    print("\n  All Saved Games:\n")

    counter = 1
    for option in get_load_options():
        print(f"    [ {counter} ] " + option.replace(".json",""))
        counter += 1

    print("\n\n")

## prints string for when you select start puzzle from Base
def print_base_input():
    print("\nEnter a pangram with seven unique letters: ")

## prints outcome for players guesses to active puzzle
def print_guess_outcome(outcome):
    if(outcome == 69420):
        print_game_over()
        return False
    elif(outcome != 0):
        print("\n\n\tWrong!")
        ## Prints detailed explanation as to why guess is wrong
        get_detailed_response(outcome)
        return True
    else:
        print("\n\n\tCorrect!")
        return True

## prints the generic help screen including game instructions
def print_help():
    help = f"""
    How to Play:
    ~ Create words using letters from the hive and try to get the maximum score. 
    ~ Words must have at least four letters and include the required letter in the center of the hive.
    ~ Letters can be used more than once.
    ~ Words with hyphens, proper nouns, vulgarities, and especially obscure words are not in the word list.
    ~ Score points by correctly guessing words to increase your rating.
    
    Scoring Points:
    ~ 4-letter words are worth 1 point each.
    ~ Longer words earn 1 point per letter.
    ~ Pangrams earn 1 point per letter, plus an additional 7 more points.
    ~ Each puzzle contains at least one “pangram”, which uses every letter in the hive at least once.

    Ranks:                                 Ranking Up:
    Beginner    0%                         ~ Every puzzle has 10 ranks that progress and change based on
    Good Start  2%                           the percentage of the puzzle completed.
    Moving Up   5%                         ~ When you reach the "Queen Bee" rank, you will be able to enter
    Good        8%                           your name to be used for a local high score for the current
    Solid       15%                          puzzle.
    Nice        25%
    Great       40%
    Amazing     50%
    Genius      70%
    Queen Bee   100%
    

    Press the space key to continue...
"""
    print(help)


def print_commands():
    commands = f"""
    Main Menu Commands:
    /newgame          Loads a new game
    /loadgame         Loads a saved game
    /startfromkey     Enter a 7 letter key to start a new puzzle
    /startsharedgame  Copies the key to your clipboard
    /highscores       Searches for the top 10 high scores from a pangram and required letter
    /help             Get instructions and commands
    /exit             Exits the program

    Puzzle Commands:
    /shuffle          Shuffles the outer letters of the hive
    /hints            Shows the hint matrix and a two-letter list
    /showall          Prints a list of correct guessed words
    /savegame         Saves the current state of the game
    /highscores       Searches for the top 10 high scores from a pangram and required letter for the current puzzle
    /sharekey         Shows a sharable key (usable for CLI and GUI)
    /shareimage       Creates a Puzzle Card containing the current statistics of your puzzle
    /giveup           Finishes the game and lets you enter a name for the current puzzle's high score
    /help             Get help on how to play the puzzle
    /commands         Get help on how to use commands in the main menu and puzzle
    /mainmenu         Go back to the main menu screen
    /exit             Exits the program

    
    Press the space key to continue...
""" 
    print(commands)

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
          You Completed the Puzzle!

      
         Press space to continue...
      """
    print(gameOver)

## Prints all the players correct word guesses 
## Layout: four coulmns and N amount of rows depending on the list size
def print_all_guesses(stats):
    print("\n\tWORDS CORRECTLY GUESSED:\n")

    prettyGuesses = "\t\t"
    counter = 0
    for guess in stats.guesses:
        counter += 1
        if len(guess) < 8:
            prettyGuesses = prettyGuesses + guess + "\t\t"
        else:
            prettyGuesses = prettyGuesses + guess + "\t"

        if(counter == 5):
            prettyGuesses = prettyGuesses + "\n\t\t"
            counter = 0

    print(prettyGuesses)
    print("\n\n\tPress the space key to continue...")

## Returns a list of all save files able to load (load options)
def get_load_options():
    options = []
    for file in os.listdir(os.getcwd()):
        if ".json" in file:
            options.append(file)

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
    print("\nEnter a shared game key: ")

## prints out the sharable key
def print_shared_key_output(key):
    print("\n\tYour Share Key is: " + str(key))
    print("\n\tPress the space key to continue...")

def print_hint():
    print("\n\t\t--------- HINTS ---------\n\n")
    print_hint_pangram()
    print_hint_matrix()
    Print_hint_two_Let_Dict()
    print("\n\tPress the space key to continue ...")

def print_hint_pangram():
    puzzle = PuzzleStats()
    print("\tPangram Overview: \n")
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

    print(two_letter_str)


def print_giveup_confirmation():
    giveup = f"""

You are about to GIVE UP your current puzzle. Are you sure you want to GIVE UP? (Y/N)"""
    print(giveup)


def print_enter_name():
    print("Enter a 3 character name for your high score: ")


def print_high_scores(req_letter, all_letters):
    all_scores = get_scores_for_puzzle(req_letter, all_letters)

    print("\n\n\tTOP 10 HIGH SCORES:\n")
    print("\tRANK  PLAYER  SCORE")
    print("\t--------------------")

    rank_num = 1
    for score in all_scores:
        print(f"\t{rank_num}     {score[0]}     {score[1]}")
        rank_num += 1
        if rank_num > 10:
            break

    print("\n\n\tPress the space key to continue...")


def print_pangram_stats(req_letter, all_letters):
    print(f"\n\tPangram: {all_letters}")
    print(f"\tRequired letter: {req_letter}")


def print_generate_image():
    print("\nWould you like to generate an image for your puzzle? (Y/N)")


def print_enable_encryption():
    print("\nWould you like to enable an Encrypted Word List for this puzzle? (Y/N)")