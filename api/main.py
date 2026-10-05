"""
Point d'entrée principal pour les tests des exercices console.
"""
import sys
from statistique import moyenne, mediane
from triangle import triangle
from multiplication import multiplication_n_m
from recursion import somme_iterative, somme_recursive, factorielle_iterative, factorielle_recursive
from read_tab import afficher_tableau
from tri_selection import tri_selection_copie, tri_selection_en_place

def run_exercice_0():
    print("=== EXERCICE 0.6 & 0.7 : Statistiques et Problème de Nicolas ===")
    salaires_nicolas = [1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000]
    
    # TODO:
    # 1. Calculer et afficher la moyenne des salaires
    # 2. Trier la liste avec tri_selection_copie()
    # 3. Calculer et afficher la médiane
    # 4. Afficher la réponse argumentée concernant l'affirmation de Nicolas
    pass

def main():
    print("BTS CIEL - Lancement des tests console")
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['intro', 'introduction', 'cyber']:
        import intro_cyber
        print("Pour tester vos fonctions d'introduction, lancez : python intro_cyber.py")
    else:
        run_exercice_0()

if __name__ == '__main__':
    main()
