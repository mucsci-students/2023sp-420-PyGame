"""
Author: Ethan Wright
    - Combines game_logic.py
    - Combines Player_Rank
"""
import os
import json

class PuzzleStats():

    def __init__(self, max_score, shuffled_puzzle):
        ## Total amount of points recieved from valid guesses
        self.score = 0
        ## Holds the index of the rank the player is at
        self.rank = 0
        ## All valid word guesses that has given points
        self.guesses = []
        ## Total amount of points in the puzzle
        self.maxScore = max_score
        ## Current puzzle layout
        self.shuffled_puzzle = shuffled_puzzle 

    ## ----------------------------------------------------------
    ## Start of Class functions

    """
    CheckGuess take One Paramater
        Guess; STR

    Function checks to see if the passed string is in the pangram word list (ie. Valid)
        Case 1: Guess word is valid; Updates the players score and lsit of correct words
        Case 2: Guess word is invalid; exits the function
    Returns
        0: Word was valid & updated player stats 
        1: Word was invalid (not a real word in list)
    """
    def CheckValidity(self, guess, wordList):
        ## Checks if word is valid
        guess = guess.lower()
        for word in wordList:
            if guess in word:
                self.guesses.append(guess)
                self.score = self.score + self.get_word_points(guess)
                self.RankIndex()
                return 0 
        ## Word not valid
        return 1

    """
    CheckGuess take One Paramater
        Guess; STR

    Function checks to see if the passed string is in the pangram word list (ie. Valid)
        Case 1: Word was already guessed
        Case 2: Word was not prev. guessed

    Returns
        True: Word was already guessed
        False: Word was not prev. guessed
    """
    def InGuesses(self, guess):
        check = bool
        check = guess.lower() in self.guesses
        return check

    """
    CheckWordReg take One Paramater
        Guess; STR

    Function checks to see if the guess word meets all pre conditions
        Case 1: Word needs to be 4 or more letters in length
        Case 2: Word needs to contain the required letter
        Case 3: Word can only contain letters from pangram

    Returns
        0: Passed all Req
        100: Word needs to be 4 or more letters in length
        200: Word needs to contain the required letter
        300: Word can only contain letters from pangram
    """
    def CheckWordReq(self, guess, letter, keyWord):
        ## Req 1: Length 4 or more
        if len(guess) < 4:
            return 100

        ## Req 2: Contains required letter
        if letter not in guess:
            return 200

        ## Req 3: Contains only given letters
        for letter in set(guess):
            if letter not in keyWord:
                return 300

        ## Base Case: Word passes
        return 0

    """
    CheckGuess take One Paramater
        Guess; STR

    Function checks to see if word is valid, updates player stats if needed

    Returns
        0: Word was valid & updated player stats 
        1: Word was invalid (not a word in pangram list)
        True: Word was already guessed
        False: Word was not prev. guessed
        100: Word needs to be 4 or more letters in length
        200: Word needs to contain the required letter
        300: Word can only contain letters from pangram
        69420: Player guessed all words. Game over
    """
    def get_check_guess(self, guess, puzzleInfo):
        wordReq = self.CheckWordReq(guess, puzzleInfo.required_letter, puzzleInfo.pangram)
        if wordReq != 0:
            return int(wordReq)
        
        wordGuessed = self.InGuesses(guess) # Bool
        if wordGuessed:
            return wordGuessed 
           
        ## Returns 0 if valid; anything else if unvalid
        outcome = self.CheckValidity(guess, puzzleInfo.current_word_list)
        if self.check_progress():
            return 69420
        else:
            return outcome
    
    """ 
    return_Rank takes in current_Points, and max_Points as parameters, then returns the correspending integer
    to the rank that the player is at.
    Must be between 0.00 and 1.00
    """
    def RankIndex(self):
        difference = self.score/self.maxScore
        if difference < 0 or difference > 1:
            ## Error
            return 1

        if difference < .03:
            self.rank = 0 #Beginner
        elif difference < .07:
            self.rank = 1 #Novice
        elif difference < .12:
            self.rank = 2 #Okay
        elif difference < .23:
            self.rank = 3 #Good
        elif difference < .35:
            self.rank = 4 #Solid
        elif difference < .56:
            self.rank = 5 #Nice
        elif difference < .72:
            self.rank = 6 #Great
        elif difference < .92:
            self.rank = 7 #Amazing
        else:
            self.rank = 8 #Genius

    def get_rank(self):
        rankSteps = ["Beginner","Novice","Okay","Good","Solid","Nice","Great","Amazing","Genius"]
        return str(rankSteps[self.rank])

    def check_progress(self):
        return (self.score == self.maxScore)

    def get_word_points(self, word):
        length = len(word)
        # If length of word is 4, worth 1 point.
        if length == 4:
            points = 1
        # If word is a pangram, worth length * 2
        elif length == len(set(word)):
            points = (length)*2
        # Else word is worth its length
        else:
            points = length
        return points
            

    """ 
    Save Game Takes Five Parameters 
        Players Score; INT
        PLayers Rank; INT
        Players Guesses; List
        puzzleId; STR
        File Name; STR (.json not included)

    Function saves the current puzzle state to a "Saves" directory in a json format
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
    def get_save_game(self, puzzleInfo, fileName):

        ## Creates the local file path, plus includes the file extension  
        saveFileName = "Saves/" + fileName + ".json"

        ## Create json object
        saveStat = {
            "Score": self.score,
            "Rank": self.rank,
            "Guesses": self.guesses,
            "Shuffle" : self.shuffled_puzzle,
            "Letter" : puzzleInfo.required_letter,
            "GameId": puzzleInfo.pangram,
            "MaxPoints" : puzzleInfo.total_points
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
    def get_check_file(self, fileName):
        check = bool
        saveGames = os.listdir("Saves")
        check = (fileName + ".json") not in saveGames
        return check

    """
    Load Game Takes One Parameter
        File Name: File name; STR (.json not included)

    Function loads the game from a given file name; Checks for valid file first
        Case 1: File Name is not valid; returns an error message
        Case 2: File Name is valid; populates Global Var with the players stats and load the puzzle

    Returns a "1" if the file name couldn"t be found
    """
    def LoadGame(self, fileName):
        ## Check if name is valid
        if self.get_check_file(fileName):
            return 1
            
        ## Loads the local file path for the saved game
        saveFile = "Saves/" + fileName + ".json"
        
        ## reads the json file as a Dict
        with open(saveFile, "r") as openfile:
            saveInfo = json.load(openfile)

        self.score = saveInfo["Score"]
        self.rank = saveInfo["Rank"]
        self.guesses = saveInfo["Guesses"]
        self.maxScore = saveInfo["MaxPoints"]
        self.shuffled_puzzle = saveInfo["Shuffle"]

        openfile.close()

        ## Passes the DB Object Id to the Load Puzzle function
        return saveInfo["GameId"], saveInfo["Letter"]


""" 
## _____________________________________
## Test Valid Guesses (get_check_guess)
## _____________________________________

