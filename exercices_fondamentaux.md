# 📝 BTS CIEL // Cahier d'Exercices Préparatoires Fondamentaux en Python
## *De l'algorithmique débranchée à la manipulation de données JSON & Objets*

> 📌 **Document destiné à l'apprentissage progressif (Imprimable pour travail sur table + validation machine)**  
> **Auteurs & Référence :** Inspiré du *« Cours de Python : Programmation Python pour les sciences de la vie »* (P. Fuchs & P. Poulain, Université Paris Cité) et adapté aux exigences du **BTS CIEL** (Informatique embarquée, Réseaux, Web, Traitement de données JSON et Objets).

---

### 🎯 Présentation et Méthodologie

Ce cahier d'exercices pose l'ensemble des fondations techniques requises avant d'aborder le cycle de développement web et API (Séances 1 à 6).

Chaque module est structuré en deux temps indissociables :
1. **📝 Partie A — Travail débranché sur table (Au stylo sur feuille imprimée)** : Vous posez les concepts, dessinez les schémas mémoire, complétez les tables de trace et écrivez les algorithmes avant de toucher au clavier.
2. **💻 Partie B — Implémentation et validation sur machine** : Vous codez votre solution dans le script compagnon [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py) et vérifiez automatiquement son bon fonctionnement avec Python 3 (`docker compose exec api python exercices_fondamentaux.py`).

---

## 📋 Sommaire de la Progression Pédagogique

| Module | Thème du Cours | Concepts Clés | Objectif Opérationnel |
| :---: | :--- | :--- | :--- |
| **M1** | **Variables, Types & Arithmétique** | Types primitifs (`int`, `float`, `str`, `bool`), affectation, casting, `//` et `%`. | Prédire les types et manipuler les conversions numériques. |
| **M2** | **Affichage & f-strings** | `print()`, arguments `sep`/`end`, formatage `{:.2f}`, alignement (`<`, `>`, `^`). | Produire des sorties formatées professionnelles en colonnes. |
| **M3** | **Listes, Slicing & Mémoire** | Indices positifs/négatifs, tranches `[::]`, mutabilité, copie par référence vs `list()`. | Maîtriser le découpage de listes et éviter les effets de bord. |
| **M4** | **Boucles `for`, `while` & Parcours** | Itération par élément vs par indice, `enumerate()`, accumulateurs, motifs 2D. | Parcourir des collections et tracer des figures géométriques. |
| **M5** | **Conditions & Tests Avancés** | `if/elif/else`, opérateurs `and`/`or`/`not`, imprécision des flottants (`isclose`). | Sécuriser la logique décisionnelle et comparer des réels. |
| **M6** | **Fichiers & Sérialisation JSON** | `with open()`, lecture/écriture, syntaxe JSON stricte, `json.dump` / `load`. | Sauvegarder et restaurer des données structurées. |
| **M7** | **Dictionnaires & Tuples** | Tables d'association `{cle: val}`, `.items()`, `.get()`, unpacking, listes de dicts. | Modéliser des enregistrements et agréger des occurrences. |
| **M8** | **Fonctions & Principe DRY** | `def`, paramètres par défaut, retours multiples (tuples), portée locale vs globale. | Écrire du code modulaire, réutilisable et sans duplication. |
| **M9** | **Programmation Orientée Objet** | Classes, `__init__`, `self`, attributs d'instance, méthodes métier, `__str__`. | Encapsuler des données et comportements dans des objets. |
| **M10** | **Grand Défi Synthèse Intégrateur** | Chaîne complète : Fichier JSON $\to$ Objets $\to$ Itérations $\to$ Rapport JSON. | Maîtriser de bout en bout l'itération et la persistance JSON. |

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 1 : Variables, Types, Conversions & Arithmétique (Ch. 2)

### 🎯 Objectif
Maîtriser les types primitifs en Python, le mécanisme d'affectation de droite à gauche, la conversion explicite de types (*casting*) et les opérateurs de division euclidienne (`//` et `%`).

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 1.1 — Prédire les types et les valeurs
Complétez le tableau suivant en déterminant pour chaque instruction la valeur obtenue et son type Python (`int`, `float`, `str`, `bool`) :

