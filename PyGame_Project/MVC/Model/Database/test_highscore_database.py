from model_highscores import *

# If None, no tables exist. 
def test_generate_table():
    cursor = generate_tables()
    result = cursor.execute("SELECT name FROM sqlite_master")
    assert result.fetchone() is not None

test_generate_table()