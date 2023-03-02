import sys
import os

from model_PuzzleStats import PuzzleStats
from model_puzzle import Puzzle
from model_shuffleLetters import ShuffleKey
from controller_universal import *
from View import *


"""
generate the Puzzle and Puzzle_Stats objects from a random word
    - returns a tuple : (puzzle, puzzle_stats)
"""
def prep_new_game():
    puzzle = Puzzle()
    puzzle.generate_random_puzzle()
    shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
    puzzle_stats = PuzzleStats(puzzle.total_points, shuffled_puzzle)
    return (puzzle, puzzle_stats)

"""
generate the Puzzle and Puzzle_Stats objects from a key 
    - Paramater: Key (or base)
    - returns 
        - if failed returns 1
        - if passed returns tuple: (puzzle, puzzle_stats)
"""
def prep_game_with_key(key):
    puzzle = Puzzle()
    if(puzzle.generate_puzzle_from_base(key) == 1):
        return 1

    shuffled_puzzle = ShuffleKey(puzzle.pangram, puzzle.required_letter)
    puzzle_stats = PuzzleStats(puzzle.total_points, shuffled_puzzle)
    return (puzzle, puzzle_stats)

"""
generate the Puzzle and Puzzle_Stats objects from load 
    - Paramater: tuple -> save info 
    - returns 
        - if failed returns 1
        - if passed returns puzzle
"""
def prep_game_from_load(save_info):
    puzzle = Puzzle()
    if(puzzle.generate_puzzle_from_load(save_info[0], save_info[1]) == 1):
        return 1

    ShuffleKey(puzzle.pangram, puzzle.required_letter)
    return puzzle

"""
generate the Puzzle and Puzzle_Stats objects from shared game 
    - Paramater: tuple -> save info 
    - returns a tuple : (puzzle, puzzle_stats)
"""
def prep_game_from_share(shared_key):
    decoded_key = puzzle.decode_puzzle_key(shared_key)
    puzzle = Puzzle()
    
    if(puzzle.generate_puzzle_from_shared(decoded_key[1:], decoded_key[0]) == 1):
        return 1

    puzzle_stats = PuzzleStats(puzzle.total_points, ShuffleKey(puzzle.pangram, puzzle.required_letter))
    puzzle_stats.score = 0
    puzzle_stats.guesses = []

    return (puzzle, puzzle_stats)