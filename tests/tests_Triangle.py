import unittest
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        a, b, c = 3, 4, 5
        expected_area = 6
        result = triangle_area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_triangle_perimeter(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12
        result = triangle_perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)
