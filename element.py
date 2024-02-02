import pygame
from screen import Screen

class Element(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (200, 200, 200)
        self.blue = (162, 210, 255)
        self.darkblue = (0, 180, 194)
        self.green = (149, 213, 178)
        self.scroll = 1


    def texte(self, texte_size, texte_content, color, x, y):
        pygame.font.init()
        Texte = pygame.font.Font('files/font/metrophobic.ttf', texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.Fenetre.blit(Texte, Texte_rect)

    def texte_not_align(self, texte_size, texte_content, color, x, y):
        Texte = pygame.font.Font('files/font/metrophobic.ttf', texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(topleft=(x, y))
        self.Fenetre.blit(Texte, Texte_rect)

    def button_rect(self, color, x, y, largeur, hauteur, arrondi):
        button = pygame.draw.rect(self.Fenetre, color, pygame.Rect(x - largeur//2, y - hauteur//2, largeur, hauteur),0, arrondi)
        return button

    def rect(self, color, x, y, largeur, hauteur, arrondi):
        button = pygame.draw.rect(self.Fenetre, color, pygame.Rect(x, y, largeur, hauteur),0, arrondi)
        return button

    def simple_rect(self, color, x, y, largeur, longueur, epaisseur, arrondi):
        button = pygame.draw.rect(self.Fenetre, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, arrondi)
        return button
   
    def img(self, x, y, largeur, hauteur, image_name):
        image = pygame.image.load(f'files/img/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        self.Fenetre.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def draw_overlay(self, coloralpha, x, y, largeur, hauteur):
        overlay_surface = pygame.Surface((largeur,hauteur), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Fenetre.blit(overlay_surface, ( x - largeur // 2, y - hauteur // 2))

    def event_scroll(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_down.collidepoint(event.pos):
                self.scroll += 50
            if self.button_up.collidepoint(event.pos):
                self.scroll -= 50
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.scroll -= 50
            elif event.key == pygame.K_UP:
                self.scroll += 50

    def scroll_bar(self):
            self.button_down = self.simple_rect(self.white, 1150, 150, 40, 40, 0, 0) 
            self.img(1150, 150, 40, 40, 'flecheup')
            self.button_up = self.simple_rect(self.white, 1150, 550, 40, 40, 0, 0) 
            self.img(1150, 550, 40, 40, 'flechedown')
            self.button_rect(self.grey, 1150, 200 - self.scroll, 39, 60, 0)
            self.simple_rect(self.black, 1150, 200 - self.scroll, 39, 60, 1, 0)
            self.simple_rect(self.black, 1150, 350, 40, 360, 1, 0)