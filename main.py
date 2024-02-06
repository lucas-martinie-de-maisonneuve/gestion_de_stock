from files.db import Database
from files.element import Element
from files.screen import Screen
from files.display import Display

class Main(Database, Element, Screen):
    def __init__(self):
        self.products = Display()
        Element.__init__(self)
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'store')
        Screen.__init__(self)
        self.products.menu()

main = Main()
main.__init__()