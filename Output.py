import os

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
Parameters: 2
    Puzzle Stats; class
    requiredLetter; str
    Remaining Letters; list
"""
def print_current_puzzle(stats):
    prettyGuesses = get_pretty_guesses(stats)
        
        
    currentProgress = f'''
        Rank: {stats.get_rank()}   
        Score: {stats.score} / {stats.maxScore} 
        Words Guessed: {prettyGuesses}
        
        Required Letter: {stats.shuffled_puzzle[3]}
        Optional Letters: {stats.shuffled_puzzle[0] + ' - ' + stats.shuffled_puzzle[1] + ' - ' + stats.shuffled_puzzle[2] + ' - ' + stats.shuffled_puzzle[4] + ' - ' + stats.shuffled_puzzle[5] + ' - ' + stats.shuffled_puzzle[6]}

        Commands: /Help /Shuffle /ShowAll /Back /Share /SaveGame /Exit
        Guess?
        '''
    print(currentProgress)

def get_pretty_guesses(stats):
    prettyGuesses = ''
    counter = 0
    if len(stats.guesses) > 3:
        while counter != -4:
            counter = counter - 1
            prettyGuesses = prettyGuesses + stats.guesses[counter] + " "
    else:
        for guess in stats.guesses:
            prettyGuesses = prettyGuesses + guess + " "
    return prettyGuesses

def print_main_menu():
    mainMenu = f'''
/NewGame
/LoadGame
/StartFromKey
/Help
/Exit
'''
    print(mainMenu)

def print_exit():
    exit = f'''
Confirm exit?
y
n
'''
    print(exit)

def print_game_save():
    gameSave = f'''
Save Game?
y
n
'''
    print(gameSave)

def print_load_game():
    load = f'''
Load Game?
y
n
'''
    print(load)

def print_load_options():
    print('All Saved Games:')
    for option in get_load_options():
        print('-- ' + option.replace('.json',''))
    print('\n(Type just the name in):')
    print('\nSelect Game to load:')

def print_base_input():
    print('Enter a 7 letter Panagram: ')


def print_guess_outcome(outcome):
    if(outcome == 69420):
        print_game_over()
        return False
    elif(outcome != 0):
        print("\n\tWrong!")
        return True
    else:
        print("\n\tCorrect!")
        return True

def print_help():
    help = f'''

Instructions

Create words using letters from the hive and try to get the maximum score. 
Words must have at least four letters and include the center letter in brackets. 
Letters can be used more than once. 
Words with hyphens, proper nouns, vulgarities, and especially obscure words are not in the word list. 
Score points to increase your rating. 
4-letter words are worth 1 point each.
Longer words earn 1 point per letter. 
Each puzzle includes at least one “pangram” which uses every letter. 
These are worth 7 extra points!
Feedback/File Bug Report: <custom url>

Commands
/NewGame         /Loads a new game
/LoadGame        /Loads a saved game
/StartFromKey    /Enter a 7 letter key to start a new puzzle
/Share           /copies the key to your clipboard
/Help            /get instructions and commands 
/Exit            /exits the game

Enter any key to continue...
''' 
    print(help)

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
      You Completed the Puzzle                      
      """
    print(gameOver)

def get_load_options():
        options = os.listdir('Saves')
        return options

def print_all_guesses(stats):
    print("\t SHOW ALL GUESSES")
    prettyGuesses = '\t\t'
    counter = 0
    for guess in stats.guesses:
        counter += 1
        prettyGuesses = prettyGuesses + guess + ", "
        if(counter == 4):
            prettyGuesses = prettyGuesses + "\n\t\t"
            counter = 0
    print(prettyGuesses)