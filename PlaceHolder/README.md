# Spelling Bee Game by PyGame
---

## Table of Contents
- [Summary](#summary)
    - [Features](##Features)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
    - [Point System](###Rewarded-points)
    - [Rank System](###Ranks)
- [Team](#Team-Members)
---

## Summary:

A simple game where a player is to create English words using a number of given characters, but the word has to use the required character.

### Features
- Large selection of randomly generated puzzles.
- Ability to create your own puzzle by inputting a word with seven unique characters.
- Word puzzles can be stored and accessed at a later time.
- Share a puzzle with a friend by generating a sharable key, unique to that puzzle.
- Choice of playing the game on a CLI or GUI.


---

## Setup:

1. Download and install [Python 3.11.1](https://www.python.org/downloads/). 
2. Clone the main branch of [PyGame's repository](https://github.com/mucsci-students/2023sp-420-PyGame) from Github to your local machine.
3. Install priject dependencies go to the directory for the repo and run the following commands:
    - Mac:
    ``` pip3 install -r mac_requirements.txt ```
    - Windows:
    ``` pip install -r win_requirements.txt ```

---

## How to Run:

1. Open your terminal or command interface and navigate to your `2023sp-420-PyGame` directory.
2. Once you are in the `2023sp-420-PyGame` directory, type ```python -- cli``` to launch our game in CLI for Window Users or ```python3 pygame -- cli``` for Mac Users, and ```pygame pygame.py``` to launch our game in GUI. 
    - if you want to run test run the following argument after pygame ``` ---test--- ``
3. If you are lost and need any help once the game is launched, type `/help` for more details


---

## How to Play:

Create words using letters from the hive and try to get the maximum score. Words must have at least four letters and include the required letter (The letter in the center of the hive). The required letter is surrounded by six letters that you use additionally (not required). Use the six additional letters along with the required letter to create words. Using letters that are not given will result in either a wrong answer or may not be entered to begin with. Every letter can be used more than one time in a single guess. Word guesses can not contain hyphens, proper nouns, vulgarities, or obscure words. Each puzzle includes at least one “pangram” which uses all seven given letters at least once.

<br>

<details>
<summary style="font-weight:bold;font-size:11.5pt;">Rewarded Points:</summary>

- 4-letter words are worth 1 point each.
- If the entered word is longer than 4 letters then you get a point for the word's character length
- Each puzzle includes at least one “pangram” which uses every letter at least once.
- Words guesses that use all seven given letters will earn double amount of points
</details>

<br>

<details>
<summary style="font-weight:bold;font-size:11.5pt;">Ranks:</summary>

Every puzzle has eight ranks that will progress and change based on the percentage that the puzzle is completed

 -  |   Rank   | Completed % |
    |----------|-------------|
    | Beginner |      3%     |
    | Novice   |      7%     |
    | Okay     |     12%     |
    | Good     |     23%     |
    | Solid    |     35%     |
    | Nice     |     56%     |
    | Great    |     72%     |
    | Amazing  |     92%     |
<br>
</details>

<br>

---

## Team Members:

| [![Kiah bucher](https://avatars.githubusercontent.com/u/70379821?v=4)](https://github.com/WhitePolaris) | [![Robert Corle](https://avatars.githubusercontent.com/u/93812563?v=4)](https://github.com/RjCor) | [![Brendan LeFevre](https://avatars.githubusercontent.com/u/26367420?v=4)](https://github.com/BrendanLeFevre) | [![Ben Nase](https://avatars.githubusercontent.com/u/121914115?v=4)](https://github.com/bennase) | [![Priscilla Tran](https://avatars.githubusercontent.com/u/81700428?v=4)](https://github.com/priscillatran) | [![Ethan Wright](https://avatars.githubusercontent.com/u/122811350?v=4)](https://github.com/EthanWright24) |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Kiah Bucher](https://github.com/WhitePolaris)                                                          | [Robert Corle](https://https://github.com/RjCor)                                                  | [Brendan LeFevre](https://github.com/BrendanLeFevre)                                                          | [Ben Nase](https://github.com/bennase)                                                           | [Priscilla Tran](https://github.com/priscillatran)                                                          | [Ethan Wright](https://github.com/EthanWright24)                                                           |