| Instruction Python | Valeur Résultante | Type (`type()`) |
| :--- | :--- | :--- |
| `a = 19 // 4` | `........................................` | `........................................` |
| `b = 19 % 4` | `........................................` | `........................................` |
| `c = 19 / 4` | `........................................` | `........................................` |
| `d = "12" + "34"` | `........................................` | `........................................` |
| `e = int("12") + float("3.5")` | `........................................` | `........................................` |
| `f = "CIEL " * 3` | `........................................` | `........................................` |
| `g = 2 ** 4` | `........................................` | `........................................` |
| `h = 2.5e3` | `........................................` | `........................................` |

#### Exercice 1.2 — Analyse d'erreur de conversion
On considère le fragment de code suivant :
```python
prix_unitaire = "15.5"
quantite = 4
total = prix_unitaire * quantite
```
1. Quelle est la valeur de la variable `total` après exécution de ce code ?  
   *Réponse :* `....................................................................`
2. Pourquoi n'obtient-on pas le montant numérique attendu ($62.0$) ?  
   *Réponse :* `................................................................................................................................`
3. Écrivez la ligne de correction indispensable pour calculer la facture exacte :  
   *Correction :* `............................................................................................................................`

#### Exercice 1.3 — Décomposition de temps (Division entière & Modulo)
On souhaite décomposer un total de secondes $S = 7\,385\text{ s}$ en heures ($H$), minutes ($M$) et secondes restantes ($R$).  
Complétez les formules mathématiques en utilisant uniquement les variables et les opérateurs `//` et `%` :
* $H = \text{secondes } // \text{ ....................}$  *(1 heure = 3 600 s)*
* $\text{secondes\_restantes} = \text{secondes } \% \text{ ....................}$
* $M = \text{secondes\_restantes } // \text{ ....................}$  *(1 minute = 60 s)*
* $R = \text{secondes\_restantes } \% \text{ ....................}$

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans le fichier [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def decomposer_secondes(secondes: int) -> tuple[int, int, int]:
    """Prend un nombre entier de secondes et retourne (heures, minutes, secondes_restantes)."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :* `assert decomposer_secondes(7385) == (2, 3, 5)` et `assert decomposer_secondes(3661) == (1, 1, 1)`.

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 2 : Affichage, Formatage et f-strings (Ch. 3)

### 🎯 Objectif
Structurer l'affichage console en évitant les concaténations fragiles, maîtriser les arguments `sep` et `end` de `print()`, et formater précisément des données textuelles et numériques avec les f-strings.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 2.1 — Comportement de `print()`
Prédisez l'affichage exact produit par les instructions suivantes dans le terminal :

1. `print("192", "168", "1", "10", sep=".")`  
   *Affichage :* `....................................................................`
2. `print("Vitesse", end=" : ") ; print(100, "km/h")`  
   *Affichage :* `....................................................................`

#### Exercice 2.2 — Spécifications de format dans les f-strings
Soit les variables `taux = 0.1965` et `valeur = 42` et `libelle = "Serveur"`. Complétez les rendus obtenus :

| Expression f-string | Rendu texte exact | Description du formatage |
| :--- | :--- | :--- |
| `f"{taux:.2%}"` | `..............................` | Pourcentage avec 2 décimales |
| `f"{valeur:05d}"` | `..............................` | Entier complété par des zéros sur 5 caractères |
| `f"{libelle:>10s}"` | `..............................` | Chaîne cadrée à droite sur 10 caractères |
| `f"{libelle:*^12s}"` | `..............................` | Chaîne centrée avec étoiles sur 12 caractères |
| `f"{1234567:.2e}"` | `..............................` | Notation scientifique à 2 décimales |

#### Exercice 2.3 — Alignement d'un tableau de bord
On désire afficher trois colonnes : `Hôte`, `Port` et `Statut`.  
Complétez la f-string ci-dessous pour que chaque ligne s'affiche avec la largeur garantie :
* `Hôte` : 15 caractères, cadré à gauche (`<`)
* `Port` : 6 caractères, cadré à droite (`>`)
* `Statut` : 10 caractères, centré (`^`)

```python
# Complétez la f-string :
ligne_formatee = f"{hote:............} | {port:............} | {statut:............}"
```

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def formater_ligne_service(hote: str, port: int, statut: str) -> str:
    """Retourne une chaîne formatée : hôte cadré à gauche (15c), port à droite (6c), statut centré (10c)."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
`assert formater_ligne_service("localhost", 80, "ACTIF") == "localhost       |     80 |   ACTIF   "`

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 3 : Listes, Indexation, Slicing & Gestion Mémoire (Ch. 4)

### 🎯 Objectif
Comprendre l'indexation directe (indices $0 \dots n-1$ et négatifs $-1 \dots -n$), maîtriser la sélection par tranches (*slicing* `[debut:fin:pas]`) et appréhender physiquement la distinction entre copie de référence et copie défensive.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 3.1 — Découpage par tranches (*Slicing*)
Soit la liste `ip = [192, 168, 10, 254, 80, 443, 22]`. Indiquez le résultat de chaque tranche :

1. `ip[0]` : `....................` | `ip[-1]` : `....................` | `ip[-3]` : `....................`
2. `ip[0:4]` : `[ ........................................................ ]`
3. `ip[4:]` : `[ ........................................................ ]`
4. `ip[::2]` : `[ ........................................................ ]`
5. `ip[::-1]` : `[ ........................................................ ]`

#### Exercice 3.2 — Le piège de la copie mémoire par référence
On exécute la séquence d'instructions suivante :
```python
L1 = [10, 20, 30]
L2 = L1
L3 = list(L1)

L1[0] = 99
```
1. Dessinez les flèches mémoire liant les variables `L1`, `L2` et `L3` aux blocs de données :
```text
[Espace des Noms]                       [Espace Mémoire]
    L1  ----------------------------->    [ ... , ... , ... ]
    L2  ----------------------------->
    L3  ----------------------------->    [ ... , ... , ... ]
```
2. Complétez les valeurs après modification de `L1[0]` :
   * Valeur de `L1` : `[ ........................................ ]`
   * Valeur de `L2` : `[ ........................................ ]`
   * Valeur de `L3` : `[ ........................................ ]`
3. Quelle fonction Python permet de vérifier si deux variables partagent la même adresse mémoire ?  
   *Réponse :* `....................................................................`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def dupliquer_sans_effet_de_bord(liste_source: list) -> list:
    """Retourne une copie indépendante de la liste passée en argument."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
```python
orig = [1, 2, 3]
copie = dupliquer_sans_effet_de_bord(orig)
copie[0] = 99
assert orig == [1, 2, 3] and copie == [99, 2, 3]
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 4 : Boucles `for`, `while` & Parcours d'Itérables (Ch. 5)

### 🎯 Objectif
Maîtriser les boucles déterministes `for`, les boucles conditionnelles `while`, l'itération combinée indices/éléments avec `enumerate()`, les accumulateurs numériques et le tracé de figures régulières.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 4.1 — Déroulement d'un accumulateur sur table
Soit la liste `releves = [12, 18, 5, 25, 8]`. On exécute :
```python
cumul = 0
nb_depassements = 0
for v in releves:
    if v >= 10:
        cumul = cumul + v
        nb_depassements = nb_depassements + 1
```
Remplissez le tableau de trace pas à pas :

| Tour | Variable `v` | Test `v >= 10` | Nouveau `cumul` | Nouveau `nb_depassements` |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 12 | VRAI | 12 | 1 |
| 2 | 18 | `............` | `............` | `............` |
| 3 | 5 | `............` | `............` | `............` |
| 4 | 25 | `............` | `............` | `............` |
| 5 | 8 | `............` | `............` | `............` |

#### Exercice 4.2 — Conception de motif géométrique simple
On souhaite tracer un triangle rectangle d'étoiles de hauteur $n$ :
```text
Pour n = 4 :
*
**
***
****
```
1. Écrivez le pseudo-code officiel de l'algorithme :
```text
Procédure triangle(entier n)
    Pour ............................................................ :
        Afficher ....................................................
Fin Procédure
```
2. Quelle opération concise sur chaîne permet en Python de répéter le caractère `"*"` sans boucle interne ?  
   *Réponse :* `....................................................................`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez les fonctions :
```python
def calculer_somme_et_moyenne(valeurs: list[float | int]) -> tuple[float, float]:
    """Calcule et renvoie la somme totale et la moyenne arithmétique avec une boucle for."""
    # TODO: À compléter
    pass

def generer_lignes_triangle(n: int) -> list[str]:
    """Génère la liste des n lignes du triangle rectangle d'étoiles."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*  
`assert calculer_somme_et_moyenne([10, 20, 30]) == (60.0, 20.0)`  
`assert generer_lignes_triangle(3) == ["*", "**", "***"]`

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 5 : Conditions, Tests Avancés & Précision des Floats (Ch. 6)

### 🎯 Objectif
Structurer les embranchements complexes (`if/elif/else`), utiliser les opérateurs logiques (`and`, `or`, `not`), maîtriser les contrôles de flux (`break`, `continue`) et appréhender l'imprécision inhérente au codage IEEE-754 des flottants.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 5.1 — Tables de vérité et tests multiples
Complétez les valeurs de vérité (`True` ou `False`) :
* `(10 > 5) and (3 == 4)` $\to$ `....................`
* `(10 > 5) or (3 == 4)` $\to$ `....................`
* `not (7 in [1, 2, 3])` $\to$ `....................`
* `(5 > 2) and not (4 < 1)` $\to$ `....................`

#### Exercice 5.2 — L'énigme des nombres flottants
Dans la console Python, on teste l'égalité :
```python
>>> 0.1 + 0.2 == 0.3
False
```
1. Expliquez pourquoi Python répond `False` à cette égalité mathématique évidente :  
   *Explication :* `....................................................................................................................................................`
2. Comment tester rigoureusement l'égalité de deux nombres flottants $a$ et $b$ avec une marge d'erreur $\epsilon = 10^{-5}$ ?  
   *Formule en Python :* `............................................................................................................................................`
3. Quelle fonction de la bibliothèque standard `math` permet de réaliser ce test de manière lisible ?  
   *Réponse :* `math.isclose( ............................................................ )`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def categoriser_valeur(valeur: float, seuil_bas: float, seuil_haut: float) -> str:
    """Retourne 'BAS', 'NORMAL', ou 'CRITIQUE' selon les seuils (inclut tolérance 1e-5)."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
`assert categoriser_valeur(15.0, 10.0, 20.0) == "NORMAL"`  
`assert categoriser_valeur(25.0, 10.0, 20.0) == "CRITIQUE"`

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 6 : Fichiers Texte, Sérialisation & Données JSON (Ch. 7)

### 🎯 Objectif
Lire et écrire des fichiers avec le gestionnaire de contexte `with open()`, convertir des flux texte en données typées et sérialiser/désérialiser des structures de données complètes au format JSON.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 6.1 — Correspondance stricte Python $\leftrightarrow$ JSON
Remplissez la grille d'équivalence entre la syntaxe Python et la norme JSON RFC 8259 :

| Concept | En Python | En JSON strict |
| :--- | :--- | :--- |
| Valeur booléenne vraie | `True` | `..............................` |
| Valeur booléenne fausse | `False` | `..............................` |
| Absence d'information | `None` | `..............................` |
| Encadrement des chaînes | `'texte'` ou `"texte"` | `..............................` *(règle stricte)* |
| Virgule après dernier élément | Tolérée `[1, 2, ]` | `..............................` |

#### Exercice 6.2 — Détection d'erreurs dans un extrait JSON
Trouvez et entourez les 3 anomalies syntaxiques qui rendent ce JSON invalide :
```json
{
    'titre': "Contrôle d'accès",
    "port": 8080,
    "actif": True,
    "services": ["SSH", "HTTP", ]
}
```
* *Anomalie 1 :* `........................................................................................................................`
* *Anomalie 2 :* `........................................................................................................................`
* *Anomalie 3 :* `........................................................................................................................`

#### Exercice 6.3 — Gestionnaire de contexte `with open`
Pourquoi l'instruction `with open("data.json", "r") as f:` est-elle nettement supérieure à un simple appel `f = open("data.json", "r")` ?  
*Réponse :* `....................................................................................................................................................`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez les fonctions :
```python
def sauvegarder_donnees_json(chemin_fichier: str, donnees: list | dict) -> None:
    """Enregistre l'objet Python dans un fichier JSON avec indent=4 et encodage utf-8."""
    # TODO: À compléter
    pass

def charger_donnees_json(chemin_fichier: str) -> list | dict:
    """Charge et retourne les données d'un fichier JSON."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
```python
test_data = [{"id": 1, "nom": "Alice", "actif": True}]
sauvegarder_donnees_json("/tmp/test.json", test_data)
assert charger_donnees_json("/tmp/test.json") == test_data
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 7 : Dictionnaires, Tuples & Modélisation de Données (Ch. 8)

### 🎯 Objectif
Créer et manipuler des dictionnaires associatifs (`dict`), parcourir clés et valeurs avec `.items()`, sécuriser la recherche avec `.get()`, utiliser les tuples immuables et le désemballage (*tuple unpacking*).

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 7.1 — Traçage de dictionnaire
Soit le dictionnaire représentant un équipement réseau :
```python
equipement = {
    "ip": "192.168.1.1",
    "nom": "Passerelle",
    "ports": 4,
    "actif": True
}
```
1. Quelle est la valeur renvoyée par `equipement["nom"]` ?  
   *Réponse :* `............................................................`
2. Que se passe-t-il si l'on exécute `equipement["vitesse"]` ?  
   *Réponse :* `............................................................`
3. Quelle méthode permet de renvoyer une valeur par défaut de `1000` si la clé n'existe pas sans générer d'erreur ?  
   *Syntaxe :* `equipement.get( ............................................................ )`

#### Exercice 7.2 — Désempaquetage de Tuples (*Unpacking*)
Soit la liste de tuples :
```python
services = [("HTTP", 80), ("HTTPS", 443), ("SSH", 22)]
```
Écrivez la boucle `for` qui désemballe directement chaque tuple en deux variables distinctes `nom` et `port` :
```python
for .................................................... in services:
    print(f"Service {nom} sur le port {port}")
```

#### Exercice 7.3 — Modélisation : Liste de Dictionnaires
Complétez la structure suivante pour modéliser deux salariés (Alice, 1500 €, et Bob, 4500 €) :
```python
salaries = [
    { "nom": "Alice", "salaire": ............ },
    { "nom": "............", "salaire": ............ }
]
```

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def compter_frequences_elements(elements: list[str]) -> dict[str, int]:
    """Compte et retourne le nombre d'occurrences de chaque chaîne dans un dictionnaire."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
`assert compter_frequences_elements(["A", "B", "A", "C", "A"]) == {"A": 3, "B": 1, "C": 1}`

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 8 : Fonctions, Modularité, Paramètres & Portée (Ch. 10)

### 🎯 Objectif
Définir des fonctions avec `def`, maîtriser la distinction entre variables locales et variables globales (règle LGI), gérer les paramètres par défaut, les retours multiples et appliquer le principe DRY (*Don't Repeat Yourself*).

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 8.1 — Analyse de la portée des variables (*Scope*)
Observez attentivement le script suivant :
```python
compteur = 100

def initialiser_session(nom: str):
    compteur = 1
    message = f"Session ouverte pour {nom} (n°{compteur})"
    return message

resultat = initialiser_session("Bob")
print(resultat)
print(compteur)
```
1. Quelle est la première ligne affichée par le `print(resultat)` ?  
   *Affichage 1 :* `....................................................................................................`
2. Quelle est la valeur affichée par `print(compteur)` ?  
   *Affichage 2 :* `....................................................................................................`
3. Pourquoi la variable `compteur` du programme principal ne vaut-elle pas `1` ?  
   *Explication :* `....................................................................................................................................................`

#### Exercice 8.2 — Fonctions à retours multiples
En Python, comment une fonction peut-elle renvoyer simultanément deux valeurs (par exemple le minimum et le maximum d'une liste) ? Quel type d'objet est implicitement retourné ?  
*Réponse :* `....................................................................................................................................................`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction :
```python
def calculer_extremums_et_etendue(valeurs: list[float | int]) -> tuple[float, float, float]:
    """Retourne un tuple (minimum, maximum, etendue) où etendue = maximum - minimum."""
    # TODO: À compléter
    pass
```
*Validation machine attendue :*
`assert calculer_extremums_et_etendue([15, 3, 22, 8]) == (3.0, 22.0, 19.0)`

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 9 : Programmation Orientée Objet — Classes & Instances (Ch. 23)

### 🎯 Objectif
Concevoir une classe (`class`), comprendre le rôle du constructeur `__init__`, maîtriser l'usage du paramètre `self`, définir des attributs d'instance et implémenter des méthodes métier ainsi que la méthode spéciale `__str__`.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 9.1 — Le rôle fondamental de `self`
1. Dans la méthode `def __init__(self, nom, salaire):`, que représente précisément le paramètre `self` ?  
   *Réponse :* `....................................................................................................................................................`
2. Quelle est la différence fondamentale entre `self.salaire` et une variable `salaire` sans `self.` au sein d'une méthode ?  
   *Réponse :* `....................................................................................................................................................`

#### Exercice 9.2 — Conception de la classe `Salarie`
Complétez le squelette de la classe ci-dessous :
```python
class Salarie:
    def __init__(self, identifiant: int, nom: str, salaire: float):
        self.id = identifiant
        self.nom = ........................
        self.salaire = ........................

    def augmenter(self, pourcentage: float) -> None:
        """Augmente le salaire de pourcentage % (ex: 10 pour +10%)."""
        self.salaire = self.salaire * (1 + ........................ / 100)

    def to_dict(self) -> dict:
        """Convertit l'instance en dictionnaire standard pour export JSON."""
        return {
            "id": self.id,
            "nom": ........................,
            "salaire": ........................
        }

    def __str__(self) -> str:
        """Représentation textuelle de l'objet pour print()."""
        return f"[{self.id}] {self.nom} : {self.salaire:.2f} €"
```

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la classe `Salarie` complète.  
*Validation machine attendue :*
```python
s = Salarie(1, "Nicolas", 2200.0)
s.augmenter(10)
assert s.salaire == 2420.0
assert s.to_dict() == {"id": 1, "nom": "Nicolas", "salaire": 2420.0}
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 10 : Grand Défi Synthèse — Pipeline de Traitement Itératif & JSON

### 🎯 Objectif
Intégrer l'ensemble des compétences : charger un flux JSON de salariés, instancier une collection d'objets `Salarie`, itérer pour filtrer les hauts salaires, calculer des statistiques globales (masse salariale, moyenne) et persister le rapport final dans un nouveau fichier JSON.

---

### 📝 Partie A : Travail Débranché (Sur Table)

#### Exercice 10.1 — Schéma synoptique du pipeline de données
Numérotez de 1 à 4 les étapes du traitement automatique des données :

* `[ ... ]` Écriture du rapport agrégé dans un fichier `rapport_entreprise.json` avec `json.dump()`.
* `[ ... ]` Ouverture et chargement du fichier source `employes_entree.json` avec `json.load()`.
* `[ ... ]` Conversion de chaque dictionnaire chargé en instance de la classe `Salarie`.
* `[ ... ]` Itération sur les instances : calcul de la somme des salaires, de la moyenne et sélection des salaires $\ge 2\,000\text{ €}$.

#### Exercice 10.2 — Remplissage de la table de trace du rapport
Soit une liste de 3 salariés :
* Alice : $1\,500.00\text{ €}$
* Bob : $4\,500.00\text{ €}$
* Nicolas : $2\,200.00\text{ €}$

Calculez manuellement sur votre feuille :
* **Effectif total** : `............`
* **Masse salariale totale** : `........................ €`
* **Salaire moyen** : `........................ €`
* **Nombre de salariés $\ge 2\,000\text{ €}$** : `............`
* **Noms des salariés sélectionnés** : `[ ........................................................ ]`

---

### 💻 Partie B : Application sur Machine (Python 3)

Dans [`api/exercices_fondamentaux.py`](file:///c:/Users/moham/.gemini/antigravity-ide/scratch/tp-python-flask-ciel/api/exercices_fondamentaux.py), implémentez la fonction globale de synthèse :
```python
def traiter_pipeline_salaries(chemin_json_entree: str, chemin_json_sortie: str) -> dict:
    """
    Lit le fichier JSON d'entrée, instancie les objets Salarie, calcule les statistiques
    (effectif, masse_salariale, moyenne, salaries_qualifies) et exporte le dictionnaire
    résultat dans le fichier JSON de sortie.
    """
    # TODO: À compléter
    pass
```

*Validation machine attendue :*
L'exécution de `docker compose exec api python exercices_fondamentaux.py` doit valider les 10 modules avec succès et afficher un résumé console complet.
