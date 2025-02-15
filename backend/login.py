import flask
from flask import Flask, request, render_template, redirect, session, Blueprint, send_file, make_response, render_template
import schedule
import time
import threading
import sqlite3
import string 
from flask import Bcrypt
from PIL import Image
from io import BytesIO
import json
import os
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=8022, decode_responses=True)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'login'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        connection = sqlite3.connect("accounts.db")
        cursor = connection.cursor()
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        cursor.close()
        # removed encryption here. don't know what overall function was
        if user and password:
            session['username'] = user['username']
            return redirect('/')
        else:
            return 'Invalid username or password'
    return render_template('login.js')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        connection = sqlite3.connect("accounts.db")
        cursor = connection.cursor()
        username = request.form['username']
        password = request.form['password']
        courses = request.form['courses']
        major = request.form['major']
        cursor.execute('SELECT * FROM accounts WHERE username = ?', (username,))
        user = cursor.fetchone()
        if user:
            return 'User already exists'
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute('INSERT INTO accounts (username, password, courses, major) VALUES (?, ?, ?, ?)', (username, hashed_password, courses, major))
            mysql.connection.commit()
            session['username'] = username
            return redirect('/')
    return render_template('signup.js')

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
            print(f"Username Found: {queryusername}")
            return True
        else:
            # username not found
            print("Username Not Found")
            return False
    except: 
        print("Username Search Failed")
        return False
    

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

schedule.every().sunday.at("00:00").do(reset_points)
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60) 
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

accounts = '''
CREATE TABLE IF NOT EXISTS accounts (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,,
    hashpassword TEXT NOT NULL,,
    points INTEGER NOT NULL,,
    courses TEXT NOT NULL,,
    major TEXT NOT NULL,,
    issession INTEGER DEFAULT 0;
);
'''
execute_query(accounts)

times = '''
CREATE TABLE IF NOT EXISTS accounts (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    sessionid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    session_start INTEGER,
    session_end INTEGER,
);
'''

#seperate function to avoid cursor errors - don't know why but was giving an error otherwise
texecute_query(times)

conversations = '''
CREATE TABLE IF NOT EXISTS conversations (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    sessionid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    time INTEGER,
    FOREIGN KEY(sessionid) REFERENCES sessions(sessionid),
);
'''

#seperate function to avoid cursor errors
cexecute_query(conversations)



