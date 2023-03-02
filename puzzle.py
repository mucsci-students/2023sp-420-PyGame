""" 
    Author: Robert 2/7/23
"""

from Database.database import get_random_word_info, get_word_info_from_pangram, get_word_info_from_load

class Puzzle:

    def __init__(self):
        self.pangram = ""
        self.required_letter = ""
        self.total_points = 0
        self.current_word_list = {}

    """ 
        Author: Robert 2/7/23
        Definition: Generates a random puzzle and sets the following values:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_random_puzzle(self):
        random_puzzle = get_random_word_info()
        self.pangram = random_puzzle[0]
        self.required_letter = random_puzzle[1]
        self.total_points = random_puzzle[2]
        self.current_word_list = random_puzzle[3]

    def generate_puzzle_from_load(self, pangram, letter):
        word = get_word_info_from_load(pangram, letter)
        self.pangram = word[0]
        self.required_letter = word[1]
        self.total_points = word[2]
        self.current_word_list = word[3]

    """ 
        Author: Robert 2/7/23
        Definition: Generates a random puzzle from a given string.
        Returns: None if key is invalid. 
            Sets the following values if a valid key is provided:
            panagram, required_letter, total_points, and current_word_list
    """
    def generate_puzzle_from_base(self, key):
        check_value = self.check_valid_word(key)
        if(check_value == 1):
            return 1
        else:
            self.pangram = check_value[0]
            self.required_letter = check_value[1]
            self.total_points = check_value[2]
            self.current_word_list = check_value[3]

    def generate_puzzle_from_shared(self, pangram, letter):
        word = get_word_info_from_load(pangram, letter)
        self.pangram = word[0]
        self.required_letter = word[1]
        self.total_points = word[2]
        self.current_word_list = word[3]

    def check_valid_word(self, key):
        key = key.lower()
        unique_char = ''.join(set(key))
        if len(unique_char) != 7:
            return 1
        word = get_word_info_from_pangram(unique_char)
        if len(word) == 0:
            return 1
        return word
    
    def encode_puzzle_key(self):
        encoded_string = ""
        puzzle = self.required_letter + self.pangram
        for char in puzzle:
            encoded_char = chr((ord(char) + 5 - 97) % 26 + 97)
            encoded_string += encoded_char
        return encoded_string

    
    def decode_puzzle_key(self, code):
        decoded_string = ""
        for char in code:
            decoded_char = chr((ord(char) - 5 - 97) % 26 + 97)
            decoded_string += decoded_char
        return decoded_string
