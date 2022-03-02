from dataclasses import dataclass
from flask import Flask, jsonify, request
import json


app = Flask(__name__)


developers = [
    {'id': 0,
    'name': 'ali',
    'skill': ['Python', "Golang", "Javascript"]
    },
    {'id': 1,
    'name': 'jonathan',
    'skill': ['javascript', 'flask', 'django']}
 ]


@app.route('/dev/<int:id>/', methods=['GET','DELETE','PUT'])
def developer(id):
    if request.method == 'GET':
        try:
            resp = developers[id]
        except IndexError:
            resp = {'status':'erro', 'message':f'developer {id} not exist'}
        return jsonify(resp)
    elif request.method == 'PUT':
        dat = json.loads(request.data)
        developers[id] = dat
        return jsonify(dat)        
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({"status":"success"})



@app.route('/dev/', methods=['GET', 'POST'])
def list_developer():
    if request.method == 'POST':
        dat = json.loads(request.data)
        developers.append(dat)
        return jsonify({'message': 'developer added'})
    elif request.method == 'GET':
        return jsonify(developers)

