from flask import Flask
from flask import request
import json

app = Flask(__name__)
users={}
id = 1

@app.route("/")
def hello():
    return "Hello World"

@app.route("/users", methods=['POST'])
def createUser():
    global id
    username = request.form['name']
    users[id] = username
    user = {'id': id, 'name': username}
    id = id+1
    return json.dumps(user),201

@app.route('/users/<int:uid>', methods=['GET','DELETE'])
def userOperations(uid):
    
    if uid in users:
        user = {'id': uid, 'name': users[uid]}
    else:
        return "User Info not found",404

    if request.method == 'GET':
        return json.dumps(user)

    if request.method == 'DELETE':
        del users[uid]
        return '',204

    
