"""
BTS CIEL // Introduction Fondamentale à Python : Les Bases Concrètes.
Exercices d'initiation : Chaînes, Listes (append/push), Dictionnaires et Traitement d'Images.
"""

from typing import List, Dict, Any


# =============================================================================
# 1. LES CHAÎNES DE CARACTÈRES (str)
# =============================================================================

def nettoyer_texte(texte: str) -> str:
    """Retire les espaces au début et à la fin, et met en minuscules."""
    return texte.strip().lower()


def est_palindrome(mot: str) -> bool:
    """Vérifie si un mot se lit de la même façon dans les deux sens grâce au slicing [::-1]."""
    mot_propre = mot.strip().lower()
    return mot_propre == mot_propre[::-1]


def decouper_liste_mots(texte: str, separateur: str = ",") -> List[str]:
    """Découpe une chaîne en liste de morceaux nettoyés."""
    morceaux = texte.split(separateur)
    return [m.strip() for m in morceaux if m.strip()]


# =============================================================================
# 2. LES LISTES (list) & L'ACCUMULATEUR (append / push)
# =============================================================================

def filtrer_pairs(nombres: List[int]) -> List[int]:
    """
    Extrait les nombres pairs avec le patron accumulateur .append()
    (équivalent strict de tableau.push() en JavaScript).
    """
    pairs = []
    for n in nombres:
        if n % 2 == 0:
            pairs.append(n)
    return pairs


def filtrer_superieur(nombres: List[float], seuil: float) -> List[float]:
    """Garde uniquement les nombres strictement supérieurs au seuil."""
    selection = []
    for val in nombres:
        if val > seuil:
            selection.append(val)
    return selection


def calculer_somme_et_moyenne(valeurs: List[float]) -> tuple[float, float]:
    """Calcule manuellement la somme et la moyenne avec une boucle for."""
    if not valeurs:
        return 0.0, 0.0
    somme = 0.0
    for val in valeurs:
        somme += val
    moyenne = somme / len(valeurs)
    return round(somme, 2), round(moyenne, 2)


# =============================================================================
# 3. LES DICTIONNAIRES (dict) & LISTES DE DICTIONNAIRES
# =============================================================================

def creer_fiche_eleve(nom: str, age: int, note: float) -> Dict[str, Any]:
    """Crée un dictionnaire représentant un élève."""
    return {
        "nom": nom,
        "age": age,
        "note": note
    }


def calculer_moyenne_classe(eleves: List[Dict[str, Any]]) -> float:
    """Calcule la moyenne des notes à partir d'une liste de dictionnaires."""
    if not eleves:
        return 0.0
    total = 0.0
    for eleve in eleves:
        total += eleve["note"]
    return round(total / len(eleves), 2)


def filtrer_admis(eleves: List[Dict[str, Any]], note_seuil: float = 10.0) -> List[Dict[str, Any]]:
    """Retourne la liste des élèves admis (note >= seuil) en utilisant .append()."""
    admis = []
    for eleve in eleves:
        if eleve.get("note", 0) >= note_seuil:
            admis.append(eleve)
    return admis


# =============================================================================
# 4. CRÉATION DE MATRICES 2D & TRAITEMENT D'IMAGE (IMAGE CACHÉE)
# =============================================================================

def creer_matrice(nb_lignes: int, nb_colonnes: int, valeur_defaut: Any = 0) -> List[List[Any]]:
    """
    Crée une matrice 2D de dimensions nb_lignes x nb_colonnes initialisée avec valeur_defaut.
    Construit chaque ligne indépendamment avec .append() pour éviter tout effet de bord.
    """
    matrice = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(valeur_defaut)
        matrice.append(ligne)
    return matrice


# Image hôte 8x8 : les valeurs sont des niveaux de gris apparemment aléatoires (100-200),
# mais les nombres IMPAIRS cachent les pixels d'un coeur secret !
IMAGE_MYSTERE = [
    [120, 135, 143, 110, 102, 187, 191, 104],
    [115, 133, 141, 127, 189, 175, 163, 147],
    [161, 179, 145, 137, 189, 177, 123, 145],
    [155, 143, 177, 189, 135, 157, 179, 191],
    [134, 189, 177, 143, 159, 175, 123, 168],
    [112, 156, 189, 177, 123, 145, 180, 142],
    [176, 142, 156, 189, 177, 124, 168, 142],
    [104, 118, 144, 134, 188, 176, 124, 140]
]


def afficher_image_console(grille_caracteres: List[List[str]]) -> None:
    """Affiche une matrice de caractères dans la console."""
    for ligne in grille_caracteres:
        print("".join(ligne))


