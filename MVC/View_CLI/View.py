import os

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
def print_current_puzzle(stats):
    prettyGuesses = get_pretty_guesses(stats.guesses)
    # variables to store each letter 
    req = stats.shuffled_puzzle[3]
    fir = stats.shuffled_puzzle[0]
    sec = stats.shuffled_puzzle[1]
    thi = stats.shuffled_puzzle[2]
    fou = stats.shuffled_puzzle[4]
    fif = stats.shuffled_puzzle[5]
    six = stats.shuffled_puzzle[6]

    currentProgress = f"""
    Puzzle:
        Rank: {stats.get_rank()}   
        Score: {stats.score} / {stats.maxScore} 
        Words Guessed: {prettyGuesses}
        
                ,---.
               /     \\
          ,---<   {fir}   >---.
         /     \     /     \\
         "  {sec}  "     "  {thi}  "
         \     /     \     /
          >---<   {req}   >---<
         /     \     /     \\
         "  {fou}  "     "  {fif}  "
         \     /     \     /
          `---<   {six}   >---'
               \     /
                "---"

               Commands
         ---------------------
          /Help      /Shuffle 
          /Back      /ShowAll 
          /Share     /SaveGame 
          /Exit      /Refresh
        
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
    /NewGame
    /LoadGame
    /StartFromKey
    /StartSharedGame
    /Help
    /Exit
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

Create words using letters from the hive and try to get the maximum score. 
Words must have at least four letters and include the center letter in brackets.
All optional letters will be surrounding the required center letter.   
Letters can be used more than once. 
Words with hyphens, proper nouns, vulgarities, and especially obscure words are not in the word list. 
Score points to increase your rating. 
4-letter words are worth 1 point each.
Longer words earn 1 point per letter. 
Each puzzle includes at least one “pangram” which uses every letter. 
These are worth double the points!

Commands
/NewGame         /Loads a new game
/LoadGame        /Loads a saved game
/StartFromKey    /Enter a 7 letter key to start a new puzzle
/Share           /copies the key to your clipboard
/Help            /get instructions and commands 
/Exit            /exits the game

Enter any key to continue...
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
    print("\t SHOW ALL GUESSES")
    prettyGuesses = "\t\t"
    counter = 0
    for guess in stats.guesses:
        counter += 1
        prettyGuesses = prettyGuesses + guess + ", "
        if(counter == 4):
            prettyGuesses = prettyGuesses + "\n\t\t"
            counter = 0
    print(prettyGuesses)
    print("\t Enter any key to continue...")

## Returns a list of all save files able to load (load options)
def get_load_options():
        options = os.listdir("Saves")
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
    print("\tYour Share Key is: " + str(key))
    print("\n\tPress any key to continue...")
