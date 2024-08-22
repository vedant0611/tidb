from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Healthy"}), 200

@app.route('/qaretrival', methods=['GET'])
def qaretrival():
    # Replace this with your logic for QA retrieval
    return jsonify({"question": "What is Flask?", "answer": "Flask is a micro web framework for Python."}), 200

if __name__ == '__main__':
    app.run(debug=True)
