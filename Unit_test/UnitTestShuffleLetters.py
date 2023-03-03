import random
import string # Used for shuffling letters
import unittest
import sys
import os

module_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MVC', 'Model')
)

# Add the directory to the system path
sys.path.insert(0, module_dir)

from model_shuffleLetters import *

class TestShuffleKey(unittest.TestCase):

    def test_base_words(self):
        # Test with required key at index 0
        puzzleKey = "twinkle"
        result = ShuffleKey(puzzleKey, "t")
        self.assertEqual(len(result), 7)
        self.assertEqual(result.count("t"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

        puzzleKey = "fedoras"
        result = ShuffleKey(puzzleKey, "f")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("f"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

        puzzleKey = "munches"
        result = ShuffleKey(puzzleKey, "m")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("m"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

    def test_already_shuffled_words(self):
        # Test with required key at index 3
        result = ShuffleKey("nlupgre", "p")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("p"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

        result = ShuffleKey("odbamne", "a")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("a"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

        result = ShuffleKey("irbvnat", "v")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("v"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

    def test_required_key_not_in_puzzle_key(self):
        # Test when required letter is not in the puzzle key
        result = ShuffleKey("abcdefg", "h")
        self.assertEqual(result, None)

    def test_duplicate_required_key_in_puzzle_key(self):
        # Test when required letter is duplicated in the puzzle key
        result = ShuffleKey("hellooo", "o")
        self.assertEqual(result, None)

    def test_uppercase_input(self):
        # Test with uppercase input
        puzzleKey = "TWINKLE"
        result = ShuffleKey(puzzleKey, "T")
        self.assertEqual(len(result), 8)
        self.assertEqual(result.count("t"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

    def test_special_characters_input(self):
        # Test with special characters input
        puzzleKey = "he#llo!"
        result = ShuffleKey(puzzleKey, "l")
        self.assertEqual(len(result), 7)
        self.assertEqual(result.count("l"), 1)
        self.assertEqual(set(result), set(string.ascii_lowercase))

    def test_invalid_input(self):
        # Test with invalid input
        self.assertRaises(TypeError, ShuffleKey, None, "a")
        self.assertRaises(TypeError, ShuffleKey, "puzzleKey", None)
        self.assertRaises(TypeError, ShuffleKey, "puzzleKey", 1)



    

if __name__ == '__main__':
    unittest.main()
