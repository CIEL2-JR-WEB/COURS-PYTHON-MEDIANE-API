"""
BTS CIEL // Cahier d'Exercices Préparatoires Fondamentaux (SUJET ÉTUDIANT).
Ce fichier contient les squelettes de code correspondant aux 10 modules du cahier
d'exercices fondamentaux (exercices_fondamentaux.md).

Complétez chaque fonction et classe sans modifier leurs signatures.
Exécutez ce script pour tester votre progression :
    python exercices_fondamentaux.py
"""

from __future__ import annotations
import json
import math
from typing import Any


# =============================================================================
# MODULE 1 : Variables, Types, Conversions & Arithmétique (Ch. 2)
# =============================================================================

def decomposer_secondes(secondes: int) -> tuple[int, int, int]:
    """
    Décompose un nombre entier de secondes en heures, minutes et secondes restantes.
    Utilise les opérateurs // et %.

    Exemple:
        decomposer_secondes(7385) -> (2, 3, 5)
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 2 : Affichage, Formatage et f-strings (Ch. 3)
# =============================================================================

def formater_ligne_service(hote: str, port: int, statut: str) -> str:
    """
    Retourne une chaîne formatée représentant un service réseau :
    - hote   : 15 caractères cadré à gauche (<)
    - port   : 6 caractères cadré à droite (>)
    - statut : 10 caractères centré (^)
    Les colonnes sont séparées par ' | '.

    Exemple:
        formater_ligne_service("localhost", 80, "ACTIF") -> "localhost       |     80 |   ACTIF   "
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 3 : Listes, Indexation, Slicing & Gestion Mémoire (Ch. 4)
# =============================================================================

def dupliquer_sans_effet_de_bord(liste_source: list[Any]) -> list[Any]:
    """
    Retourne une copie indépendante (copie superficielle défensive) de la liste
    passée en argument afin d'éviter tout effet de bord lors de modifications futures.

    Exemple:
        l1 = [1, 2, 3]
        l2 = dupliquer_sans_effet_de_bord(l1)
        l2[0] = 99
        -> l1 reste intact [1, 2, 3]
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 4 : Boucles for, while & Parcours d'Itérables (Ch. 5)
# =============================================================================

def calculer_somme_et_moyenne(valeurs: list[float | int]) -> tuple[float, float]:
    """
    Calcule et renvoie la somme totale et la moyenne arithmétique de la liste
    en parcourant les éléments avec une boucle for et un accumulateur.

    Exemple:
        calculer_somme_et_moyenne([10, 20, 30]) -> (60.0, 20.0)
    """
    # TODO: À compléter par l'étudiant
    pass


def generer_lignes_triangle(n: int) -> list[str]:
    """
    Génère et renvoie une liste de n chaînes d'étoiles représentant un triangle
    rectangle de hauteur n.

    Exemple:
        generer_lignes_triangle(3) -> ["*", "**", "***"]
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 5 : Conditions, Tests Avancés & Précision des Floats (Ch. 6)
# =============================================================================

def categoriser_valeur(valeur: float, seuil_bas: float, seuil_haut: float) -> str:
    """
    Catégorise une mesure physique flottante :
    - 'BAS' si valeur < seuil_bas (avec tolérance 1e-5 via math.isclose)
    - 'CRITIQUE' si valeur > seuil_haut (avec tolérance 1e-5 via math.isclose)
    - 'NORMAL' si valeur comprise entre seuil_bas et seuil_haut inclus

    Exemple:
        categoriser_valeur(15.0, 10.0, 20.0) -> "NORMAL"
        categoriser_valeur(25.0, 10.0, 20.0) -> "CRITIQUE"
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 6 : Fichiers Texte, Sérialisation & Données JSON (Ch. 7)
# =============================================================================

def sauvegarder_donnees_json(chemin_fichier: str, donnees: list | dict) -> None:
    """
    Sérialise et sauvegarde l'objet Python 'donnees' dans un fichier JSON
    en utilisant with open(), l'encodage utf-8 et une indentation de 4 espaces.
    """
    # TODO: À compléter par l'étudiant
    pass


def charger_donnees_json(chemin_fichier: str) -> list | dict:
    """
    Ouvre et désérialise le fichier JSON spécifié en utilisant with open()
    et l'encodage utf-8, puis renvoie la structure Python correspondante.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 7 : Dictionnaires, Tuples & Modélisation de Données (Ch. 8)
# =============================================================================

def compter_frequences_elements(elements: list[str]) -> dict[str, int]:
    """
    Compte le nombre d'occurrences de chaque chaîne de caractères présente
    dans la liste 'elements' et renvoie le résultat sous forme de dictionnaire {element: count}.

    Exemple:
        compter_frequences_elements(["A", "B", "A", "C", "A"]) -> {"A": 3, "B": 1, "C": 1}
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 8 : Fonctions, Modularité, Paramètres & Portée (Ch. 10)
# =============================================================================

def calculer_extremums_et_etendue(valeurs: list[float | int]) -> tuple[float, float, float]:
    """
    Retourne un tuple de 3 floats (minimum, maximum, etendue) où
    etendue = maximum - minimum.

    Exemple:
        calculer_extremums_et_etendue([15, 3, 22, 8]) -> (3.0, 22.0, 19.0)
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# MODULE 9 : Programmation Orientée Objet — Classes & Instances (Ch. 23)
# =============================================================================

