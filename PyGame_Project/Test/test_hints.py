import pytest



from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *

pytest.fixture
def puzzleGen():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    prep_game_from_share(shareable_key)
    ## generate hints class
    PuzzleStats().generate_hints()



"""
Test to see if generating hints 
    - relies on generate from share
"""
def test_generate_hints():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    prep_game_from_share(shareable_key)

    ## generate hints class
    PuzzleStats().generate_hints()

    ## Check to see if added an attribute "hints" to PuzzleStats
    ## Check to make sure hints.words is a list
    ## Check to see if it got passed a list of words 
    ## Check to see if it got passed a valid pangram
    assert hasattr(PuzzleStats(), 'hints') and type(PuzzleStats().hints.words) == list and len(PuzzleStats().hints.words) > 0 and len(PuzzleStats().hints.pangram) == 7


"""
Test to see if it is generating correct two letter dictionary 
    - relies on generate from share
"""
def test_two_letter_dict():
    ## generate puzzle to check hint values
    puzzleGen()

    # calculated list
    check_val = {'st': 49, 'ta': 52, 'te': 45, 'bl': 14, 'me': 26, 'se': 20, 'el': 4, 'em': 4, 'la': 15, 'ma': 28, 'ab': 10, 'ba': 26, 'be': 25, 'ea': 5, 'sa': 15, 'sm': 5, 'al': 5, 'at': 11, 'es': 5, 'le': 7, 'ts': 2, 'as': 2, 'eb': 2, 'sl': 6, 'tm': 1, 'et': 1}
   
    ## generate tbhe hints
    two_letter_dict = PuzzleStats().hints.two_letter_dict

    assert two_letter_dict == check_val

"""
Test to see if generating coreect hints matrix
    - relies on generate from share
"""
def test_2D_array():
    ## generate puzzle to check hint values
    puzzleGen()

    # calculated list
    check_val =  [[' ', 4, 5, 6, 7, 8, 9, 10, 11], ['B', 12, 19, 16, 9, 6, 2, 1, ' ', 65], ['T', 24, 25, 19, 13, 10, 4, 3, 2, 100], ['S', 11, 25, 24, 12, 12, 7, 3, 1, 95], ['E', 4, 4, 5, 3, 3, 2, ' ', ' ', 21], ['M', 10, 10, 9, 11, 9, 3, 2, ' ', 54], ['A', 4, 6, 9, 7, 2, ' ', ' ', ' ', 28], ['L', 6, 4, 4, 3, 2, 3, ' ', ' ', 22], [' ', 71, 93, 86, 58, 44, 21, 9, 3, 385]]
    ## generate tbhe hints
    two_D_array =  PuzzleStats().hints.two_d_array
    assert two_D_array == check_val
