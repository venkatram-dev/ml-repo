import pytest
from app.main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_predict(app, client):
    response = client.post('/predict', json={'feature_value': 1.5})
    assert response.status_code == 200
    assert 'predicted_value' in response.get_json()

def test_predict_missing_feature_value(client):
    # Simulate a POST request without the required 'feature_value' in the JSON payload
    response = client.post('/predict', json={})

    # Expect a 400 Bad Request response, indicating that the request was malformed
    assert response.status_code == 400

    # Optionally, check for an error message in the response to ensure the error is communicated to the client
    assert 'error' in response.get_json()