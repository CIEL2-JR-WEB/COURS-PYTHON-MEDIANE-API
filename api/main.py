"""
Point d'entrée principal - Démonstration et validation console complète - CORRIGÉ.
"""
from statistique import moyenne, mediane
from tri_selection import tri_selection_copie

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
    print("-> Affirmation de Nicolas : \"Je suis dans les moins bien payés de l'entreprise !\"")
    if salaire_nicolas > med:
        print("-> Bilan : FAUX. Nicolas gagne plus que la médiane (2200 € > 2000 €). Il est mieux payé que plus de la moitié des salariés de l'entreprise.")
    elif salaire_nicolas < med:
        print("-> Bilan : VRAI. Nicolas gagne moins que la médiane.")
    else:
        print("-> Bilan : Nicolas gagne exactement le salaire médian.")

if __name__ == '__main__':
    run_exercice_0()
