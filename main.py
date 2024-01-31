import pygame
from db import Database
from element import Element
from screen import Screen

class Main(Database, Element, Screen):
    def __init__(self):
        Element.__init__(self)
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'store')
        Screen.__init__(self)
        self.menu_run = True

    def affichage(self):
        menu_button1_rect = pygame.Rect(0, 0, 0, 0)
        menu_button2_rect = pygame.Rect(0, 0, 0, 0)
        menu_button3_rect = pygame.Rect(0, 0, 0, 0)
        
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button1_rect.collidepoint(event.pos):
                        input_name = 1
                    elif menu_button2_rect.collidepoint(event.pos):
                        input_name = 2

            self.img(600, 350, 1200, 700, 'background')
            self.draw_overlay((120,120,120,30), 600, 400, 1100, 500)
            if menu_button1_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button1_rect = self.button_rect(self.darkblue, 200, 75, 175, 50)
            else:
                menu_button1_rect = self.button_rect(self.blue, 200, 75, 175, 50)
            self.texte(30, 'Fiches', self.black, 200, 75)

            if menu_button2_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button2_rect = self.button_rect(self.darkblue, 600, 75, 175, 50)
            else:
                menu_button2_rect = self.button_rect(self.blue, 600, 75, 175, 50)
            self.texte(30, 'Entrées', self.black, 600, 75)

            if menu_button3_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button3_rect = self.button_rect(self.darkblue, 1000, 75, 175, 50)
            else:
                menu_button3_rect = self.button_rect(self.blue, 1000, 75, 175, 50)
            self.texte(30, 'Sorties', self.black, 1000, 75)


            self.update()

main = Main()
main.affichage()
