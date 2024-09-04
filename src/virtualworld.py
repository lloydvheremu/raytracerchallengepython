from src.vectors import Vector


class Position(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Velocity(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Projectile:
    def __init__(self, position: Position, velocity: Velocity):
        """Intialize a projectile"""
        self.position = position
        self.velocity = velocity
    
    def __str__(self):
        return f'Projectile({self.position}, {self.velocity})'
        


class Gravity(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Wind(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

class Enviroment:
    def __init__(self, gravity: Gravity, wind: Wind):
        self.gravity = gravity
        self.wind = wind

    def __str__(self):
        return f'Enviroment({self.gravity}, {self.wind})'
        

def tick(env: Enviroment, proj: Projectile):
    position = proj.position.value() + proj.velocity.value() * 4
    velocity = proj.velocity.value() + env.gravity + env.wind.value()

    return Projectile(position=position, velocity=velocity)

# projectile starts one unit above the origin.
# velocity is normalized to 1 unit/tick.
p = Projectile(position=Position(0, 1, 0), velocity=Velocity(1, 1, 0).nomarlize())

# gravity -0.1 unit/tick, and wind is -0.01 unit/tick.
e = Enviroment(gravity=Gravity(0, -0.1, 0), wind=Wind(-0.01, 0, 0))

i = 0
while p.position.y >= 0:
    i += 1
    print(f'{i}. {p.position}')
    p = tick(e, p)
    