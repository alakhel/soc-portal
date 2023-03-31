from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from db import DBMachine, db


class Machine(Resource):

    # Get a machine
    def get(self):
        machine = Machine.query.get(request.get_json()['machine_id'])
        if machine:
            return {'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group}, 200
        else:
            return {'error': 'Machine not found'}, 404

    # Create a machine
    @jwt_required()
    def post(self):
        if not get_jwt()['admin']:
            return {'message': 'Must be admin to create a machine'}, 403

        data = request.get_json()
        machine = Machine(hostname=data['hostname'], ip=data['ip'], group=data['group'])
        db.session.add(machine)
        db.session.commit()
        return {'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group}, 200

    # Update a machine
    @jwt_required()
    def update(self):
        if not get_jwt()['admin']:
            return {'message': 'Must be admin to create a machine'}, 403

        data = request.get_json()
        machine = Machine.query.get(data['machine_id'])
        if machine:
            data = request.get_json()
            machine.hostname = data['hostname']
            machine.ip = data['ip']
            machine.group = data['group']
            db.session.commit()
            return {'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group}, 200
        else:
            return {'error': 'Machine not found'}, 404

    # Delete a machine
    @jwt_required()
    def delete(self):
        if not get_jwt()['admin']:
            return {'message': 'Must be admin to create a machine'}, 403

        data = request.get_json()
        machine = Machine.query.get(data['machine_id'])
        if machine:
            db.session.delete(machine)
            db.session.commit()
            return {'message': 'Machine deleted successfully'}, 200
        else:
            return {'error': 'Machine not found'}, 404