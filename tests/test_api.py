from fastapi.testclient import TestClient
from qbe_factor.api import app
import json

client = TestClient(app)

def load_json_file(filename):
    with open(filename) as file:
        return json.load(file)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "PONG"}


def test_validate():
    input_data = load_json_file("tests/test_input.json")
    response = client.post("/validate", json=input_data)
    assert response.status_code == 200

    validation_data = response.json()
    assert validation_data['valid'] is True
    assert validation_data['message'] == ''


def test_get_factors():
    input_data = load_json_file("tests/test_input.json")
    response = client.post("/get_factors", json=input_data)
    assert response.status_code == 200

    response_data = response.json()
    assert len(input_data['data']) == response_data['results']

    for variable, result in zip(input_data['data'], response_data['results']):
        assert variable['var_name'] == result['var_name']
        assert variable['category'] == result['category']
        assert 'factor' in result

        factor = result['factor']
        assert isinstance(factor, float)
        assert 0.0 <= factor <= 1.0  # Python chained comparison




