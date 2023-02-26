from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_rbac import RBAC, UserMixin, RoleMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

# Flask-JWT-Extended setup
jwt = JWTManager(app)

# Flask-RBAC setup
rbac = RBAC(app, db_session=db.session)

# Define the User and Role models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(RoleMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<User {self.username}>'

# Create some roles
@app.before_first_request
def create_roles():
    db.create_all()
    roles = [
        {'name': 'admin', 'description': 'Administrator role'},
        {'name': 'user', 'description': 'Regular user role'}
    ]
    for role in roles:
        role_obj = Role(name=role['name'], description=role['description'])
        db.session.add(role_obj)
    db.session.commit()

# Flask-JWT-Extended authentication
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return User.query.get(identity)

@jwt_required
def protected_route():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({'message': f'Hello {user.username}! This is a protected route.'})

# Flask-RBAC authorization
@rbac.allow(['admin'])
def admin_route():
    return jsonify({'message': 'Hello admin!'})

@rbac.allow(['user'])
def user_route():
    return jsonify({'message': 'Hello user!'})

# Define the API routes
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = jwt.create_access_token(identity=user)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials.'}), 401

@app.route('/protected')
@jwt_required
def protected():
    return protected_route()

@app.route('/admin')
@rbac.allow(['admin'])
def admin():
    return admin_route()

@app.route('/user')
@rbac.allow(['user'])
def user():
    return user_route()

if __name__ == '__main__':
    app.run(debug=True)
