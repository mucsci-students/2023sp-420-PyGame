import os, sys, pytest

if os.name!="nt": 
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Controller")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model/Database")
else:
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Controller")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model\\Database")



from model_puzzle import *
from controller_universal import *

## default puzzle generation for testing 
pytest.fixture
def puzzleGen():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    prep_game_from_share(shareable_key)
    

## ---------- Testing vaid user guesses ---------- ##
def test_valid_guessed_word():
    puzzleGen()
    return_val = PuzzleStats().get_check_guess("meat")

    ## if guessed word is valid, the function should return 0
    ## check to see that only one thing was added in the guesses list
    ## the correct word should be added in guesses list
    assert return_val == 0 and len(PuzzleStats().guesses) == 1 and ("meat" in PuzzleStats().guesses)


## ---------- Testing InGuesses() ---------- ##
def test_valid_guessed_word():
    puzzleGen()
    return_val = PuzzleStats().get_check_guess("meat")
    return_val = PuzzleStats().get_check_guess("meat")
    assert return_val == True


## ------------- testing CheckWordReg() ------------- ##

def test_invalid_guessed_word_req_v1():
    ## word less than 4 letters
    puzzleGen()
    return_val = PuzzleStats().get_check_guess("mea")

    ## if guessed word is less than 4, the function should return 100
    assert return_val == 100

def test_invalid_guessed_word_req_v2():
    ## word doesnt contain req. letter
    puzzleGen()

    ## this puzzle has T as req letter
    return_val = PuzzleStats().get_check_guess("meaa")

    ## if guessed word is less than 4, the function should return 200
    assert return_val == 200

def test_invalid_guessed_word_req_v3():
    ## word contains non given letters
    puzzleGen()

    ## this puzzle has T as req letter
    return_val = PuzzleStats().get_check_guess("meatq")

    ## if guessed word is less than 4, the function should return 200
    assert return_val == 300