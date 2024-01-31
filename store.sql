CREATE DATABASE STORE;

USE STORE;
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price INT,
    quantity INT,
    id_category INT
);

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO category (name) VALUES
    ('Alimentaire'),
    ('Électronique'),
    ('Divers');

INSERT INTO product (name, description, price, quantity, id_category) VALUES
    ('Banane', 'Fruit frais', 1, 50, 1),
    ('Pain', 'Baguette traditionnelle', 2, 30, 1),
    ('Pâtes', 'Paquet de pâtes alimentaires', 3, 40, 1),
    ('Lait', 'Bouteille de lait demi-écrémé', 1, 20, 1),
    ('IceTea', 'Boisson saveur pêche', 4, 25, 1),
    ('Smartphone', 'Téléphone portable haut de gamme', 500, 10, 2),
    ('Ordinateur portable', 'PC portable avec processeur i7', 800, 8, 2),
    ('Casque audio', 'Casque audio sans fil', 100, 15, 2),
    ('Enceinte Bluetooth', 'Enceinte portable', 80, 20, 2),
    ('Écouteurs', 'Écouteurs intra-auriculaires', 50, 25, 2),
    ('Livre', 'Roman à suspense', 15, 35, 3),
    ('Balle de tennis', 'Balle de tennis pour pratiquer le sport', 3, 50, 3),
    ('Lampe de bureau', 'Lampe LED réglable', 20, 18, 3),
    ('Parapluie', 'Parapluie pliable compact', 10, 30, 3),
    ('Crayons de couleur', 'Boîte de crayons de couleur', 5, 40, 3);
