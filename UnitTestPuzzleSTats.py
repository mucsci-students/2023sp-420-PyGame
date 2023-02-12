import unittest
from PuzzleStats import PuzzleStats
import io
import sys
import os

#UNIT TEST CLASS FOR THE OUTPUT.PY FILE.
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
    
    def test_check_validity(self):
        max_score = 50
        shuffled_puzzle = "abcd"
        puzzle_stats = PuzzleStats(max_score, shuffled_puzzle)
        word_list = {
            "abcd": 10,
            "dcba": 20,
            "cbad": 30
        }

        # Test valid word
        result = puzzle_stats.CheckValidity("abcd", word_list)
        self.assertEqual(result, 0)
        self.assertEqual(puzzle_stats.score, 10)
        self.assertEqual(puzzle_stats.guesses, ["abcd"])

        # Test invalid word
        result = puzzle_stats.CheckValidity("efgh", word_list)
        self.assertEqual(result, 1)
        self.assertEqual(puzzle_stats.score, 10)
        self.assertEqual(puzzle_stats.guesses, ["abcd"])

    def test_in_guesses(self):
        max_score = 50
        shuffled_puzzle = "abcd"
        puzzle_stats = PuzzleStats(max_score, shuffled_puzzle)
        puzzle_stats.guesses = ["abcd", "dcba", "cbad"]

        # Test word in guesses
        result = puzzle_stats.InGuesses("abcd")
        self.assertTrue(result)

        # Test word not in guesses
        result = puzzle_stats.InGuesses("efgh")
        self.assertFalse(result)

    

if __name__ == '__main__':
    unittest.main()
