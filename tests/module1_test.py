import unittest
from ..app import app

class TestAppRoutes(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

    def test_home_route(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COSMETIC PRODUCTS', response.data)

    def test_add_product_route(self):
        # Test the add product route
        response = self.app.post('/add_product', data=dict(
            name='New Product',
            brand='Test Brand',
            price='$19.99'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New Product', response.data)
        self.assertIn(b'Test Brand', response.data)
        self.assertIn(b'$19.99', response.data)

if __name__ == '__main__':
    unittest.main()
