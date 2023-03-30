from model_puzzle import *
from collections import OrderedDict
#from array import *
'''    
m_letters = puzzle.pangram
m_word_count = 0
m_points = puzzle.total_points
m_pangram_count = 0
m_letterMatrix = [[str()]]
m_twoLetterDictionary = {}
#puzzle = puzzle.stats
m_words =  puzzle.current_word_list'''


# Returns string of letters for the current puzzle
def generateLetters():
    return puzzle.pangram
# Returns string of word count
def generateWordCount(words):
    return str(len(words))
# Returns str of points
def generatePoints():
    return str(puzzle.total_points)
# Returns string of pangram counts
def generatePangramCount(words, letters):
    #words = puzzle.current_word_list
    #letters = puzzle.pangram
    pangram_count = 0
    for word in words:
        if(len(word) >= 7 ):
            if all(letter in word for letter in letters):
                pangram_count += 1    
    return str(pangram_count)

# Parmeters: the words of the current_puzzle as list and the puzzle.pangram as list of letters
# Returns  list[list[str]] of the letters and count array
def generateLetterMatrix(words, letters):
   # words = puzzle.current_word_list
    #letters = puzzle.pangram
    
    if(words == [] or len(letters) < 7):
        return 1
    #gets max length of all words
    maxLength = len(max(words, key=len))   
    if(maxLength < 7):
        return 1
    # Initialize letterMatrix 
    # (maxLength - 1) for maxLength -3 for lengths + total + column label
    # 9 is for 7 letters + total + row label
    letterMatrix = []
    for i in range(0, 9):
        letterMatrix.append([str(0)]*(maxLength - 1))
    
    letter_index = 1
    for i in letters:
        letterMatrix[letter_index][0] = i
        letter_index += 1
    letterMatrix[8][0] = "tot"
    #Initialized word length on top column

    for i in range(1, maxLength - 2):
        letterMatrix[0][i] = str(i + 3)
    letterMatrix[0][maxLength - 2] = "tot"
    for word in words:
        word_column = len(word) - 3
        first_letter = word[0]
        word_row = letters.index(first_letter.upper()) + 1
        letterMatrix[word_row][word_column] = str(int(letterMatrix[word_row][word_column]) + 1 )


    '''
    
    column_totals = []
    for i in range(0, maxLength - 1):
        column_totals.append(0)
    for j in range(1,7):
        row_total = 0
        for i in range(1, maxLength - 1):#uninclusive end
            val = int(letterMatrix[j][i])
            row_total += val
            column_totals[i] += val
        letterMatrix [j][maxLength - 2] = str(row_total)
    for j in range(1, maxLength - 1)
        letterMatrix [j][maxLength - 2] = str(column_totals[j])
    '''
    
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
# Returns Dictionary of countaining  starting two letters : count AS (str) : (int)
def generateTwoLetterDictionary(words):
    #words = puzzle.current_word_list    
    twoLetterDictionary = {}
    for word in words:
        twoLetters = word[0:2]
        if twoLetters not in twoLetterDictionary: 
            twoLetterDictionary[twoLetters] = 0
        twoLetterDictionary[twoLetters] += 1
    #twoLetterDictionary = sorted(twoLetterDictionary)
    dict1 = OrderedDict(sorted(twoLetterDictionary.items()))
    return dict1
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
'''
# Testing
#Working
 
testletters = 'LZAETQU'
require_letter = "Q"
word_list = ['quetzal', 'equate', 'quelea', 'quezal', 'aquae', 'equal', 'quale', 'quate', 'quell', 'queue', 'tuque', 'aqua']


#individual function testing
generateLetters()
generatePoints()
generatePangramCount(word_list, testletters)
generateWordCount(word_list)

var = generateLetterMatrix(word_list, testletters)
#print(var)
dicton = generateTwoLetterDictionary(word_list)
print(dicton.keys())
for x, y in dicton.items():
  print(x, y)
#print(generateBingo(var))

'''
