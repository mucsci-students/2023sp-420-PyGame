from json import load
import sqlite3
import unittest
import random
import os
import sys
from unittest.mock import MagicMock, Mock, patch
module_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MVC', 'Model', 'Database')
)

# Add the directory to the system path
sys.path.insert(0, module_dir)

# Import the model_database module
from model_database import get_possible_words, get_random_puzzle_word, get_word_info_from_load, get_word_info_from_pangram, get_puzzle_from_pangram, get_total_points


# Tests the Get Word Info From Pangram method in model_database
class TestGetWordInfoFromPangram(unittest.TestCase):
    
    def test_get_word_info_from_pangram(self):
        # Test with a pangram that includes all the letters of the alphabet
        pangram = "abcdefghijklmnopqrstuvwxyz"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

        # Test with a pangram that includes duplicate letters
        pangram = "aaabbbcccddd"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

        # Test with a pangram that includes special characters
        pangram = "ab@cd$efghijklmnopqrstuvwxyz"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

        # Test with an empty pangram
        pangram = ""
        try:
            result = get_word_info_from_pangram(pangram)
        except:
            print()

        # Test with a pangram that includes only one letter
        pangram = "aaaaaaa"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

        # Test with a pangram that includes only two letters
        pangram = "aabbbbbb"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

        # Test with a pangram that includes only three letters
        pangram = "aaabbbccc"
        result = get_word_info_from_pangram(pangram)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], pangram)
        self.assertIn(result[1], pangram)
        self.assertGreaterEqual(result[2], 0)
        self.assertIsInstance(result[3], list)

class TestGetPuzzleFromPangram(unittest.TestCase):
    
    # testing function with a pangram containing multiple letters
    @patch('random.choice', side_effect=['b'])
    def test_get_puzzle_from_pangram(self, mock_choice):
        result = get_puzzle_from_pangram('abcde')
        self.assertEqual(result, ('b', 'abcde')) # assert that the function returns the expected tuple
    
    # testing function with a pangram containing a single letter
    @patch('random.choice', side_effect=['a'])
    def test_get_puzzle_from_pangram_with_single_letter_pangram(self, mock_choice):
        result = get_puzzle_from_pangram('a')
        self.assertEqual(result, ('a', 'a')) # assert that the function returns the expected tuple
    
    # testing function with a pangram containing duplicate letters
    @patch('random.choice', side_effect=['a'])
    def test_get_puzzle_from_pangram_with_duplicate_letters(self, mock_choice):
        result = get_puzzle_from_pangram('aaaabbbccddee')
        self.assertEqual(result, ('a', 'aaaabbbccddee')) # assert that the function returns the expected tuple
    
    # testing function with a pangram missing one letter
    @patch('random.choice', side_effect=['f'])
    def test_get_puzzle_from_pangram_with_missing_letter(self, mock_choice):
        result = get_puzzle_from_pangram('abcde')
        self.assertEqual(result, ('f', 'abcde')) # assert that the function returns the expected tuple
    
    # testing function with an empty pangram
    @patch('random.choice', side_effect=['a'])
    def test_get_puzzle_from_pangram_with_empty_pangram(self, mock_choice):
        result = get_puzzle_from_pangram('')
        self.assertEqual(result, ('a', '')) # assert that the function returns the expected tuple
    
    # testing function with all letters in the pangram
    @patch('random.choice', side_effect=['z'])
    def test_get_puzzle_from_pangram_with_all_letters(self, mock_choice):
        result = get_puzzle_from_pangram('abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(result, ('z', 'abcdefghijklmnopqrstuvwxyz')) # assert that the function returns the expected tuple



class TestGetPossibleWords(unittest.TestCase):

    def setUp(self):
        self.cursor = Mock()

    def test_with_no_matching_words(self):
        self.cursor.fetchall.return_value = []
        self.assertEqual(get_possible_words(self.cursor, 'a', 'qwerty'), [])

    def test_with_matching_words(self):
        self.cursor.fetchall.return_value = [('art',), ('rat',), ('tar',)]
        self.assertEqual(get_possible_words(self.cursor, 'a', 'rat'), [('art',), ('rat',), ('tar',)])

    def test_query_execution(self):
        with patch.object(self.cursor, 'execute') as mock_execute:
            self.cursor.fetchall.return_value = []
            get_possible_words(self.cursor, 'z', 'test')
            mock_execute.assert_called_once_with("SELECT z FROM words WHERE z GLOB '*z*' AND z NOT GLOB '*[^test]*'")

    def test_query_execution_with_multiple_matching_letters(self):
        with patch.object(self.cursor, 'execute') as mock_execute:
            self.cursor.fetchall.return_value = []
            get_possible_words(self.cursor, 'a', 'rat')
            mock_execute.assert_called_once_with("SELECT a FROM words WHERE a GLOB '*a*' AND a NOT GLOB '*[^rat]*'")

class TestGetTotalPoints(unittest.TestCase):

    def test_empty_input(self):
        # Test with empty input
        puzzle_list = []
        self.assertEqual(get_total_points(puzzle_list), 0)

    def test_no_word_with_scores(self):
        # Test with 9 points
        puzzle_list = [['foo', 'a'], ['bar', 'b']]
        self.assertEqual(get_total_points(puzzle_list), 9)

    def test_single_word_with_score(self):
        # Test with 12 points
        puzzle_list = [['dog', 'd'], ['cat', 'c']]
        self.assertEqual(get_total_points(puzzle_list), 12)

    def test_multiple_words_with_scores(self):
        # Test with 22 points
        puzzle_list = [['dog', 'd'], ['cat', 'c'], ['zebra', 'z']]
        self.assertEqual(get_total_points(puzzle_list), 22)

    def test_multiple_words_with_same_letter(self):
        # Test with 3 points
        puzzle_list = [['doom', 'o'], ['loom', 'o'], ['moon', 'o']]
        self.assertEqual(get_total_points(puzzle_list), 3)

    def test_words_with_duplicate_letters(self):
        # Test with 3 points
        puzzle_list = [['hill', 'l'], ['hall', 'l'], ['hail', 'l']]
        self.assertEqual(get_total_points(puzzle_list), 3)

    def test_words_with_maximum_score(self):
        # Test with 2 points
        puzzle_list = [['quiz', 'q'], ['jazz', 'z']]
        self.assertEqual(get_total_points(puzzle_list), 2)

if __name__ == '__main__':
    unittest.main()