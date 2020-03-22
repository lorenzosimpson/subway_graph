import json
from flask import Flask, jsonify, request
from subway_graph import SubwayGraph, Station, locations, sg
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    response = 'API running'
    return jsonify(response), 200

@app.route('/route', methods=['POST'])
def route():
    data = request.get_json()
    origin = data['origin'].lower()
    destination = data['destination'].lower()

    response = sg.route(origin, destination)

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

