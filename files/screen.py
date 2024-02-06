import pygame

class Screen:
    def __init__(self):
        self.W = 1200
        self.H = 700
        self.Fenetre = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Gestion de Stock")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Fenetre.fill((255, 255, 255))

