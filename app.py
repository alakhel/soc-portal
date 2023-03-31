from flask import Flask, send_file
from flask_jwt_extended import JWTManager
from db import db
from flask_restful import Api
from login import Login
from user import User
from users import Users
from machine import Machine
from machines import Machines


app = Flask(__name__, static_folder='public', static_url_path='/public')

app.config['JWT_SECRET_KEY'] = 'doNotTellMyMaster!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

jwt = JWTManager(app)
api = Api(app)

api.add_resource(Login, '/api/login')
api.add_resource(User, '/api/user')
api.add_resource(Users, '/api/users')
api.add_resource(Machine, '/api/machine')
api.add_resource(Machines, '/api/machines')


##############################
# GENERAL HTML ENDPOINT
##############################
# Home Page
@app.route('/')
def serve_index():
    return send_file('index.html')

# Protected Dashboard
@app.route('/dashboard', methods=['GET'])
# @jwt_required
def dashboard():
     return send_file('dashboard.html')

###############################
# USER HTML ENDPOINT
###############################
#Users admin panel
@app.route('/userpage')
def serve_user_page():
    return send_file('user.html')

#profile Page
@app.route('/profile', methods=['GET'])
def profile():
    return send_file('profile.html')

#Login Page
@app.route('/login', methods=['GET'])
def loginPage():
    return send_file('loginPage.html')


###############################
# MACHINE HTML ENDPOINT
###############################
#machine Page
@app.route('/machine', methods=['GET'])
def machine_html():
    return send_file('machine.html')

@app.errorhandler(404)
def page_not_found(e):
    return send_file('notfound.html'), 404

def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)


