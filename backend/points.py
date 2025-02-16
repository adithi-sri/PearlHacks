import time
import sqlite3
import redis 

r = redis.Redis(host='localhost', port=8022, decode_responses=True)

# start study session

def start_study_session(username):
    conn = sqlite3.connect("times.db")
    cursor = conn.cursor()

    session_start = int(time.time())  # Current time in epoch format

    cursor.execute("INSERT INTO times (username, session_start) VALUES (?, ?)", (username, session_start))

    conn.commit()

    cursor.execute('UPDATE accounts SET issession = 1 WHERE username = ?', (username,))
    conn.commit()
    
    print(f"Started study session for {username} at {session_start}")
    conn.close()

# end study session

# update points

# order leaderboard