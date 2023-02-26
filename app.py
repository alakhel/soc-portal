from flask import Flask, send_file, jsonify, request, Response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, decode_token
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, static_folder='public', static_url_path='/public')



app.config['JWT_SECRET_KEY'] = 'doNotTellMyMaster!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
jwt = JWTManager(app)

#Home Page
@app.route('/')
def serve_index():
    return send_file('index.html')
#Login Page
@app.route('/login', methods=['GET'])
def loginPage():
    return send_file('loginPage.html')

#profile Page
@app.route('/profile', methods=['GET'])
def profile():
    return send_file('profile.html')

#machine Page
@app.route('/machine', methods=['GET'])
def machine():
    return send_file('machine.html')
#Users admin panel
@app.route('/userpage')
def serve_user_page():
    return send_file('user.html')

#Login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Verify the user's credentials here (e.g. by querying a database)

    access_token = create_access_token(identity=username)
    #response.set_cookie('access_token', access_token, httponly=True)
    return jsonify({'login': True, 'access_token': access_token}), 200

#Protected Dashboard
@app.route('/dashboard', methods=['GET'])
#@jwt_required
def dashboard():
     return send_file('dashboard.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50))
    nom = db.Column(db.String(50))
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    groupe = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {self.id}>'

def create_tables():
    with app.app_context():
        db.create_all()

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(prenom=data['prenom'], nom=data['nom'], login=data['login'], password=data['password'], groupe=data['groupe'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully.'}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'password': user.password, 'groupe': user.groupe}
        result.append(user_data)
    return jsonify(result), 200

# Get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_data = {'id': user.id, 'prenom': user.prenom, 'nom': user.nom, 'login': user.login, 'password': user.password, 'groupe': user.groupe}
        return jsonify(user_data), 200
    else:
        return jsonify({'message': 'User not found.'}), 404

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        data = request.json
        user.prenom = data['prenom']
        user.nom = data['nom']
        user.login = data['login']
        user.password = data['password']
        user.groupe = data['groupe']
        db.session.commit()
        return jsonify({'message': 'User updated successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404

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

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)


