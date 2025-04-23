# import sqlite3

# def setup_db():
#     conn = sqlite3.connect("hangman.db")
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS hall_of_fame (
#                     level TEXT PRIMARY KEY,
#                     name TEXT,
#                     remaining_lives INTEGER)''')
#     conn.commit()
#     conn.close()

# def update_hall_of_fame(player_name, level, remaining_lives):
#     conn = sqlite3.connect("hangman.db")
#     cur = conn.cursor()
#     cur.execute("SELECT remaining_lives FROM hall_of_fame WHERE level=?", (level,))
#     row = cur.fetchone()
#     if row is None or remaining_lives > row[0]:
#         cur.execute("REPLACE INTO hall_of_fame (level, name, remaining_lives) VALUES (?, ?, ?)",
#                     (level, player_name, remaining_lives))
#         conn.commit()
#     conn.close()

# def show_hall_of_fame():
#     import tableprint as tp
#     conn = sqlite3.connect("hangman.db")
#     cur = conn.cursor()
#     cur.execute("SELECT level, name, remaining_lives FROM hall_of_fame")
#     rows = cur.fetchall()
#     conn.close()
#     print("\nHALL OF FAME")
#     tp.table(rows, header=["Level", "Winner", "Lives"], width=50)






import sqlite3
import os

# Function to set up the database and create the hall_of_fame table if it doesn't exist
def setup_db():
    db_file = "hangman.db"
    if not os.path.exists(db_file):
        print("Setting up the database...")
    else:
        print("Database already exists.")
    
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS hall_of_fame (
                        level TEXT PRIMARY KEY,
                        name TEXT,
                        remaining_lives INTEGER)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error setting up the database: {e}")
        conn.close()


# Function to update hall of fame based on the player's performance
def update_hall_of_fame(player_name, level, remaining_lives):
    try:
        conn = sqlite3.connect("hangman.db")
        cur = conn.cursor()

        # Checking if the level has a record, and if the current score beats the stored one
        cur.execute("SELECT remaining_lives FROM hall_of_fame WHERE level=?", (level,))
        row = cur.fetchone()

        # Insert or replace the record for that level if the new score is better
        if row is None or remaining_lives > row[0]:
            cur.execute("REPLACE INTO hall_of_fame (level, name, remaining_lives) VALUES (?, ?, ?)",
                        (level, player_name, remaining_lives))
            conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error updating hall of fame: {e}")
        conn.close()


# Function to display the hall of fame (leaderboard)
def show_hall_of_fame():
    import tableprint as tp
    try:
        conn = sqlite3.connect("hangman.db")
        cur = conn.cursor()
        cur.execute("SELECT level, name, remaining_lives FROM hall_of_fame")
        rows = cur.fetchall()
        conn.close()

        if rows:
            print("\nHALL OF FAME")
            tp.table(rows, headers=["Level", "Winner", "Lives"], width=50)
        else:
            print("\nHALL OF FAME: No records yet.")
    except sqlite3.Error as e:
        print(f"Error displaying hall of fame: {e}")
