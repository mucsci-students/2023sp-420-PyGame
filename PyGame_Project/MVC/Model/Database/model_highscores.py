import sqlite3
import hashlib

def generate_tables():
    conn = sqlite3.connect("PyGame_Project/MVC/Model/Database/highscoreDB")
    cursor = conn.cursor()

    # Create the 'puzzles' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS puzzles (
        id INTEGER PRIMARY KEY,
        unique_identifier TEXT UNIQUE,
        required_letter TEXT,
        all_letters TEXT
    );
    """)

    # Create the 'scores' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS highscores (
        id INTEGER PRIMARY KEY,
        player_name TEXT,
        puzzle_id INTEGER,
        score INTEGER,
        FOREIGN KEY (puzzle_id) REFERENCES puzzles (id)
    );
    """)
    return cursor


def get_scores_for_puzzle(required_letter, all_letters):
    
    identifier = generate_puzzle_identifier(required_letter, all_letters)
    conn = sqlite3.connect("PyGame_Project/MVC/Model/Database/highscoreDB")
    cursor = conn.cursor()

    # Fetch scores for the puzzle with the given unique_identifier
    query = """
    SELECT hs.player_name, hs.score
    FROM highscores AS hs
    JOIN puzzles AS pz ON hs.puzzle_id = pz.id
    WHERE pz.unique_identifier = ?
    ORDER BY hs.score DESC;
    """

    # Execute and fetch the results
    cursor.execute(query, (identifier,))
    scores = cursor.fetchall()

    # Close the connection
    conn.close()

    return scores

def insert_or_update_score(player_name, required_letter, all_letters, score):
    
    identifier = generate_puzzle_identifier(required_letter, all_letters)
    conn = sqlite3.connect("PyGame_Project/MVC/Model/Database/highscoreDB")
    cursor = conn.cursor()

    # Insert puzzle into puzzle table if it doesn't exist.
    cursor.execute("""
    INSERT OR IGNORE INTO puzzles (unique_identifier, required_letter, all_letters)
    VALUES (?, ?, ?);
    """, (identifier, required_letter, ''.join(sorted(all_letters))))

    # Update or insert score for player if it doesn't exist.
    cursor.execute("""
    INSERT OR REPLACE INTO highscores (id, player_name, puzzle_id, score)
    SELECT hs.id, ?, pz.id, ?
    FROM puzzles AS pz
    LEFT JOIN highscores AS hs ON hs.player_name = ? AND hs.puzzle_id = pz.id
    WHERE pz.unique_identifier = ?;
    """, (player_name, score, player_name, identifier))

    conn.commit()
    conn.close()


def get_player_rank(player_name, required_letter, all_letters):

    identifier = generate_puzzle_identifier(required_letter, all_letters)
    conn = sqlite3.connect("PyGame_Project/MVC/Model/Database/highscoreDB")
    cursor = conn.cursor()

    # Fetch rank for a specific player
    query = """
    WITH ranked_scores AS (
        SELECT hs.player_name,
               hs.score,
               RANK() OVER (PARTITION BY pz.unique_identifier ORDER BY hs.score DESC) AS rank
        FROM highscores AS hs
        JOIN puzzles AS pz ON hs.puzzle_id = pz.id
        WHERE pz.unique_identifier = ?
    ),
    total_players AS (
        SELECT COUNT(*) AS total
        FROM highscores AS hs
        JOIN puzzles AS pz ON hs.puzzle_id = pz.id
        WHERE pz.unique_identifier = ?
    )
    SELECT rs.player_name, rs.score, rs.rank, tp.total
    FROM ranked_scores AS rs, total_players AS tp
    WHERE rs.player_name = ?;
    """

    # Execute and fetch the results
    cursor.execute(query, (identifier, identifier, player_name))
    result = cursor.fetchone()
    conn.close()

    return result

def generate_puzzle_identifier(required_letter, all_letters):
    # Combine the required letter and other letters into a single string
    combined_letters = required_letter + ''.join(sorted(all_letters))
    
    # Generate a hash based on required letter + letters
    hash_object = hashlib.sha256(combined_letters.encode())
    identifier = hash_object.hexdigest()
    
    return identifier


# generate_tables()
insert_or_update_score('Robert', 's', 'efdoras', 421)
insert_or_update_score('Benjy', 's', 'efdoras', 69)
insert_or_update_score('Ethan', 's', 'efdoras', 68)
insert_or_update_score('Priscilla', 's', 'efdoras', 100)
insert_or_update_score('Kiah', 's', 'efdoras', 100)

player_rank = get_player_rank('Benjy', 's', 'efdoras')
all_scores = get_scores_for_puzzle('s', 'efdoras')
print(f'Player rank is: {player_rank}')
print(f'All scores for puzzle are: {all_scores}')
