import unittest
import sys
sys.path.insert(0, 'C:\\Users\\Bjlef\\Documents\\GitHub\\2023sp-420-PyGame')
#from puzzle import Puzzle
from model_hints_module import *
from collections import OrderedDict

class TestHints(unittest.TestCase):
    
    letters = 'LZAETQU'
    word_list = ['quetzal', 'equate', 'quelea', 'quezal', 'aquae', 'equal', 'quale', 'quate', 'quell', 'queue', 'tuque', 'aqua']
    
    def test_generatePangramCount(self):
        self.assertIsInstance(generatePangramCount(word_list, letters), str)
        self.assertEqual(generatePangramCount(word_list, letters), str(1))
     

    def generateWordCount(self):
        self.assertIsInstance(generateWordCount(self), str)
        self.assertEqual(generateWordCount(word_list), str(len(word_list)))

    def test_generateLetterMatrix(self):
        var =   [['0',  '4',    '5',    '6',    '7',    'tot'],
                 ['L',  '0',    '0',    '0',    '0',    '0'],
                 ['Z',  '0',    '0',    '0',    '0',    '0'],
                 ['A',  '1',    '1',    '0',    '0',    '2'],
                 ['E',  '0',    '1',    '1',    '0',    '2'],
                 ['T',  '0',    '1',    '0',    '0',    '1'],
                 ['Q',  '0',    '4',    '2',    '1',    '7'],
                 ['U',  '0',    '0',    '0',    '0',    '0'],
                 ['tot','1',    '7',    '3',    '1',    '13']]
        self.assertEqual(self.puzzle.generateLetterMatrix(word_list, letters), var )
        #print(self.puzzle.generateLetterMatrix(word_list, letters))

    def generateTwoLetterDictionary(self):
      
        test = {"qu":7, "eq":2, "aq":2, "tu":1}
        sorted(test)
        self.assertIsInstance(generateTwoLetterDictionary(word_list), dict)
        self.assertEqual(generateTwoLetterDictionary(word_list), test)

    def test_generateBingo(self):
        self.assertIsInstance(generateBingo(self.puzzle.generateLetterMatrix(word_list, letters)), int)
        self.assertEqual(generateBingo(self.puzzle.generateLetterMatrix(word_list, letters)), 0)

if __name__ == '__main__':
    unittest.main()