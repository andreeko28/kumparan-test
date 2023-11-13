from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello this is from Service B!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)