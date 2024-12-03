import unittest
from web.app import app
from flask import jsonify
import json
from web.utils import connect_to_mongo
from unittest.mock import patch


class FlaskAppTests(unittest.TestCase):

    @patch('web.utils.connect_to_mongo')
    def test_get_data_success(self, mock_connect):
        mock_connect.return_value = {"my_collection": [{"name": "Test", "value": 123}]}
        with app.test_client() as client:
            response = client.get('/api/data')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(response.json) > 0)

    @patch('web.utils.connect_to_mongo')
    def test_get_data_failure(self, mock_connect):
        mock_connect.return_value = None
        with app.test_client() as client:
            response = client.get('/api/data')
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json['error'], "Database connection failed")

    def test_post_data_success(self):
        with app.test_client() as client:
            response = client.post('/api/data', json={"name": "Test", "value": 123})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], "Data inserted successfully!")

    def test_post_data_missing_fields(self):
        with app.test_client() as client:
            response = client.post('/api/data', json={"name": "Test"})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['error'], "Invalid data. 'name' and 'value' are required.")

    @patch('web.utils.connect_to_mongo')
    def test_post_data_failure(self, mock_connect):
        mock_connect.return_value = None
        with app.test_client() as client:
            response = client.post('/api/data', json={"name": "Test", "value": 123})
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json['error'], "Database connection failed")

    @patch('web.utils.connect_to_mongo')
    def test_network_failure(self, mock_connect):
        mock_connect.side_effect = Exception("Network error")
        with app.test_client() as client:
            response = client.get('/api/data')
            self.assertEqual(response.status_code, 500)
            self.assertTrue("Error fetching data" in response.json['error'])

if __name__ == '__main__':
    unittest.main()
