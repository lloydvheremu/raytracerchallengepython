import unittest

from src.colors import Color

class TestColor(unittest.TestCase):
    def setUp(self):
        self.a = Color(1, 2, 3)
        self.b = Color(2, 4, 6)
        self.scalar = 2

    def test_adding_colors(self):
        result = self.a + self.b
        self.assertEqual(
            result,
            Color(
                self.a.red + self.b.red,
                self.a.green + self.b.green,
                self.a.blue + self.b.blue,
            )
        )

    def test_subtracting_colors(self):
        result = self.a - self.b
        self.assertEqual(
            result,
            Color(
                self.a.red - self.b.red,
                self.a.green - self.b.green,
                self.a.blue - self.b.blue,
            )
        )

    def test_multiplying_colors_by_scalar(self):
        result = self.a * self.scalar
        self.assertEqual(
            result,
            Color(
                self.a.red * self.scalar,
                self.a.green * self.scalar,
                self.a.blue * self.scalar,
            )
        )
    
    def test_multiplying_two_colors(self):
        result = self.a * self.b
        self.assertEqual(
            result,
            Color(
                self.a.red * self.b.red,
                self.a.green * self.b.green,
                self.a.blue * self.b.blue,
            )
        )            


if __name__ == '__main__':
    unittest.main()