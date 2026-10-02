"""
Calculs itératifs et récursifs - CORRIGÉ.
"""

def somme_iterative(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def somme_recursive(n: int) -> int:
    if n <= 0:
        return 0
    return n + somme_recursive(n - 1)

def factorielle_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("La factorielle n'est définie que pour les entiers positifs.")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def factorielle_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("La factorielle n'est définie que pour les entiers positifs.")
    if n <= 1:
        return 1
    return n * factorielle_recursive(n - 1)

if __name__ == '__main__':
    print("Somme iterative(5)   :", somme_iterative(5))
    print("Somme recursive(5)   :", somme_recursive(5))
    print("Factorielle iter(5)  :", factorielle_iterative(5))
    print("Factorielle recur(5) :", factorielle_recursive(5))
