
from flask import Flask, request, render_template, redirect, session
import schedule
import time
flask-mysqldb
import sqlite3
from flask import Bcrypt
from PIL import Image
import redis
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        connection = sqlite3.connect("accounts.db")
        cursor = connection.cursor()
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.check_password_hash(user['password'], password):
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
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        if user:
            return 'User already exists'
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute('INSERT INTO users (username, password, courses, major) VALUES (%s, %s, %s, %s)', (username, hashed_password, courses, major))
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

def reset_points():
    query = "UPDATE accounts SET points = 0"
    connection = sqlite3.connect("accounts.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    
schedule.every().sunday.at("00:00").do(reset_points)

accounts = '''
CREATE TABLE IF NOT EXISTS accounts (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hashpassword TEXT,
    points INTEGER,
    courses TEXT,
    major TEXT,
    issession INTEGER DEFAULT 0,
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
execute_query(times)


