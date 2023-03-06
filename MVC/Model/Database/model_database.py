'''
  Author: Robert Corle
  Date: 2/12/23
'''
import sqlite3
import random
import os
'''
  generate_table()
    Creates our table using the .txt files in Database/Individual_letters where
    each file contains only words that contain a given letter.
'''

def generate_table():
  conn = sqlite3.connect("MVC/Model/Database/wordDB")
  cursor = conn.cursor()

  # Create the table to store the words
  columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' + ','.join(['{} text'.format(chr(97+i)) for i in range(26)])
  cursor.execute(f"CREATE TABLE IF NOT EXISTS words ({columns})")
  conn.commit()

  # Loop through each file and add one word from each file to the table
  for i in range(26):
      with open(f'MVC/Model/Database/Individual_letters/words_with_{i+1}.txt', 'r') as file:
          lines = file.readlines()
          for j, line in enumerate(lines):
              cursor.execute(f"UPDATE words SET {chr(97+i)}=? WHERE id=?", (line.strip(), j+1))
              if cursor.rowcount == 0:
                  cursor.execute(f"INSERT INTO words ({','.join([chr(97+k) for k in range(26)])}) VALUES ({','.join(['?' for k in range(26)])})", [None if k != i else line.strip() for k in range(26)])

  # Commit the changes to the database
  conn.commit()

  # Close the connection to the database
  conn.close()

'''
  get_word_info_from_pangram(pangram)
    Given a pangram:
      1. Generate a puzzle with a required letter. 
      2. Calculate the max points of this puzzle.
      3. Find all possible words.
      4. Returns as a list[word, letter, total_score, puzzle_list]
'''

def get_word_info_from_pangram(pangram):
  # Make connection to DB.
  conn = sqlite3.connect("MVC/Model/Database/wordDB")
  cursor = conn.cursor()
  letter, pangram = get_puzzle_from_pangram(pangram)

  puzzle_list = get_possible_words(cursor, letter, pangram)
  total_score = get_total_points(puzzle_list)
  conn.commit()
  conn.close()
  return([pangram, letter, total_score, puzzle_list])

def get_word_info_from_load(pangram, letter):
  # Make connection to DB.
  conn = sqlite3.connect("MVC/Model/Database/wordDB")
  cursor = conn.cursor()

  puzzle_list = get_possible_words(cursor, letter, pangram)
  total_score = get_total_points(puzzle_list)
  conn.commit()
  conn.close()
  return([pangram, letter, total_score, puzzle_list])
  
'''
  get_puzzle_from_pangram(cursor, pangram)
    Given a DB connection and pangram, generate a required letter and find
      a word with the pangram + required letter.
'''

def get_puzzle_from_pangram(pangram):
    # use random letter from pangram as required.
    letter = random.choice(pangram)
    return letter, pangram

'''
  get_random_word_info()
    1. Connect to the database. 
    2. Randomly select a required letter and its pangram.
    3. Find all words fitting the above criteria.
    4. Calculate the total possible score for this puzzle.
    5. Returns as a list[word, letter, total_score, puzzle_list]
'''

def get_random_word_info():
  # Make connection to DB.

  conn = sqlite3.connect("MVC/Model/Database/wordDB")
  cursor = conn.cursor()
  while True:
    letter, word = get_random_puzzle_word(cursor)
    puzzle_list = get_possible_words(cursor, letter, word)
    # If list of words to guess is 0, that's boring. Generate again.
    if len(puzzle_list) >= 1:
      break
  total_score = get_total_points(puzzle_list)
  conn.commit()
  conn.close()
  # return puzzle, letter, total_score, list of possible words
  return([word, letter, total_score, puzzle_list])

'''
  get_random_puzzle_word(cursor)
    Given a DB connection, generate a random puzzle by first selecting a 
      letter of the alphabet as a required letter. Then, grab the column
      correlating to that required letter. Find all 7 letter pangrams having
      the required letter, and choose one at random to be the puzzle.
'''

def get_random_puzzle_word(cursor):
  # Column names are letters and correspond to required letter.
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letter = random.choice(alphabet)

  # Execute the query
  cursor.execute(f'SELECT {letter} FROM words')
  words = cursor.fetchall()

  # Filter out words that are of length 7 and have all unique characters.
  result = []
  for word in words:
    try:
      if len(word[0]) == 7 and len(set(word[0])) == 7:
        result.append(word[0])
    except TypeError:
      pass
  
  # Grab a random word from this filtered list.
  word = random.choice(result)
  return letter, word

'''
  get_possible_words(cursor, required_letter, word)
    Given a DB connection, required letter, and word.
      1. Find the column relating to the required letter.
      2. Retrieve all words containing that letter && is made up of the given pangram.
'''

# Return all words that can be spelled with the required letter + pangram.
def get_possible_words(cursor, required_letter, word):
  # Query a list of words that contain ONLY the required letter and the characters from the passed in word.
  query = "SELECT {} FROM words WHERE {} GLOB '*{}*' AND {} NOT GLOB '*[^{}]*'".format(required_letter, required_letter, required_letter, required_letter, word)
  cursor.execute(query)

  # Fetch all the results of the query
  results = cursor.fetchall()
  return results

'''
  get_total_points(puzzle_list)
    Given a list of words for a puzzle, calculate it's total by:
      1. A word of length 4 is 1 point.
      2. A word whose set() is the same length as itself is (length)*2 points.
      3. A word whose length is larger than 4 is length points.
'''

def get_total_points(puzzle_list):
  total_points = 0
  for word in puzzle_list:
    length = len(word[0])
    # If length of word is 4, worth 1 point.
    if length == 4:
      total_points += 1
    # If word is a pangram, worth length * 2
    elif length == 7 and len(set(word)) == 7:
      total_points += (length)*2
    # Else word is worth its length
    else:
      total_points += length
  return total_points