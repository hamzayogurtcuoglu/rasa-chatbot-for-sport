import sqlite3
from datetime import datetime

def create_database():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    
    # Create the stadiums table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS stadiums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stadium_name TEXT,
            city TEXT,
            capacity INTEGER,
            team TEXT
        )
    ''')

    # Create the match scores table if it doesn't exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS match_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team1 TEXT NOT NULL,
        team2 TEXT NOT NULL,
        team1_score INTEGER NOT NULL,
        team2_score INTEGER NOT NULL,
        scorers_team1 TEXT,      -- Players who scored, separated by commas
        scorers_team2 TEXT,      -- Players who scored, separated by commas
        referee TEXT,            -- Referee of the match
        yellow_cards TEXT,       -- Players who received yellow cards, separated by commas
        red_cards TEXT,          -- Players who received red cards, separated by commas
        weather TEXT             -- Weather during the match
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def get_city(team_name):
    # Get the city for a given team
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT city FROM stadiums WHERE team = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the city name
    else:
        return "Team not found."  # Return an error message if the team is not found

def get_stadium(team_name):
    # Get the stadium name for a given team
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT stadium_name FROM stadiums WHERE team = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the stadium name
    else:
        return "Team not found."  # Return an error message if the team is not found

def get_capacity(stadium_name):
    # Get the capacity of a given stadium
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT capacity FROM stadiums WHERE stadium_name = ?", (stadium_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the capacity
    else:
        return "Stadium not found."  # Return an error message if the stadium is not found

def get_match_info(team1, team2):
    # Get match information (scores and scorers) for the two teams
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
        return result  # Return (team1_score, team2_score, scorers_team1, scorers_team2)
    else:
        return None  # Return None if the match is not found

def get_match_referee(team1, team2):
    # Get the referee for the match between two teams
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT referee 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the referee name
    else:
        return None  # Return None if the match is not found

def get_match_yellow_cards(team1, team2):
    # Get yellow card information for the match between two teams
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT yellow_cards 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return yellow cards information
    else:
        return None  # Return None if the match is not found

def get_match_red_cards(team1, team2):
    # Get red card information for the match between two teams
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT red_cards
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return red cards information
    else:
        return None  # Return None if the match is not found

def get_match_weather(team1, team2):
    # Get weather information for the match between two teams
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT weather 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return weather information
    else:
        return None  # Return None if the match is not found

def add_stadium(stadium_name, city, capacity, team):
    # Add a new stadium to the database
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("INSERT INTO stadiums (stadium_name, city, capacity, team) VALUES (?, ?, ?, ?)",
              (stadium_name, city, capacity, team))
    conn.commit()
    conn.close()

def add_match_scores(team1, team2, team1_score, team2_score, scorers_team1, scorers_team2, referee, yellow_cards, red_cards, weather):
    # Add match score information to the database
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO match_scores (team1, team2, team1_score, team2_score, scorers_team1, scorers_team2, referee, yellow_cards, red_cards, weather) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (team1, team2, team1_score, team2_score, scorers_team1, scorers_team2, referee, yellow_cards, red_cards, weather))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")
