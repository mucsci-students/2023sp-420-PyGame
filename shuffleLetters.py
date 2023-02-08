
import random           # Used for shuffling letters
import sys              # Used to exit function (invalid puzzleKey length)

puzzleKey = "twinkle"   # Global variable test



"""
ShuffleKey function
    curr; STR

Function shuffles the letters in the current word when the shuffle command
is entered.

Rundown:
    - Converts current word into all lowercase, if not already
    - Checks for valid word length
    - If the word is the puzzleKey (unshuffled word), the required letter is
      at index 0
    - If the word is an already shuffled word, the required letter is index 3
    - Take the required letter out of the word, shuffle the other 6 letters
    - Insert the required letter back into the middle (index = 3)
    - Return the shuffled word

"""
def ShuffleKey(curr):

    # (Is this global variable here correct?)
    global puzzleKey

    curr = curr.lower()

    LengthPrereq(curr)

    if curr != puzzleKey:
        requiredKey = curr[3]
    else:
        requiredKey = puzzleKey[0]

    result = curr.replace(requiredKey, '')
    result = random.sample(result, len(result))
    result.insert(3, requiredKey)
    result = ''.join(result)

    return result



"""
LengthPrereq function
    word; STR

Function to check if the length of the puzzleKey is exactly 7 letters long.

Rundown:
    - If the word is not exactly 7 letters in length, then exit function
    - Otherwise, do nothing
"""
def LengthPrereq(word):
    if len(word) < 7 or len(word) > 7:
        print("puzzleKey is " + str(len(word)) + " letters long..")
        sys.exit()






"""

################################### TESTS ###################################

# base words (requiredKey at index 0):
puzzleKey = "twinkle"
print(ShuffleKey(puzzleKey))      # t is required letter

puzzleKey = "fedoras"
print(ShuffleKey(puzzleKey))      # f is required letter

puzzleKey = "munches"
print(ShuffleKey(puzzleKey))      # m is required letter

#############################################################################

# already shuffled words (requiredKey at index 3):
print(ShuffleKey("nlupgre"))      # p is required letter (puzzleKey = plunger)
print(ShuffleKey("odbamne"))      # a is required letter (puzzleKey = abdomen)
print(ShuffleKey("irbvnat"))      # v is required letter (puzzleKey = vibrant)

"""