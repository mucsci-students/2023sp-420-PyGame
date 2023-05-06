from PyGame_Project.MVC.Model.Database.model_highscores import *

# If None, no tables exist. 
def test_generate_table():
    cursor = generate_tables()
    result = cursor.execute("SELECT name FROM sqlite_master")
    assert result.fetchone() is not None



import pytest


from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *

## default puzzle generation for testing 
pytest.fixture
def puzzleGen():
    PuzzleStats().clear()
    shareable_key = "ygyxjrfq"
    prep_game_from_share(shareable_key)
    

def test_insert():
    puzzleGen()

    insert_or_update_score("test", PuzzleStats().required_letter, PuzzleStats().pangram, PuzzleStats().score)

    conn = sqlite3.connect("PyGame_Project/MVC/Model/Database/highscoreDB")
    cursor = conn.cursor()

    # Fetch scores for the puzzle with the given unique_identifier
    query = """
    SELECT hs.player_name
    FROM highscores AS hs
    """

    # Execute and fetch the results
    cursor.execute(query,)
    names = cursor.fetchall()

    # Close the connection
    conn.close()

    WordList = []
    for word in names:
        WordList.append(word[0])

    assert "test" in WordList


def test_get_score():
    puzzleGen()

    ## Insert tests
    insert_or_update_score("test", "a", "das", 420)
    insert_or_update_score("test2", "a", "das", 42069)

    scores = get_scores_for_puzzle("a", "das")


    assert len(scores) == 2





