from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "Simplicity is the soul of efficiency.",
    "Code never lies, comments sometimes do."
]

@app.route('/')
def home():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
