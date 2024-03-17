"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class CaclTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subsctract(self):
        res = calc.substract(15, 10)

        self.assertEqual(res, 5)
