CREATE DATABASE IF NOT EXISTS bunny_village;
USE bunny_village;

CREATE TABLE breeds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE rabbits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    breed_id INT,
    age INT,
    diet INT,
    FOREIGN KEY (breed_id) REFERENCES breeds(id) ON DELETE SET NULL
);

CREATE TABLE toys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE rabbit_toys (
    rabbit_id INT,
    toy_id INT,
    PRIMARY KEY (rabbit_id, toy_id),
    FOREIGN KEY (rabbit_id) REFERENCES rabbits(id) ON DELETE CASCADE,
    FOREIGN KEY (toy_id) REFERENCES toys(id) ON DELETE CASCADE
);

-- Тестові дані
INSERT INTO breeds (name) VALUES ('Lionhead'), ('Netherland Dwarf'), ('Holland Lop');
INSERT INTO rabbits (name, breed_id, age, diet) VALUES 
('Marshmallow', 1, 2, 5),
('Clover', 2, 1, 3),
('Pumpkin', 3, 4, 6);

INSERT INTO toys (name) VALUES ('Морквинка-гризунець'), ('Тунель'), ('М\'ячик');
INSERT INTO rabbit_toys (rabbit_id, toy_id) VALUES (1, 1), (1, 2), (2, 3);