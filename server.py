from flask import Flask, make_response, redirect, render_template, request, url_for
import os
import sqlite3

database_path = os.path.join(os.path.dirname(__file__), "users_data.db")

app = Flask(__name__, template_folder='./dist', static_folder='./dist/static')

def create_db_if_not_exist() -> None:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        cursor.execute(
            "create table if not exists users(username text, password text, userid text, usage_volume real ,primary key(username))")
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def update_user_userid(username: str, userid: str) -> None:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        cursor.execute(
            "update users set userid = ? where username = ?", (userid, username))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def check_userid_exist(userid: str) -> bool:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select * from users where userid = ?", (userid,)).fetchall()
        if(len(rows) == 0):
            return False
        else:
            return True
    finally:
        cursor.close()
        connection.close()


def create_user(username: str, password: str) -> bool:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select * from users where username = ?", (username,)).fetchall()
        if(len(rows) == 0):
            cursor.execute(
                "insert into users values (?, ?, null, 0)", (username, password))
            connection.commit()
            return True
        else:
            return False
    finally:
        cursor.close()
        connection.close()


def check_user_password(username: str, password: str) -> bool:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select * from users where username = ?", (username,)).fetchall()
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


def is_user_exist(username: str) -> bool:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select * from users where username = ?", (username,)).fetchall()
        if(len(rows) == 0):
            return False
        else:
            return True
    finally:
        cursor.close()
        connection.close()


def get_usage_volume_from_userid(userid: str):
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select usage_volume from users where userid = ?", (userid,)).fetchall()
        if(len(rows) == 0):
            return -1
        else:
            return rows[0][0]
    finally:
        cursor.close()
        connection.close()


def update_usage_volume_from_userid(userid: str, usage_volume: float) -> bool:
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        if(not check_userid_exist(userid)):
            print("update volume: userid not exist")
            return False
        cursor.execute(
            "update users set usage_volume = ? where userid = ?", (usage_volume, userid))
        connection.commit()
        return True
    finally:
        cursor.close()
        connection.close()


create_db_if_not_exist()



# server part
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/succeed')
def succeed():
    # check cookie to see whether user is logged in
    userid = request.cookies.get('userid')
    if(userid is None or not check_userid_exist(userid)):
        # redirect to main page
        return redirect('/')
    else:
        # disable cache
        return make_response(render_template("succeed.html"), 200, {'Cache-Control': 'no-cache'})

# API part

# get/update user usage volume by cookie userid


@app.route('/api/usage_volume', methods=['GET', 'POST'])
def usage_volume():
    userid = request.cookies.get('userid')
    if(userid is None or not check_userid_exist(userid)):
        return "userid not exist", 401

    if(request.method == 'GET'):
        return str(get_usage_volume_from_userid(userid))
    elif(request.method == 'POST'):
        usage_volume = float(request.json.get('new_usage_volume'))
        update_result = update_usage_volume_from_userid(userid, usage_volume)
        resp = None
        if(update_result):
            resp = make_response(f"update succeed", 200)
        else:
            resp = make_response(f"update failed", 400)
        return resp


# get user name from cookie userid
@app.route('/api/get_username', methods=['GET'])
def get_username():
    userid = request.cookies.get('userid')
    connection = sqlite3.connect(database=database_path)
    cursor = connection.cursor()
    try:
        rows = cursor.execute(
            "select * from users where userid = ?", (userid,)).fetchall()
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
