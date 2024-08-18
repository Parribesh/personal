import os
from flask import Flask, request, jsonify,  render_template

app = Flask(__name__)

# Change the current working directory to the root directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Handle GET request


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Handle POST request


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


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
    app.run(host='0.0.0.0', port=8000)
