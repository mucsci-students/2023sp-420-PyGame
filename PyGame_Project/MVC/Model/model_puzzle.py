""" 
    Author: Ethan (model_PuzzleStats)
"""
import os, json, random

from PyGame_Project.MVC.Model.Database.model_database import get_random_word_info, get_word_info_from_pangram, get_word_info_from_load
from PyGame_Project.MVC.Model.model_hints import *
from PyGame_Project.MVC.Model.encryption import *

## Super Class
class Puzzle():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.pangram = ""
            cls.required_letter = ""
            cls.total_points = 0
            cls.current_word_list = []

        return cls._instance

    """ 
        Definition: Generates a random puzzle and sets the following values:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_random_puzzle(self):
        random_puzzle = get_random_word_info()
        self.pangram = random_puzzle[0]
        self.required_letter = random_puzzle[1]
        self.total_points = random_puzzle[2]
        self.current_word_list = random_puzzle[3]

    def generate_puzzle_from_load(self, pangram, letter):
        check_value = self.check_valid_word(pangram)
        if(check_value == 1):
            return 1
        else:
            word = get_word_info_from_load(pangram, letter)
            self.pangram = word[0]
            self.required_letter = word[1]
            self.total_points = word[2]
            self.current_word_list = word[3]

    """ 
        Definition: Generates a random puzzle from a given string.
        Returns: None if key is invalid. 
            Sets the following values if a valid key is provided:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_puzzle_from_base(self, key):
        check_value = self.check_valid_word(key)
        if(check_value == 1):
            return 1
        else:
            self.pangram = check_value[0]
            self.required_letter = check_value[1]
            self.total_points = check_value[2]
            self.current_word_list = check_value[3]

    def generate_puzzle_from_shared(self, pangram, letter):
        check_value = self.check_valid_word(pangram)
        if(check_value == 1):
            return 1
        word = get_word_info_from_load(pangram, letter)
        self.pangram = word[0]
        self.required_letter = word[1]
        self.total_points = word[2]
        self.current_word_list = word[3]

    def check_valid_word(self, key):
        key = key.lower()
        unique_char = ''.join(set(key))
        if len(unique_char) != 7:
            return 1
        word = get_word_info_from_pangram(unique_char)
        if len(word) == 0:
            return 1
        return word
    
    def encode_puzzle_key(self):
        encoded_string = ""
        puzzle = self.required_letter + self.pangram
        for char in puzzle:
            encoded_char = chr((ord(char) + 5 - 97) % 26 + 97)
            encoded_string += encoded_char
        return encoded_string
    
    def decode_puzzle_key(self, code):
        decoded_string = ""
        for char in code:
            decoded_char = chr((ord(char) - 5 - 97) % 26 + 97)
            decoded_string += decoded_char
        return decoded_string

