from db import Database

class Gestion(Database):
    def __init__(self):
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'store')

    def create_category(self, name):
        query = f'INSERT INTO category (name) VALUES (%s)'
        params = (name,)
        self.executeQuery(query, params)

    def read_categories(self):
        query = f'SELECT * FROM category'
        return self.fetch(query)
    
    def update_category(self, name, id):
        query = f'UPDATE category SET name=%s WHERE id=%s'
        params = (name, id)
        self.executeQuery(query, params)

    def delete_category(self, id):
        query = f'DELETE FROM category WHERE id=%s'
        params = (id,)
        self.executeQuery(query, params)
    
    def find_category(self, id):
        query = f'SELECT * FROM category WHERE id=%s'
        params = (id,)
        return self.fetch(query, params)
    
    def all_product(self):
        query = f'SELECT product.id, product.name, product.description, product.price, product.quantity, category.name AS category FROM product JOIN category ON product.id_category = category.id;'
        return self.fetch(query)
    
    def add_product(self, name, description, price, quantity, id_category):
        query = f'INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.executeQuery(query, params)
    
    def remove_product(self, id):
        query = f'DELETE FROM product WHERE id=%s'
        params = (id,)
        self.executeQuery(query, params)

    def update_product(self, name, description, price, quantity, id_category, id):
        query = f'UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s'
        params = (name, description, price, quantity, id_category, id)
        self.executeQuery(query, params)

    def find_product(self, id):
        query = f'SELECT * FROM product WHERE id=%s'
        params = (id,)
        return self.fetch(query, params)
    
    def get_products_by_category(self, id_category):
        query = f'SELECT * FROM product WHERE id_category=%s'
        params = (id_category,)
        return self.fetch(query, params)
    
    def get_products_count(self, id_category):
        query = f'SELECT COUNT(*) FROM product WHERE id_category=%s'
        params = (id_category,)
        return self.fetch(query, params)
    
    def get_product_price(self, id):
        query = f'SELECT price FROM product WHERE id=%s'
        params = (id,)
        return self.fetch(query, params)
