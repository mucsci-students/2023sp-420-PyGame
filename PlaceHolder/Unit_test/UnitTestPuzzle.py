import unittest
import sys
import io
sys.path.insert(0, 'C:\\Users\\Bjlef\\Documents\\GitHub\\2023sp-420-PyGame')
from Database.database import get_word_info_from_pangram, get_word_info_from_load, get_random_word_info
from puzzle import Puzzle

class TestPuzzle(unittest.TestCase):

    def setUp(self):
        self.puzzle = Puzzle()

    def test_generate_random_puzzle(self):
        self.puzzle.generate_random_puzzle()
        self.assertIsInstance(self.puzzle.pangram, str)
        self.assertIsInstance(self.puzzle.required_letter, str)
        self.assertIsInstance(self.puzzle.total_points, int)
        self.assertIsInstance(self.puzzle.current_word_list, list)

    def test_generate_puzzle_from_load(self):
        pangram = "abcdefg"
        letter = "a"
        self.puzzle.generate_puzzle_from_load(pangram, letter)
        self.assertEqual(self.puzzle.pangram, pangram)
        self.assertEqual(self.puzzle.required_letter, letter)
        self.assertIsInstance(self.puzzle.total_points, int)
        self.assertIsInstance(self.puzzle.current_word_list, list)

    def test_generate_puzzle_from_base_valid_key(self):
        key = "abcdefg"
        self.puzzle.generate_puzzle_from_base(key)
        self.assertIsInstance(self.puzzle.required_letter, str)
        self.assertIsInstance(self.puzzle.total_points, int)
        self.assertIsInstance(self.puzzle.current_word_list, list)

    def test_generate_puzzle_from_base_invalid_key(self):
        key = "abcde"
        self.assertEqual(self.puzzle.generate_puzzle_from_base(key), 1)

    def test_check_valid_word_valid_key(self):
        key = "abcdefg"
        result = self.puzzle.check_valid_word(key)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)

    def test_check_valid_word_invalid_key(self):
        key = "abcde"
        self.assertEqual(self.puzzle.check_valid_word(key), 1)

    
if __name__ == '__main__':
    unittest.main()