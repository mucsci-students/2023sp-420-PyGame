


from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *

"""
Test puzzle generation for random selection
    - uses the universal controller to test
"""
def test_random_puzzle():
    PuzzleStats().clear()
    prep_new_game()
    ## test pangram value is populated and shuffled letter is set 
    assert len(PuzzleStats().pangram) == 7 and len(PuzzleStats().shuffled_puzzle) == 7

"""
Test puzzle generation with key (base word)
    - check to see if the correct puzzle was generated with a valid key (meatballs)
"""
def test_puzzle_from_key_valid_key():
    PuzzleStats().clear()
    key = "meatballs"
    key_set = {"m", "e", "a", "t", "b", "l", "s"}
    prep_val = prep_game_with_key(key)
    generated_key_set = set(PuzzleStats().pangram)
    ## prev value 1 means invalid key so a valid key should return 0 to pass
    ## generated_key_set should have length 7 
    ## generated_key_set should be a set similar to key_set, a union with length 7 means that it contains the same letters
    assert (prep_val != 1) and (len(generated_key_set) == 7) and (len(generated_key_set.intersection(key_set)) == 7)


"""
Test puzzle generation with key (base word)
    - check to see if it doesn't generate a puzzle given an invalid key
    - invalid key is one letter short
"""
def test_puzzle_from_key_invalid_key_1():
    PuzzleStats().clear()
    key = "meatball"
    prep_val = prep_game_with_key(key)
    ## invalid key was entered, prep_game_with_key should return a 1
    assert prep_val == 1

"""
Test puzzle generation with key (base word)
    - check to see if it doesn't generate a puzzle given an invalid key
    - invalid key is one letter to long
"""
def test_puzzle_from_key_invalid_key_2():
    PuzzleStats().clear()
    key = "meatballsk"
    ## invalid key was entered, prep_game_with_key should return a 1
    prep_val = prep_game_with_key(key)
    assert prep_val == 1

"""
Test puzzle generation with share code 
    - check to see if it generates the same puzzle given an share code
"""
def test_puzzle_from_share():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    share_set = {"m", "e", "a", "t", "b", "l", "s"}
    center_letter = "t"

    prep_value = prep_game_from_share(shareable_key)
    generated_share_set = set(PuzzleStats().pangram)

    ## prev value 1 means invalid key so a valid key should return 0 to pass
    ## generated_share_set should have length 7
    ## generated_share_set should be a set similar to key_set, a union with length 7 means that it contains the same letters
    ## PuzzleStats().required_letter should match expected from share 
    assert (prep_value != 1) and (len(generated_share_set) == 7) and (len(generated_share_set.intersection(share_set)) == 7) and (PuzzleStats().required_letter == center_letter)

"""
Test puzzle generation with share code 
    - check to see if it generates the same puzzle given an share code
    - share code is one letter short
"""
def test_puzzle_from_share_invalid_code_v1():
    PuzzleStats().clear()
    shareable_key = "gyxjrfq"

    prep_value = prep_game_from_share(shareable_key)

    ## prev value 1 means invalid key so a valid key should return 0 to pass
    assert prep_value == 1

"""
Test puzzle generation with share code 
    - check to see if it generates the same puzzle given an share code
    - share code is one letter long
"""
def test_puzzle_from_share_invalid_code_v2():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfqo"

    prep_value = prep_game_from_share(shareable_key)

    ## prev value 1 means invalid key so a valid key should return 0 to pass
    assert prep_value == 1