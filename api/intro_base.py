"""
BTS CIEL // Introduction Fondamentale à Python : Algorithmique, Listes & Matrices (SUJET ÉTUDIANT).
Complétez chaque fonction ci-dessous selon les consignes du sujet (README.md).
"""

from typing import List, Tuple, Dict, Any


# =============================================================================
# EXERCICE 0.1 : Indice du minimum d'une liste
# =============================================================================

def indice_minimum(L: List[float | int]) -> int:
    """
    Retourne l'indice où se trouve le minimum de la liste L.
    Si la valeur minimale apparaît plusieurs fois, retourne le premier indice.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.2 : Somme de 1 à n (Itératif vs Récursif)
# =============================================================================

def somme_iterative(n: int) -> int:
    """Calcule 1 + 2 + ... + n de manière itérative avec une boucle for."""
    # TODO: À compléter par l'étudiant
    pass


def somme_recursive(n: int) -> int:
    """
    Calcule 1 + 2 + ... + n de manière récursive.
    Pensez à définir le cas d'arrêt et le cas récursif.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.3 : Puissance x^n (Itératif vs Récursif - Même type)
# =============================================================================

def puissance_iterative(x: float | int, n: int) -> float | int:
    """Calcule x^n avec une boucle for."""
    # TODO: À compléter par l'étudiant
    pass


def puissance_recursive(x: float | int, n: int) -> float | int:
    """
    Calcule x^n de manière récursive.
    Pensez au cas d'arrêt (n == 0) et au cas récursif.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.4 : Taille totale d'une liste de listes
# =============================================================================

def taille_totale(L: List[List[Any]]) -> int:
    """
    Retourne la taille totale (nombre total d'éléments) de la liste de listes L.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 7
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.5 : Somme et Maximum d'une liste de listes
# =============================================================================

def somme_liste_de_listes(L: List[List[float | int]]) -> float | int:
    """
    Retourne la somme de tous les nombres contenus dans toutes les sous-listes de L.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 26
    """
    # TODO: À compléter par l'étudiant
    pass


def maximum_liste_de_listes(L: List[List[float | int]]) -> float | int:
    """
    Retourne le plus grand nombre figurant dans la liste de listes L, sans le localiser.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 6
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.6 : Création de matrice régulière 2D & Inversion binaire
# =============================================================================

def creer_matrice(nb_lignes: int, nb_colonnes: int, valeur_defaut: Any = 0) -> List[List[Any]]:
    """
    Crée une matrice 2D indépendante de dimensions nb_lignes x nb_colonnes.
    Attention au piège des références partagées : construisez chaque ligne indépendamment.
    """
    # TODO: À compléter par l'étudiant
    pass


def inverser_matrice_binaire(M: List[List[int]]) -> List[List[int]]:
    """
    Inverse une matrice binaire (0 devient 1, et 1 devient 0) et retourne la nouvelle matrice.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.7 : Produit cartésien de deux listes (Couples)
# =============================================================================

def produit_cartesien(L1: List[Any], L2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Retourne la liste de tous les couples formés d'un élément de L1 et d'un élément de L2.
    Exemple : [0, 1] et [1, 4] -> [(0, 1), (0, 4), (1, 1), (1, 4)]
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.8 : Réorganisation ordonnée d'une liste de couples selon un pivot
# =============================================================================

def reorganiser_couples(l: List[Tuple[Any, Any]], i: int) -> List[Tuple[Any, Any]]:
    """
    Prend en entrée une liste l de couples et un indice i (0 <= i < len(l)).
    Retourne une permutation de l selon la règle :
    1. Le couple à l'indice i (pivot) ;
    2. Les couples de l dont le premier élément est égal à celui du pivot (ordre préservé) ;
    3. Tous les autres couples de l (ordre préservé).
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.9 : Triangle d'étoiles simple (Hauteur n)
# =============================================================================

def afficher_triangle_simple(n: int) -> None:
    """
    Affiche un triangle rectangle simple de hauteur n.
    Chaque ligne i (de 1 à n) contient exactement i étoiles.
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# EXERCICE 0.10 : Objets & Dictionnaires (dict) & Statistiques de promotion
# =============================================================================

def creer_fiche_etudiant(nom: str, note: float, age: int | None = None) -> Dict[str, Any]:
    """Crée un dictionnaire modélisant une fiche étudiante."""
    # TODO: À compléter par l'étudiant
    pass


def modifier_note(fiche: Dict[str, Any], nouvelle_note: float) -> None:
    """Modifie directement la note de l'étudiant en mémoire."""
    # TODO: À compléter par l'étudiant
    pass


def statistiques_promo(etudiants: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Prend une liste de dictionnaires (chacun avec 'nom' et 'note') et calcule :
    - effectif total
    - moyenne des notes
    - note maximale
    - liste des noms des étudiants admis (note >= 10.0)
    """
    # TODO: À compléter par l'étudiant
    pass


# =============================================================================
# DÉMONSTRATION / TESTS ÉTUDIANT
# =============================================================================

def run_introduction():
    print("=" * 72)
    print("BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON (SUJET ÉTUDIANT)")
    print("Complétez les fonctions dans intro_base.py puis réexécutez ce script.")
    print("=" * 72)


if __name__ == "__main__":
    run_introduction()
