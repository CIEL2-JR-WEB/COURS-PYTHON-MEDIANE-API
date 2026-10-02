"""
Tracé de triangle console - CORRIGÉ.
"""
import sys

def triangle(n: int) -> None:
    """Affiche un triangle de hauteur n."""
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            valeur = int(sys.argv[1])
            triangle(valeur)
        except ValueError:
            print("Erreur : l'argument doit être un entier positif.")
    else:
        # Valeur de repli par défaut si non spécifié
        triangle(4)
