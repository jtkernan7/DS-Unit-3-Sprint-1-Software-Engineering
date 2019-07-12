import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """"test default flame to be 0.5"""
        prod = Product('Test2')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_product(self):
        """test steal function"""
        prod = Product('Test3', 20, 1, .5)
        self.assertEqual(prod.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for product in products:
            split = product.name.split()
            self.assertIn(split[0], ADJECTIVES)
            self.assertIn(split[1], NOUNS)


if __name__ == '__main__':
    unittest.main()