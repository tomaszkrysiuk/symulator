from entity import Entity

class Ball(Entity):
    def __init__(self, x, y, r, color):
        Entity.__init__(self, x, y)
        self.radious = r
        self.color = color
