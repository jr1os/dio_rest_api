from flask import Flask, request 
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Persons, Activities, Users
from skill import Skill
import json

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# users = {
#        'ali': '0123',
#        'galleani': '321'
#        }


@auth.verify_password
def vefification(login, password):
    if not (login, password):
        return False 
    return Users.query.filter_by(login=login, password=password).first()


class Person(Resource):
    @auth.login_required
    def get(self, name):
        person = Persons.query.filter_by(name=name).first()
        try:
            resp = {
                    'name': person.name,
                    'age': person.age,
                    'id': person.id 
                    } 
        except AttributeError:
            menssage = f"Person {name} not exist"
            resp = {"status": "error", "menssage": menssage}
        return resp 

    def put(self, name):
        person = Persons.query.filter_by(name=name).first()
        dat = request.json
        if 'name' in dat:
            person.name = dat['name']
        if 'age' in dat:
            person.age = dat['age']
        person.save()
        resp = {
                'id': person.id,
                'name': person.name,
                'age': person.age
                }
        return resp 

    def delete(self, name):
        person = Persons.query.filter_by(name=name).first()
        person.delete()
        return {"status": "success", "menssage": "deleted registry"}


class ListPersons(Resource):
    @auth.login_required
    def get(self):
        person = Persons.query.all()
        resp = [
                {'id': p.id,
                    'name': p.name, 
                    'age': p.age} for p in person
                ]
        return resp
    
    def post(self):
        dat = request.json
        person = Persons(name=dat['name'], age=dat['age'])
        person.save()
        resp = {
                'id': person.id,
                'name': person.name,
                'age': person.id
                }
        return resp


class ListActivites(Resource):

    def get(self):
        activity = Activities.query.all()
        resp = [
                {'id': a.id,
                 'name': a.name} for a in activity 
                ]
        return resp 
    
    def post(self):
        dat = request.json
        person = Persons.query.filter_by(name=dat['person']).first()
        activity = Activities(name=dat['name'], person=person)
        activity.save()
        resp = {
                'name': activity.name,
                'person': activity.person.name,
                'id': activity.id
                }
        return resp


api.add_resource(ListPersons, "/person/") 
api.add_resource(Person, "/person/<string:name>/")
api.add_resource(ListActivites, "/activities/")

