import unittest
from shapes.geometry import Circle, Triangle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), math.pi * 4)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(0)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0  # right-angled triangle with sides 3, 4, 5
        self.assertAlmostEqual(triangle.area(), expected_area)

    def test_is_right_angled_true(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_is_right_angled_false(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angled())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # doesn't form a triangle

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)

if __name__ == '__main__':
    unittest.main()