print("Word Reg Test")
print(str(CheckGuess("dcba")))
print(str(CheckGuess("abc")))
print(str(CheckGuess("abcc")))
print(str(CheckGuess("abde")))

print("In Guesses Test")
print(InGuesses("daha"))
print(InGuesses("dahaa"))

print("Check Validity")
## Test: Add valid word to player guess list & points
print (CheckValidity("efgh"))
print (str(playerGuesses))

## Test: Word is invalid
print(CheckValidity("aaaa"))
print (str(playerGuesses))

 ## Test: Player Score
print (playerScore)
print (CheckValidity("efgh"))
print (str(playerGuesses))
print (playerScore)
print(CheckValidity("aaaa"))
print (str(playerGuesses))
print (playerScore)
print (CheckValidity("abcd"))
print (str(playerGuesses))
print (playerScore)
"""

""" 
## __________________________________________________________________________________________
## Test For the Save Game Funciton
## __________________________________________________________________________________________

SaveGame(100, 1, ["a","b","c","d","e"], "DBObjectId", "test")
"""

"""
## __________________________________________________________________________________________
## Testing for the Check File Name Function
## __________________________________________________________________________________________

print(CheckFileName("test"))
print(CheckFileName("te"))
"""

""" 
## __________________________________________________________________________________________
## Testin for the Load Game Function
## __________________________________________________________________________________________

testFileName = "test"
LoadGame(testFileName)
## Print Player Stats (Global Var) if file name is valid
if not CheckFileName(testFileName):
    print("Player Score is: " + str(playerScore))
    print("Player Rank is: " + str(playerRank))
    print("Players Guesses are: " + str(playerGuesses))
 """