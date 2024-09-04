
import math
from unittest import TestCase
import unittest

from src import vectors

class TestVector(TestCase):
    def setUp(self):
        self.a = vectors.Vector(1, 2, 3)
        self.b = vectors.Vector(2, 4, 6)
        self.scalar = 2
    
    def test_add(self):
        result = vectors.Vector(
            self.a.x + self.b.x,
            self.a.y + self.b.y,
            self.a.z + self.b.z,
        )
        self.assertEqual(result, self.a + self.b, 'Not Equal')
    
    def test_subtract(self):
        result = vectors.Vector(
            self.a.x - self.b.x,
            self.a.y - self.b.y,
            self.a.z - self.b.z,
        )
        self.assertEqual(result, self.a - self.b, 'Not Equal')

    def test_multiply(self):
        result = vectors.Vector(
            self.a.x * self.scalar,
            self.a.y * self.scalar,
            self.a.z * self.scalar,
        )
        self.assertEqual(result, self.a * self.scalar)

    def test_division(self):
        result = vectors.Vector(
            self.a.x / self.scalar,
            self.a.y / self.scalar,
            self.a.z / self.scalar,
        )
        self.assertEqual(result, self.a / self.scalar)

    def test_negation(self):
        result = vectors.Vector(
            -self.a.x,
            -self.a.y,
            -self.a.z,
        )
        self.assertEqual(result, -self.a)

    def test_equality(self):
        self.assertEqual(self.a, self.a)
        self.assertNotEqual(self.a, self.b)

    def test_magnitues(self):
        result = math.sqrt(
            self.a.x*self.a.x +
            self.a.y*self.a.y +
            self.a.z*self.a.z
        )
        self.assertEqual(abs(self.a), result)

    def test_normalization(self):
        self.assertEqual(abs(self.a.nomarlize()), 1.0)

    def test_dot_product(self):
        result  = self.a @ self.b
        dot_result = self.a.x*self.b.x + self.a.y*self.b.y + self.a.z*self.b.z
        self.assertEqual(result, dot_result)

    def test_cross_product(self):
        result = vectors.Vector(
            self.a.y*self.b.z - self.a.z*self.b.y,
            self.a.z*self.b.x - self.a.x*self.b.z,
            self.a.x*self.b.y - self.a.y*self.b.x,
        )
        self.assertEqual(result, self.a.cross(self.b))

if __name__ == '__main__':
    unittest.main()