# test_routes.py

import unittest
from flask import Flask
from your_app import create_app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = create_app(testing=True)
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)

    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
test_routes.py
