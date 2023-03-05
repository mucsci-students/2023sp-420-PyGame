import string
from array import *

def count_letters(filename, letters):
    # initialize counters
    word_count = 0
    pangram_count = 0
    two_letter_counts = {}
    letter_counts = []
    max_word_length = 15

    # initialize letter and length lists
    letter_list = list(letters.upper())
    length_list = list(range(4, max_word_length + 1))

    # initialize array
    array = [[" "]+[str(i) for i in length_list]+["tot"]]
    for letter in letter_list:
        array.append([letter]+["-" for _ in range(len(length_list))]+[0])  # check output for -  if needed or remove

    # read file and count letters
    with open(filename, 'r') as f:
        for line in f:
            for word in line.strip().split():
                # check for pangram
                if set(word.upper()) == set(letters.upper()):
                    pangram_count += 1

                # count first two letters
                if len(word) > 1:
                    two_letters = word[:2].upper()
                    if two_letters in two_letter_counts:
                        two_letter_counts[two_letters] += 1
                    else:
                        two_letter_counts[two_letters] = 1

                # count first letter and word length
                if len(word) in length_list:
                    first_letter = word[0].upper()
                    if first_letter in letter_counts:
                        letter_counts[first_letter] += 1
                    else:
                        letter_counts[first_letter] = 1

                    index = length_list.index(len(word)) + 1
                    array[letter_list.index(first_letter)][index] =  array[letter_list.index(first_letter)][index] + 1  # + 1 aft first letter()

                # count words
                word_count += 1

    # calculate total counts and add to array
    for i in range(1, len(letter_list) + 1):
        total_count = sum(array[i][1:-1])
        array[i][-1] = total_count

    # format and print results
    print(f"words: {word_count}")
    print(f"pangrams: {pangram_count}\n")
    for letter in letter_list:
        print(f"{letter}: ", end="")
        for i in range(1, len(length_list) + 2):
            print(f"{array[letter_list.index(letter) + 1][i]:<2}", end="")
        print("")
    print("'Two letter list:'")
    print("\t".join([""] + [str(i) for i in length_list] + ["tot"]))
    for letter in string.ascii_uppercase:
        two_letter_count = 0
        two_letter_list = []
        for key, value in two_letter_counts.items():
            if key.startswith(letter):
                two_letter_count += value
                two_letter_list.append(key)
        if two_letter_count > 0:
            print(f"{letter}\t", end="")
            for length in length_list:
                count = sum([1 for w in two_letter_list if len(w) == length])
                print(f"{count:<2}", end="")
            print(f"{two_letter_count}")
count_letters("whiskey.txt", "whiskey")