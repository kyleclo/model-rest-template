import uuid
import json

from flask import Flask, jsonify, request

app = Flask(__name__)

ALL_MODELS = {
    'a': 1,
    'b': 2
}

@app.route('/')
def hello():
    return 'Hi'

@app.route('/health')
def health():
    return jsonify({'status': 'UP'})

@app.route('/list', methods=['GET'])
def list_all_models():
    return jsonify(ALL_MODELS)

@app.route('/add', methods=['GET'])
def add_new_model():
    model_id = str(uuid.uuid4())
    ALL_MODELS[model_id] = 3
    return jsonify({'model_id': model_id})


@app.route('/<model_id>/train', methods=['POST'])
def train(model_id):
    data = request.json
    return

@app.route('/<model_id>/predict', methods=['POST'])
def predict(model_id):
    data = request.json
    return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)