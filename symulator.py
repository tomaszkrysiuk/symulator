import pygame
import random
from colider import colide
from ball import Ball


white = (255, 255, 255)
black = (  0,   0,   0)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)
colors = [white, black, red, green, blue]

class Symulator:
    def start(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Symulator')
        self.clock = pygame.time.Clock()

        self.symulatorLoop()

        pygame.quit()

    def symulatorLoop(self):
        self.screen.fill(white)
        shouldQuit = False
        entities = []
        entities += self.createBalls()

        while not shouldQuit:
            for event in pygame.event.get():
                shouldQuit = (event.type == pygame.QUIT)

            self.screen.fill(white)
            #self.applyGravity(entities)
            self.moveEntities(entities)
            colide(entities)
            self.drawEntities(entities)
            pygame.display.update()
            self.clock.tick(60)

    def applyGravity(self, entities):
        for e in entities:
            e.acceleration = (e.acceleration[0], e.acceleration[1] + 0.4)

    def drawEntities(self, entities):
        for e in entities:
            e.draw(self.screen)

    def moveEntities(self, entities):
        for e in entities:
            e.move()
            if e.x > (self.width - e.radious):
                e.x = self.width - e.radious
                e.velocity = (-e.velocity[0], e.velocity[1])
            if e.y > (self.height - e.radious):
                e.y = self.height - e.radious
                e.velocity = (e.velocity[0], -e.velocity[1])
            if e.x < (0 + e.radious):
                e.x = 0 + e.radious
                e.velocity = (-e.velocity[0], e.velocity[1])
            if e.y < 0 + e.radious:
                e.y = 0 + e.radious
                e.velocity = (e.velocity[0], -e.velocity[1])

    def createBalls(self):
        balls = []
        for i in range(5):
            balls.append(Ball((self.width/2) + random.randint(-100, 100),
                              (self.width/2) + random.randint(-100, 100),
                              random.randint(60, 85),
                              colors[random.randint(1, 4)],
                              (random.randint(-10, 10), random.randint(-10, 10))))
        return balls

