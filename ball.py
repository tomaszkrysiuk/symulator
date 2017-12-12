from entity import Entity
import pygame

class Ball(Entity):
    def __init__(self, x, y, r, color, mass = 1):
        Entity.__init__(self, x, y, (0, 0), mass)
        self.radious = r
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radious)

