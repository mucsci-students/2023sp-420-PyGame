""" 
    Author: Robert 2/7/23
"""

from Database.database import get_word_info, get_word_info_from_key, get_random_word, get_word_list

class Puzzle:

    def __init__(self):
        self.pangram = ""
        self.required_letter = ''
        self.total_points = 0
        self.current_word_list = {}

    """ 
        Author: Robert 2/7/23
        Definition: Generates a random puzzle and sets the following values:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_random_puzzle(self):
        random_puzzle = get_word_info()
        current_puzzle = get_random_word(random_puzzle)
        self.pangram = current_puzzle[0]
        self.required_letter = current_puzzle[1]
        self.total_points = current_puzzle[2]
        self.current_word_list = get_word_list(current_puzzle[0])

    """ 
        Author: Robert 2/7/23
        Definition: Generates a random puzzle from a given string.
        Returns: None if key is invalid. 
            Sets the following values if a valid key is provided:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_puzzle_from_base(self, key):
        word = get_word_info_from_key(key.lower())
        if len(word) == 0:
            print("Word doesn't exist")
            return None
        else:
            pangram, letter, total_points = word[0]
            self.pangram = pangram
            self.required_letter = letter
            self.total_points = total_points
            self.current_word_list = get_word_list(pangram)



# puzzle = Puzzle()
# puzzle2 = Puzzle()
# puzzle.generate_random_puzzle()
# puzzle2.generate_puzzle_from_base("dubstepp")