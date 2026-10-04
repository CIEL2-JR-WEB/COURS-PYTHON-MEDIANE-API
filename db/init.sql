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

-- ========================================================
-- Initialisation de la base de données CRUD2 (Exercice 7)
-- ========================================================
CREATE DATABASE IF NOT EXISTS CRUD2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE CRUD2;

-- 1. Table employees originale (3 employés issus de employees.sql)
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    salary INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO employees (id, name, address, salary) VALUES
(1, 'Roland Mendel', 'C/ Araquil, 67, Madrid', 5000),
(2, 'Victoria Ashworth', '35 King George, London', 6500),
(3, 'Martin Blank', '25, Rue Lauriston, Paris', 8000);

-- 2. Tables normalisées : employes et salaires (avec dates pour l'historique)
DROP TABLE IF EXISTS salaires;
DROP TABLE IF EXISTS employes;

CREATE TABLE employes (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO employes (id, name, address) VALUES
(1, 'Roland Mendel', 'C/ Araquil, 67, Madrid'),
(2, 'Victoria Ashworth', '35 King George, London'),
(3, 'Martin Blank', '25, Rue Lauriston, Paris');

CREATE TABLE salaires (
    idsalaires INT NOT NULL AUTO_INCREMENT,
    salary INT NOT NULL,
    employes_id INT NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (idsalaires),
    CONSTRAINT fk_salaires_employes FOREIGN KEY (employes_id) REFERENCES employes(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Données salariales historiques
INSERT INTO salaires (salary, employes_id, date) VALUES
-- Roland Mendel (id=1)
(4800, 1, '2021-01-15'),
(5000, 1, '2021-07-15'),
(5200, 1, '2022-01-15'),
(5400, 1, '2022-07-15'),
(5600, 1, '2023-01-15'),
-- Victoria Ashworth (id=2)
(6200, 2, '2021-03-01'),
(6500, 2, '2022-03-01'),
(6700, 2, '2022-09-01'),
(7000, 2, '2023-03-01'),
-- Martin Blank (id=3)
(7500, 3, '2021-06-01'),
(7800, 3, '2022-02-01'),
(8200, 3, '2022-08-01'),
(8500, 3, '2023-05-01');

-- 3. Tables pour l'exercice sur les jointures multi-tables (Question 10)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Products (product_id, product_name, price) VALUES
(1, 'Burger', 10),
(2, 'Sandwich', 15);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Customers (customer_id, customer_name, email) VALUES
(1, 'Alice', 'alice@alice.com'),
(2, 'Bob', 'bob@bob.com');

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Orders (order_id, customer_id, product_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1);

-- Attribution des privilèges sur CRUD2 au compte applicatif 'eleve'
GRANT ALL PRIVILEGES ON CRUD2.* TO 'eleve'@'%';
FLUSH PRIVILEGES;
