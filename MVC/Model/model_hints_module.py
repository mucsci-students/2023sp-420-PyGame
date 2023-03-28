"""
    generateHints: must be called first
    Takes Three Parameters
        Words: List of words from puzzle
        Letters: Array of letters from the model
        Points: Total points in the puzzle
    Returns 0
"""

m_letters = []
m_word_count = 0
m_points = 0
m_pangram_count = 0
m_letterMatrix = [[str()]]
m_twoLetterDictionary = {}

def generateHints(words, letters, points): 
    m_letters = letters
    
    word_count = 0
    pangram_count = 0
    #points = 0#some function call
    twoLetterDictionary = {}
    
    
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
    
    
    # total words at [7][maxlength - 4] is total words
    # count the total number of words 
    for word in words:
    # Word Count
        word_count += 1
        current_word_length = len(word)
        # Boilerplate  for indexing string
        if current_word_length < 2:
            return "Hint Calc error: word not long enough"
        # Get the starting letters of the word
        first_letter = word[0]
        twoLetters = word[0:2]     
    # Pangram Check   
        if(current_word_length >= 7 ):
            if all(letter in word for letter in letters):
                pangram_count += 1
        
        # Check 2s letter directory, give it 2 letters, to count the words of each unique combo, 
        #adds entry to 2 letter dict
        
    #  Collect and count starting 2 letters 
        if twoLetters not in twoLetterDictionary: 
            twoLetterDictionary[twoLetters] = 0
        twoLetterDictionary[twoLetters] += 1
    # Counts letter into matrix
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
#ASSEMBLES 2 LETTER COUNTS
    twoLetterDictionary = sorted(twoLetterDictionary)
    
    letters = str(letters)
    word_count = str(word_count)
    points = str(points)
    pangram_count = str(pangram_count)
    
    m_letters = letters
    m_word_count = word_count
    m_points = points
    m_pangram_count = pangram_count
    m_letterMatrix = letterMatrix
    m_twoLetterDictionary = twoLetterDictionary
    
   
    return 0 

# Returns string of letters
def getLetters():
    return m_letters
# Returns string of word count
def getWordCount():
    return m_word_count
# Returns string of points
def getPoints():
    return m_points
# Returns string of pangram counts
def getPangramCount():
    return m_pangram_count
# Returns  list[list[str]] of the letters and count array
def getLetterMatrix():
    return m_letterMatrix
# Returns Dictionary of countaining  starting two letters : count
def geTwoLetterDictionary():
    return m_twoLetterDictionary

