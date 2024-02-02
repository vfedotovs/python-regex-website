import unittest
from flask import Flask
from ..app import index  # Import your index function from your actual app file

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_request_with_valid_pattern(self):
        response = self.client.post('/', data=dict(pattern=r'\d+', text='123abc456'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'123, 456', response.data)

    def test_post_request_with_invalid_pattern(self):
        response = self.client.post('/', data=dict(pattern='[a-z+', text='123abc456'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid regex pattern', response.data)

if __name__ == '__main__':
    unittest.main()