class Salarie:
    """
    Modélise un employé d'entreprise avec son identifiant, son nom et son salaire brut.
    """

    def __init__(self, identifiant: int, nom: str, salaire: float) -> None:
        """Constructeur initialisant les attributs d'instance self.id, self.nom, self.salaire."""
        # TODO: À compléter par l'étudiant
        pass

    def augmenter(self, pourcentage: float) -> None:
        """
        Augmente le salaire de l'employé de 'pourcentage' %
        (ex: pourcentage = 10.0 pour une augmentation de 10%).
        """
        # TODO: À compléter par l'étudiant
        pass

    def to_dict(self) -> dict[str, Any]:
        """
        Retourne un dictionnaire standard sérialisable en JSON
        avec les clés 'id', 'nom', 'salaire'.
        """
        # TODO: À compléter par l'étudiant
        pass

    def __str__(self) -> str:
        """
        Retourne une représentation lisible pour print() au format :
        '[<id>] <nom> : <salaire:.2f> €'
        """
        # TODO: À compléter par l'étudiant
        pass


# =============================================================================
# MODULE 10 : Grand Défi Synthèse — Pipeline de Traitement Itératif & JSON
# =============================================================================

def traiter_pipeline_salaries(chemin_json_entree: str, chemin_json_sortie: str) -> dict[str, Any]:
    """
    Exécute le pipeline complet de traitement :
    1. Charge la liste des dictionnaires de salariés depuis le fichier JSON d'entrée.
    2. Instancie une liste d'objets Salarie.
    3. Itère sur la collection pour calculer :
       - 'effectif_total' : nombre total de salariés
       - 'masse_salariale' : somme des salaires bruts
       - 'salaire_moyen' : moyenne arithmétique des salaires
       - 'salaries_qualifies' : liste des dictionnaires (via to_dict()) des salariés ayant un salaire >= 2000.0
    4. Construit le dictionnaire de rapport final et le sauvegarde dans chemin_json_sortie.
    5. Retourne le dictionnaire de rapport.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# PROGRAMME DE VALIDATION & AUTO-CONTRÔLE
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("BTS CIEL // SUITE D'AUTO-CONTRÔLE : EXERCICES FONDAMENTAUX")
    print("=" * 70)

    # Dictionnaire de suivi des tests
    tests = [
        ("M1 - decomposer_secondes", lambda: decomposer_secondes(7385) == (2, 3, 5)),
        ("M2 - formater_ligne_service", lambda: formater_ligne_service("localhost", 80, "ACTIF") == "localhost       |     80 |   ACTIF   "),
        ("M3 - dupliquer_sans_effet_de_bord", lambda: (
            (l := [1, 2, 3]) and (c := dupliquer_sans_effet_de_bord(l)) and c.append(4) is None and l == [1, 2, 3] and c == [1, 2, 3, 4]
        )),
        ("M4 - calculer_somme_et_moyenne", lambda: calculer_somme_et_moyenne([10, 20, 30]) == (60.0, 20.0)),
        ("M4 - generer_lignes_triangle", lambda: generer_lignes_triangle(3) == ["*", "**", "***"]),
        ("M5 - categoriser_valeur", lambda: categoriser_valeur(15.0, 10.0, 20.0) == "NORMAL" and categoriser_valeur(25.0, 10.0, 20.0) == "CRITIQUE"),
        ("M6 - sauvegarder/charger_json", lambda: (
            sauvegarder_donnees_json("test_tmp.json", [{"id": 1, "ok": True}]) is None and
            charger_donnees_json("test_tmp.json") == [{"id": 1, "ok": True}]
        )),
        ("M7 - compter_frequences_elements", lambda: compter_frequences_elements(["A", "B", "A", "C", "A"]) == {"A": 3, "B": 1, "C": 1}),
        ("M8 - calculer_extremums_et_etendue", lambda: calculer_extremums_et_etendue([15, 3, 22, 8]) == (3.0, 22.0, 19.0)),
        ("M9 - Salarie (classe & méthodes)", lambda: (
            (s := Salarie(1, "Nicolas", 2200.0)) and s.augmenter(10.0) is None and
            s.salaire == 2420.0 and s.to_dict() == {"id": 1, "nom": "Nicolas", "salaire": 2420.0}
        )),
        ("M10 - traiter_pipeline_salaries", lambda: (
            sauvegarder_donnees_json("entree_test.json", [
                {"id": 1, "nom": "Alice", "salaire": 1500.0},
                {"id": 2, "nom": "Bob", "salaire": 4500.0},
                {"id": 3, "nom": "Nicolas", "salaire": 2200.0}
            ]) is None and
            (rep := traiter_pipeline_salaries("entree_test.json", "rapport_test.json")) and
            rep["effectif_total"] == 3 and
            math.isclose(rep["masse_salariale"], 8200.0, abs_tol=1e-3) and
            len(rep["salaries_qualifies"]) == 2
        ))
    ]

    reussis = 0
    total = len(tests)

    for nom, test_fn in tests:
        try:
            if test_fn():
                print(f"  [SUCCES] {nom}")
                reussis += 1
            else:
                print(f"  [ECHEC]  {nom} (Résultat inattendu)")
        except Exception as e:
            print(f"  [A FAIRE] {nom} : Non implémenté ({type(e).__name__})")

    print("-" * 70)
    print(f"Bilan de votre progression : {reussis} / {total} validés.")
    if reussis == total:
        print("Félicitations ! Tous les fondamentaux sont maîtrisés.")
    else:
        print("Complétez les fonctions 'TODO' et relancez ce script.")
    print("=" * 70)
