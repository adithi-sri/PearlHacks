
from flask import Flask, request, render_template, redirect, session
import mysql.connector
from flask import Bcrypt

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
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect('/')
        else:
            return 'Invalid username or password'
    return render_template('login.js')

def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        if user:
            return 'User already exists'
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            mysql.connection.commit()
            session['username'] = username
            return redirect('/')
    return render_template('signup.js')
