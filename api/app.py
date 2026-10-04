"""
API REST Flask - BTS CIEL
Gestion des routes HTTP pour les exercices 4.2, 4.3, 5 et 6.
"""
from flask import Flask, request, jsonify
from statistique import moyenne, mediane
from tri_selection import tri_selection_copie
import db

app = Flask(__name__)

@app.route('/api/tri', methods=['GET'])
def route_tri():
    """
    Exercice 4.2 & 4.3 :
    Reçoit un paramètre t dans la Query String (ex: /api/tri?t=15,3,8).
    Retourne le tableau trié et la médiane au format JSON.
    """
    # TODO:
    # 1. Récupérer 't' depuis request.args
    # 2. Convertir la chaîne en liste d'entiers
    # 3. Trier la liste avec tri_selection_copie()
    # 4. Calculer la médiane avec mediane()
    # 5. Retourner avec jsonify()
    return jsonify({"message": "TODO: Implémenter /api/tri"}), 501


@app.route('/api/fusion', methods=['GET'])
def route_fusion():
    """
    Exercice 5 :
    Reçoit t1 et t2 dans l'URL (ex: /api/fusion?t1=12,5&t2=8,20).
    Concatène les deux listes, effectue le tri et calcule la médiane.
    """
    # TODO:
    # 1. Extraire t1 et t2
    # 2. Concaténer avec l'opérateur +
    # 3. Trier et calculer la médiane
    return jsonify({"message": "TODO: Implémenter /api/fusion"}), 501


@app.route('/api/salaires/stats', methods=['GET'])
def route_salaires_stats():
    """
    Exercice 6 :
    Interroge la table employees, lit les salaires et renvoie moyenne et médiane en JSON.
    """
    # TODO:
    # 1. Récupérer la liste des salaires via db.get_all_salaries()
    # 2. Calculer moyenne() et mediane(tri_selection_copie(salaires))
    # 3. Renvoyer le JSON
    return jsonify({"message": "TODO: Implémenter /api/salaires/stats"}), 501


@app.route('/api/employees/<int:emp_id>/comparaison', methods=['GET'])
def route_employee_comparaison(emp_id):
    """
    Exercice 6 :
    Situe le salaire d'un employé donné par rapport à la moyenne et à la médiane globale.
    """
    # TODO:
    # 1. Récupérer l'employé avec db.get_employee_by_id(emp_id) -> 404 si non trouvé
    # 2. Récupérer l'ensemble des salaires et calculer moyenne et médiane
    # 3. Comparer le salaire de l'employé et retourner le bilan JSON
    return jsonify({"message": "TODO: Implémenter /api/employees/<id>/comparaison"}), 501


@app.route('/api/salaires/periode', methods=['GET'])
def route_salaires_periode():
    """
    Exercice 7 :
    Route GET /api/salaires/periode
    Paramètres optionnels de Query String :
    - p  : identifiant de l'employé (int)
    - d1 : date de début (AAAA-MM-JJ)
    - d2 : date de fin (AAAA-MM-JJ)

    Gère les 4 cas métier :
    1. p présent + d1 et d2 présents -> Salaire moyen de p entre d1 et d2
    2. p présent + une seule date    -> Salaire moyen de p à partir de cette date
    3. p absent  + d1 et d2 présents -> Médiane des salaires moyens des employés entre d1 et d2
    4. p absent  + aucune date       -> Médiane des salaires moyens de tous les employés (toutes dates)
    """
    # TODO: Exercice 7
    # 1. Récupérer p, d1, d2 depuis request.args :
    #    p = request.args.get('p')
    #    d1 = request.args.get('d1')
    #    d2 = request.args.get('d2')
    # 2. Détecter le cas d'usage parmi les 4 possibilités
    # 3. Interroger db.py (base CRUD2) pour récupérer les moyennes SQL
    # 4. Pour les cas 3 et 4 :
    #    - Trier les moyennes avec tri_selection_copie(moyennes)
    #    - Calculer la médiane avec mediane(...)
    # 5. Renvoyer la réponse formatée avec jsonify(...)
    return jsonify({"message": "TODO: Implémenter /api/salaires/periode"}), 501


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

