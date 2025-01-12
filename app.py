import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import generate_chat_response

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "https://medicgpt.vercel.app"
        ]
    }
})

# Define a root route for testing the deployment
@app.route('/')
def index():
    return "Welcome to the Flask app deployed on Render!", 200

@app.route('/generate-response', methods=['POST'])
def generate_response():
    data = request.json
    text_message = data['textMessage']
    
    try:
        response = generate_chat_response(text_message)
        return jsonify({"response": response}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # Disable debug mode in production