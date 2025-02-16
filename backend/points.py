import time
import sqlite3
import redis 

r = redis.Redis(host='localhost', port=8022, decode_responses=True)

# start study session

def start_study_session(username):
    conn_times = sqlite3.connect("times.db")
    cursor = conn_times.cursor()

    session_start = int(time.time())  # Current time in epoch format

    cursor.execute("INSERT OR REPLACE INTO times (username, session_start) VALUES (?, ?)", (username, session_start))

    conn_times.commit()
    conn_times.close()

    conn_accounts = sqlite3.connect("accounts.db")
    cursor = conn_accounts.cursor()

    cursor.execute('UPDATE accounts SET issession = 1 WHERE username = ?', (username,))
    conn_accounts.commit()
    
    conn_accounts.close()

# end study session
def end_study_session(username):
    conn_endtimes = sqlite3.connect("times.db")
    cursor = conn_endtimes.cursor()

    session_end = int(time.time())  # Current time in epoch format
    cursor.execute("""
    UPDATE times 
    SET session_end = ? 
    WHERE username = ? AND session_end IS NULL
    """, (session_end, username))


    conn_endtimes.commit()
    conn_endtimes.close()

    conn_accounts = sqlite3.connect("accounts.db")
    cursor = conn_accounts.cursor()

    cursor.execute('UPDATE accounts SET issession = 0 WHERE username = ?', (username,))
    conn_accounts.commit()
    
    conn_accounts.close()

# get session duration 

def get_session_duration(username):
    # Fetch the session start and end times for the latest session (assuming sessionid is the latest)
    conn = sqlite3.connect("times.db")
    cursor = conn.cursor()
    
    # Fetch the most recent session start time for the user
    cursor.execute("""
    SELECT session_start 
    FROM times 
    WHERE username = ? 
    ORDER BY session_start DESC 
    LIMIT 1;
    """, (username,))
    session_start = cursor.fetchone()[0]  # Extract the session_start value from the tuple
    print("Session Start:", session_start)

    # Fetch the most recent session end time for the user
    cursor.execute("""
    SELECT session_end 
    FROM times 
    WHERE username = ? 
    ORDER BY session_end DESC 
    LIMIT 1;
    """, (username,))

    session_end = cursor.fetchone()[0]  # Extract the session_end value from the tuple
    print("Session End:", session_end)

 
    if session_start and session_end:
        if session_end != 0:  # Ensure session_end is populated
            duration = int(session_end) - int(session_start)  # Duration in seconds
            duration_minutes = round(duration // 1)  # Convert to minutes
            print(f"Session duration for {username} is {duration_minutes} minutes.")
            return duration_minutes  # Return duration in minutes (or seconds if preferred)
        else:
            print(f"Session for {username} is still ongoing.")
            conn.close()
            return 0  # If session is still ongoing, duration is 0
    else:
        print(f"No session found for {username}.")
        conn.close()
        return 0  # No session found for the user

# update points

def update_points(username):
    # Get the session duration in minutes
    duration = get_session_duration(username)
    points_earned = duration
    if duration >= 0:
        
        # Update the points in the accounts table
        conn = sqlite3.connect("accounts.db")
        cursor = conn.cursor()
        
        # Fetch current points
        cursor.execute("SELECT points FROM accounts WHERE username = ?", (username,))
        current_points = cursor.fetchone()
        
        if current_points:
            print(f"current points is {current_points}")
            current_points = current_points[0]
            new_points = current_points + points_earned
            cursor.execute("UPDATE accounts SET points = ? WHERE username = ?", (new_points, username))
            conn.commit()
            print(f"{username} earned {points_earned} points. Total points: {new_points}")
        else:
            print(f"User {username} not found.")
        
        conn.close()
    else:
        print(f"Session duration for {username} is too short or still ongoing.")

# order leaderboard

def get_top_9_users():
    # SQL query to get the top 9 users based on points
    query = "SELECT username, points FROM accounts ORDER BY points DESC LIMIT 9"
    
    # Connect to the accounts database
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)
    
    # Fetch the results
    top_users = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    # Return the list of top 9 users with their points
    return top_users

