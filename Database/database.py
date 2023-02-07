import json
import sqlite3
import random

# connect to the database
conn = sqlite3.connect("Database/allwords")
cursor = conn.cursor()

def generate_table():
# load the JSON data from the file
  with open("Database/dictionary.json", "r") as f:
    data = json.load(f)

  # create a table to store the data
  conn.execute("""
  CREATE TABLE IF NOT EXISTS all_words (
    key TEXT,
    word TEXT,
    points INTEGER
  )
  """)
  conn.execute("""
  CREATE TABLE IF NOT EXISTS word_info (
    key TEXT,
    required_letter TEXT,
    total_points INTEGER
  )
  """)

  # insert the data into the table
  for key, values in data.items():
      required_letter = values[0]
      total_points = values[1]
      conn.execute("""
      INSERT INTO word_info (key, required_letter, total_points)
      VALUES (?,?,?)
      """, (key, required_letter, total_points, ))

      for word, points in values[2].items():
          conn.execute("""
          INSERT INTO all_words (key, word, points)
          VALUES (?,?,?)
          """, (key, word, points, ))
          
""" 
  Author: Robert 2/3/23
  Last Edited:
  Parameters: 1 paramter
    "Key" string
  Returns: A dictionary
  Definition: Return list of possible words for panagram given a keyword.
"""

def get_word_list(key):
  conn = sqlite3.connect("Database/allwords")
  cursor = conn.cursor()
  cursor.execute("SELECT word, points FROM all_words WHERE key=?", (key,))
  words = cursor.fetchall()
  dictionary = {}
  for key, value in words:
    dictionary.setdefault(key, value)
  conn.commit()
  conn.close()
  return dictionary

""" 
  Author: Robert 2/3/23
  Last Edited:
  Returns: A list - ('string', 'string', int)
  Definition: Returns ('panagram', 'required letter', total_points)
"""

def get_word_info():
  conn = sqlite3.connect("Database/allwords")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM word_info")
  info = cursor.fetchall()
  conn.commit()
  conn.close()
  return info

""" 
  Author: Robert 2/3/23
  Last Edited:
  Returns: string
  Definition: Returns a random keyword from list of possible words.
"""

def get_random_word(panagram_list):
  rand_num = random.randint(0, len(panagram_list))
  return panagram_list[rand_num]

# all_words = get_word_info()
# rand_word = get_random_word(all_words)
# print(rand_word)
# print(rand_word[0])

# cursor.execute("DROP TABLE all_words")
# cursor.execute("DROP TABLE word_info")
# generate_table()

# save the changes and close the connection
conn.commit()
conn.close()