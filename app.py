from flask import Flask, send_file, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app.config['JWT_SECRET_KEY'] = 'doNotTellMyMaster!'
jwt = JWTManager(app)

app = Flask(__name__, static_folder='public', static_url_path='/public')

app.config['JWT_SECRET_KEY'] = 'doNotTellMyMaster!'
jwt = JWTManager(app)

#Home Page
@app.route('/')
def serve_index():
    return send_file('index.html')
#Login Page
@app.route('/login', methods=['GET'])
def loginPage():
    return send_file('loginPage.html')


#Login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Verify the user's credentials here (e.g. by querying a database)

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

#Protected Dashboard
@app.route('/dashboard', methods=['GET'])
#@jwt_required
def dashboard():
     return send_file('dashboard.html')


if __name__ == '__main__':
    app.run()
