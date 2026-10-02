-- Initialisation de la base de données CRUD pour le TP BTS CIEL
CREATE DATABASE IF NOT EXISTS CRUD CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE CRUD;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    salary INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Données exactes de l'activité
INSERT INTO employees (id, name, address, salary) VALUES
(2, 'Victoria Ashworth', '35 King George, London', 6500),
(3, 'Martin Blank', '25, Rue Lauriston, Paris', 8000),
(4, 'Alain Gouiri', '3 allee du Paradis', 1200),
(8, 'Thomas Demarcy', '9 rue du Louvre', 25000),
(20, 'test', 'test', 100000),
(21, 'testo', 'tosta', 40000);
