from flask_restful import Resource
from db import DBMachine


class Machines(Resource):

    def get(self):
        machines = DBMachine.query.all()
        result = [{'id': m.id, 'hostname': m.hostname, 'ip': m.ip, 'group': m.group} for m in machines]
        return result, 200
