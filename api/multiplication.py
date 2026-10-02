"""
Table de multiplication formatée - CORRIGÉ.
"""
import sys

def multiplication_n_m(n: int, m: int) -> None:
    """
    Affiche une table n x m avec un espacement constant.
    Utilisation de .rjust() pour calibrer l'alignement.
    """
    for i in range(1, n + 1):
        ligne = "".join(str(i * j).rjust(4) for j in range(1, m + 1))
        print(ligne)

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    multiplication_n_m(n, m)
