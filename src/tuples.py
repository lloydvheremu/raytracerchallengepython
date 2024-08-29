"""Scenario 1: Defining vectors """

import math


point = (4, -4, 3, 1)

class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def value(self):
        return self

    def __add__(self, other):
        # Addition of two vectors
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __mul__(self, scalar):
        # Multiplication with a scalar
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Vector(x, y, z)
    
    def __truediv__(self, scalar):
        # Division with a scalar
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        return Vector(x, y, z)


    def __sub__(self, other):
        # Subtract two vectors
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector(x, y, z)
        
    def __neg__(self):
        # Negate instance
        x = -self.x
        y = -self.y
        z = -self.z    
        return Vector(x, y, z)
    
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
    
        

a1 = Vector(3, -2, 5)

a2 = Vector(1, 2, 3)

n = Vector(2, 3, 4)
m = Vector(1, 2, 3)

# a3 = a1.add(a2)
a3 = m @ n

print(a3)
