"""
BTS CIEL // Introduction Fondamentale à Python : Algorithmique, Listes & Matrices (CORRECTION).
Exercices d'entraînement :
- Exercice 0.1 : Indice du minimum d'une liste
- Exercice 0.2 : Somme de 1 à n (Itératif & Récursif)
- Exercice 0.3 : Puissance x^n (Itératif & Récursif - Même type)
- Exercice 0.4 : Taille totale d'une liste de listes
- Exercice 0.5 : Somme et Maximum d'une liste de listes
- Exercice 0.6 : Création de matrice 2D régulière & Inversion binaire
- Exercice 0.7 : Produit cartésien de deux listes (Couples)
- Exercice 0.8 : Réorganisation ordonnée selon un pivot
- Exercice 0.9 : Triangle d'étoiles simple (n lignes)
- Exercice 0.10 : Objets (dict) & Statistiques de promotion
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
    if not L:
        raise ValueError("La liste ne doit pas être vide.")
    min_idx = 0
    for i in range(1, len(L)):
        if L[i] < L[min_idx]:
            min_idx = i
    return min_idx


# =============================================================================
# EXERCICE 0.2 : Somme de 1 à n (Itératif vs Récursif)
# =============================================================================

def somme_iterative(n: int) -> int:
    """Calcule 1 + 2 + ... + n de manière itérative."""
    total = 0
    for k in range(1, n + 1):
        total += k
    return total


def somme_recursive(n: int) -> int:
    """
    Calcule 1 + 2 + ... + n de manière récursive.
    Cas d'arrêt : n <= 0 -> 0 (ou n == 1 -> 1)
    Cas récursif : n + somme_recursive(n - 1)
    """
    if n <= 0:
        return 0
    return n + somme_recursive(n - 1)


# =============================================================================
# EXERCICE 0.3 : Puissance x^n (Itératif vs Récursif - Exercice simple même type)
# =============================================================================

def puissance_iterative(x: float | int, n: int) -> float | int:
    """Calcule x^n (x élevé à la puissance n >= 0) avec une boucle for."""
    resultat = 1
    for _ in range(n):
        resultat *= x
    return resultat


def puissance_recursive(x: float | int, n: int) -> float | int:
    """
    Calcule x^n de manière récursive.
    Cas d'arrêt : n == 0 -> 1 (car x^0 = 1)
    Cas récursif : x * puissance_recursive(x, n - 1)
    """
    if n == 0:
        return 1
    return x * puissance_recursive(x, n - 1)


# =============================================================================
# EXERCICE 0.4 : Taille totale d'une liste de listes
# =============================================================================

def taille_totale(L: List[List[Any]]) -> int:
    """
    Retourne la taille totale (nombre total d'éléments) de la liste de listes L.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 7
    """
    total = 0
    for sous_liste in L:
        total += len(sous_liste)
    return total


# =============================================================================
# EXERCICE 0.5 : Somme et Maximum d'une liste de listes
# =============================================================================

def somme_liste_de_listes(L: List[List[float | int]]) -> float | int:
    """
    Retourne la somme de tous les nombres contenus dans toutes les sous-listes de L.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 26
    """
    somme = 0
    for sous_liste in L:
        for val in sous_liste:
            somme += val
    return somme


def maximum_liste_de_listes(L: List[List[float | int]]) -> float | int:
    """
    Retourne le plus grand nombre figurant dans la liste de listes L, sans le localiser.
    Exemple : [[2, 5, 4], [3, 6], [4], [2]] -> 6
    """
    if not L or not any(sous_liste for sous_liste in L):
        raise ValueError("La liste de listes ne doit pas être vide.")
    
    max_val = None
    for sous_liste in L:
        for val in sous_liste:
            if max_val is None or val > max_val:
                max_val = val
    return max_val


# =============================================================================
# EXERCICE 0.6 : Création de matrice régulière 2D & Inversion binaire
# =============================================================================

def creer_matrice(nb_lignes: int, nb_colonnes: int, valeur_defaut: Any = 0) -> List[List[Any]]:
    """
    Crée une matrice 2D indépendante de dimensions nb_lignes x nb_colonnes.
    Utilise .append() pour chaque ligne afin d'éviter le piège des références partagées.
    """
    matrice = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(valeur_defaut)
        matrice.append(ligne)
    return matrice


def inverser_matrice_binaire(M: List[List[int]]) -> List[List[int]]:
    """
    Inverse une matrice binaire (0 devient 1, et 1 devient 0) et retourne la nouvelle matrice.
    """
    nouvelle_matrice = []
    for ligne in M:
        nouvelle_ligne = []
        for pixel in ligne:
            nouvelle_ligne.append(1 if pixel == 0 else 0)
        nouvelle_matrice.append(nouvelle_ligne)
    return nouvelle_matrice


# =============================================================================
# EXERCICE 0.7 : Produit cartésien de deux listes (Couples)
# =============================================================================

def produit_cartesien(L1: List[Any], L2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Retourne la liste de tous les couples formés d'un élément de L1 et d'un élément de L2.
    Exemple : [0, 1] et [1, 4] -> [(0, 1), (0, 4), (1, 1), (1, 4)]
    """
    couples = []
    for a in L1:
        for b in L2:
            couples.append((a, b))
    return couples


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
    Exemple : l = [(2, 3), (1, 0), (2, 1), (3, 5), (3, 4), (3, 0), (2, 5)] et i = 4 (pivot = (3, 4))
    Retourne : [(3, 4), (3, 5), (3, 0), (2, 3), (1, 0), (2, 1), (2, 5)]
    """
    if i < 0 or i >= len(l):
        raise IndexError("Indice de pivot hors limites.")

    pivot = l[i]
    cle_pivot = pivot[0]

    meme_cle = []
    autres = []

    for idx, couple in enumerate(l):
        if idx == i:
            continue
        if couple[0] == cle_pivot:
            meme_cle.append(couple)
        else:
            autres.append(couple)

    return [pivot] + meme_cle + autres


# =============================================================================
# EXERCICE 0.9 : Triangle d'étoiles simple (Hauteur n)
# =============================================================================

def afficher_triangle_simple(n: int) -> None:
    """
    Affiche un triangle rectangle simple de hauteur n.
    Chaque ligne i (de 1 à n) contient exactement i étoiles.
    Exemple pour n = 4 :
    *
    **
    ***
    ****
    """
    for i in range(1, n + 1):
        print("*" * i)


# =============================================================================
# EXERCICE 0.10 : Objets & Dictionnaires (dict) & Statistiques de promotion
# =============================================================================

def creer_fiche_etudiant(nom: str, note: float, age: int | None = None) -> Dict[str, Any]:
    """Crée un dictionnaire modélisant une fiche étudiante."""
    return {
        "nom": nom,
        "note": note,
        "age": age
    }


def modifier_note(fiche: Dict[str, Any], nouvelle_note: float) -> None:
    """Modifie directement la note de l'étudiant en mémoire."""
    fiche["note"] = nouvelle_note


def statistiques_promo(etudiants: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Prend une liste de dictionnaires (chacun avec 'nom' et 'note') et calcule :
    - effectif total
    - moyenne des notes
    - note maximale
    - liste des noms des étudiants admis (note >= 10.0)
    """
    if not etudiants:
        return {"effectif": 0, "moyenne": 0.0, "note_max": 0.0, "admis": []}

    total_notes = 0.0
    note_max = etudiants[0]["note"]
    admis = []

    for e in etudiants:
        note = e["note"]
        total_notes += note
        if note > note_max:
            note_max = note
        if note >= 10.0:
            admis.append(e["nom"])

    moyenne = round(total_notes / len(etudiants), 2)
    return {
        "effectif": len(etudiants),
        "moyenne": moyenne,
        "note_max": note_max,
        "admis": admis
    }


# =============================================================================
# DÉMONSTRATION GLOBALE
# =============================================================================

def run_introduction():
    print("=" * 72)
    print("BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON (ALGORITHMIQUE & DONNÉES)")
    print("=" * 72)

    print("\n--- [Exercice 0.1] Indice du minimum d'une liste ---")
    liste_test = [15, 3, 22, 8]
    idx_min = indice_minimum(liste_test)
    print(f"Liste : {liste_test} -> Indice du minimum : {idx_min} (valeur = {liste_test[idx_min]})")

    print("\n--- [Exercice 0.2] Somme de 1 à n (Itératif & Récursif) ---")
    n_somme = 5
    print(f"Somme de 1 à {n_somme} (itératif) : {somme_iterative(n_somme)}")
    print(f"Somme de 1 à {n_somme} (récursif) : {somme_recursive(n_somme)}")

    print("\n--- [Exercice 0.3] Puissance x^n (Itératif & Récursif) ---")
    x, n_puiss = 2, 4
    print(f"{x}^{n_puiss} (itératif) : {puissance_iterative(x, n_puiss)}")
    print(f"{x}^{n_puiss} (récursif) : {puissance_recursive(x, n_puiss)}")

    print("\n--- [Exercice 0.4] Taille totale d'une liste de listes ---")
    L_imbriquee = [[2, 5, 4], [3, 6], [4], [2]]
    print(f"Liste L : {L_imbriquee}")
    print(f"Taille totale : {taille_totale(L_imbriquee)} éléments")

    print("\n--- [Exercice 0.5] Somme et Maximum d'une liste de listes ---")
    somme = somme_liste_de_listes(L_imbriquee)
    max_val = maximum_liste_de_listes(L_imbriquee)
    print(f"Somme de tous les éléments : {somme}")
    print(f"Maximum figurant dans L    : {max_val}")

    print("\n--- [Exercice 0.6] Matrice régulière 2D & Inversion binaire ---")
    M = creer_matrice(3, 4, 0)
    M[1][2] = 9
    print("Matrice 3x4 créée avec .append() et modification en [1][2] = 9 :")
    for lig in M:
        print(" ", lig)
    grille_binaire = [[0, 1, 0], [1, 1, 0]]
    grille_inversee = inverser_matrice_binaire(grille_binaire)
    print("Grille binaire inversée :", grille_inversee)

    print("\n--- [Exercice 0.7] Produit cartésien de deux listes (Couples) ---")
    L1 = [0, 1]
    L2 = [1, 4]
    couples = produit_cartesien(L1, L2)
    print(f"L1 = {L1}, L2 = {L2} -> Couples : {couples}")

    print("\n--- [Exercice 0.8] Réorganisation ordonnée selon un pivot ---")
    liste_couples = [(2, 3), (1, 0), (2, 1), (3, 5), (3, 4), (3, 0), (2, 5)]
    couples_reorganises = reorganiser_couples(liste_couples, 4)
    print(f"Liste originale : {liste_couples}")
    print(f"Pivot choisi à l'indice 4 : {liste_couples[4]}")
    print(f"Liste réorganisée        : {couples_reorganises}")

    print("\n--- [Exercice 0.9] Triangle d'étoiles simple (n = 4) ---")
    afficher_triangle_simple(4)

    print("\n--- [Exercice 0.10] Objets (dict) & Statistiques de promotion ---")
    etudiants = [
        creer_fiche_etudiant("Alice", 14.5, 19),
        creer_fiche_etudiant("Bob", 8.0, 20),
        creer_fiche_etudiant("Nicolas", 15.0, 19),
        creer_fiche_etudiant("Chloé", 9.5, 21)
    ]
    stats = statistiques_promo(etudiants)
    print("Fiches étudiantes chargées :", len(etudiants))
    print(f"Statistiques calculées : Effectif = {stats['effectif']}, Moyenne = {stats['moyenne']}/20, Note max = {stats['note_max']}")
    print(f"Étudiants admis (>= 10) : {stats['admis']}")
    print("=" * 72)


if __name__ == "__main__":
    run_introduction()