def reveler_image_secrete(image_hote: List[List[int]]) -> List[List[str]]:
    """
    Révèle l'image cachée en analysant la parité de chaque pixel :
    - Si le nombre est IMPAIR (pixel % 2 != 0) -> pixel secret '#' (allumé).
    - Si le nombre est PAIR   (pixel % 2 == 0) -> pixel secret ' ' (espace/éteint).
    Utilise .append() pour chaque pixel et chaque ligne.
    """
    image_revelee = []
    for ligne in image_hote:
        ligne_revelee = []
        for pixel in ligne:
            if pixel % 2 != 0:
                ligne_revelee.append("#")
            else:
                ligne_revelee.append(" ")
        image_revelee.append(ligne_revelee)
    return image_revelee


def cacher_motif(image_base: List[List[int]], motif_binaire: List[List[int]]) -> List[List[int]]:
    """
    Modifie les pixels de image_base pour y inscrire le motif binaire :
    - pixel secret = 1 -> le pixel devient impair.
    - pixel secret = 0 -> le pixel devient pair.
    """
    hauteur = len(image_base)
    largeur = len(image_base[0])
    image_modifiee = []
    for i in range(hauteur):
        nouvelle_ligne = []
        for j in range(largeur):
            pixel = image_base[i][j]
            secret = motif_binaire[i][j]
            if secret == 1 and pixel % 2 == 0:
                pixel += 1
            elif secret == 0 and pixel % 2 != 0:
                pixel -= 1
            nouvelle_ligne.append(pixel)
        image_modifiee.append(nouvelle_ligne)
    return image_modifiee


# =============================================================================
# DÉMONSTRATION GLOBALE
# =============================================================================

def run_introduction():
    print("=" * 72)
    print("BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON (BASES CONCRÈTES)")
    print("=" * 72)

    print("\n--- [Exercice 0.1] Les Chaînes de caractères (str) & Slicing ---")
    saisie = "   BTS CIEL 2026   "
    print(f"Saisie brute       : '{saisie}'")
    print(f"Texte nettoyé      : '{nettoyer_texte(saisie)}'")
    for mot in ["radar", "python", "kayak"]:
        print(f"'{mot}' est palindrome ? {est_palindrome(mot)}")
    liste_villes = decouper_liste_mots("Paris, Lyon, Marseille, Toulouse")
    print(f"Villes découpées   : {liste_villes}")

    print("\n--- [Exercice 0.2] Les Listes (list) & Accumulateur .append() (push JS) ---")
    nombres = [12, 5, 8, 21, 14, 3, 30]
    pairs = filtrer_pairs(nombres)
    somme, moy = calculer_somme_et_moyenne(nombres)
    print(f"Liste initiale     : {nombres}")
    print(f"Pairs (avec .append) : {pairs}")
    print(f"Somme = {somme} | Moyenne = {moy}")

    print("\n--- [Exercice 0.3] Les Dictionnaires (dict) & Liste de fiches ---")
    eleves = [
        creer_fiche_eleve("Alice", 19, 14.5),
        creer_fiche_eleve("Bob", 20, 8.0),
        creer_fiche_eleve("Nicolas", 19, 15.0),
        creer_fiche_eleve("Chloé", 21, 9.5)
    ]
    moy_classe = calculer_moyenne_classe(eleves)
    admis = filtrer_admis(eleves, 10.0)
    print(f"Nombre d'élèves    : {len(eleves)}")
    print(f"Moyenne de classe  : {moy_classe}/20")
    print(f"Élèves admis       : {[e['nom'] for e in admis]}")

    print("\n--- [Exercice 0.4] Création de Matrice 2D & Manipulation d'Indices ---")
    mat_demo = creer_matrice(3, 4, 0)
    mat_demo[1][2] = 9  # Modification de la case ligne 1, colonne 2
    print("Matrice 3x4 générée avec .append() (modification en [1][2] = 9) :")
    for lig in mat_demo:
        print(" ", lig)

    print("\n--- [Exercices 0.5 & 0.6] Traitement d'Image : Image Cachée dans une Image ---")
    print("Matrice apparente 8x8 (niveaux de gris) :")
    for lig in IMAGE_MYSTERE[:3]:
        print(" ", lig)
    print("  ...")
    print("\nRévélation de l'image secrète par parité des pixels (pixel % 2 != 0) :")
    revelee = reveler_image_secrete(IMAGE_MYSTERE)
    print("+--------+")
    for lig in revelee:
        print("|" + "".join(lig) + "|")
    print("+--------+")
    print("-> L'image secrète (un cœur) a été révélée avec succès !")
    print("=" * 72)


if __name__ == "__main__":
    run_introduction()