## Sub Class
class PuzzleStats(Puzzle):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.score = 0
            cls._instance.rank = 0
            cls._instance.guesses = []
            cls._instance.wordList = []
            cls._instance.shuffled_puzzle = ""
        return cls._instance

    def __init__(self):
        ## Declare the Super class
        super().__init__()

    def clear(self):
        self.score = 0
        self.rank = 0
        self.guesses = []
        self.wordList = []
        self.shuffled_puzzle = ""
        if hasattr(self, 'hints'):
            del self.hints 
        

    ## ----------- Function Block for Checking Guess Req's ----------- ##

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
    def get_check_guess(self, guess):
        wordReq = self.CheckWordReq(guess.lower())
        if wordReq != 0:
            return int(wordReq)
        
        ## return true or false
        wordGuessed = self.InGuesses(guess) # Bool
        if wordGuessed:
            return wordGuessed 
        
        ## Returns 0 if valid; anything else if unvalid
        outcome = self.CheckValidity(guess)
        if self.check_progress():
            return 69420
        else:
            return outcome
        
    """
    CheckWordReg take three Paramaters
        Guess; STR
        Letter; CHAR
        Keyword

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
    def CheckWordReq(self, guess):
        ## Req 1: Length 4 or more
        if len(guess) < 4:
            return 100

        ## Req 2: Contains required letter
        if self.required_letter not in guess:
            return 200

        ## Req 3: Contains only given letters
        for letter in set(guess):
            if letter not in self.pangram:
                return 300

        ## Base Case: Word passes
        return 0
    
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
    CheckGuess take One Paramater
        Guess; STR

    Function checks to see if the passed string is in the pangram word list (ie. Valid)
        Case 1: Guess word is valid; Updates the players score and lsit of correct words
        Case 2: Guess word is invalid; exits the function
    Returns
        0: Word was valid & updated player stats 
        1: Word was invalid (not a real word in list)
    """
    def CheckValidity(self, guess):
        ## Checks if word is valid
        guess = guess.lower()
        for word in self.current_word_list:
            if guess in word:
                self.guesses.append(guess)
                self.score = self.score + self.get_word_points(guess)
                self.RankIndex()
                return 0
        ## Word not valid
        return 1


    ## ----------- Function Block for Rank Info ----------- ##

    """ 
    return_Rank takes in current_Points, and max_Points as parameters, then returns the correspending integer
    to the rank that the player is at.
    Must be between 0.00 and 1.00
    """
    def RankIndex(self):
        if self.score == 0:
            self.rank = 0
            return
        else:
            difference = self.score/self.total_points
            if difference < 0 or difference > 1:
                ## Error
                return 1

            if difference < .02:
                self.rank = 0 #Beginner
            elif difference < .05:
                self.rank = 1 #Good Start
            elif difference < .08:
                self.rank = 2 #Moving up
            elif difference < .15:
                self.rank = 3 #Good
            elif difference < .25:
                self.rank = 4 #Solid
            elif difference < .40:
                self.rank = 5 #Nice
            elif difference < .50:
                self.rank = 6 #Great
            elif difference < .70:
                self.rank = 7 #Amazing
            elif difference < 1:
                self.rank = 8 #Genius
            else:
                self.rank = 9 #Queen Bee

    def get_rank(self):
        rankSteps = ["Beginner","Good Start","Moving Up","Good","Solid","Nice","Great","Amazing","Genius","Queen Bee"]
        return str(rankSteps[self.rank])

    def check_progress(self):
        return (self.score == self.total_points)
    
    def get_word_points(self, word):
        length = len(word)
        # If length of word is 4, worth 1 point.
        if length == 4:
            points = 1
        # If word is a pangram, worth length * 2
        elif len(set(word)) == 7:
            points = length + 7
        # Else word is worth its length
        else:
            points = length
        return points


    ## ----------- Function Block for Save/Load ----------- ##

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
        "CurrentPoints": playerRank,
        "GuessedWords": playerGuesses,
        "PuzzleLetters": puzzleId 
    }
    """
    def  get_save_game(self, fileName, encodeWords = False):
        ## Creates the local file path, plus includes the file extension  
        saveFileName = os.path.join(os.getcwd(), fileName + ".json")

        ## Converting out List-List to List
        WordList = []
        for word in self.current_word_list:
            WordList.append(word[0])
        saveStat = {
                "RequiredLetter": self.required_letter,
                "PuzzleLetters": self.pangram,
                "CurrentPoints": self.score,
                "MaxPoints" : self.total_points,
                "GuessedWords": self.guesses
            }
        ## Create json object
        if(encodeWords):
            WordList = '. '.join(WordList)
            saveStat.update({
                "SecretWordList" : encrypt(WordList),
                "WordList" : []
            })
        else:
        #if not encrypted
            saveStat.update({
                "SecretWordList" : [],
                "WordList" : WordList
            })
        
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
        # print(f'filename is: {fileName}')
        check = bool
        saveGames = os.listdir(os.getcwd())
        check = (fileName + ".json") in saveGames
        return check

    """
    Load Game Takes One Parameter
        File Name: File name; STR (.json not included)

    Function loads the game from a given file name; Checks for valid file first
        Case 1: File Name is not valid; returns an error message
        Case 2: File Name is valid; populates Global Var with the players stats and load the puzzle
        Reads file for secret word list, if this fails, it must be unencrypted, and continues loading.
    Returns a "1" if the file name couldn"t be found
    """
    def LoadGame(self, fileName):
        ## Check if name is valid
        if not self.get_check_file(fileName):
            return 1
            
        ## Loads the local file path for the saved game
        saveFile = os.path.join(os.getcwd(), fileName + ".json")
        
        ## reads the json file as a Dict
        with open(saveFile, "r") as openfile:
            saveInfo = json.load(openfile)


        self.score = saveInfo["CurrentPoints"]
        self.guesses = saveInfo["GuessedWords"]
        self.total_points = saveInfo["MaxPoints"]   
        try:
            self.wordList  = decrypt(saveInfo["SecretWordList"]).split(". ")
        except:
            self.wordList = saveInfo["WordList"]
        
        self.generate_puzzle_from_load(saveInfo["PuzzleLetters"], saveInfo["RequiredLetter"])
        self.RankIndex()

        openfile.close()
        return 0
        

    ## ----------- Function Block for Shuffle ----------- ##

    """
    ShuffleKey function
        current_puzzle; STR

    Function shuffles the letters in the current word when the shuffle command
    is entered.

    Rundown:
        - Converts current word into all lowercase, if not already
        - Checks for valid word length
        - If the word is the puzzleKey (unshuffled word), the required letter is
        at index 0
        - If the word is an already shuffled word, the required letter is index 3
        - Take the required letter out of the word, shuffle the other 6 letters
        - Insert the required letter back into the middle (index = 3)
        - Return the shuffled word
    """
    def ShuffleKey(self):        
        uniqueSet = list(set(self.pangram.lower()))
        uniqueSet = "".join(uniqueSet)

        requiredKey = self.required_letter

        result = uniqueSet.replace(requiredKey, "")
        result = random.sample(result, len(result))
        result.insert(0, requiredKey)
        result = "".join(result)

        self.shuffled_puzzle = result

        return result
    
    def generate_hints(self):
        if not hasattr(self, 'hints'):
            self.hints = Hints(self.current_word_list, self.pangram)

            
