
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL of the Chainlit apps
CHAINLIT_APP_1_URL = 'http://localhost:8001/process'
CHAINLIT_APP_2_URL = 'http://localhost:8002/process'  # Assuming similar setup for Chainlit app 2

@app.route('/process', methods=['POST'])
def process_request():
    user_input = request.json.get('input')

    # Send the input to both Chainlit apps
    response_1 = requests.post(CHAINLIT_APP_1_URL, json={'input': user_input})
    response_2 = requests.post(CHAINLIT_APP_2_URL, json={'input': user_input})

    # Get responses
    response_1_data = response_1.json()
    response_2_data = response_2.json()

    # Return combined responses
    return jsonify({
        'chainlit_app_1_response': response_1_data,
        'chainlit_app_2_response': response_2_data
    })

if __name__ == '__main__':
    app.run(debug=True)
