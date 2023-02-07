### Main Menu CLI

import random

#Variables to print

###----------------START SCREEN-------------------
startingscreen = f"""
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

curentPuzzle = f'''

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
sevenKey = f'''
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

def main_menu_handler(currentPuzzle):
    runningGame = false
    #loop
    
    while (runningGame):
        print(mainMenu)
        userInput = (input("Select Your Option")) # User should select from the options listed
        match userInput:
            case ['/NewGame']:
            #calls loadNewGame
            #this generates a new puzzle and fills all the variables. Theese will populate the following printCurentPuzzle()
                print(currentPuzzle)
            #prints load gets input then if y prints 
            case ['/LoadGame']:
            #calls loadGame
              loadSaveGame()
              answer = input
              match answer:
                  case ['/y']:
                      print(gameSelect)
                          #TODO actually get what game file they select, could be a list of numbered options on each new line they select             
                  case ['/n']:
                      print(mainMenu)
                  #return to main menu screen : or abstracted the last screen
                  case _: # if any other command not in the list is entered, then this output will be returned
                      print('Command Not Recognized')
              
            case['/Start From Key']:
              keyStart()
              print(sevenKey)
              answer = input
              #CHECK IF input is valid 
              #generate new puzzle based on input
              #populates globals, ect. 
              print(currentPuzzle)

            case['/Help']:
              print(help)
            
            case['/Exit']:
              runningGame = exitCall() 

            case _:
              print('Command Not Recognized')


###-----CLEAN UP FOR MAIN MENU------

# when user wants to load a saved game
def loadSaveGame():
  print(<savedGames>) #will display list of saved games, will need to change to actual name
    #will have the saved game 

# when user wants to load a game with a key
def keyStart():
    key = getkey()
    puzzle = generatePuzzle(key)
    startGame()# with key

# function to allow user to enter a 7 character key
def getKey():
    while (True):       
        print(sevenKey)
        answer = input
              #if validKey(answer) return answer
    else: print('Enter 7 unique letters as a key:')

# function to exit out of current screen
def exitCall():
    while(True):
        print(exit)
        answer = input
        match answer:
            case ['/y']:
                return False             
            case ['/n']:
                return True
            case _: 
                print('Command not recognized')

# function to save game
def saveGamePrompt(): 
    print(saveAs)
    while(True):
     userInput = input #asks user for an input
     match userInput:

        case['/Current']:
         print('Enter title to save current as:')
         answer = input
         saveCurrentGame(answer) #title given will be used within saveCurrentGame, will need to change name
         print(f'{userInput} has been saved.')

        case['/Blank']:
         print['Enter title to save blank as:'] 
         answer = input
         saveCurrentGame(answer)
         print(f'{userInput} has been saved.')

        case _: 
         print('Command not recognized')    

###------------ACTIVE GAME SCREEN---------------

# when an active game is in play
def activeGame(currentPuzzle):
    print(currentPuzzle)
    userInput = input #asks user for input to match
    if(userInput[0] == '/'):
        match userInput:
         case ['/Help']:
            print(help)
            #then return to default state. perhaps call main menu handler???(this would eventually lead to stack overflow  😦  )

         case ['/Shuffle']:
            myList= ["a","b","c","d","e","f","g"] #temporary example of a list
            random.shuffle(myList)  
            print(myList)  

         case ['/Share']:
            myList= ["a","b","c","d","e","f","g"] #temporary example of a list
            print(f'Share the following ID:{myList}')

         case ['/Exit']:
             print(f'Would you like to save?{gameSave}')
             answer = input
             match answer:
              case['/y']: 
                saveGamePrompt()
                runningGame = exitCall() #temporary variable
              case['/n']:
                runningGame = exitCall() 
              case _:
                print('Command not recognized')
              #should proceed with exiting. if !running game
         case _: 
             print('Command not recognized')
             
    