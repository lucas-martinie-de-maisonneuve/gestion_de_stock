import pygame
from stock import Gestion
from element import Element

class Display(Element):
    def __init__(self):
        Element.__init__(self)
        self.menu_run = True
        self.showProduct_run = False
        self.add_product_run = False
        self.liste_product_run = False
        self.modify_delete_run = False
        self.gestion = Gestion()
        self.list_product = self.gestion.all_product()
        self.list_category = self.gestion.read_categories()
        self.category_choose = ""        
        self.back_menu = pygame.Rect(0, 0, 0, 0)
        self.deleted = False

    def menu(self):
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
                        self.showProduct_run = True
                        self.showproduct()
                        self.menu_run = False
                    elif menu_button2_rect.collidepoint(event.pos):
                        self.add_product_run = True
                        self.display_add_product()
                        self.menu_run = False
                    elif menu_button3_rect.collidepoint(event.pos):
                        self.liste_product_run = True
                        self.liste_products()
                        self.menu_run = False

            self.img(600, 350, 1200, 700, 'background')
            self.draw_overlay((120,120,120,30), 600, 400, 1100, 500)
            self.button_rect((233, 236, 239), 250, 200, 300, 50, 15)
            self.simple_rect((173, 181, 189), 250, 200, 300, 50, 5, 15)
            self.texte(30, 'Tableau de bord', self.black, 250, 200)
            
            if menu_button1_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button1_rect = self.button_rect(self.darkblue, 200, 75, 240, 60, 5)
                self.simple_rect(self.black, 200, 75, 240, 60,2, 5)
            else:
                menu_button1_rect = self.button_rect(self.blue, 200, 75, 230, 50, 5)
                self.simple_rect(self.black, 200, 75, 230, 50,2, 5)
            self.texte(30, 'Liste produits', self.black, 200, 75)

            if menu_button2_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button2_rect = self.button_rect(self.darkblue, 600, 75, 240, 60, 5)
                self.simple_rect(self.black, 600, 75, 240, 60,2, 5)

            else:
                menu_button2_rect = self.button_rect(self.blue, 600, 75, 230, 50, 5)
                self.simple_rect(self.black, 600, 75, 230, 50,2, 5)
            self.texte(30, 'Ajouter produit', self.black, 600, 75)

            if menu_button3_rect.collidepoint(pygame.mouse.get_pos()):
                menu_button3_rect = self.button_rect(self.darkblue, 1000, 75, 240, 60, 5)
                self.simple_rect(self.black, 1000, 75, 240, 60,2, 5)
            else:
                menu_button3_rect = self.button_rect(self.blue, 1000, 75, 230, 50, 5)
                self.simple_rect(self.black, 1000, 75, 230, 50,2, 5)
            self.texte(30, 'Modifier produit', self.black, 1000, 75)
            
            last_product = self.gestion.get_last_product()
            detail_last_product = last_product[0]
            self.texte_not_align(20, "Dernier produit ajouté :", (self.black), 80, 250)
            self.texte_not_align(25, f"{detail_last_product[1]}", (self.black), 120, 280)

            max_product = self.gestion.get_highest_product()
            detail_highest_product = max_product[0]
            self.texte_not_align(20, "Produit avec le plus de capacité:", (self.black), 80, 350)
            self.texte_not_align(25, f"{detail_highest_product[1]} ({detail_highest_product[4]})", (self.black), 120, 380)


            self.update()


    def showproduct(self):
        self.list_product = self.gestion.all_product()
        while self.showProduct_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.event_scroll(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_menu.collidepoint(event.pos):
                        self.menu_run = True
                        self.menu()
                        self.showProduct_run = False

            self.img(600, 350, 1200, 700, 'background')
            i = 1
            self.scroll_bar()
#Show products
            self.texte_not_align(20, 'ID', self.black, 68 ,120 + self.scroll)
            self.texte_not_align(20, 'Produits', self.black, 150 , 120 + self.scroll)
            self.texte(20, 'Description', self.black, 500 ,120 + self.scroll)
            self.texte(20, 'Prix', self.black, 750 ,120 + self.scroll)
            self.texte(20, 'Quantité', self.black, 850 ,120 + self.scroll)
            self.texte(20, 'Catégorie', self.black, 975 ,120 + self.scroll)

            for product in self.list_product:
                i += 1
                self.rect((254, 250, 224), 50 ,70 + 50 * i + self.scroll, 1000, 40, 2)
                self.texte_not_align(20, f"{int(product[0])} |", self.black, 70 ,75 + 50 * i + self.scroll)
                self.texte_not_align(20, f"    {product[1]}", self.black, 125 ,75 + 50 * i + self.scroll)
                self.texte_not_align(20, f"- {product[2]}", self.black, 350 ,75 + 50 * i + self.scroll)
                self.texte(20, f"{int(product[3])} €", self.black, 750 ,85 + 50 * i + self.scroll)
                self.texte(20, f"{int(product[4])} ", self.black, 850 ,85 + 50 * i + self.scroll)
                self.texte(20, f"{(product[5])}", self.black, 975 ,85 + 50 * i + self.scroll)

            if self.back_menu.collidepoint(pygame.mouse.get_pos()):
                self.back_menu = self.button_rect(self.darkblue, 1140, 55, 110, 55, 5)
            else:
                self.back_menu = self.button_rect(self.blue, 1140, 55, 100, 45, 2)
            self.texte(25, 'Menu', self.black, 1140, 50)

            self.update()
        
    def display_add_product(self):
        self.cate = 1
        name = ""
        description = ""
        prix = ""
        quantity = ""
        all_info = False
        confirm = pygame.Rect(0, 0, 0, 0)
        confirm_message = False
        self.back_menu_add = pygame.Rect(0, 0, 0, 0)
        while self.add_product_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.back_menu_add.collidepoint(event.pos):
                        self.menu_run = True
                        self.menu()
                        self.add_product_run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not confirm_message:
                    if name_input.collidepoint(event.pos):
                        self.cate = 1
                    elif description_input.collidepoint(event.pos):
                        self.cate = 2
                    elif prix_input.collidepoint(event.pos):
                        self.cate = 3
                    elif quantity_input.collidepoint(event.pos):
                        self.cate = 4
                    elif category_select.collidepoint(event.pos):
                        category_select = category[0]
                    elif all_info:
                        if confirm.collidepoint(event.pos) and all_info:
                            self.gestion.add_product(name, description, int(prix), int(quantity), int(self.category_choose))
                            confirm_message = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.cate == 1 :
                            name = name[:-1]
                        if self.cate == 2 :
                            description = description[:-1]
                        if self.cate == 3 :
                            prix = prix[:-1]
                        if self.cate == 4 :
                            quantity = quantity[:-1]
                    else:
                        if self.cate == 1:
                            if event.unicode.isalpha() and len(name) < 15:
                                name += event.unicode
                                name = name.capitalize()
                        elif self.cate == 2:
                            if event.unicode:
                                description += event.unicode
                                description = description
                        elif self.cate == 3:
                            if event.unicode.isdigit():
                                prix += event.unicode
                        elif self.cate == 4:
                            if event.unicode.isdigit():
                                quantity += event.unicode

            self.img(600, 350, 1200, 700, 'background')

            if self.back_menu_add.collidepoint(pygame.mouse.get_pos()) and not confirm_message:
                self.back_menu_add = self.button_rect(self.darkblue, 1100, 55, 160, 60, 5)
            else:
                self.back_menu_add = self.button_rect(self.blue, 1100, 55, 150, 50, 2)
            self.texte(30, 'Menu', self.black, 1100, 55)

            if self.cate == 1:
                self.img(25, 70, 50, 50, 'fleche')
            self.texte(20, "Nom du produit :", self.black,300, 20)
            name_input = self.button_rect(self.white, 300, 70, 450 ,70, 5)
            self.simple_rect(self.black, 300, 70, 450, 70, 3, 5)
            self.texte(20, name, self.black,300, 70)

            if self.cate == 2:
                self.img(25, 200, 50, 50, 'fleche')
            self.texte(20, "Description", self.black,300, 150)
            description_input = self.button_rect(self.white, 300, 200, 450 ,70, 5)
            self.simple_rect(self.black, 300, 200, 450, 70, 3, 5)
            self.texte(20, description, self.black,300, 200)

            if self.cate == 3:
                self.img(25, 330, 50, 50, 'fleche')
            self.texte(20, "Prix :", self.black,300, 280)
            prix_input = self.button_rect(self.white, 300, 330, 450 ,70, 5)
            self.simple_rect(self.black, 300, 330, 450, 70, 3, 5)
            self.texte(20,f"{prix} €", self.black,300, 330)

            if self.cate == 4:
                self.img(25, 460, 50, 50, 'fleche')
            self.texte(20, "Quantité :", self.black,300, 410)
            quantity_input = self.button_rect(self.white, 300, 460, 450 ,70, 5)
            self.simple_rect(self.black, 300, 460, 450, 70, 3, 5)
            self.texte(20, quantity, self.black,300, 460)

            self.texte(20, "Catégorie :", self.black,300, 540)
            self.button_rect(self.white, 300, 590, 450 ,70, 5)
            self.simple_rect(self.black, 300, 590, 450, 70, 3, 5)
            if self.category_choose == "":
                self.texte(20, "Veuillez selectionner une catégrie à droite", self.grey,300, 590)
            else:
                self.texte(20, self.display_choose, self.black,300, 590)

            max_cate = len(self.list_category)
            y = self.H // max_cate
            i = 0
            for category in self.list_category:
                category_select = self.button_rect(self.grey,650, 100 +  y * i, 150, 50, 1)
                self.texte(20, category[1], self.black, 650,100 + y * i)
                if category_select.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:       
                    self.category_choose = category[0]
                    self.display_choose = category [1]
                i += 1

            self.texte_not_align(15, "Nom du produit", (self.black), 875, 510)
            self.texte_not_align(15, "Description", (self.black), 875, 540)
            self.texte_not_align(15, "Prix", (self.black), 875, 570)
            self.texte_not_align(15, "Quantité", (self.black), 875, 600)
            self.texte_not_align(15, "Catégorie", (self.black), 875, 630)

            if name != "" and description != ""  and prix != "" and quantity != "" and self.category_choose != "":
                confirm = self.button_rect(self.green, 975, 350, 300, 300, 10)
                self.texte(30, "Cliquez ici pour", (self.black), 975, 300)
                self.texte(30, "ajouter le produit", (self.black), 975, 400)
                all_info = True
            else:
                self.button_rect(self.grey, 975, 350, 300, 300, 10)
                self.texte(30, "Veuillez compléter", (self.black), 975, 300)
                self.texte(30, "les infos produit", (self.black), 975, 400)
            if name == "":
                self.img(860, 520, 25,25,'invalide')
            else:
                self.img(860, 520, 25,25,'valide')
            if description == "":
                self.img(860, 550, 25,25,'invalide')
            else:
                self.img(860, 550, 25,25,'valide')
            if prix == "":
                self.img(860, 580, 25,25,'invalide')
            else:
                self.img(860, 580, 25,25,'valide')
            if quantity == "":
                self.img(860, 610, 25,25,'invalide')
            else:
                self.img(860, 610, 25,25,'valide')
            if self.category_choose == "":
                self.img(860, 640, 25,25,'invalide')
            else:
                self.img(860, 640, 25,25,'valide')

            if confirm_message:
                self.button_rect(self.blue, 600, 300, 800, 400, 15)
                self.simple_rect(self.black, 600, 300, 800, 400, 5 ,15)
                self.texte(30, f"Le produit {name} a bien été ajouté", (self.black), 600, 280)
                if self.back_menu_add.collidepoint(pygame.mouse.get_pos()):
                    self.back_menu_add = self.button_rect(self.darkblue, 600, 400, 175,70, 10)
                else:
                    self.back_menu_add = self.button_rect(self.grey, 600, 400, 165, 60, 10)
                self.texte(25, f"Retour menu", (self.black), 600, 400)
            self.update()

    def liste_products(self):
        self.list_product = self.gestion.all_product()
        while self.liste_product_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
            self.img(600, 350, 1200, 700, 'background')
            for i, product in enumerate(self.list_product):
                column = i % 5
                row = i // 5
                product_select = self.simple_rect(self.grey, 110 + column * 240, 150 + row * 100, 200, 35, 4, 3)
                self.texte(20, product[1], self.black, 110 + column * 240, 150 + row * 100)
                if product_select.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.modify_delete_run = True
                    self.modify_delete(product)
                    self.liste_product_run = False
                
            self.update()

    def modify_delete(self, product):
        name, description, prix, quantity,self.display_choose = product[1],product[2],str(product[3]),str(product[4]), product[5]
        self.modif_name = pygame.Rect(0, 0, 0, 0)
        self.modif_desc = pygame.Rect(0, 0, 0, 0)
        self.modif_prix = pygame.Rect(0, 0, 0, 0)
        self.modif_quant = pygame.Rect(0, 0, 0, 0)
        self.modif_categ = pygame.Rect(0, 0, 0, 0)
        self.delete_button_confirm = pygame.Rect(0, 0, 0, 0)
        self.back_menu_modify = pygame.Rect(0, 0, 0, 0)
        self.cate = 1
        self.category_choose = 0
        confirm_delete = False
        deleted = False
        for category in self.list_category:
            if category[1] == product[5]:
                self.category_choose = category[0]

        while self.modify_delete_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and not confirm_delete:
                    if self.modif_name.collidepoint(event.pos):
                        self.cate = 1
                    elif self.modif_desc.collidepoint(event.pos):
                        self.cate = 2
                    elif self.modif_prix.collidepoint(event.pos):
                        self.cate = 3
                    elif self.modif_quant.collidepoint(event.pos):
                        self.cate = 4
                    elif self.modif_categ.collidepoint(event.pos):
                        self.cate = 5
                    elif self.update_button.collidepoint(event.pos) :
                        self.gestion.update_product(str(name), str(description), int(prix), int(quantity), int(self.category_choose), product[0])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_menu_modify.collidepoint(event.pos):
                        self.menu_run = True
                        self.menu()
                        self.modify_delete_run = False
                    elif self.delete_button.collidepoint(event.pos):
                        confirm_delete = True
                    elif self.delete_button_confirm.collidepoint(event.pos):
                        self.gestion.remove_product(product[0])
                        deleted = True
                        confirm_delete = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.cate == 1 :
                            name = name[:-1]
                        if self.cate == 2 :
                            description = description[:-1]
                        if self.cate == 3 :
                            prix = prix[:-1]
                        if self.cate == 4 :
                            quantity = quantity[:-1]
                    else:
                        if self.cate == 1:
                            if event.unicode.isalpha() and len(name) < 15:
                                name += event.unicode
                                name = name.capitalize()
                        elif self.cate == 2:
                            if event.unicode:
                                description += event.unicode
                                description = description.capitalize()
                        elif self.cate == 3:
                            if event.unicode.isdigit():
                                prix += event.unicode
                        elif self.cate == 4:
                            if event.unicode.isdigit():
                                quantity += event.unicode

            self.img(600, 350, 1200, 700, 'background')


            if self.modif_name.collidepoint(pygame.mouse.get_pos()):
                self.modif_name = self.button_rect(self.darkblue, 200, 60, 180, 50 +10, 5)
            else:
                self.modif_name = self.button_rect(self.blue, 200, 60, 170, 50, 2)
            self.texte(25, 'Modif. Nom', self.black, 200, 60 - 5)

            if self.modif_desc.collidepoint(pygame.mouse.get_pos()):
                self.modif_desc = self.button_rect(self.darkblue, 400, 60, 180 + 10, 50 +10, 5)
            else:
                self.modif_desc = self.button_rect(self.blue, 400, 60, 170, 50, 2)
            self.texte(25, 'Modif. Desc', self.black, 400, 60 - 5)

            if self.modif_prix.collidepoint(pygame.mouse.get_pos()):
                self.modif_prix = self.button_rect(self.darkblue, 600, 60, 180 + 10, 50 +10, 5)
            else:
                self.modif_prix = self.button_rect(self.blue, 600, 60, 170, 50, 2)
            self.texte(25, 'Modif. Prix', self.black, 600, 60 - 5)

            if self.modif_quant.collidepoint(pygame.mouse.get_pos()):
                self.modif_quant = self.button_rect(self.darkblue, 1000, 60, 180 + 10, 50 +10, 5)
            else:
                self.modif_quant = self.button_rect(self.blue, 1000, 60, 170, 50, 2)
            self.texte(25, 'Modif. Quant', self.black, 1000, 60 - 5)
            if self.modif_categ.collidepoint(pygame.mouse.get_pos()):
                self.modif_categ = self.button_rect(self.darkblue, 800, 60, 180 + 10, 50 +10, 5)
            else:
                self.modif_categ = self.button_rect(self.blue, 800, 60, 170, 50, 2)
            self.texte(25, 'Modif. Categ', self.black, 800, 60 - 5)
         
            self.texte(30, f"    {product[1]}", self.black, 600 ,150)

            self.button_rect(self.white, 600, 300, 450 ,70, 5)
            self.simple_rect(self.black, 600, 300, 450, 70, 3, 5)

            if self.cate == 1:
                self.texte(20, "Modifier le nom du produit :", self.black,600, 250)
                self.texte(20, name, self.black,600, 300)
            elif self.cate == 2:
                self.texte(20, "Modifier la description du produit :", self.black,600, 250)
                self.texte(20, description, self.black,600, 300)
            elif self.cate == 3:
                self.texte(20, "Modifier le prix du produit :", self.black,600, 250)
                self.texte(20, prix, self.black,600, 300)
            elif self.cate == 4:
                self.texte(20, "Modifier la quantité du produit :", self.black,600, 250)
                self.texte(20, quantity, self.black,600, 300)
            elif self.cate == 5:
                max_cate = len(self.list_category)
                y = self.W // max_cate
                i = 0
                for category in self.list_category:
                    category_select = self.button_rect(self.grey,100+  y * i, 400 , 150, 50, 1)
                    self.texte(20, category[1], self.black, 100 + y * i,400)
                    if category_select.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:   
                        self.category_choose = category[0]
                        self.display_choose = category [1]
                    i += 1
                self.texte(20, "Modifier la catégorie du produit :", self.black,600, 250)
                if self.category_choose == "":
                    self.texte(20, "Veuillez selectionner une catégrie ci-dessous", self.grey,600, 300)
                else:
                    self.texte(20, self.display_choose, self.black,600, 300)
                    
            self.update_button = self.button_rect((self.blue), 600, 550, 200, 70, 5)
            self.simple_rect((self.black), 600, 550, 200, 70,2, 5)
            self.texte(20, 'Valider', self.black, 600, 550)
            
            if not deleted:
                self.delete_button = self.button_rect((self.red), 120, self.H -55, 200, 70, 5)
                self.simple_rect((self.black), 120, self.H -55, 200, 70,2, 5)
                self.texte(20, 'Supprimer', self.white, 120, self.H -55)
            
                if self.back_menu_modify.collidepoint(pygame.mouse.get_pos()):
                    self.back_menu_modify = self.button_rect(self.darkblue, 1140, self.H -50, 110, 55, 5)
                else:
                    self.back_menu_modify = self.button_rect(self.blue, 1140, self.H -50, 100, 45, 2)
                self.texte(25, 'Menu', self.black, 1140, self.H -55)
            else:
                self.button_rect(self.grey, 600,350, 800, 400, 10)
                self.simple_rect(self.black, 600,350, 800, 400, 3, 10)
                self.texte(25, f'{product[1]} a bien été supprimé', self.black, 600, 350)
                if self.back_menu_modify.collidepoint(pygame.mouse.get_pos()):
                    self.back_menu_modify = self.button_rect(self.darkblue, 600, 500, 200, 70, 5)
                else:
                    self.back_menu_modify = self.button_rect(self.blue, 600, 500, 200, 70, 5)

                self.simple_rect((self.black), 600, 500, 200, 70,2, 5)
                self.texte(20, 'Menu', self.black, 600, 500)
            if confirm_delete:
                self.button_rect(self.grey, 600,350, 800, 400, 10)
                self.simple_rect(self.black, 600,350, 800, 400, 3, 10)
                self.texte(25, f'Etes vous sur de vouloir supprimer {product[1]} ?', self.black, 600, 350)
                self.delete_button_confirm = self.button_rect(self.red, 600, 500, 200, 70, 5)
                self.simple_rect((self.black), 600, 500, 200, 70,2, 5)
                self.texte(20, 'Supprimer', self.white, 600, 500)


            self.update()