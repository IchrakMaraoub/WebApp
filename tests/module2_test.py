import unittest
from app import app

class TestAppFunctionality(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

    def test_add_product_functionality(self):
        # Test the functionality of adding a product
        initial_products_count = len(app.products)

        response = self.app.post('/add_product', data=dict(
            name='Test Product',
            brand='Test Brand',
            price='$9.99'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product', response.data)
        self.assertIn(b'Test Brand', response.data)
        self.assertIn(b'$9.99', response.data)

        # Check if the product count increased
        final_products_count = len(app.products)
        self.assertEqual(final_products_count, initial_products_count + 1)

if __name__ == '__main__':
    unittest.main()
