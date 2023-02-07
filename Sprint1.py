import os
import json
from Database.database import get_word_info, get_random_word, get_word_list


## Global Var for file name, use for checks?
loadedFileName = ''

## Global Var for Player Stats, eventually class attributes?
playerScore = 0
playerRank = 0
playerGuesses = []


""" 
Save Game Takes Five Parameters 
    Players Score; INT
    PLayers Rank; INT
    Players Guesses; List
    puzzleId; STR
    File Name; STR (.json not included)

Function saves the current puzzle state to a 'Saves' directory in a json format
    Case 1: FileName is new; Function creates the new .json file
    Case 2: FileName is already created; Overwrite the .json file with the new data

json format:
{
    "Score": playerScore,
    "Rank": playerRank,
    "Guesses": playerGuesses,
    "GameId": puzzleId 
}
"""

def SaveGame(playerScore, playerRank, playerGuesses, puzzleId, fileName):

    ## Creates the local file path, plus includes the file extension  
    saveFileName = 'Saves/' + fileName + '.json'

    ## Create json object
    saveStat = {
        "Score": playerScore,
        "Rank": playerRank,
        "Guesses": playerGuesses,
        "GameId": puzzleId 
    }
    
    json_object = json.dumps(saveStat, indent=4)

    # Writing to sample.json
    with open(saveFileName, "w") as outfile:
        outfile.write(json_object)

    outfile.close()

"""
CheckFileName Takes One Parameter
    File Name; STR (.json not included)

Function Checks to see if the file name is already in use (case sensitive) and returns a Bool Value
    Case 1: FileName is new; Returns True
    Case 2: FileName is in use; Return Flase 
"""
def CheckFileName(fileName):
    check = bool
    saveGames = os.listdir('Saves')
    check = (fileName + '.json') not in saveGames
    return check

"""
Load Game Takes One Parameter
    File Name: File name; STR (.json not included)

Function loads the game from a given file name; Checks for valid file first
    Case 1: File Name is not valid; returns an error message
    Case 2: File Name is valid; populates Global Var with the players stats and load the puzzle

Returns a '1' if the file name couldn't be found
"""
def LoadGame(fileName):
    ## Check if name is valid
    if CheckFileName(fileName):
        return 1
        
    ## Loads the local file path for the saved game
    saveFile = 'Saves/' + fileName + '.json'
    
    ## reads the json file as a Dict
    with open(saveFile, "r") as openfile:
        saveInfo = json.load(openfile)

    ## Save Stats to global Var
    global playerScore
    global playerRank 
    global playerGuesses
    playerScore = saveInfo["Score"]
    playerRank = saveInfo["Rank"]
    playerGuesses = saveInfo["Guesses"]

    ## Passes the DB Object Id to the Load Puzzle function
    # FUNCTION_LOAD_PUZZLE(saveInfo["GameId"])
    openfile.close()

"""
Load Shared Game Takes one pareamater
    Puzzle Id; STR

Function loads a puzzled ID for shared puzzles, Also reset the player stat values
"""
def LoadSharedGame(puzzleId):
    global playerScore
    global playerRank 
    global playerGuesses
    playerScore = 0
    playerRank = 0
    playerGuesses = []



def GenerateRandomPuzzle():
    random_puzzle = get_word_info()
    current_puzzle = get_random_word(random_puzzle)
    print(current_puzzle)
    word_list = get_word_list(current_puzzle[0])
    print(word_list)


""" 
## __________________________________________________________________________________________
## Test For the Save Game Funciton
## __________________________________________________________________________________________

SaveGame(100, 1, ['a','b','c','d','e'], 'DBObjectId', 'test')
"""

"""
## __________________________________________________________________________________________
## Testing for the Check File Name Function
## __________________________________________________________________________________________

print(CheckFileName('test'))
print(CheckFileName('te'))
"""

""" 
## __________________________________________________________________________________________
## Testin for the Load Game Function
## __________________________________________________________________________________________

testFileName = 'test'
LoadGame(testFileName)
## Print Player Stats (Global Var) if file name is valid
if not CheckFileName(testFileName):
    print('Player Score is: ' + str(playerScore))
    print('Player Rank is: ' + str(playerRank))
    print('Players Guesses are: ' + str(playerGuesses))
 """
GenerateRandomPuzzle()