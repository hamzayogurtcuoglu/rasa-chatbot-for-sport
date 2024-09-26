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
        scorers_team1 TEXT,      -- Gol atan oyuncular, virgülle ayrılmış
        scorers_team2 TEXT,      -- Gol atan oyuncular, virgülle ayrılmış
        referee TEXT,            -- Maçın hakemi
        yellow_cards TEXT,       -- Sarı kart gören oyuncular, virgülle ayrılmış
        red_cards TEXT,          -- Kırmızı kart gören oyuncular, virgülle ayrılmış
        weather TEXT             -- Maç sırasındaki hava durumu
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


def get_match_referee(team1, team2):
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
        return result[0]  # referee
    else:
        return None  # Eğer maç bulunamazsa None döner

def get_match_yellow_cards(team1, team2):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT yellow_card 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # yellow_card
    else:
        return None  # Eğer maç bulunamazsa None döner

def get_match_red_cards(team1, team2):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute('''
        SELECT red_card 
        FROM match_scores 
        WHERE team1 = ? AND team2 = ?
    ''', (team1, team2))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # red_card
    else:
        return None  # Eğer maç bulunamazsa None döner

def get_match_weather(team1, team2):
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
        return result[0]  # weather
    else:
        return None  # Eğer maç bulunamazsa None döner


def add_stadium(stadium_name, city, capacity, team):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("INSERT INTO stadiums (stadium_name, city, capacity, team) VALUES (?, ?, ?, ?)",
              (stadium_name, city, capacity, team))
    conn.commit()
    conn.close()

def add_match_scores(team1, team2, team1_score, team2_score, scorers_team1, scorers_team2, referee, yellow_cards, red_cards, weather):
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