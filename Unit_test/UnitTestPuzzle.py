import unittest
import sys
import os
from unittest.mock import patch
module_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MVC', 'Model')
)

# Add the directory to the system path
sys.path.insert(0, module_dir)
from model_puzzle import Puzzle

class TestPuzzleInit(unittest.TestCase):

    def setUp(self):
        self.puzzle = Puzzle()

    def test_init(self):
        self.assertEqual(self.puzzle.pangram, "")
        self.assertEqual(self.puzzle.required_letter, "")
        self.assertEqual(self.puzzle.total_points, 0)
        self.assertEqual(self.puzzle.current_word_list, {})
    def test_generate_random_puzzle(self):
        p = Puzzle()
        p.generate_random_puzzle()
        self.assertTrue(isinstance(p.pangram, str))
        self.assertTrue(len(p.pangram) == 7)
        self.assertTrue(isinstance(p.required_letter, str))
        self.assertTrue(len(p.required_letter) == 1)
        self.assertTrue(isinstance(p.total_points, int))
        self.assertTrue(isinstance(p.current_word_list, list))

    def test_generate_puzzle_from_load(self):
        p = Puzzle()
        p.generate_puzzle_from_load("inconveniencing", "e")
        self.assertEqual(p.pangram, "inconveniencing")
        self.assertEqual(p.required_letter, "e")
        self.assertEqual(p.total_points, 496)
        self.assertTrue(isinstance(p.current_word_list, list))

    def test_generate_puzzle_from_base(self):
        p = Puzzle()
        p.generate_puzzle_from_base("unequipped")
        self.assertTrue(isinstance(p.current_word_list, list))


    def test_generate_puzzle_from_shared(self):
        p = Puzzle()
        p.generate_puzzle_from_shared("horsing", "l")
        self.assertEqual(p.pangram, "horsing")
        self.assertEqual(p.required_letter, "l")
        self.assertEqual(p.total_points, 96)
        self.assertTrue(isinstance(p.current_word_list, list))

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()