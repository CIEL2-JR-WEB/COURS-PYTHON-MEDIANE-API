"""
Module d'affichage de tableaux formatés - CORRIGÉ.
"""

def afficher_tableau(t: list, titre: str = "Contenu du tableau") -> None:
    """Affiche proprement une liste avec les indices d'éléments."""
    print(f"--- {titre} (taille = {len(t)}) ---")
    for idx, val in enumerate(t):
        print(f"  [{idx}] : {val}")
    print("-" * (len(titre) + 8))

if __name__ == '__main__':
    afficher_tableau([1500, 4500, 2200], "Test Salaires")
