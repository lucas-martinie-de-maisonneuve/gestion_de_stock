import pygame
from db import Database
from element import Element
from screen import Screen
from afficher_produits import Afficher_products

class Main(Database, Element, Screen):
    def __init__(self):
        self.products = Afficher_products()
        Element.__init__(self)
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'store')
        Screen.__init__(self)
        self.products.menu()

main = Main()
main.__init__()