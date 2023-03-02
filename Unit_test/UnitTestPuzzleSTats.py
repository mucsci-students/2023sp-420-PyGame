import unittest
import io
import sys
import os
sys.path.insert(0, 'C:\\Users\\Bjlef\\Documents\\GitHub\\2023sp-420-PyGame')
from PuzzleStats import PuzzleStats
from unittest.mock import Mock

#UNIT TEST CLASS FOR THE PuzzleStats FILE.
class TestSpellingBeePuzzleStats(unittest.TestCase):

    def test_init(self):
        max_score = 50
        shuffled_puzzle = "abcd"
        puzzle_stats = PuzzleStats(max_score, shuffled_puzzle)

        self.assertEqual(puzzle_stats.score, 0)
        self.assertEqual(puzzle_stats.rank, 0)
        self.assertEqual(puzzle_stats.guesses, [])
        self.assertEqual(puzzle_stats.maxScore, max_score)
        self.assertEqual(puzzle_stats.shuffled_puzzle, shuffled_puzzle)
    
    def setUp(self):
        self.max_score = 100
        self.shuffled_puzzle = 'puzzle'
        self.my_instance = PuzzleStats(self.max_score, self.shuffled_puzzle)

    def test_get_check_guess(self):
        # create an instance of your class
        my_instance = PuzzleStats()

        # create some mock data for testing
        class PuzzleInfo:
            def __init__(self, required_letter, pangram, current_word_list):
                self.required_letter = required_letter
                self.pangram = pangram
                self.current_word_list = current_word_list
        
        # test case 1: guess passes all requirements
        guess = "word"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        expected_outcome = 0
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 2: guess fails length requirement
        guess = "abc"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        expected_outcome = 100
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 3: guess fails required letter requirement
        guess = "abc"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        expected_outcome = 200
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 4: guess fails contains only given letters requirement
        guess = "abcd"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        expected_outcome = 300
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 5: guess has already been guessed
        guess = "word"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        my_instance.previous_guesses = [guess]
        expected_outcome = 1
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 6: guess is not a valid word
        guess = "notaword"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        expected_outcome = 2
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

        # test case 7: check_progress is True
        guess = "word"
        puzzle_info = PuzzleInfo(required_letter="w", pangram="word", current_word_list=["word"])
        my_instance.previous_guesses = [guess]
        my_instance.current_word = "word"
        my_instance.word_list = ["word"]
        my_instance.valid_word_count = 1
        my_instance.current_score = 100
        my_instance.win_score = 1000
        my_instance.round_count = 10
        expected_outcome = 69420
        self.assertEqual(my_instance.get_check_guess(guess, puzzle_info), expected_outcome)

if __name__ == '__main__':
    unittest.main()
