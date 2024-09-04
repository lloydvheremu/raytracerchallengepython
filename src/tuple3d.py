class Tuple3d:
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
        return Tuple3d(x, y, z)

    def __mul__(self, other):
        # Multiplication with a scalar or vector
        if isinstance(other, (int, float)):
            # Scalar Multilplication
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return Tuple3d(x, y, z)
        elif isinstance(other, Tuple3d):
            # Vector Multiplication
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand for '*'.")

    def __truediv__(self, scalar):
        # Division with a scalar
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        return Tuple3d(x, y, z)


    def __sub__(self, other):
        # Subtract two vectors
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Tuple3d(x, y, z)
        
    def __neg__(self):
        # Negate instance
        x = -self.x
        y = -self.y
        z = -self.z    
        return Tuple3d(x, y, z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        return f'Tuple3d( {self.x}, {self.y}, {self.z})'
        