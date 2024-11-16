import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        radius = 5
        expected_area = math.pi * radius * radius
        result = circle_area(radius)
        self.assertEqual(result, expected_area)

    def test_circle_perimeter(self):
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = circle_perimeter(radius)
        self.assertEqual(result, expected_perimeter)
