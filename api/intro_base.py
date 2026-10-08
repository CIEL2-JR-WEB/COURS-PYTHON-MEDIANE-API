"""
BTS CIEL // Introduction Fondamentale à Python : Algorithmique, Listes & Matrices.
Exercices d'entraînement : Minimums, Listes de listes, Recherche ordonnée (itératif/récursif),
Produits cartésiens, Permutations de couples, Motifs de boucles, Matrices 2D et Objets.
"""

from typing import List, Tuple, Dict, Any


# =============================================================================
# EXERCICE 0.1 : Indice du minimum d'une liste
# =============================================================================

def indice_minimum(L: List[float | int]) -> int:
    """
    Retourne l'indice où se trouve le minimum de la liste L.
    Si la liste contient plusieurs fois la valeur minimale, retourne le premier indice rencontré.
    """
    if not L:
        raise ValueError("La liste ne doit pas être vide.")
    min_idx = 0
    for i in range(1, len(L)):
        if L[i] < L[min_idx]:
            min_idx = i
    return min_idx


# =============================================================================
# EXERCICE 0.2 : Recherche séquentielle et récursive dans une liste triée
# =============================================================================

def recherche_liste_triee(L: List[Any], x: Any) -> bool:
    """
    Version itérative : détermine si la valeur x est dans la liste croissante L.
    S'arrête prématurément dès qu'un élément dépasse x.
    """
    for val in L:
        if val == x:
            return True
        elif val > x:
            return False
    return False


def recherche_recursive_triee(L: List[Any], x: Any) -> bool:
    """
    Version récursive facile : détermine si x est présent dans la liste croissante L.
    Cas de base 1 : liste vide -> False
    Cas de base 2 : premier élément égal à x -> True
    Cas de base 3 : premier élément supérieur à x -> False
    Cas récursif  : recherche sur le reste de la liste L[1:]
    """
    if not L:
        return False
    if L[0] == x:
        return True
    if L[0] > x:
        return False
    return recherche_recursive_triee(L[1:], x)


# =============================================================================
# EXERCICE 0.3 : Taille totale d'une liste de listes
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
# EXERCICE 0.4 : Somme et Maximum d'une liste de listes
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
    
    # Initialisation avec le premier élément valide rencontré
    max_val = None
    for sous_liste in L:
        for val in sous_liste:
            if max_val is None or val > max_val:
                max_val = val
    return max_val


# =============================================================================
# EXERCICE 0.5 : Création de matrice régulière 2D & Inversion binaire
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
# EXERCICE 0.6 : Produit cartésien de deux listes (Couples)
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
# EXERCICE 0.7 : Réorganisation ordonnée d'une liste de couples selon un pivot
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
            continue  # Le pivot est déjà traité en tête
        if couple[0] == cle_pivot:
            meme_cle.append(couple)
        else:
            autres.append(couple)

    return [pivot] + meme_cle + autres


# =============================================================================
# EXERCICE 0.8 : Motif console de 2*n - 1 lignes
# =============================================================================

def afficher_figure_etoiles(n: int) -> None:
    """
    Imprime une figure décroissante puis croissante sur 2*n - 1 lignes.
    Pour n = 6 : 6 étoiles, 5, 4, 3, 2, 1, puis 2, 3, 4, 5, 6 étoiles.
    """
    # Partie décroissante : de n étoiles à 1 étoile
    for k in range(n, 0, -1):
        print("*" * k)
    # Partie croissante : de 2 étoiles à n étoiles
    for k in range(2, n + 1):
        print("*" * k)


# =============================================================================
# EXERCICE 0.9 : Objets & Dictionnaires (dict) & Manipulation de propriétés
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


# =============================================================================
# EXERCICE 0.10 : Tableaux d'Objets (Liste de dictionnaires) & Statistiques
# =============================================================================

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

    print("\n--- [Exercice 0.2] Recherche dans une liste croissante (Itératif & Récursif) ---")
    liste_triee = [2, 5, 8, 12, 19]
    print(f"Liste triée : {liste_triee}")
    print(f"Présence de 8 (itératif) : {recherche_liste_triee(liste_triee, 8)}")
    print(f"Présence de 8 (récursif) : {recherche_recursive_triee(liste_triee, 8)}")
    print(f"Présence de 7 (itératif) : {recherche_liste_triee(liste_triee, 7)}")
    print(f"Présence de 7 (récursif) : {recherche_recursive_triee(liste_triee, 7)}")

    print("\n--- [Exercice 0.3] Taille totale d'une liste de listes ---")
    L_imbriquee = [[2, 5, 4], [3, 6], [4], [2]]
    print(f"Liste L : {L_imbriquee}")
    print(f"Taille totale : {taille_totale(L_imbriquee)} éléments")

    print("\n--- [Exercice 0.4] Somme et Maximum d'une liste de listes ---")
    somme = somme_liste_de_listes(L_imbriquee)
    max_val = maximum_liste_de_listes(L_imbriquee)
    print(f"Somme de tous les éléments : {somme}")
    print(f"Maximum figurant dans L    : {max_val}")

    print("\n--- [Exercice 0.5] Matrice régulière 2D & Inversion binaire ---")
    M = creer_matrice(3, 4, 0)
    M[1][2] = 9
    print("Matrice 3x4 créée avec .append() et modification en [1][2] = 9 :")
    for lig in M:
        print(" ", lig)
    grille_binaire = [[0, 1, 0], [1, 1, 0]]
    grille_inversee = inverser_matrice_binaire(grille_binaire)
    print("Grille binaire inversée :", grille_inversee)

    print("\n--- [Exercice 0.6] Produit cartésien de deux listes (Couples) ---")
    L1 = [0, 1]
    L2 = [1, 4]
    couples = produit_cartesien(L1, L2)
    print(f"L1 = {L1}, L2 = {L2} -> Couples : {couples}")

    print("\n--- [Exercice 0.7] Réorganisation ordonnée selon un pivot ---")
    liste_couples = [(2, 3), (1, 0), (2, 1), (3, 5), (3, 4), (3, 0), (2, 5)]
    couples_reorganises = reorganiser_couples(liste_couples, 4)
    print(f"Liste originale : {liste_couples}")
    print(f"Pivot choisi à l'indice 4 : {liste_couples[4]}")
    print(f"Liste réorganisée        : {couples_reorganises}")

    print("\n--- [Exercice 0.8] Figure sablier d'étoiles (n = 6, 11 lignes) ---")
    afficher_figure_etoiles(6)

    print("\n--- [Exercices 0.9 & 0.10] Objets (dict) & Statistiques de promotion ---")
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
