from flask import Flask, make_response, redirect, render_template, request, url_for
import os
import sqlite3

database_path = os.path.join(os.path.dirname(__file__), "users_data.db")


app = Flask(__name__, template_folder='./dist', static_folder='./dist/static')

def create_db_if_not_exist():
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        cursor.execute("create table if not exists users(username text, password text, userid text)")
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def update_user_userid(username : str, userid : str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        cursor.execute("update users set userid = ? where username = ?", (userid, username))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def check_userid_exist(userid : str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute("select * from users where userid = ?", (userid,)).fetchall()
        if(len(rows) == 0):
            return False
        else:
            return True
    finally:
        cursor.close()
        connection.close()
    

def create_user(username : str, password : str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute("select * from users where username = ?", (username,)).fetchall()
        if(len(rows) == 0):
            cursor.execute("insert into users values (?, ?, null)", (username, password))
            connection.commit()
            return True
        else:
            return False
    finally:
        cursor.close()
        connection.close()

def check_user_password(username : str, password : str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute("select * from users where username = ?", (username,)).fetchall()
        if(len(rows) == 0):
            return False
        else:
            if(rows[0][1] == password):
                return True
            else:
                return False
    finally:
        cursor.close()
        connection.close()

def is_user_exist(username : str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute("select * from users where username = ?", (username,)).fetchall()
        if(len(rows) == 0):
            return False
        else:
            return True
    finally:
        cursor.close()
        connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/succeed')
def succeed():
    # check cookie to see whether user is logged in
    userid = request.cookies.get('userid')
    if(userid is None or not check_userid_exist(userid)):
        # redirect to main page 
        return redirect(url_for(''))
    else:
        return render_template("succeed.html")

# get user name from cookie userid
@app.route('/api/get_username')
def get_username():
    userid = request.cookies.get('userid')
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute("select * from users where userid = ?", (userid,)).fetchall()
        if(len(rows) == 0):
            return "None"
        else:
            return rows[0][0]
    finally:
        cursor.close()
        connection.close()

@app.route('/api/login', methods=['POST'])
def login():
    username = str(request.json.get('username'))
    password = str(request.json.get('password'))
    # create user with password if not exist
    if(not is_user_exist(username)):
        create_user(username, password)
    else:
        # return error information if password is wrong
        if(not check_user_password(username, password)):
            return make_response("Wrong password", 401)
    # generate random userid and update it to database
    userid = os.urandom(16).hex()
    print(f"username: {username} userid: {userid}")
    update_user_userid(username, userid)
    # make response with userid
    resp = make_response(f"Receive login request, user {username}", 200)
    resp.set_cookie('userid', userid, max_age=60*60*24)
    return resp


if __name__ == '__main__':
    create_db_if_not_exist()
    app.run()
