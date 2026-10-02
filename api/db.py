"""
Gestion de la persistance MySQL - CORRIGÉ.
"""
import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Établit la connexion avec MySQL dans un try/except robuste."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'db'),
            port=int(os.getenv('MYSQL_PORT', 3306)),
            database=os.getenv('MYSQL_DB', 'CRUD'),
            user=os.getenv('MYSQL_USER', 'eleve'),
            password=os.getenv('MYSQL_PASSWORD', 'eleve')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erreur de connexion MySQL : {e}")
        return None


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
