"""
Exercice 1 : Tracé d'un triangle console.
"""
import sys

def triangle(n: int) -> None:
    """
    Affiche en console un triangle d'étoiles de hauteur n.
    Exemple pour n = 4 :
    *
    **
    ***
    ****
    """
    # TODO: Exercice 1
    # Utiliser une boucle for avec range() et l'opérateur de répétition '*' * i
    pass

if __name__ == '__main__':
    # Lecture de n passé via les arguments de la ligne de commande (sys.argv)
    if len(sys.argv) > 1:
        taille = int(sys.argv[1])
        triangle(taille)
    else:
        print("Usage: python triangle.py <nombre_de_lignes>")
