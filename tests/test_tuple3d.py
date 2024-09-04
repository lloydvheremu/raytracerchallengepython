import unittest

from src.tuple3d import Tuple3d

class TestTuple3d(unittest.TestCase):
    def setUp(self):
        self.a = Tuple3d(1, 2, 3)
        self.b = Tuple3d(2, 4, 6)
        self.scalar = 2

    def test_add(self):
        result = Tuple3d(
            self.a.x + self.b.x,
            self.a.y + self.b.y,
            self.a.z + self.b.z,
        )
        self.assertEqual(result, self.a + self.b, 'Not Equal')
    
    def test_subtract(self):
        result = Tuple3d(
            self.a.x - self.b.x,
            self.a.y - self.b.y,
            self.a.z - self.b.z,
        )
        self.assertEqual(result, self.a - self.b, 'Not Equal')

    def test_multiply(self):
        result = Tuple3d(
            self.a.x * self.scalar,
            self.a.y * self.scalar,
            self.a.z * self.scalar,
        )
        self.assertEqual(result, self.a * self.scalar)

    def test_division(self):
        result = Tuple3d(
            self.a.x / self.scalar,
            self.a.y / self.scalar,
            self.a.z / self.scalar,
        )
        self.assertEqual(result, self.a / self.scalar)

    def test_negation(self):
        result = Tuple3d(
            -self.a.x,
            -self.a.y,
            -self.a.z,
        )
        self.assertEqual(result, -self.a)

    def test_equality(self):
        self.assertEqual(self.a, self.a)
        self.assertNotEqual(self.a, self.b)
    

if __name__ == '__main__':
    unittest.main()