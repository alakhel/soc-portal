from flask import Flask, send_file, jsonify, request, Response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, decode_token
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate





app = Flask(__name__, static_folder='public', static_url_path='/public')


app.config['JWT_SECRET_KEY'] = 'doNotTellMyMaster!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
jwt = JWTManager(app)

##############################
# GENERAL HTML ENDPOINT
##############################
#Home Page
@app.route('/<path:filename>')
def serve_dist(filename):
    return send_from_directory('dist', filename)
@app.route('/')
def serve_index():
    return send_file('index.html')
#Protected Dashboard
@app.route('/dashboard', methods=['GET'])
#@jwt_required
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
def machine():
    return send_file('machine.html')


####################################
#    USER CRUD ENDPOINT            #
####################################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50))
    nom = db.Column(db.String(50))
    login = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    groupe = db.Column(db.String(50))
    firstLogin = db.Column(db.Boolean, default=True)



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id}>'



#-----------------------------------#
#Login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Get user from the database
    user = User.query.filter_by(login=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Create access token for the user
    access_token = create_access_token(identity=user.id)
    return jsonify({'login': True, 'access_token': access_token}), 200
#-----------------------------------#
# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(prenom=data['prenom'], nom=data['nom'], login=data['login'], groupe=data['groupe'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully.'}), 201
#-----------------------------------#
# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'groupe': user.groupe}
        result.append(user_data)
    return jsonify(result), 200
 #-----------------------------------#
# Get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_data = {'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'groupe': user.groupe}
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found.'}), 404
#-----------------------------------#
# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        data = request.json
        if data['prenom'] != "" :
            user.prenom = data['prenom']
        if data['nom'] != "" :
            user.nom = data['nom']
        if data['login'] != "" :
            user.login = data['login']
        if data['password'] != "" :
            user.set_password(data['password'])
        if data['groupe'] != "" :
            user.groupe = data['groupe']
        db.session.commit()
        return jsonify({'message': 'User updated successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404
#-----------------------------------#
# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404


###############################
# MACHINE API ENDPOINT
###############################

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(255), nullable=False)
    ip = db.Column(db.String(15), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f'<Machine {self.id}>'    
#-----------------------------------#
@app.route('/machines', methods=['GET'])
def get_machines():
    machines = Machine.query.all()
    return jsonify([{'id': m.id, 'hostname': m.hostname, 'ip': m.ip, 'group': m.group} for m in machines])
#-----------------------------------#
@app.route('/machines/<int:machine_id>', methods=['GET'])
def get_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if machine:
        return jsonify({'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group})
    else:
        return jsonify({'error': 'Machine not found'})
#-----------------------------------#
@app.route('/machines', methods=['POST'])
def add_machine():
    data = request.get_json()
    machine = Machine(hostname=data['hostname'], ip=data['ip'], group=data['group'])
    db.session.add(machine)
    db.session.commit()
    return jsonify({'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group})
#-----------------------------------#
@app.route('/machines/<int:machine_id>', methods=['PUT'])
def update_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if machine:
        data = request.get_json()
        machine.hostname = data['hostname']
        machine.ip = data['ip']
        machine.group = data['group']
        db.session.commit()
        return jsonify({'id': machine.id, 'hostname': machine.hostname, 'ip': machine.ip, 'group': machine.group})
    else:
        return jsonify({'error': 'Machine not found'})
#-----------------------------------#
@app.route('/machines/<int:machine_id>', methods=['DELETE'])
def delete_machine(machine_id):
    machine = Machine.query.get(machine_id)
    if machine:
        db.session.delete(machine)
        db.session.commit()
        return jsonify({'message': 'Machine deleted successfully'})
    else:
        return jsonify({'error': 'Machine not found'})

@app.errorhandler(404)
def page_not_found(e):
    return send_file('notfound.html'), 404

def create_tables():
    with app.app_context():
        db.create_all()
migrate = Migrate(app, db)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)


