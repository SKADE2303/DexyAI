from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def home():
    return 'Server runnning succesfully'

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Log the raw request data for debugging
        print("Raw request data:", request.get_data(as_text=True))
        
        # Check if JSON data exists
        if not request.is_json:
            return jsonify({"error": "Request content-type must be application/json"}), 400

        # Parse the JSON data
        data = request.json
        print("Parsed JSON data:", data)

        # Validate the 'message' field
        if 'message' not in data:
            return jsonify({"error": "'message' field is required"}), 400

        message = data['message']
        print("Message received:", message)

        
        result = subprocess.run(
            ["python", "send_message.py", message],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            return jsonify({"status": "Message sent successfully!"})
        else:
            return jsonify({"status": "Failed to send message", "details": result.stderr}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

if __name__ == "__main__":
    app.run(debug=True)
