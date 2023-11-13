from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, REGISTRY
import requests

app = Flask(__name__)

# Define a counter metric
counter = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route('/')
def hello():
    return jsonify(message="Hello this is testing from Flask App!")

@app.route('/call_service')
def call_service():
    # Simulate calling another service
    response = requests.get('http://service-b:5001')
    return jsonify(message=f"Response from Service B: {response.json()['message']}")

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)