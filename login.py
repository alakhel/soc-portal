from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from db import DBUser
from utils import check_args


class Login(Resource):

    args = [
        "username",
        "password"
    ]

    def post(self):
        if not check_args(request.get_json(), *self.args):
            return "Missing Arguments", 400

        data = request.get_json()
        user = DBUser.query.filter_by(login=data['username']).first()
        if not user or not check_password_hash(user.password_hash, data['password']):
            return {'error': 'Invalid username or password'}, 403

        claims = {"admin": False}
        if data['username'] == "admin":
            claims['admin'] = True

        # Create access token for the user
        access_token = create_access_token(identity=user.id, claims=claims)
        return {'login': True, 'access_token': access_token}, 200
