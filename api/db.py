"""
Exercice 6 : Module de connexion MySQL et requêtes.
"""
import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """
    Établit la connexion à la base MySQL 'CRUD' dans un bloc try/except.
    Retourne l'objet connexion ou None en cas d'erreur.
    """
    # TODO: Exercice 6
    # Lire les paramètres d'environnement (MYSQL_HOST, MYSQL_USER, etc.)
    # Se connecter avec mysql.connector.connect(...)
    # Intercepter Error et afficher l'erreur si échec
    pass


def get_all_salaries() -> list:
    """
    Récupère l'ensemble des salaires de la table 'employees' sous forme de liste d'entiers.
    """
    # TODO:
    # Exécuter : SELECT salary FROM employees
    # Extraire les valeurs dans une liste Python [row[0] ...]
    pass


def get_employee_by_id(emp_id: int):
    """
    Récupère un employé par son identifiant unique.
    Retourne un dictionnaire {id, name, address, salary} ou None.
    """
    # TODO:
    # Requête préparée : SELECT id, name, address, salary FROM employees WHERE id = %s
    pass
