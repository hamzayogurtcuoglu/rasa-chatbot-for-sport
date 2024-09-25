import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS stadiums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stadium_name TEXT,
            city TEXT,
            capacity INTEGER,
            team TEXT
        )
    ''')

    # Match scores table creation
    c.execute('''
        CREATE TABLE IF NOT EXISTS match_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1 TEXT NOT NULL,
            team2 TEXT NOT NULL,
            team1_score INTEGER NOT NULL,
            team2_score INTEGER NOT NULL,
            scorers_team1 TEXT,  -- Gol atan oyuncular, virgülle ayrılmış
            scorers_team2 TEXT   -- Gol atan oyuncular, virgülle ayrılmış
        )
    ''')

    conn.commit()
    conn.close()

def get_city(team_name):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT city FROM stadiums WHERE team = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Team not found."

def get_stadium(team_name):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT stadium_name FROM stadiums WHERE team = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Team not found."

def get_capacity(stadium_name):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT capacity FROM stadiums WHERE stadium_name = ?", (stadium_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Team not found."

def get_match_info(team1, team2):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT team1_score, team2_score, scorers_team1, scorers_team2 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result  # (team1_score, team2_score, scorers_team1, scorers_team2)
    else:
        return None  # Eğer maç bulunamazsa None döner


def add_stadium(stadium_name, city, capacity, team):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("INSERT INTO stadiums (stadium_name, city, capacity, team) VALUES (?, ?, ?, ?)",
              (stadium_name, city, capacity, team))
    conn.commit()
    conn.close()

def add_match_scores(team1, team2, team1_score, team2_score, scorers_team1, scorers_team2):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO match_scores (team1, team2, team1_score, team2_score, scorers_team1, scorers_team2) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (team1, team2, team1_score, team2_score, scorers_team1, scorers_team2))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")