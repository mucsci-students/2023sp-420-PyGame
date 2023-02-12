import unittest
from puzzle import Puzzle
from Database.database import get_word_info, get_word_info_from_key, get_random_word, get_word_list
import io
import sys
import os

#UNIT TEST FOR THE PUZZLE.PY CLASS
class TestSpellingBeePuzzle(unittest.TestCase):

    #Unit test for init
    def test_init(self):
        puzzle1 = Puzzle()

        # check if the instance variables have been properly initialized
        self.assertEqual(puzzle1.pangram, "")
        self.assertEqual(puzzle1.required_letter, "")
        self.assertEqual(puzzle1.total_points, 0)
        self.assertEqual(puzzle1.current_word_list, {})

    #unit test for generate_random_puzzle
    def test_generate_random_puzzle(self):
        puzzle = Puzzle()
        puzzle.generate_random_puzzle()

        # Check that pangram is set
        self.assertIsNotNone(puzzle.pangram)
        self.assertIsInstance(puzzle.pangram, str)
        
        # Check that required_letter is set
        self.assertIsNotNone(puzzle.required_letter)
        self.assertIsInstance(puzzle.required_letter, str)
        
        # Check that total_points is set
        self.assertIsNotNone(puzzle.total_points)
        self.assertIsInstance(puzzle.total_points, int)
        
        # Check that current_word_list is set
        self.assertIsNotNone(puzzle.current_word_list)
        self.assertIsInstance(puzzle.current_word_list, dict)

    #Unit test for generate_puzzle_from_base
    def test_generate_puzzle_from_base(self):
        puzzle = Puzzle()

        # Test valid key
        key = "valid_key"
        puzzle.check_valid_word = lambda x: (("pangram", "letter", 100),)
        puzzle.generate_puzzle_from_base(key)
        self.assertEqual(puzzle.pangram, "pangram")
        self.assertEqual(puzzle.required_letter, "letter")
        self.assertEqual(puzzle.total_points, 100)
        self.assertEqual(puzzle.current_word_list, get_word_list("pangram"))

        # Test invalid key
        key = "invalid_key"
        puzzle.check_valid_word = lambda x: 1
        self.assertEqual(puzzle.generate_puzzle_from_base(key), 1)
    

if __name__ == '__main__':
    unittest.main()
