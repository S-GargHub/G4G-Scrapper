# File: test_api.py
import requests
from flask import Flask

app = Flask(__name__)

def test_api_endpoint_success():
    # Assuming your Flask app is running on localhost and port 5000
    url = 'http://localhost:5000/user/akashnnegi'

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response and check if it contains the expected message
    data = response.json()
    assert 'info' in data
    assert 'username' in data['info']
    assert data['info']['username'] == 'akashnnegi'


def test_api_endpoint_failure():
    # Assuming your Flask app is running on localhost and port 5000
    url = 'http://localhost:5000/akashnnegi'

    # Make a GET request to the API endpoint
    response = requests.get(url)

    assert response.status_code == 404