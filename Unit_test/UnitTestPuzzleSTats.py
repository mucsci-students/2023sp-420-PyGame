import unittest
import os
import sys

module_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MVC', 'Model')
)

# Add the directory to the system path
sys.path.insert(0, module_dir)
from model_PuzzleStats import PuzzleStats


class TestPuzzleStats(unittest.TestCase):

    def setUp(self):
        self.word_list = ["a", "an", "ant", "art", "rat", "tar", "rant", "tart", "start"]
        self.pangram = "artnst"
        self.max_score = 50
        self.puzzle_stats = PuzzleStats(self.max_score, self.pangram)

    def test_initialization(self):
        self.assertEqual(self.puzzle_stats.score, 0)
        self.assertEqual(self.puzzle_stats.rank, 0)
        self.assertEqual(self.puzzle_stats.guesses, [])
        self.assertEqual(self.puzzle_stats.maxScore, self.max_score)
        self.assertEqual(self.puzzle_stats.shuffled_puzzle, self.pangram)

    def test_check_word_req(self):
        # test case where word is too short
        self.assertEqual(self.puzzle_stats.CheckWordReq("an", "a", self.pangram), 100)
        # test case where word doesn't contain required letter
        self.assertEqual(self.puzzle_stats.CheckWordReq("rants", "c", self.pangram), 200)
        # test case where word contains invalid letter
        self.assertEqual(self.puzzle_stats.CheckWordReq("nart", "a", self.pangram), 0)
        # test case where word passes requirements
        self.assertEqual(self.puzzle_stats.CheckWordReq("art", "a", self.pangram), 100)

    def test_check_validity(self):
        # test case where guess is valid
        self.assertEqual(self.puzzle_stats.CheckValidity("start", self.word_list), 0)
        self.assertEqual(self.puzzle_stats.score, 5)
        self.assertEqual(self.puzzle_stats.guesses, ["start"])
        self.assertEqual(self.puzzle_stats.rank, 3)
        # test case where guess is invalid
        self.assertEqual(self.puzzle_stats.CheckValidity("car", self.word_list), 1)
        self.assertEqual(self.puzzle_stats.score, 5)
        self.assertEqual(self.puzzle_stats.guesses, ["start"])
        self.assertEqual(self.puzzle_stats.rank, 3)

    def test_in_guesses(self):
        # test case where guess has been made before
        self.puzzle_stats.guesses.append("start")
        self.assertTrue(self.puzzle_stats.InGuesses("start"))
        # test case where guess has not been made before
        self.assertFalse(self.puzzle_stats.InGuesses("rat"))

    def test_get_check_guess(self):
        # test case where guess passes all requirements and is valid
        self.assertEqual(self.puzzle_stats.get_check_guess("start", self.puzzle_stats), 0)
        self.assertEqual(self.puzzle_stats.score, 5)
        self.assertEqual(self.puzzle_stats.guesses, ["start"])
        self.assertEqual(self.puzzle_stats.rank, 1)
        # test case where guess is already in guesses
        self.assertEqual(self.puzzle_stats.get_check_guess("start", self.puzzle_stats), True)
        self.assertEqual(self.puzzle_stats.score, 5)
        self.assertEqual(self.puzzle_stats.guesses, ["start"])
        self.assertEqual(self.puzzle_stats.rank, 1)
        # test case where guess is invalid
        self.assertEqual(self.puzzle_stats.get_check_guess("car", self.puzzle_stats), 1)
        self.assertEqual(self.puzzle_stats.score, 5)
        self.assertEqual(self.puzzle_stats.guesses, ["start"])
        self.assertEqual(self.puzzle_stats.rank, 1)
        

if __name__ == '__main__':
    unittest.main()