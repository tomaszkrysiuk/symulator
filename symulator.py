import pygame


white = (255, 255, 255)
black = (  0,   0,   0)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

class Symulator:
    def start(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.init()
        pygame.display.set_caption('Symulator')
        sef.clock = pygame.time.Clock()

        self.symulatorLoop()

        pygame.quit()

    def symulatorLoop(self):
        self.screen.fill(white)
        shouldQuit = False
        while not shouldQuit:
            for event in pygame.event.get():
                shouldQuit = (event.type == pygame.QUIT)

            pygame.display.update()
            self.clock.tick(24)

