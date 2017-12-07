class Entity:
    def __init__(self, x = 0, y = 0, velocity = (0.0, 0.0), mass = 1.0):
        self.x = x
        self.y = y
        self.velocity = velocity
        if mass == 0:
            mass = 0.001
        self.mass = mass
        self.acceleration = 0.0, 0.0

    def applyForce(self, x, y):
        self.acceleration = (self.acceleration[0] + x/self.mass,
                             self.acceleration[1] + y/self.mass)

    def move(self):
        self.velocity = (self.velocity[0] + self.acceleration[0],
                         self.velocity[1] + self.acceleration[1])
        self.acceleration = 0, 0
        self.x += self.velocity[0]
        self.y += self.velocity[1]
