import math
from src.tuple3d import Tuple3d

class Color(Tuple3d):
    def __init__(self, red, green, blue):
        super().__init__(x=red, y=green, z=blue)
        self.red = red
        self.green = green
        self.blue = blue


    def __mul__(self, other):
        # Multiplication with a scalar or color object
        if isinstance(other, (int, float)):
            # Scalar Multilplication
            x = self.red * other
            y = self.green * other
            z = self.blue * other
            return Color(x, y, z)
        elif isinstance(other, Color):
            # Vector Multiplication
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue
            )
        else:
            raise TypeError("Unsupported operand type for '*'.")

    def to_rgb(self):
        # ensure value is in range 0 - 255
        r = math.ceil(min(255.0, max(0.0, self.red * 255.0)))
        g = math.ceil(min(255.0, max(0.0, self.green * 255.0)))
        b = math.ceil(min(255.0, max(0.0, self.blue * 255.0)))      

        return r, g, b
    
    def __str__(self):
        return f'Color( {self.red}, {self.green}, {self.blue})'
        
    def __repr__(self) -> str:
        # string representations for list
        return self.__str__()
    
