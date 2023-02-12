import random # Used for shuffling letters
import unittest
import shuffleLetters

class TestShuffleKeyFunctions(unittest.TestCase):

    def test_ShuffleKey_base_words(self):
    # base words (requiredKey at index 0):
        puzzleKey = "twinkle"
        result = shuffleLetters.ShuffleKey(puzzleKey, "t")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "t")
    
        puzzleKey = "fedoras"
        result = shuffleLetters.ShuffleKey(puzzleKey, "f")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "f")
    
        puzzleKey = "munches"
        result = shuffleLetters.ShuffleKey(puzzleKey, "m")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "m")
    
    def test_ShuffleKey_already_shuffled_words(self):
    # already shuffled words (requiredKey at index 3):
        result = shuffleLetters.ShuffleKey("nlupgre", "p")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "p")
    
        result = shuffleLetters.ShuffleKey("odbamne", "a")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "a")
    
        result = shuffleLetters.ShuffleKey("irbvnat", "v")
        self.assertEqual(len(result), 7)
        self.assertEqual(result[3], "v")
    
    def test_LengthPrereq(self):
        # Testing LengthPrereq function
        self.assertEqual(shuffleLetters.LengthPrereq(""), 1)
        self.assertEqual(shuffleLetters.LengthPrereq("abc"), 1)
        self.assertEqual(shuffleLetters.LengthPrereq("abcdefg"), None)
        self.assertEqual(shuffleLetters.LengthPrereq("abcdefgh"), 1)

if __name__ == '__main__':
    unittest.main()
