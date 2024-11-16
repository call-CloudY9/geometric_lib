import unittest
import math
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_calc_with_valid_circle(self):
        fig = 'circle'
        func = 'area'
        size = [5]
        expected_result = math.pi * 25
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_calc_with_valid_square(self):
        fig = 'square'
        func = 'perimeter'
        size = [4]
        expected_result = 16
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_calc_with_valid_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]
        expected_result = 6
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_calc_raises_error_for_invalid_figure(self):
        fig = 'invalid'
        func = 'area'
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_raises_error_for_invalid_function(self):
        fig = 'circle'
        func = 'invalid'
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_raises_error_for_negative_size(self):
        fig = 'circle'
        func = 'area'
        size = [-5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_raises_error_for_invalid_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [1, 1, 3]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)
