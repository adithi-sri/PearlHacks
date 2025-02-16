import flask
from flask import Flask, request, render_template, redirect, session, Blueprint, send_file, make_response, render_template
#import schedule
import time
import threading
import sqlite3
import string 
#from PIL import Image
from io import BytesIO
import hashlib
import json
import os
import redis
import random
import points

app = Flask(__name__)
r = redis.Redis(host='localhost', port=8022, decode_responses=True)

app.secret_key = 'your secret key'


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
        Allows login with a POST request
    '''
    if request.method == "GET":
        return render_template('login.j2')
    elif request.method == "POST":
        fields = ['mode', 'username', 'password']
        for f in fields:
            if f not in request.form:
                return "ERROR"
    
        verb = ''

        # login user
        if request.form.get('mode') == 'login':
            verb = 'LOGIN'
            password = request.form.get('password')
            username = request.form.get('username')
            print("Logging In:", username)
            # gets password from database and formats it into a string return
            if validate_password(username, password) == False:
                message = "Password Invalid. Please try again."
                return render_template('login.j2',error=message)
            #SETS USER TOKEN
            cookie = uuid4()
            r.set(f'{cookie}', f'{username}')

            response = make_response(redirect('/homepage'))
            response.set_cookie('sessiontoken', str(cookie))

            return response
            
        elif request.form.get('mode') == 'register':
            verb = 'REGISTER'
            username = request.form.get('username')
            password = request.form.get('password')
            usernameexists = username_found(username)

            print(usernameexists)
            if len(username) < 5:
                message = "Your username should be between 5 - 12 characters."
                return render_template('login.j2',error=message)
            if len(username) > 12:
                message = "Your username should be between 5 - 12 characters."
                return render_template('login.j2',error=message)
            if usernameexists == False:
                register_new_user(username, password)
                #SETS USER TOKEN
                cookie = uuid4()
                r.set(f'{cookie}', f'{username}')
                response = make_response(redirect('/homepage'))
                response.set_cookie('sessiontoken', str(cookie))

                return response
            if usernameexists == "Account Exists" or usernameexists == True:
                print("Server Knows Account Exists")
                message = "This account already exists. Please login."
                return render_template('login.j2',error=message)
        
            else:
                message = "username already exists"
                return render_template('login.j2',error=message)
    
        else:
            return "ERROR"

        print(f"MODE: {verb} {request.form.get('username')} {request.form.get('password')}") 

    return render_template('login.js')

"""
This function adds a user to the database and takes a string of the username and 
the password. It returns a boolean or a string that describes what happened.
"""
@app.route("/register", methods=['GET', 'POST'])
def register_new_user(username, password):
    data = request.get_json()
    username = data['username']
    password = data['password']
    # establishes connection to accounts database
    salt = str(''.join(random.choices(string.printable, k = 10)))
    saltedpassword = password + salt
    hashAlgo = hashlib.sha256()
    hashAlgo.update(saltedpassword.encode())
    hashpassword = hashAlgo.hexdigest()
    
    # ensures that the username doesn't exist in the database
    if username_found(username) == True:
        # tells the server that the username exists
        return "Account Exists"

    # inse.rts info to the user table
    insert = "INSERT INTO accounts (username, hashpassword, salt) VALUES(?,?,?)"

    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()
    cur.execute(insert, (username, hashpassword, salt))
    conn.commit()
    cur.close()
    conn.close()

    if validate_password(username, password) == True:
        print(f"user {username} registered and in the database")

    return True

"""
This function looks for a username and returns a boolean
"""
# determines if username exists
def username_found(username):
    try:
        # inserts info to the user table
        insert = "SELECT username FROM accounts WHERE username = ?"
        conn = sqlite3.connect("accounts.db")
        cur = conn.cursor()
        cur.execute(insert, (username,))
        conn.commit()
        queryusername = cur.fetchone()[0]
        cur.close()
        conn.close()
    
        if queryusername == username:
            # username found
            return True
        else:
            # username not found
            return False
    except: 
        return False


def validate_password(username, password):
    #connection = sqlite3.connect("accounts.db")
    # gets password from database and formats it into a string return
    conn = sqlite3.connect("accounts.db")
    # select and salt user password
    querysalt = "SELECT salt FROM accounts WHERE username = ?"
    cur = conn.cursor()
    cur.execute(querysalt, (username,))
    conn.commit()
    querysalt = cur.fetchone()[0]
    cur.close()
    conn.close()

    if not querysalt:
        return False
    
    password += str(querysalt)
    # hash user password
    hashAlgo = hashlib.sha256()
    hashAlgo.update(password.encode())
    hashpassword = hashAlgo.hexdigest()
    conn = sqlite3.connect("accounts.db")
    querypassword = "SELECT hashpassword FROM accounts WHERE username = ?"
    cur = conn.cursor()
    cur.execute(querypassword, (username,))
    conn.commit()
    querypassword = cur.fetchone()[0]
    cur.close()
    conn.close()

    # compare password
    if querypassword == hashpassword:
        return True
    elif querypassword != hashpassword:
        print("Error: password is incorrect")
        return False

    
def getusers():
    # inserts info to the user table
    insert = "SELECT username FROM accounts"
    conn = sqlite3.connect("accounts.db")
    cur = conn.cursor()
    cur.execute(insert)
    conn.commit()
    usernames = list(cur.fetchall())
    cur.close()
    conn.close()
    usernames = [item[0] for item in usernames if item[0]]
    return usernames

def execute_query(query):
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        return ('\t'.join(str(column).replace('|', '\t') for column in row))
    connection.close()

def texecute_query(query):
    connection = sqlite3.connect("times.db")
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        return ('\t'.join(str(column).replace('|', '\t') for column in row))
    connection.close()

def cexecute_query(query):
    connection = sqlite3.connect("conversations.db")
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        return ('\t'.join(str(column).replace('|', '\t') for column in row))
    connection.close()

def reset_points():
    query = "UPDATE accounts SET points = 0"
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    
def get_messages(user1, user2):
    # inserts info to the user table
    print(f"ATTEMPTING TO GET MESSAGES FROM CONVERSATION #")
    insert = "SELECT * FROM conversations WHERE (conversationid = ?)"
    conn = sqlite3.connect("conversations.db")
    cur = conn.cursor()
    cur.execute(insert, (user1, user2, user2, user1))
    conn.commit()
    messages = cur.fetchall()
    cur.close()
    conn.close()
    if messages == None:
        conn = sqlite3.connect("conversations.db")
        cur = conn.cursor()
        # Conversation doesn't exist, insert a new row
        insert = "INSERT INTO conversations (user1, user2, messages) VALUES(?,?,?)"
        cur.execute(insert, (user1, user2, ""))
        conn.commit()
        messages = ""
        cur.close()
        conn.close()

    # should be a tuple
    return list(messages)

#schedule.every().sunday.at("00:00").do(reset_points)
def run_scheduler():
    while True:
        #schedule.run_pending()
        time.sleep(60) 

scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

accounts = '''
CREATE TABLE IF NOT EXISTS accounts (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hashpassword TEXT,
    points INTEGER DEFAULT 0,
    courses TEXT,
    major TEXT,
    issession INTEGER DEFAULT 0,
    salt TEXT
);
'''
execute_query(accounts)

times = '''
CREATE TABLE IF NOT EXISTS times (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    sessionid INTEGER,
    username TEXT,
    session_start INTEGER,
    session_end INTEGER
);
'''

#seperate function to avoid cursor errors - don't know why but was giving an error otherwise
texecute_query(times)

conversations = '''
CREATE TABLE IF NOT EXISTS conversations (
    rowid INTEGER,
    sessionid INTEGER,
    username TEXT,
    message TEXT,
    time INTEGER,
    FOREIGN KEY(sessionid) REFERENCES sessions(sessionid)
);
'''

#seperate function to avoid cursor errors
cexecute_query(conversations)

register_new_user("molly", "slkdsjaf")
register_new_user("billy", "slkdsjaf")
register_new_user("honey", "slkdsjaf")


def test_study_sessions():
    # 1. Test setup - Register some users (you might need to create them in the DB first or ensure they're added beforehand)
    # You should already have a way to add test users in your database
    test_users = ["billy", "molly", "willy"]
    
    # 2. Test the start and end study sessions
    for username in test_users:
        points.start_study_session(username)
        timeint = random.randint(0,10)
        time.sleep(timeint)
        points.end_study_session(username)
    
    # 3. Test points update
    for username in test_users:
        points.update_points(username)

    # 4. Get the top 9 users based on points
    print("Top 9 Users by Points:")
    top_users = points.get_top_9_users()
    for i, user in enumerate(top_users, 1):
        print(f"{i}. {user[0]} - {user[1]} points")

def toggle_session(username):
    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()

    cursor.execute('SELECT issession FROM accounts WHERE username = ?', (username,))
    is_session = cursor.fetchone()[0]

    if is_session == 1:
        points.end_study_session(username)
    else:
        points.start_study_session(username)

    conn.close()

@app.route("/start_session", methods=['POST'])
def start_session():
    username = request.form.get('username')
    if username:
        points.start_study_session(username)
        return {"status": "success", "message": "Study session started."}, 200
    return {"status": "error", "message": "Username is required."}, 400

@app.route("/end_session", methods=['POST'])
def end_session():
    username = request.form.get('username')
    if username:
        points.end_study_session(username)
        points.update_points(username)
        return {"status": "success", "message": "Study session ended and points updated."}, 200
    return {"status": "error", "message": "Username is required."}, 400

@app.route("/get_top_users", methods=['GET'])
def get_top_users():
    top_users = points.get_top_9_users()
    return {"status": "success", "top_users": top_users}, 200

# Run the test
test_study_sessions()

app.run(host="0.0.0.0", port=8022, debug=True)