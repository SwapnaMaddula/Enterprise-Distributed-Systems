from flask import Flask
from flask import request
import json
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/users", methods=['POST'])
def create_users():
    user_data = request.get_json()
    value1 = user_data.get('id')
    value2 = user_data.get('name')
    conn = sql.connect("mydatabase.db")
    c = conn.cursor()
    c.execute("INSERT INTO users(id,name) VALUES (?,?)", (value1, value2))
    conn.commit()
    c.close()
    return json.dumps(user_data),201

@app.route('/users/<string:id>', methods=['GET','DELETE'])
def new_users(id):
    con = sql.connect("mydatabase.db")
    con.row_factory = sql.Row 
    cur = con.cursor()
    if request.method == 'GET':
        rows=cur.execute("select name,id from users where id = ?",id).fetchall()
        return json.dumps( [dict(row) for row in rows] )
    if request.method == 'DELETE':
        cur.execute("delete from users where id = ?",id)
        con.commit()
        return '',204

    