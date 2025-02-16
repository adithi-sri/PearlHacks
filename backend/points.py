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
def end_study_session(username):
    conn_times = sqlite3.connect("times.db")
    cursor = conn_times.cursor()

    session_end = int(time.time())  # Current time in epoch format

    cursor.execute("INSERT INTO times (username, session_end) VALUES (?, ?)", (username, session_end))

    conn_times.commit()
    conn_times.close()

    conn_accounts = sqlite3.connect("accounts.db")
    cursor = conn_accounts.cursor()

    cursor.execute('UPDATE accounts SET issession = 0 WHERE username = ?', (username,))
    conn_accounts.commit()
    
    print(f"End study session for {username} at {session_end}")
    conn_accounts.close()

# get session duration 

def get_session_duration(username):
    # Fetch the session start and end times for the latest session (assuming sessionid is the latest)
    conn = sqlite3.connect("times.db")
    cursor = conn.cursor()
    
    cursor.execute('SELECT session_start, session_end FROM times WHERE username = ? ORDER BY sessionid DESC LIMIT 1', (username,))
    session = cursor.fetchone()
    
    if session:
        session_start, session_end = session
        if session_end != 0:  # Ensure session_end is populated
            duration = session_end - session_start  # Duration in seconds
            duration_minutes = duration // 60  # Convert to minutes
            print(f"Session duration for {username} is {duration_minutes} minutes.")
            return duration_minutes  # Return duration in minutes (or seconds if preferred)
        else:
            print(f"Session for {username} is still ongoing.")
            return 0  # If session is still ongoing, duration is 0
    else:
        print(f"No session found for {username}.")
        return 0  # No session found for the user
    
    conn.close()

# update points

# order leaderboard