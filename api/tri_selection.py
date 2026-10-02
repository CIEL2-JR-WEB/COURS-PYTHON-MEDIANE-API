"""
Implémentation du tri par sélection - CORRIGÉ.
Strictement conforme au pseudo-code de l'énoncé.
"""
from read_tab import afficher_tableau

def tri_selection_copie(t: list) -> list:
    """
    Tri par sélection - Version passage par valeur.
    Travaille sur une copie de la liste originale et la retourne triée.
    """
    copie = list(t)
    tri_selection_en_place(copie)
    return copie


def tri_selection_en_place(t: list) -> None:
    """
    Tri par sélection - Version passage par référence (en place).
    Modifie la liste passée en paramètre directement en mémoire.
    """
    n = len(t)
    for i in range(n - 1):  # pour i de 0 à n - 2
        min_idx = i
        for j in range(i + 1, n):  # pour j de i + 1 à n - 1
            if t[j] < t[min_idx]:
                min_idx = j
        if min_idx != i:
            # Échange idiomatique en Python : t[i], t[min] = t[min], t[i]
            t[i], t[min_idx] = t[min_idx], t[i]


if __name__ == '__main__':
    tab_test = [15, 3, 22, 8, 19]
    print("Tableau original :", tab_test)
    
    tab_trie = tri_selection_copie(tab_test)
    print("Après tri_selection_copie(t) ->", tab_trie)
    print("Tableau original non modifié :", tab_test)

    tri_selection_en_place(tab_test)
    print("Après tri_selection_en_place(t) -> t a été modifié directement :", tab_test)
