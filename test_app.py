import pytest
from flask import Flask
from app import index  # Import your index function from your actual app file


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_post_request_with_valid_pattern(client):
    response = client.post('/', data=dict(pattern=r'\d+', text='123abc456'))
    assert response.status_code == 200
    assert b'123, 456' in response.data


def test_post_request_with_invalid_pattern(client):
    response = client.post('/', data=dict(pattern='[a-z+', text='123abc456'))
    assert response.status_code == 200
    assert b'Invalid regex pattern' in response.data
