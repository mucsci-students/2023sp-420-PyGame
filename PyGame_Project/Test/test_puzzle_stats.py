""" 
done - ShuffleKey
done - get_word_points
done - RankIndex
 """


import pytest


from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *

## default puzzle generation for testing 
pytest.fixture
def puzzleGen():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    prep_game_from_share(shareable_key)
    
## ---------- Testing shuffle ---------- ##
def test_shuffle_key():
    puzzleGen()

    ## check three times, as long as two dont match the test pass
    original_val = PuzzleStats().shuffled_puzzle
    check_list = []
    check_list.append(original_val != PuzzleStats().ShuffleKey())
    check_list.append(check_list[0] != PuzzleStats().ShuffleKey())
    check_list.append(check_list[1] != PuzzleStats().ShuffleKey())

    ## count how many pass
    pass_count = 0
    for check in check_list:
        if check == True:
            pass_count += 1

    # if atleast 2 pass, test pass (small chance it could shuffle to the same lineup)
    assert pass_count >= 2


## ---------- Testing points calcualtions ---------- ##
def test_word_points_calc_4():
    puzzleGen()
    ##check length 4
    points = PuzzleStats().get_word_points("asdf")
    assert points == 1

def test_word_points_calc_7():
    ## non-pangram
    puzzleGen()
    ##check length 4
    points = PuzzleStats().get_word_points("asdfghh")
    assert points == 7

def test_word_points_calc_5():
    puzzleGen()
    ##check length 4
    points = PuzzleStats().get_word_points("asdfg")
    assert points == 5

def test_word_points_calc_pangram():
    puzzleGen()
    ##check length 4
    points = PuzzleStats().get_word_points("asdfghj")
    assert points == 14


## ---------- Testing ranges for rank index ---------- ##
def test_rank_index_calc_rank_0():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 0
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 0

    PuzzleStats().score = 1.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 0

    assert check_1 and check_2

def test_rank_index_calc_rank_1():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 2
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 1

    PuzzleStats().score = 4.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 1

    assert check_1 and check_2

def test_rank_index_calc_rank_2():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 5
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 2

    PuzzleStats().score = 7.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 2

    assert check_1 and check_2

def test_rank_index_calc_rank_3():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 8
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 3

    PuzzleStats().score = 14.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 3

    assert check_1 and check_2

def test_rank_index_calc_rank_4():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 15
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 4

    PuzzleStats().score = 24.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 4

    assert check_1 and check_2

def test_rank_index_calc_rank_5():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 25
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 5

    PuzzleStats().score = 39.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 5

    assert check_1 and check_2

def test_rank_index_calc_rank_6():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 40
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 6

    PuzzleStats().score = 49.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 6

    assert check_1 and check_2

def test_rank_index_calc_rank_7():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 50
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 7

    PuzzleStats().score = 69.9
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 7

    assert check_1 and check_2

def test_rank_index_calc_rank_8():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 70
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 8

    PuzzleStats().score = 99
    PuzzleStats().RankIndex()
    check_2 = PuzzleStats().rank == 8

def test_rank_index_calc_rank_8():
    puzzleGen()
    
    PuzzleStats().total_points = 100

    PuzzleStats().score = 100
    PuzzleStats().RankIndex()
    check_1 = PuzzleStats().rank == 9

    assert check_1 



