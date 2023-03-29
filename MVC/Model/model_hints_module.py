"""
    generateHints: must be called first
    Takes Three Parameters
        Words: List of words from puzzle
        Letters: Array of letters from the model
        Points: Total points in the puzzle
    Returns 0
"""
from puzzle import *

    
m_letters = puzzle.pangram
m_word_count = 0
m_points = puzzle.total_points
m_pangram_count = 0
m_letterMatrix = [[str()]]
m_twoLetterDictionary = {}
#puzzle = puzzle.stats
m_words =  puzzle.current_word_list


# Returns string of letters for the current puzzle
def generateLetters():
    m_letters = puzzle.pangram
    return puzzle.pangram
# Returns string of word count
def generateWordCount(words):
    word_count = 0
    for word in words:
        word_count += 1
    return str(word_count)
# Returns str of points
def generatePoints():
    return str(puzzle.total_points())
# Returns string of pangram counts
def generatePangramCount(words, letters):
    for word in words:
        if(len(word) >= 7 ):
            if all(letter in word for letter in letters):
                pangram_count += 1    
    return str(pangram_count)

# Parmeters: the words of the current_puzzle as list and the puzzle.pangram as list of letters
# Returns  list[list[str]] of the letters and count array
def generateLetterMatrix(words, letters):
   
    
    if(words == [] or len(letters) < 7):
        return 1
    #gets max length of all words
    maxLength = len(max(words, key=len))   
    if(maxLength < 7):
        return 1
    # Initialize letterMatrix 
    # (maxLength - 1) for maxLength -3 for lengths + total + column label
    # 9 is for 7 letters + total + row label
    letterMatrix = [[str(0)]*(maxLength - 1)]*9 
    letter_index = 1
    for i in letters:
        letterMatrix[letter_index][0] = str(i)
        letter_index += 1
    letterMatrix[8][0] = "tot"
    
    for i in range(1, maxLength - 2):
        letterMatrix[0][i] = str(i)
    letterMatrix[0][maxLength - 2] = "tot"
    for word in words:
        current_word_length = len(word)
        first_letter = word[0]
        letterMatrix[letters.index(first_letter) + 1][current_word_length - 3] = \
            int(letterMatrix[letters.index(first_letter) + 1][current_word_length - 3]) + 1 
#LETTER MATRIX
    # Totals Rows
    for letter in letters:
        row_total = 0
        for i in range(1, maxLength - 2):#uninclusive end
            row_total += int(letterMatrix[letters.index(letter) + 1][i])
        letterMatrix [letters.index(letter) + 1][maxLength - 2] = str(row_total)
    # Totals Columns
    for j in range(1, maxLength - 1):#uninclusive end
        count = 0 
        for i in range(1,8):
            count += int(letterMatrix[i][j])
        letterMatrix [8][j] = str(count)
    return letterMatrix
# Returns Dictionary of countaining  starting two letters : count
def generateTwoLetterDictionary(words):
    twoLetterDictionary = {}
    for word in words:
        twoLetters = word[0:2]
        if twoLetters not in twoLetterDictionary: 
            twoLetterDictionary[twoLetters] = 0
        twoLetterDictionary[twoLetters] += 1
    twoLetterDictionary = sorted(twoLetterDictionary)

    return twoLetterDictionary
# Prerequisite: Two letter Matrix generated 
# Param: the letter matrix generated 
#Looks at the totals for each letter in rows of the letter matrix, 
# Returns if bingo (collective of letters all used once to start words)
def generateBingo(letterMatrix):
    index = []
    for i in range(1,8):
        index.append(int(letterMatrix[i][-1]))
   
    if(min(index) < 1):
        return 0
    return 1
    
    

puzzle = Puzzle()
puzzle.generate_random_puzzle()
#generateHints(puzzle.current_word_list, puzzle.pangram, puzzle.total_points)

#individual functions
generateLetters()
generatePoints()
generatePangramCount(puzzle.current_word_list, puzzle.pangram)
generateWordCount(puzzle.current_word_list)
var = generateLetterMatrix(puzzle.current_word_list, puzzle.pangram)
generateTwoLetterDictionary(puzzle.current_word_list)
generateBingo(var)

