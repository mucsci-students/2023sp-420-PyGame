### Main Menu CLI

import random

from game_logic import CheckGuess
from puzzle import Puzzle
from save_system import SaveGame

activeRank = ""
activeProgress = 0
activeScore = 0
activeGuesses = {}
activePuzzleLetters = ""
# currentPuzzle = ""

#Variables to print

###----------------START SCREEN-------------------
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

###----------------CURRENT PUZZLE--------------------------

#playerScore = 0
#playerRank = 0
#playerGuesses = []

currentPuzzle = f'''

Rank: {activeRank} {activeProgress}
Score: {activeScore}
Words Guessed: {activeGuesses}

{activePuzzleLetters}

Commands: /Help /Shuffle /Share /Exit
Guess?
'''
###---------------- MAIN MENU--------------------------

mainMenu = f'''
/NewGame
/LoadGame
/Start From Key
/Help
/Exit
'''

###----------------EXIT----------------
exit = f'''
Confirm exit?
/y
/n
'''

###----------------SAVE GAME----------------
gameSave = f'''
Save Game?
/y
/n
'''
saveAs = f'''
Save as?
/Current
/Blank
'''
###----------------LOAD GAME---------------
load = f'''
Load Game?
/y
/n
'''
gameSelect = f'''
Select Game to Load:
'''
#then  calls a function to get a list of game save files F#

###----------------ENTER 7 LETTER KEY----------------
baseKey = f'''
Enter 7 letters:
'''
###----------------COMMAND/HELP SCREEN----------------
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
/Start from key  /Enter a 7 letter key to start a new puzzle
/Share           /copies the key to your clipboard
/Help            /get instructions and commands 
/Exit            /exits the game
''' 
###------------MAIN MENU SCREEN---------------

def main_menu_handler():
    global currentPuzzle
    runningGame = True

    #loop
    while (runningGame):
      print(mainMenu)
      
      userInput = (input("Select Your Option\n")) # User should select from the options listed
      userInput = userInput.lower()
      match userInput:
        case "/newgame":
          start_new_game()
          activeGameLoop()
          #calls loadNewGame
          #this generates a new puzzle and fills all the variables. Theese will populate the following printCurentPuzzle()

          #prints load gets input then if y prints 
        case "/loadgame":
          #calls loadGame
          loadSaveGame()
          answer = input
          match answer:
            case "/y":
              print(gameSelect)
              #TODO actually get what game file they select, could be a list of numbered options on each new line they select             
            case "/n":
              print(mainMenu)
              #return to main menu screen : or abstracted the last screen
            case _: # if any other command not in the list is entered, then this output will be returned
              print('Command Not Recognized')
              
        case "/start from key":
          keyStart()
          print(sevenKey)
          answer = input
          #CHECK IF input is valid 
          #generate new puzzle based on input
          #populates globals, ect. 
          print(currentPuzzle)

        case "help":
          print(help)
            
        case "exit":
          runningGame = exitCall() 

        case "_":
          print('Command Not Recognized')


###-----CLEAN UP FOR MAIN MENU------

# when user wants to load a saved game
def loadSaveGame():
  # print(<savedGames>) #will display list of saved games, will need to change to actual name
    print("lawl")
    #will have the saved game 
    #TO DO: call function LoadGame
    #TO DO: check to see if game was loaded or not
  

# when user wants to load a game with a key
def keyStart(getKey):
    key = getkey()
    puzzle = generatePuzzle(key)
    startGame()# with key, will need to create startGame

# function to allow user to enter a 7 character key
def getKey():
    while (True):       
        print(baseKey)
        answer = input
              #if validKey(answer) return answer
    else: print('Enter 7 unique letters as a key:')

# function to exit out of current screen
def exitCall():
    while(True):
        print(exit)
        answer = input
        match answer:
            case "/y":
                return False             
            case "/n":
                return True
            case _: 
                print('Command not recognized')

# function to save game
def saveGamePrompt(): 
    print(saveAs)
    while(True):
     userInput = input #asks user for an input
     match userInput:

        case "/current":
         print('Enter title to save current as:')
         answer = input
         SaveGame(answer) #title given will be used within saveCurrentGame, will need to change name
         print(f'{userInput} has been saved.')

        case "blank":
         print['Enter title to save blank as:'] 
         answer = input
         SaveGame(answer)
         print(f'{userInput} has been saved.')

        case _: 
         print('Command not recognized')    

###------------ACTIVE GAME SCREEN---------------
#Loops thru the active game screens
def activeGameLoop():
  loop = True
  while (loop):
    loop = activeGame()

# when an active game is in play
def activeGame():
  global currentPuzzle
  print(currentPuzzle)
  userInput = input("Enter your guess. \n").lower() #asks user for input to match
  if (userInput == ""):
    return True
  elif (userInput[0] != "/"):
    CheckGuess(userInput)
    return True
    # CheckGuess(userInput, puzzle))
  else:
    match userInput:
      case "help":
        print(help)
        return True
        #then return to default state. perhaps call main menu handler???(this would eventually lead to stack overflow  😦  )

      case "shuffle":
        myList = ["a","b","c","d","e","f","g"] #temporary example of a list
        random.shuffle(myList)  
        print(myList)  
        return True

      case "share":
        myList= ["a","b","c","d","e","f","g"] #temporary example of a list
        print(f'Share the following ID:{myList}')
        return True

      case "exit":
        print(f'Would you like to save?{gameSave}')
        answer = input
        match answer:
          case "/y": 
            saveGamePrompt()
            runningGame = exitCall() #temporary variable
          case "/n":
            runningGame = exitCall() 
            return False
          case _:
            print('Command not recognized')
              #should proceed with exiting. if !running game
            return False
      case _:
        print('Command not recognized')
        return True

def start_new_game():
  global activeRank
  global activePuzzleLetters
  global currentPuzzle
  puzzle = Puzzle()
  puzzle.generate_random_puzzle()
  
  # This will need to be shuffled.
  activePuzzleLetters = puzzle.pangram
  currentPuzzle = puzzle.pangram
  print("My letters are: " + activePuzzleLetters)
  activeRank = "Beginner"
    
main_menu_handler()
