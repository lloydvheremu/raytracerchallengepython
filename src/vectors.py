"""Scenario 1: Defining vectors """

import math

from src.tuple3d import Tuple3d


point = (4, -4, 3, 1)

class Vector(Tuple3d):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
            
    def __abs__(self):
        # Get Magnitude
        x = self.x * self.x
        y = self.y * self.y
        z = self.z * self.z
        return math.sqrt(x + y + z)
    

    def __eq__(self, other, e=0.00001):
        x_result = False
        y_result = False
        z_result = False

        if abs(self.x - other.x) <= e:
            x_result = True
        if abs(self.y - other.y) <= e:
            y_result = True
        if abs(self.z - other.z) <= e:
            z_result = True

        return x_result * y_result * z_result
    
    def nomarlize(self):
        return Vector(
            self.x / abs(self),
            self.y / abs(self),
            self.z / abs(self),
        )
    
    def cross(self, other):
        return Vector(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x,
        )
    
    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
       

    def __str__(self):
        return f'Vector( {self.x}, {self.y}, {self.z})'