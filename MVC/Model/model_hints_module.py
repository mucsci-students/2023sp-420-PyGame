"""
    generateHints 
    Takes Three Parameters
        Words: List of words from puzzle
        Letters: Array of letters from the model
        Points: Total points in the puzzle
    Returns
         1d array of [letters, word_count, points, pangram_count], a list[list[str]] letter counts with 
         letters and word lengths in the rows and columns, 
         and dictionary Of First Two Letters with the letters as the key and count as the pair
"""
def generateHints(words, letters, points): 
    word_count = 0
    pangram_count = 0
    #points = 0#some function call
    dictOfFirstTwoLetters = {}
    
    if(words == [] or len(letters) < 7):
        return 1
    #gets max length of all words
    maxLength = len(max(words, key=len))   
    if(maxLength < 7):
        return 1
    # Initialize letterCountArray2d 
    # (maxLength - 1) for maxLength -3 for lengths + total + column label
    # 9 is for 7 letters + total + row label
    letterCountArray2d = [[str(0)]*(maxLength - 1)]*9 
    
    letter_index = 1
    for i in letters:
        letterCountArray2d[letter_index][0] = str(i)
        letter_index += 1
    letterCountArray2d[8][0] = "tot"
    
    for i in range(1, maxLength - 2):
        letterCountArray2d[0][i] = str(i)
    letterCountArray2d[0][maxLength - 2] = "tot"
    
    
    # total words at [7][maxlength - 4] is total words
    # count the total number of words 
    for word in words:
        word_count += 1
#        length = word
        # check if the word is a pangram
        current_word_length = len(word)
        # Boilerplate  for indexing string
        if current_word_length < 2:
            return "Hint Calc error: word not long enough"
        # count the starting letters of the word
        first_letter = word[0]
        twoLetters = word[0:2]         
        if(current_word_length >= 7 ):
            if all(letter in word for letter in letters):
                pangram_count += 1
        
        # Check 2 letter directory, give it 2 letters, to count the words of each unique combo, 
        #adds entry to 2 letter dict 
        if twoLetters not in dictOfFirstTwoLetters: 
            dictOfFirstTwoLetters[twoLetters] = 0
        dictOfFirstTwoLetters[twoLetters] += 1
        letterCountArray2d[letters.index(first_letter) + 1][current_word_length - 3] = \
            int(letterCountArray2d[letters.index(first_letter) + 1][current_word_length - 3]) + 1 #Check syntax here 


#LETTER MATRIX
    # Totals Rows
    for letter in letters:
        row_total = 0
        for i in range(1, maxLength - 2):#uninclusive end
            row_total += int(letterCountArray2d[letters.index(letter) + 1][i])
        letterCountArray2d [letters.index(letter) + 1][maxLength - 2] = str(row_total)
    # Totals Columns
    for j in range(1, maxLength - 1):#uninclusive end
        count = 0 
        for i in range(1,8):
            count += int(letterCountArray2d[i][j])
        letterCountArray2d [8][j] = str(count)
#ASSEMBLES 2 LETTER COUNTS
    dictOfFirstTwoLetters = sorted(dictOfFirstTwoLetters)
    
    letters = str(letters)
    word_count = str(word_count)
    points = str(points)
    pangram_count = str(pangram_count)
    # returns array of letters word count points and pangram, then a list[list[str]] of the letters and count array, 
    # then a dictionary of the two letters words start with
    return [letters, word_count, points, pangram_count], letterCountArray2d, dictOfFirstTwoLetters#, twoLetters_counts

