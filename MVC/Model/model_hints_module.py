
#TODO imports

#TODO Abstract the big mess.
#TODO figure out top and side placement for word length  ???? (maybe just for output)   and side for letters



"""
    generateHints Takes Two Parameters
        Words: List of words from puzzle
        Letters: Array of letters from the model

    Returns an array of letters and word lengths  
    # 1d array of [letters, word_count, points, pangram_count], 2d array of letter counts  with letters and word lengths, 
    and dictionary Of First Two Letters with the letters as the key and count as the pair
"""
def generateHints(words, letters): 
    word_count = 0
    pangram_count = 0
    points = 0#some function call
    dictOfFirstTwoLetters = {}
    
    if(words == [] or len(letters) < 7):
        return 1
    # will contain the total length, maxLength - 3 will be the total length of the Y axis(includes 4 to max and sum) counting from 0
    maxLength = 7 #min
    #[1]
    #twoLetters_counts = []
           
    #words.sort(key=len)
    #gets max length of all words
    maxLength = len(max(words, key=len))  
    #maxLength = len(words[-1]) #assumes list is sorted by size
    #if(maxLength < 7):
    #    return 1#list not sorted
    #currently a touple,, Would be treated as a 2d array 
    #letterCountArray2d = [[0 for x in range(maxLength - 3)] for y in range(8)]  #no words less than leanth of 4    #changed to reflect non inclusive aspect of range to - 3 adn 8   
    # 
    # Initialize array
    
    letterCountArray2d = [8][maxLength - 2] #Vectorize  #changed to -3 from -4 
    letterCountArray2d[0][0] = ""
    letter_index = 1
    for i in letters:
        letterCountArray2d[letter_index [0]] = i
        letter_index += 1
    letterCountArray2d[8][0] = "tot"
    
    for i in range(1, maxLength - 2):
        letterCountArray2d[0][i] = i
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
            #twoLetters_counts.append(0)
        dictOfFirstTwoLetters[twoLetters] += 1
        #twoLetters_counts[dictOfFirstTwoLetters.index(twoLetters)] += 1        

        #print(f"{word} first letter {i}, length  {l}")
        letterCountArray2d[letters.index(first_letter) + 1][current_word_length - 3] += 1 #Check syntax here 
#    total_score = some function
    '''
    output = letters  #bold  required letter
    output += f"words: {word_count} points:  pangrams: {pangram_count}\nLetter Matrix:\n"
    '''

#LETTER MATRIX
    # Totals Rows
    for letter in letters:
        #row_str = letter + "\t"
        row_total = 0
        for i in range(1, maxLength - 2):#uninclusive end
            #count = letterCountArray2d[letters.index(letter)[i]] 
            row_total += letterCountArray2d[letters.index(letter) + 1][i] 
        letterCountArray2d [letters.index(letter) + 1][maxLength - 2] = row_total
    # Totals Columns
    for j in range(1, maxLength - 1):#uninclusive end
        count = 0 
        for i in range(1,8):
            count += letterCountArray2d[i][j]
        letterCountArray2d [8][j] = count
#ASSEMBLES 2 LETTER COUNTS
    dictOfFirstTwoLetters = sorted(dictOfFirstTwoLetters)
    '''
    str_two_letter_list = f"{dictOfFirstTwoLetters[0]}: {twoLetters_counts[0]} " 
    for i in range(1, len(dictOfFirstTwoLetters)): 
       
        #compares first letter in 2 letters to previous print, if different, new line
        if((dictOfFirstTwoLetters[i])[0] != (dictOfFirstTwoLetters[i - 1])[0]):
            str_two_letter_list += '\n'
        str_two_letter_list += f"{dictOfFirstTwoLetters[i]}: {twoLetters_counts[i]} " 
    output += str_two_letter_list
    '''
    #print(output)
    return [letters, word_count, points, pangram_count], letterCountArray2d, dictOfFirstTwoLetters#, twoLetters_counts
def generalStats():
    if(word_count == 0):
        return 1
    return [letters, word_count, points, pangram_count]
def dictOfFirstTwoLetters():
    if (dictOfFirstTwoLetters == []):
        return 1
    return dictOfFirstTwoLetters
def LetterCountArray2d():
    if(letterCountArray2d == []):
        return 1
    return letterCountArray2d
generateHints(["whiskey", "whisk"], "whiskey")