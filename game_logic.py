from Database.database import get_word_info, get_random_word, get_word_list

## TEST Global Var
playerScore = 0
playerRank = 0
playerGuesses = ["daha"]
puzzleKey = "dcba"
wordList= {
    "abcd": 1,
    "efgh": 1,
    "ijkl": 1,
    "aaha": 1,
    "ahah": 1
}


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
def CheckValidity(guess):
    global playerScore 
    global playerGuesses
    global wordList

    ## Checks if word is valid
    guess = guess.lower()
    if guess in wordList: 
        playerGuesses.append(guess)
        playerScore = playerScore + wordList[guess]
        return 0 

    ## Word not valid
    return 1

def GenerateRandomPuzzle():
    random_puzzle = get_word_info()
    current_puzzle = get_random_word(random_puzzle)
    print(current_puzzle)
    word_list = get_word_list(current_puzzle[0])
    print(word_list)

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
def InGuesses(guess):
    check = bool
    check = guess.lower() in playerGuesses
    return check

"""
CheckGuess take One Paramater
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
def CheckWordReq(guess):
    ## Req 1: Length 4 or more
    if len(guess) < 4:
        return 100

    ## Req 2: Contains required letter
    if puzzleKey[0] not in guess:
        return 200

    ## Req 3: Contains only given letters
    for letter in set(guess):
        if letter not in puzzleKey:
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
"""
def CheckGuess(guess):
    wordReq = CheckWordReq(guess)
    if wordReq != 0:
        return int(wordReq)
    
    wordGuessed = InGuesses(guess) # Bool
    if wordGuessed:
        return wordGuessed 

    return CheckValidity(guess)


""" 
## _____________________________________
## Test Valid Guesses
## _____________________________________

print('Word Reg Test')
print(str(CheckGuess("dcba")))
print(str(CheckGuess("abc")))
print(str(CheckGuess("abcc")))
print(str(CheckGuess("abde")))

print('In Guesses Test')
print(InGuesses("daha"))
print(InGuesses("dahaa"))

print('Check Validity')
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
GenerateRandomPuzzle()