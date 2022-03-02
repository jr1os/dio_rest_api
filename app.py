from crypt import methods
from flask import Flask, jsonify, request
import json


app = Flask(__name__)

tasks = [
    {
        "id": 0,
        "responsible": "ali rios",
        "task": "create page html",
        "status": "not started"},
    {
        "id": 1,
        "responsible": "jonathan torres",
        "task": "upgrade page javascript",
        "status": "pending"
    }]

@app.route("/task/<int:id>/", methods=["GET", "PUT", "DELETE"])
def task(id):
    if request.method == "GET":
        try:
            resp = tasks[id]
        except IndexError:
            resp = {"status": "error", "message": f"id {id} not exist"}
        return resp
    elif request.method == "PUT":
        dat = json.loads(request.data)
        tasks[id] = dat
        return jsonify(dat)
    elif request.method == "DELETE":
        tasks.pop(id)
        return jsonify({"status": "sucess", "message": f"id {id} deleted"})

@app.route("/task/", methods=["GET", "POST"])
def list_task():
    if request.method == "POST":
        dat = json.loads(request.data)
        tasks.append(dat)
        return jsonify({"status":"task added"})
    elif request.method == "GET":
        return jsonify(tasks)
