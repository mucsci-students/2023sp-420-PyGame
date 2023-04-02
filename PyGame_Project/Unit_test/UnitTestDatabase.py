import unittest
import sqlite3
import sys
sys.path.insert(0, 'C:\\Users\\Bjlef\\Documents\\GitHub\\2023sp-420-PyGame\\Database')
from Database.database import generate_table, get_word_info_from_pangram, get_word_info_from_load, get_random_word_info, get_random_puzzle_word, get_possible_words

class TestDBClass(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        generate_table()

    def test_get_word_info_from_pangram(self):
        word_info = get_word_info_from_pangram('abcdefghijklmnopqrstuvwxyz')
        self.assertIsInstance(word_info, list)
        self.assertEqual(len(word_info), 4)
        self.assertIsInstance(word_info[0], str)
        self.assertIsInstance(word_info[1], str)
        self.assertIsInstance(word_info[2], int)
        self.assertIsInstance(word_info[3], list)

    def test_get_word_info_from_load(self):
        word_info = get_word_info_from_load('abcdefghijklmnopqrstuvwxyz', 'a')
        self.assertIsInstance(word_info, list)
        self.assertEqual(len(word_info), 4)
        self.assertIsInstance(word_info[0], str)
        self.assertIsInstance(word_info[1], str)
        self.assertIsInstance(word_info[2], int)
        self.assertIsInstance(word_info[3], list)

    def test_get_random_word_info(self):
        word_info = get_random_word_info()
        self.assertIsInstance(word_info, list)
        self.assertEqual(len(word_info), 4)
        self.assertIsInstance(word_info[0], str)
        self.assertIsInstance(word_info[1], str)
        self.assertIsInstance(word_info[2], int)
        self.assertIsInstance(word_info[3], list)

    def test_get_random_puzzle_word(self):
        letter, word = get_random_puzzle_word(self.cursor)
        self.assertIsInstance(letter, str)
        self.assertIsInstance(word, str)

    def test_get_possible_words(self):
        word_list = get_possible_words(self.cursor, 'a', 'abcdefghijklmnopqrstuvwxyz')
        self.assertIsInstance(word_list, list)
        self.assertGreater(len(word_list), 0)

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()