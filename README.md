# Spelling Bee Game by PyGame
---

## Table of Contents
- [Summary](#summary)
    - [Features](#features)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [How to Run Test](#how-to-run)
- [How to Play](#how-to-play)
    - [Point System](###Rewarded-points)
    - [Rank System](###Ranks)
- [Team](#team-members)
---

## Summary:

A simple game where a player is to create English words using a number of given characters, but the word has to use the required character.

### Features
- Large selection of randomly generated puzzles.
- Ability to create your own puzzle by inputting a word with seven unique characters.
- Word puzzles can be stored and accessed at a later time.
- Share a puzzle with a friend by generating a sharable key, unique to that puzzle.
- Display usefull hints generated for each puzzle
- Choice of playing the game on a CLI or GUI.


---

## Setup:

1. Download and install [Python 3.11.1](https://www.python.org/downloads/). 
2. Clone the main branch of [PyGame's repository](https://github.com/mucsci-students/2023sp-420-PyGame) from Github to your local machine.
3. Navigate to the cloned repository and set up virtual environment with the following command
    - ``` python3 -m venv venv ``` 
4. Activate the virtual environment with 
    - Windows:
    ``` .\venv\Scripts\activate ```
    - Mac:
    ``` source venv/bin/activate ```
5. Install project dependencies go to the directory for the project by running the following commands:
    - Mac:
    ``` pip install -r requirements.txt ```
    - Windows:
    ``` pip install -r requirements.txt ```
6. Install our PyGame directory to your venv with the following commands:
    - Mac:
    ``` python3 -m pip install -e . ```
    - Windows:
    ``` python -m pip install -e . ```
---

## How to Run:

1. Open your terminal or command interface and navigate to your `2023sp-420-PyGame` directory.

2. Activate the virtual environment with ``` .\venv\Scripts\activate ```

5. Once you are in the venv, type ```PyGame``` to launch our game, it will default to run the game with a GUI active. 
    - if you want to run our project in CLI run the following argument after PyGame ``` -- cli ``

6. If you are lost and need any help once the game is launched, type `/help` for more details

---

## How to Run Test:

1. Open your terminal or command interface and navigate to your `2023sp-420-PyGame` directory.

2. Activate the virtual environment with ``` .\venv\Scripts\activate ```

3. Once you are in the venv, type ```pytest``` to run our project test 
    - to see code coverage run ``` pytest --cov ```
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

Every puzzle has 10 ranks that will progress and change based on the percentage that the puzzle is completed:

|   Rank     | Completed % |
|------------|-------------|
| Beginner   |     <2%     |
| Good Start |      2%     |
| Moving Up  |      5%     |
| Good       |      8%     |
| Solid      |     15%     |
| Nice       |     25%     |
| Great      |     40%     |
| Amazing    |     50%     |
| Genius     |     70%     |
| Queen Bee  |    100%     |
<br>
</details>

<br>

---

## Team Members:

| [![Kiah bucher](https://avatars.githubusercontent.com/u/70379821?v=4)](https://github.com/WhitePolaris) | [![Robert Corle](https://avatars.githubusercontent.com/u/93812563?v=4)](https://github.com/RjCor) | [![Ben Nase](https://avatars.githubusercontent.com/u/121914115?v=4)](https://github.com/bennase) | [![Priscilla Tran](https://avatars.githubusercontent.com/u/81700428?v=4)](https://github.com/priscillatran) | [![Ethan Wright](https://avatars.githubusercontent.com/u/122811350?v=4)](https://github.com/EthanWright24) |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Kiah Bucher](https://github.com/WhitePolaris)                                                          | [Robert Corle](https://https://github.com/RjCor)                                                  | [Ben Nase](https://github.com/bennase)                                                           | [Priscilla Tran](https://github.com/priscillatran)                                                          | [Ethan Wright](https://github.com/EthanWright24)                                                           |
