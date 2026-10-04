"""
Gestion de la persistance MySQL - CORRIGÉ (Exercices 6 & 7).
"""
import os
import mysql.connector
from mysql.connector import Error

def get_db_connection(database: str = None):
    """Établit la connexion avec MySQL dans un try/except robuste."""
    target_db = database if database else os.getenv('MYSQL_DB', 'CRUD')
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            port=int(os.getenv('MYSQL_PORT', 3306)),
            database=target_db,
            user=os.getenv('MYSQL_USER', 'eleve'),
            password=os.getenv('MYSQL_PASSWORD', 'eleve')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erreur de connexion MySQL ({target_db}) : {e}")
        return None


# =========================================================================
# Exercice 6 : Requêtes sur la table 'employees' (Base CRUD)
# =========================================================================

def get_all_salaries() -> list:
    """Récupère l'intégralité des salaires sous forme d'une liste d'entiers."""
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT salary FROM employees")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    except Error as e:
        print(f"Erreur SQL get_all_salaries : {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def get_employee_by_id(emp_id: int):
    """Récupère un employé par son ID unique sous forme de dictionnaire."""
    conn = get_db_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, address, salary FROM employees WHERE id = %s", (emp_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"Erreur SQL get_employee_by_id : {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# =========================================================================
# Exercice 7 : Requêtes avec jointures sur la base CRUD2
# =========================================================================

def get_employee_average_salary(emp_id: int, d1: str = None, d2: str = None):
    """
    Exercice 7 (Cas 1 et 2) :
    Calcule le salaire moyen d'un employé donné (emp_id) sur la base CRUD2.
    - Si d1 et d2 sont fournis : filtre sur la période (BETWEEN %s AND %s)
    - Si seul d1 (ou d2) est fourni : filtre à partir de cette date (>= %s)
    Retourne un dict {'id': emp_id, 'name': nom, 'salaire_moyen': float} ou None.
    """
    conn = get_db_connection(database='CRUD2')
    if not conn:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name FROM employes WHERE id = %s", (emp_id,))
        emp = cursor.fetchone()
        if not emp:
            return None

        params = [emp_id]
        if d1 and d2:
            sql = """
                SELECT e.id, e.name, AVG(s.salary) AS moyenne
                FROM employes e
                INNER JOIN salaires s ON e.id = s.employes_id
                WHERE e.id = %s AND s.date BETWEEN %s AND %s
                GROUP BY e.id, e.name
            """
            params.extend([d1, d2])
        elif d1 or d2:
            target_date = d1 if d1 else d2
            sql = """
                SELECT e.id, e.name, AVG(s.salary) AS moyenne
                FROM employes e
                INNER JOIN salaires s ON e.id = s.employes_id
                WHERE e.id = %s AND s.date >= %s
                GROUP BY e.id, e.name
            """
            params.append(target_date)
        else:
            sql = """
                SELECT e.id, e.name, AVG(s.salary) AS moyenne
                FROM employes e
                INNER JOIN salaires s ON e.id = s.employes_id
                WHERE e.id = %s
                GROUP BY e.id, e.name
            """

        cursor.execute(sql, tuple(params))
        row = cursor.fetchone()
        if row and row['moyenne'] is not None:
            return {
                "id": row['id'],
                "name": row['name'],
                "salaire_moyen": round(float(row['moyenne']), 2)
            }
        else:
            return {
                "id": emp['id'],
                "name": emp['name'],
                "salaire_moyen": 0.0
            }
    except Error as e:
        print(f"Erreur SQL get_employee_average_salary : {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def get_all_employees_average_salaries(d1: str = None, d2: str = None) -> list:
    """
    Exercice 7 (Cas 3 et 4) :
    Calcule le salaire moyen de chaque employé sur la base CRUD2 (GROUP BY).
    - Si d1 et d2 sont fournis : filtre sur la période (BETWEEN %s AND %s)
    - Si aucune date n'est fournie : prend en compte tous les salaires
    Retourne une liste de flottants contenant les salaires moyens de chaque employé.
    """
    conn = get_db_connection(database='CRUD2')
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        if d1 and d2:
            sql = """
                SELECT AVG(s.salary) AS moyenne
                FROM employes e
                INNER JOIN salaires s ON e.id = s.employes_id
                WHERE s.date BETWEEN %s AND %s
                GROUP BY e.id
                ORDER BY e.id ASC
            """
            cursor.execute(sql, (d1, d2))
        else:
            sql = """
                SELECT AVG(s.salary) AS moyenne
                FROM employes e
                INNER JOIN salaires s ON e.id = s.employes_id
                GROUP BY e.id
                ORDER BY e.id ASC
            """
            cursor.execute(sql)

        rows = cursor.fetchall()
        return [round(float(row[0]), 2) for row in rows if row[0] is not None]
    except Error as e:
        print(f"Erreur SQL get_all_employees_average_salaries : {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
