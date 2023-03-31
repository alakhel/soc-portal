from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from db import User, db


class User(Resource):

    # Get a user(s)
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        if user:
            user_data = {'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'groupe': user.groupe}
            return user_data, 200
        else:
            return {'message': 'User not found.'}, 404

    # Create a user
    @jwt_required()
    def post(self):
        if get_jwt()['admin']:
            data = request.get_json()
            user = User(prenom=data['prenom'], nom=data['nom'], login=data['login'], groupe=data['groupe'])
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            return {'message': 'User created successfully.'}, 201
        else:
            return {"message": "Must be admin to create a user"}, 403

    # Delete a user
    @jwt_required()
    def delete(self):
        claims = get_jwt()
        if not claims['admin']:
            return {'message': 'Must be admin to delete a user'}, 403

        data = request.get_json()
        user = User.query.filter_by(id=data['user_id']).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully.'}, 200
        else:
            return {'message': 'User not found.'}, 404

    # Update a user
    @jwt_required()
    def update(self):
        claims = get_jwt()
        if claims['admin']:
            user_id = request.get_json()['user_id']
        else:
            user_id = get_jwt_identity()

        data = request.get_json()
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return {'message': "User doesn't exist"}, 404

        fields = ['nom', 'prenom', 'login', 'password', 'groupe']
        for i in fields:
            if i in data and data[i] != "":
                if i == "password":
                    user.set_password(data[i])
                else:
                    setattr(user, i, data[i])

        return {'message': 'User updated succesfully'}, 200