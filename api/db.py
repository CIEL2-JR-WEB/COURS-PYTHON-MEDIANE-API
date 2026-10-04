"""
Exercice 6 & 7 : Module de connexion MySQL et requêtes.
"""
import os
import mysql.connector
from mysql.connector import Error

def get_db_connection(database: str = None):
    """
    Établit la connexion à MySQL dans un bloc try/except.
    Par défaut, se connecte à la base 'CRUD' (Exercice 6).
    Si le paramètre 'database' est précisé (ex: 'CRUD2'), se connecte à celle-ci.
    Retourne l'objet connexion ou None en cas d'erreur.
    """
    # TODO: Exercice 6 & 7
    # Lire les paramètres d'environnement (MYSQL_HOST, MYSQL_USER, etc.)
    # Utiliser le paramètre database si non None, sinon os.getenv('MYSQL_DB', 'CRUD')
    # Se connecter avec mysql.connector.connect(...)
    # Intercepter Error et afficher l'erreur si échec
    pass


def get_all_salaries() -> list:
    """
    Exercice 6 :
    Récupère l'ensemble des salaires de la table 'employees' sous forme de liste d'entiers.
    """
    # TODO:
    # Exécuter : SELECT salary FROM employees
    # Extraire les valeurs dans une liste Python [row[0] ...]
    pass


def get_employee_by_id(emp_id: int):
    """
    Exercice 6 :
    Récupère un employé par son identifiant unique.
    Retourne un dictionnaire {id, name, address, salary} ou None.
    """
    # TODO:
    # Requête préparée : SELECT id, name, address, salary FROM employees WHERE id = %s
    pass


# =========================================================================
# Exercice 7 : Requêtes avec jointures sur la base CRUD2
# =========================================================================

def get_employee_average_salary(emp_id: int, d1: str = None, d2: str = None):
    """
    Exercice 7 (Cas 1 et 2) :
    Calcule le salaire moyen d'un employé donné (emp_id) sur la base CRUD2.
    - Si d1 et d2 sont fournis : filtre sur la période (BETWEEN %s AND %s)
    - Si seul d1 (ou d2) est fourni : filtre à partir de cette date (>= %s)
    Retourne un dictionnaire {'id': emp_id, 'name': nom, 'salaire_moyen': float} ou None.
    """
    # TODO: Exercice 7
    # 1. Se connecter à CRUD2 : conn = get_db_connection(database='CRUD2')
    # 2. Construire la requête SQL avec jointure :
    #    SELECT e.id, e.name, AVG(s.salary) AS moyenne
    #    FROM employes e
    #    INNER JOIN salaires s ON e.id = s.employes_id
    #    WHERE e.id = %s ...
    #    GROUP BY e.id, e.name
    # 3. Exécuter la requête préparée et retourner le dictionnaire
    pass


def get_all_employees_average_salaries(d1: str = None, d2: str = None) -> list:
    """
    Exercice 7 (Cas 3 et 4) :
    Calcule le salaire moyen de chaque employé sur la base CRUD2 (GROUP BY).
    - Si d1 et d2 sont fournis : filtre sur la période (BETWEEN %s AND %s)
    - Si aucune date n'est fournie : prend en compte tous les salaires
    Retourne une liste de flottants contenant les salaires moyens de chaque employé.
    """
    # TODO: Exercice 7
    # 1. Se connecter à CRUD2 : conn = get_db_connection(database='CRUD2')
    # 2. Construire la requête :
    #    SELECT AVG(s.salary) AS moyenne
    #    FROM employes e
    #    INNER JOIN salaires s ON e.id = s.employes_id
    #    [WHERE s.date BETWEEN %s AND %s]
    #    GROUP BY e.id
    #    ORDER BY e.id ASC
    # 3. Extraire chaque moyenne dans une liste Python [float(row[0]), ...]
    pass

