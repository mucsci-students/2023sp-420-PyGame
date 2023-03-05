

# define the file path and list of letters
filename = "whiskey.txt"
letters = ["w", "h", "i", "s", "k", "e", "y"]

def main(): 
    
#def count_letters(filename, letters):
    # initialize variables
    filename = "whiskey.txt"
    letters = ["w", "h", "i", "s", "k", "e", "y"]
    
    words = []
    word_count = 0
    pangram_count = 0
    maxLength = 7
    listOfFirstTwoLetters = []
    twoLetters_counts = []

    # loop through each line in the file
    with open(filename, "r") as f:
        for line in f:
            # split the line into words 
            words += line.strip().lower()
    words.sort(key=len)
    #generates array based on longest word in length, TODO INIT all to 0?

    #gets max length of all words  
  
    maxLength = len(words[-1])

    #currently a touple,, Would be treated as a 2d array 
    letterCountArray2d = (7, maxLength)                                                             #FLAG

    # count the total number of words
    for word in words:
        word_count += 1
#        length = word
        # check if the word is a pangram
        if all(letter in word for letter in letters):
            pangram_count += 1
        #boilerplate for indexing string
        if len(word) < 2:
            return "Hint Calc error: word not long enough"
        # count the starting letters of the word
        first_letter = word[0]
        twoLetters = first_letter + word[1] 

        # Check 2 letter directory, give it 2 letters, to count the words of each unique combo, 
        # #Initially all is unsorted as nescicity, we'll get there latter 
        #adds entry to 2 letter dict 
        if twoLetters not in listOfFirstTwoLetters: 
            listOfFirstTwoLetters.append(twoLetters)
            twoLetters_counts.append(0)
        twoLetters_counts[listOfFirstTwoLetters.index(twoLetters)] += 1
        
        
        #letterCountArray2d[twoLetters].update({"twoLetters" :letterCountArray2d.get(letterCountArray2d) + 1 }) #+= 1 #Check syntax here

       # if first_letter not in twoLetters_counts: #adds entry to 1 letter 
       #    twoLetters_counts[first_letter] = {}
       # if len(word) not in twoLetters_counts[first_letter]:
      #      twoLetters_counts[first_letter][len(word)] = 0
        letterCountArray2d(letters.index(first_letter), len(word) - 4) += 1 #Check syntax here
    
    # #Ordered to catch all
    # #Calculate sums by row
    # for i in range(0, 7):
    #     count = 0
    #     for j in range(0, maxLength):
    #         count += letterCountArray2d[i][j]
    #     letterCountArray2d[i][maxLength] = count #sum(letterCountArray2d[i][range(0, maxLength)])
    # #Calculate sums by column
    # for i in range(0, maxLength + 1):
    #     count = 0
    #     for j in range(0, 8):
    #         count += letterCountArray2d[j][i]
    #     letterCountArray2d[8][i] = count


    # print the results
    output = ""
    output += f"words: {word_count} pangrams: {pangram_count}\nLetter Matrix:\n"
    #     print(f"total score; {get from another F#call}\n")




##below be dragons

 #letter counts be    letterCountArray2d

    ##Prnt the two letters output here
#LETTER MATRIX
    # ADD from 4 to maxLength + \ttot
    str = "\t4\t5\t6\t7"
    if maxLength > 7:
        for s in range(8,maxLength):
            str + f"\t{s}"     
    str += "\ttot\n"

    for letter in letters:
        row_str = letter + "\t"
        row_total = 0
        for i in range(0, maxLength):
            count = letterCountArray2d[letters.index(letter)][i]  
            row_str += f"{count}\t"
            row_total += count
        row_str += f"{row_total}"
        output += row_str
    tot_str = "tot\t"
    tot_total = 0
    
    ##check
    for i in range(0, maxLength + 1):
        count = 0 
        for j in range(0,7):
            count += letterCountArray2d[i][j]

        tot_str += f"{count}\t"
        tot_total += count
    tot_str += f"{tot_total}"
    #print(tot_str) #will return instead

    output += str + tot_str +"\nTwo letter list:\n"

    #Print 2 letter counts

    #TODO Sort the  listOfFirstTwoLetters = []
    # twoLetters_counts = []
    str2 += f"{listOfFirstTwoLetters[0]}: {twoLetters_counts[0]} " 
    for i in range(1, length(listOfFirstTwoLetters)):
        str2 += f"{listOfFirstTwoLetters[i]}: {twoLetters_counts[i]} " 
        #compares first letter in 2 letters to previous print, if different, new line
        if((listOfFirstTwoLetters[i])[0] != (listOfFirstTwoLetters[i - 1])[0]):
            str2 += '\n'


    print(output)


#(filename, letters)