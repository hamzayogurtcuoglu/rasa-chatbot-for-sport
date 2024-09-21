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

def get_capacity(team_name):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("SELECT capacity FROM stadiums WHERE team = ?", (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Team not found."

def add_stadium(stadium_name, city, capacity, team):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute("INSERT INTO stadiums (stadium_name, city, capacity, team) VALUES (?, ?, ?, ?)",
              (stadium_name, city, capacity, team))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")