from flask import Flask
from flask import send_file

app = app = Flask(__name__, static_folder='public', static_url_path='/public')



@app.route('/')
def serve_index():
    return send_file('index.html')

@app.route('/api/v1/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
