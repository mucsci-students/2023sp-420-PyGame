import sys
import os

from model_puzzle import *
from View import *


"""
generate the Puzzle and Puzzle_Stats objects from a random word
    - returns a tuple : (puzzle, puzzle_stats)
"""
def prep_new_game():
    puzzle = PuzzleStats()
    puzzle.generate_random_puzzle()
    puzzle.ShuffleKey()

"""
generate the Puzzle and Puzzle_Stats objects from a key 
    - Paramater: Key (or base)
    - returns 
        - if failed returns 1
        - if passed returns 0
"""
def prep_game_with_key(key):
    puzzle = PuzzleStats()
    if check_key(key) == 1:
        return 1
    
    if(puzzle.generate_puzzle_from_base(key) == 1):
        input("2")
        return 1

    puzzle.ShuffleKey()
    return 0 


"""  

"""
def check_key(key):
    if len(set(key)) != 7:
        return 1



"""
generate the Puzzle and Puzzle_Stats objects from load 
    - Paramater: tuple -> save info 
    - returns 
        - if failed returns 1
        - if passed returns 0
"""
def prep_game_from_load(save_info):
    puzzle = PuzzleStats()
    if puzzle.LoadGame(save_info) == 1:
        return 1
    
    puzzle.ShuffleKey()
    return 0 

"""
generate the Puzzle and Puzzle_Stats objects from shared game 
    - Paramater: tuple -> save info 
    - returns 0
"""
def prep_game_from_share(shared_key):
    if len(shared_key) < 7:
        return 1
    puzzle = PuzzleStats()
    decoded_key = puzzle.decode_puzzle_key(shared_key)
    
    if(puzzle.generate_puzzle_from_shared(decoded_key[1:], decoded_key[0]) == 1):
        return 1

    puzzle.ShuffleKey()
    puzzle.score = 0
    puzzle.guesses = []

    return 0