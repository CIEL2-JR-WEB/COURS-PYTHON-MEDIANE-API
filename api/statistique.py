"""
Module de calculs statistiques élémentaires - CORRIGÉ.
Conforme aux exigences : aucun recours à statistics ni sorted().
"""

def moyenne(tab: list) -> float:
    """
    Calcule la moyenne arithmétique d'une liste de nombres.
    """
    if not tab:
        return 0.0
    somme = sum(tab)
    return round(float(somme) / len(tab), 2)


def mediane(tab: list) -> float:
    """
    Calcule la médiane d'une série SUPPOSÉE TRIÉE.
    - N impair : élément central d'indice N // 2
    - N pair : moyenne des deux éléments au centre
    """
    if not tab:
        return 0.0

    n = len(tab)
    centre = n // 2

    # Modulo de N pour vérifier la parité
    if n % 2 != 0:
        # N impair : valeur centrale exacte
        return float(tab[centre])
    else:
        # N pair : moyenne arithmétique des deux valeurs centrales
        valeur_centrale_gauche = tab[centre - 1]
        valeur_centrale_droite = tab[centre]
        return round((valeur_centrale_gauche + valeur_centrale_droite) / 2.0, 2)
