# -*- coding: utf-8 -*-
"""Acme_test.py

test module for Product class of Acme.py
"""

#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        
    def test_product_name(self):
        """Test name to insure string""""
        prod = Product('Test Product')
        self.assertEqual(prod.name, str)
        
    def test_product_weight(self):
        """Test default product weight"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)  
        
class AcmeReportTest(unittest.TestCase):
    """Assert Class quality of report"""
    def test_generate_prods(self
        if len(set(product)) < 30:
            print("Not enough unique products, check random sample")
    def test_products_weights(self):
        


if __name__ == '__main__':
    unittest.main()
