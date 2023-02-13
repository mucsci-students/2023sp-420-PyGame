import unittest
from PuzzleStats import PuzzleStats
import io
import sys
import os

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
    
    #def test_get_check_guess(self):
    #    # Setup
    #    puzzleInfo = PuzzleInfo(required_letter='a', pangram=False, current_word_list=['word'])
    #    game = Game()
    #    game.guesses = []
    #    
    #    # Test returns 1 if guess doesn't contain required letter
    #    guess = 'word'
    #    expected = 1
    #    result = game.get_check_guess(guess, puzzleInfo)
    #    self.assertEqual(result, expected)
        
        # Test returns 2 if guess isn't a pangram
     #   puzzleInfo.required_letter = None
     #   puzzleInfo.pangram = True
        #expected = 2
      #  result = game.get_check_guess(guess, puzzleInfo)
      #  self.assertEqual(result, expected)

        # Test returns True if guess has been made before
       # puzzleInfo.pangram = False
       # game.guesses = ['word']
       # expected = True
        #result = game.get_check_guess(guess, puzzleInfo)
        #self.assertEqual(result, expected)

        # Test returns 0 if guess meets requirements and hasn't been made before
        #game.guesses = []
        #expected = 0
        #result = game.get_check_guess(guess, puzzleInfo)
        #self.assertEqual(result, expected)

        # Test returns 1 if guess isn't in current word list
       # guess = 'words'
        #expected = 1
       # result = game.get_check_guess(guess, puzzleInfo)
       # self.assertEqual(result, expected)

        # Test returns 69420 if all words have been guessed
       # game.current_word_list = []
       # expected = 69420
       # result = game.get_check_guess(guess, puzzleInfo)
       # self.assertEqual(result, expected)

    

if __name__ == '__main__':
    unittest.main()
