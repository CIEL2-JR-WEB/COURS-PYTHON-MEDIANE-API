"""
Point d'entrée principal pour les tests des exercices console (0.1 à 4.1).
"""
import sys
from statistique import moyenne, mediane
from triangle import triangle
from multiplication import multiplication_n_m
from recursion import somme_iterative, somme_recursive, factorielle_iterative, factorielle_recursive
from read_tab import afficher_tableau
from tri_selection import tri_selection_copie, tri_selection_en_place

def run_exercice_0():
    print("=== EXERCICE 0.1 & 0.2 : Statistiques et Problème de Nicolas ===")
    salaires_nicolas = [1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000]
    
    # TODO:
    # 1. Calculer et afficher la moyenne des salaires
    # 2. Trier la liste avec tri_selection_copie()
    # 3. Calculer et afficher la médiane
    # 4. Afficher la réponse argumentée concernant l'affirmation de Nicolas
    pass

def main():
    print("BTS CIEL - Lancement des tests console")
    # Pour tester un exercice spécifique, décommentez ou passez des arguments
    run_exercice_0()

if __name__ == '__main__':
    main()
