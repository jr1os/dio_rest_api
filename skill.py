from flask_restful import Resource

list_skill = ['Python', 'Golang', 'Flask', 'fiber']


class Skill(Resource):
    def get(self):
        return list_skill
    
