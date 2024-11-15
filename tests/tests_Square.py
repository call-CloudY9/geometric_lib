import unittest
from square import area as square_area, perimeter as square_perimeter


class TestSquare(unittest.TestCase):
    def test_square_area(self):
        side = 4
        expected_area = 16
        result = square_area(side)
        self.assertEqual(result, expected_area)

    def test_square_perimeter(self):
        side = 4
        expected_perimeter = 16
        result = square_perimeter(side)
        self.assertEqual(result, expected_perimeter)
