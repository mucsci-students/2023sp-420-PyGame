import os, sys

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

""" def test_save_file():

    ##Generate a puzzle, relied on puzzle generation with share code and check guesses
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    share_set = {"m", "e", "a", "t", "b", "l", "s"}
    center_letter = "t"
    prep_value = prep_game_from_share(shareable_key)
    generated_share_set = set(PuzzleStats().pangram)

    ## input some test values to check later
    PuzzleStats().get_check_guess("tale")
    PuzzleStats().get_check_guess("tales")

    ## Save the puzzle
    fileName = "test_1"
    PuzzleStats().get_save_game(fileName)

    ## Check saved valuse are correct
    saveFile = "Saves/" + fileName + ".json"
    
    ## if file doenst exist will throw an exception, not passing the test
    ## reads the json file as a Dict
    with open(saveFile, "r") as openfile:
        saveInfo = json.load(openfile)


    check_1 = saveInfo["CurrentPoints"] == 2
    check_2 = len(saveInfo["GuessedWords"]) == 2
    check_3 = saveInfo["MaxPoints"] > 0
    check_4 = saveInfo["WordList"] > 0
    check_5 = saveInfo["RequiredLetter"] == center_letter
    check_6 = len(set(saveInfo["PuzzleLetters"]).intersection(share_set)) == 7

    
    assert check_1 and check_2 and check_3 and check_4 and check_4 and check_5 and check_6
     """


