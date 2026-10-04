"""
API REST Flask Complète - CORRIGÉ.
"""
from flask import Flask, request, jsonify
from statistique import moyenne, mediane
from tri_selection import tri_selection_copie
import db

app = Flask(__name__)

def parse_int_list(raw_string: str) -> list:
    """Convertit une chaîne '12, 15, 8' en liste d'entiers [12, 15, 8]."""
    if not raw_string:
        return []
    result = []
    for item in raw_string.split(','):
        clean = item.strip()
        if clean:
            result.append(int(clean))
    return result


@app.route('/api/tri', methods=['GET'])
def route_tri():
    """
    Exercice 4.2 & 4.3 :
    Exemple d'appel : /api/tri?t=1500,4500,2200,1500,3300,1800,1700,2000,4000
    """
    raw_t = request.args.get('t', '')
    if not raw_t:
        return jsonify({"erreur": "Paramètre 't' manquant"}), 400

    try:
        tableau_original = parse_int_list(raw_t)
        tableau_trie = tri_selection_copie(tableau_original)
        valeur_mediane = mediane(tableau_trie)

        return jsonify({
            "original": tableau_original,
            "tri": tableau_trie,
            "mediane": valeur_mediane
        }), 200
    except ValueError:
        return jsonify({"erreur": "Le paramètre 't' doit contenir uniquement des nombres entiers séparés par des virgules."}), 400


@app.route('/api/fusion', methods=['GET'])
def route_fusion():
    """
    Exercice 5 :
    Concaténation de deux listes t1 et t2.
    Exemple d'appel : /api/fusion?t1=12,18,5&t2=20,8,14
    """
    raw_t1 = request.args.get('t1', '')
    raw_t2 = request.args.get('t2', '')

    try:
        t1 = parse_int_list(raw_t1)
        t2 = parse_int_list(raw_t2)

        # Concaténation de listes en Python via l'opérateur +
        fusion = t1 + t2
        tableau_trie = tri_selection_copie(fusion)
        valeur_mediane = mediane(tableau_trie)

        return jsonify({
            "t1": t1,
            "t2": t2,
            "fusion": fusion,
            "tri": tableau_trie,
            "mediane": valeur_mediane
        }), 200
    except ValueError:
        return jsonify({"erreur": "Format des paramètres t1 ou t2 invalide."}), 400


@app.route('/api/salaires/stats', methods=['GET'])
def route_salaires_stats():
    """
    Exercice 6 :
    Lecture des salaires depuis MySQL, calcul de la moyenne et de la médiane.
    """
    salaires = db.get_all_salaries()
    if not salaires:
        return jsonify({"erreur": "Impossible de lire les salaires en base de données"}), 500

    salaires_tries = tri_selection_copie(salaires)
    moy = moyenne(salaires)
    med = mediane(salaires_tries)

    return jsonify({
        "nombre_employes": len(salaires),
        "salaires_bruts": salaires,
        "salaires_tries": salaires_tries,
        "moyenne": moy,
        "mediane": med
    }), 200


@app.route('/api/employees/<int:emp_id>/comparaison', methods=['GET'])
def route_employee_comparaison(emp_id):
    """
    Exercice 6 :
    Compare le salaire de l'employé 'emp_id' aux statistiques globales.
    """
    employe = db.get_employee_by_id(emp_id)
    if not employe:
        return jsonify({"erreur": "Employé introuvable"}), 404

    salaires = db.get_all_salaries()
    salaires_tries = tri_selection_copie(salaires)
    moy = moyenne(salaires)
    med = mediane(salaires_tries)

    salaire_emp = employe['salary']

    situation_moyenne = "égal"
    if salaire_emp > moy:
        situation_moyenne = "supérieur"
    elif salaire_emp < moy:
        situation_moyenne = "inférieur"

    situation_mediane = "égal"
    if salaire_emp > med:
        situation_mediane = "supérieur"
    elif salaire_emp < med:
        situation_mediane = "inférieur"

    return jsonify({
        "employe": employe,
        "statistiques_globales": {
            "moyenne": moy,
            "mediane": med
        },
        "situation": {
            "par_rapport_a_la_moyenne": situation_moyenne,
            "par_rapport_a_la_mediane": situation_mediane
        }
    }), 200



@app.route('/api/salaires/periode', methods=['GET'])
def route_salaires_periode():
    """
    Exercice 7 - CORRIGÉ :
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
    raw_p = request.args.get('p')
    d1 = request.args.get('d1')
    d2 = request.args.get('d2')

    if raw_p is not None and raw_p.strip() == '':
        raw_p = None
    if d1 is not None and d1.strip() == '':
        d1 = None
    if d2 is not None and d2.strip() == '':
        d2 = None

    # Validation du format des dates et cohérence chronologique
    for d_name, d_val in [('d1', d1), ('d2', d2)]:
        if d_val:
            try:
                from datetime import datetime
                datetime.strptime(d_val, '%Y-%m-%d')
            except ValueError:
                return jsonify({"erreur": f"Le format de {d_name} doit être AAAA-MM-JJ"}), 400

    if d1 and d2 and d1 > d2:
        return jsonify({"erreur": "La date de début d1 doit être antérieure ou égale à la date de fin d2"}), 400

    # Cas 1 & 2 : p est renseigné
    if raw_p is not None:
        try:
            emp_id = int(raw_p)
        except ValueError:
            return jsonify({"erreur": "Le paramètre 'p' doit être un nombre entier"}), 400

        res = db.get_employee_average_salary(emp_id, d1, d2)
        if not res:
            return jsonify({"erreur": f"Employé avec id={emp_id} introuvable dans la base CRUD2"}), 404

        if d1 and d2:
            return jsonify({
                "cas": "employe_periode",
                "employe_id": res["id"],
                "employe_nom": res["name"],
                "d1": d1,
                "d2": d2,
                "salaire_moyen": res["salaire_moyen"]
            }), 200
        else:
            date_ref = d1 if d1 else d2
            return jsonify({
                "cas": "employe_partir_de",
                "employe_id": res["id"],
                "employe_nom": res["name"],
                "date_debut": date_ref,
                "salaire_moyen": res["salaire_moyen"]
            }), 200

    # Cas 3 & 4 : p est absent -> Médiane des salaires moyens
    moyennes = db.get_all_employees_average_salaries(d1, d2)
    if not moyennes:
        return jsonify({"erreur": "Aucune donnée salariale trouvée pour cette période"}), 404

    # Calcul de la médiane via les algorithmes maison en Python
    moyennes_triees = tri_selection_copie(moyennes)
    valeur_mediane = mediane(moyennes_triees)

    if d1 and d2:
        return jsonify({
            "cas": "mediane_periode",
            "d1": d1,
            "d2": d2,
            "nombre_employes": len(moyennes),
            "moyennes_individuelles": moyennes_triees,
            "mediane_des_moyennes": valeur_mediane
        }), 200
    else:
        return jsonify({
            "cas": "mediane_globale",
            "nombre_employes": len(moyennes),
            "moyennes_individuelles": moyennes_triees,
            "mediane_des_moyennes": valeur_mediane
        }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

