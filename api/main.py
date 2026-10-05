"""
Point d'entrée principal - Démonstration et validation console complète - CORRIGÉ.
"""
import sys
from statistique import moyenne, mediane
from tri_selection import tri_selection_copie
import intro_cyber


def run_introduction():
    intro_cyber.run_introduction_interactive()


def run_exercice_0():
    print("=== EXERCICE 0.1 & 0.2 : Statistiques et Problème de Nicolas ===")
    
    # Données officielles fournies
    salaires_nicolas = [1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000]
    salaire_nicolas = 2200

    # 1. Calcul de la moyenne
    moy = moyenne(salaires_nicolas)
    
    # 2. Tri de la série
    salaires_tries = tri_selection_copie(salaires_nicolas)
    
    # 3. Calcul de la médiane
    med = mediane(salaires_tries)

    print(f"Salaires de l'entreprise : {salaires_nicolas}")
    print(f"Moyenne des salaires : {moy:.2f} €")
    print(f"Salaires triés       : {salaires_tries}")
    print(f"Médiane des salaires : {med:.2f} €")
    print(f"Salaire de Nicolas   : {salaire_nicolas:.2f} €")

    # 4. Conclusion sur l'affirmation de Nicolas
    print("-> Problématique : Nicolas gagne 2 200 € alors que le salaire moyen est de 2 500 €.")
    print("   Il affirme : \"Je suis dans les moins bien payés de l'entreprise !\"")
    if salaire_nicolas > med:
        print("-> Analyse : FAUX. Nicolas confond salaire moyen et salaire médian.")
        print(f"   La médiane réelle est de {med:.2f} €. Avec {salaire_nicolas:.2f} €, Nicolas se situe")
        print("   au-dessus de la médiane (6e sur 9). Il fait partie des salariés les mieux rémunérés.")
        print("   La moyenne est tirée vers le haut par les salaires extrêmes (4000 € et 4500 €).")
    elif salaire_nicolas < med:
        print("-> Analyse : VRAI. Nicolas gagne moins que la médiane.")
    else:
        print("-> Analyse : Nicolas gagne exactement le salaire médian.")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['intro', 'introduction', 'cyber']:
        run_introduction()
    elif len(sys.argv) > 1 and sys.argv[1].lower() in ['all', 'tout']:
        run_introduction()
        print("\n")
        run_exercice_0()
    else:
        run_exercice_0()
