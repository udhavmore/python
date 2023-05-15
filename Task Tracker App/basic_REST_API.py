import flask
from flask import jsonify, request
import sqlite3

app = flask.Flask(__name__)

data = [
    {
        'id': 1,
        'name': 'Kal El',
        'planet': 'Krypton'
    },
    {
        'id': 2,
        'name': 'Jon Jones',
        'planet': 'Mars'
    }
]


@app.route('/', methods=['GET'])
def main():
    return '''
    <h1>API Sample</h1>
    <br>
    <p>This is an API sample code</p>
    <br>
    <a href= 'http://127.0.0.1:5000/dc-identity?id=1'>1</a><br>
    <a href= 'http://127.0.0.1:5000/dc-identity?id=2'>2</a><br>
    '''


@app.route('/dc-identity', methods=['GET'])
def rev_identity():
    if 'id' in request.args:
        print(request.args)
        id = int(request.args['id'])
    else:
        return "Error: No ID was provided"

    results = []

    for name in data:
        print(name)
        if name['id'] == id:
            results.append(name)
            return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
