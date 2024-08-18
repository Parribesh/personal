from flask import Flask, request, jsonify

app = Flask(__name__)

# Handle GET request


@app.route('/', methods=['GET'])
def home():
    return "Hello, World! Welcome through jenkins ci/cd"

# Handle POST request


@app.route('/post', methods=['POST'])
def handle_post():
    data = request.json  # Get JSON data sent in the request
    return jsonify({
        "message": "Data received",
        "data": data
    })

# Handle GET request with URL parameters


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"

# Handle PUT request


@app.route('/put', methods=['PUT'])
def handle_put():
    data = request.json  # Get JSON data sent in the request
    return jsonify({
        "message": "Put data received",
        "data": data
    })

# Handle DELETE request


@app.route('/delete/<int:id>', methods=['DELETE'])
def handle_delete(id):
    return jsonify({
        "message": f"Resource with ID {id} deleted"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
