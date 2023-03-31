from flask_restful import Resource
from db import User, db


class Users(Resource):

    # Get all users
    def get(self):
        users = User.query.all()
        result = [{'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'groupe': user.groupe} for user in users]
        return result, 200
