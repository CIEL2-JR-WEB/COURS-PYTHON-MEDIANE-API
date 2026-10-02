"""
Exercice 4.1 : Tri par sélection selon le pseudo-code imposé.
RAPPEL : Ne pas utiliser sorted() ni .sort().
"""

def tri_selection_copie(t: list) -> list:
    """
    Tri par sélection - Version par valeur (retourne une nouvelle liste triée).
    La liste originale 't' passée en argument ne DOIT PAS être modifiée.
    """
    # TODO:
    # 1. Créer une copie de la liste : copie = t.copy() ou list(t)
    # 2. Implémenter l'algorithme sur la copie
    # 3. Retourner la liste triée
    pass


def tri_selection_en_place(t: list) -> None:
    """
    Tri par sélection - Version en place (modifie directement la liste en mémoire).
    Ne retourne rien (None).
    """
    # TODO:
    # Implémenter l'algorithme directement sur t selon le pseudo-code de l'énoncé :
    # pour i de 0 à n - 2
    #     min ← i
    #     pour j de i + 1 à n - 1
    #         si t[j] < t[min], alors min ← j
    #     fin pour
    #     si min ≠ i, alors échanger t[i] et t[min]
    pass
