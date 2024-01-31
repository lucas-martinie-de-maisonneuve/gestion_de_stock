import pygame
from screen import Screen

class Element(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 180, 194)
        self.darkblue = (0, 107, 114)

    def texte(self, texte_size, texte_content, color, x, y):
        pygame.font.init()
        Texte = pygame.font.SysFont('Calibri', texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.Fenetre.blit(Texte, Texte_rect)

    def button_rect(self, color, x, y, longueur, largeur):
        button = pygame.draw.rect(self.Fenetre, color, pygame.Rect(x - longueur//2, y - largeur//2, longueur, largeur),0,2)
        return button
    
    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'img/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        self.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def draw_overlay(self, coloralpha, x, y, largeur, longueur):
        overlay_surface = pygame.Surface((largeur, longueur), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Fenetre.blit(overlay_surface, (x - largeur // 2, y - longueur // 2))