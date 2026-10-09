# 📝 BTS CIEL // Cahier d'Exercices Préparatoires Fondamentaux en Python
## *CORRECTION OFFICIELLE & GUIDE ENSEIGNANT*

> 📌 **Document de référence pour l'enseignant et correction détaillée des exercices.**  
> **Auteurs & Référence :** Inspiré du *« Cours de Python : Programmation Python pour les sciences de la vie »* (P. Fuchs & P. Poulain, Université Paris Cité) et adapté aux exigences du **BTS CIEL** (Informatique embarquée, Réseaux, Web, Traitement de données JSON et Objets).

---

### 🎯 Présentation et Méthodologie

Ce cahier regroupe les corrections complètes du cahier d'exercices fondamentaux. Pour chaque module :
1. **📝 Partie A (Débranché)** : Réponses complètes aux tableaux de prédiction, schémas mémoire et questions algorithmiques.
2. **💻 Partie B (Machine)** : Code Python 3 validé et testé, disponible dans [`api/exercices_fondamentaux.py`](api/exercices_fondamentaux.py).

---

## 📋 Sommaire de la Progression Pédagogique

| Module | Thème du Cours | Concepts Clés | Statut Correction |
| :---: | :--- | :--- | :---: |
| **M1** | **Variables, Types & Arithmétique** | Types primitifs (`int`, `float`, `str`, `bool`), affectation, casting, `//` et `%`. | ✅ Résolu |
| **M2** | **Affichage & f-strings** | `print()`, arguments `sep`/`end`, formatage `{:.2f}`, alignement (`<`, `>`, `^`). | ✅ Résolu |
| **M3** | **Listes, Slicing & Mémoire** | Indices positifs/négatifs, tranches `[::]`, mutabilité, copie par référence vs `list()`. | ✅ Résolu |
| **M4** | **Boucles `for`, `while` & Parcours** | Itération par élément vs par indice, `enumerate()`, accumulateurs, motifs 2D. | ✅ Résolu |
| **M5** | **Conditions & Tests Avancés** | `if/elif/else`, opérateurs `and`/`or`/`not`, imprécision des flottants (`isclose`). | ✅ Résolu |
| **M6** | **Fichiers & Sérialisation JSON** | `with open()`, lecture/écriture, syntaxe JSON stricte, `json.dump` / `load`. | ✅ Résolu |
| **M7** | **Dictionnaires & Tuples** | Tables d'association `{cle: val}`, `.items()`, `.get()`, unpacking, listes de dicts. | ✅ Résolu |
| **M8** | **Fonctions & Principe DRY** | `def`, paramètres par défaut, retours multiples (tuples), portée locale vs globale. | ✅ Résolu |
| **M9** | **Programmation Orientée Objet** | Classes, `__init__`, `self`, attributs d'instance, méthodes métier, `__str__`. | ✅ Résolu |
| **M10** | **Grand Défi Synthèse Intégrateur** | Chaîne complète : Fichier JSON $\to$ Objets $\to$ Itérations $\to$ Rapport JSON. | ✅ Résolu |

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 1 : Variables, Types, Conversions & Arithmétique (Ch. 2)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 1.1 — Prédire les types et les valeurs
| Instruction Python | Valeur Résultante | Type (`type()`) | Explication |
| :--- | :---: | :---: | :--- |
| `a = 19 // 4` | **`4`** | **`int`** | Division entière : quotient entier de $19 / 4$. |
| `b = 19 % 4` | **`3`** | **`int`** | Modulo : reste entier ($19 = 4 \times 4 + 3$). |
| `c = 19 / 4` | **`4.75`** | **`float`** | En Python 3, `/` produit toujours un `float`. |
| `d = "12" + "34"` | **`"1234"`** | **`str`** | Concaténation de deux chaînes. |
| `e = int("12") + float("3.5")` | **`15.5`** | **`float`** | Casting $12 + 3.5 = 15.5$. |
| `f = "CIEL " * 3` | **`"CIEL CIEL CIEL "`** | **`str`** | Duplication d'une chaîne par un entier. |
| `g = 2 ** 4` | **`16`** | **`int`** | Élévation à la puissance ($2^4 = 16$). |
| `h = 2.5e3` | **`2500.0`** | **`float`** | Notation scientifique $2.5 \times 10^3$, toujours `float`. |

#### Exercice 1.2 — Analyse d'erreur de conversion
1. Valeur de `total` : **`"15.515.515.515.5"`**  
2. Cause : `prix_unitaire` est une chaîne (`str`). L'opérateur `*` entre une chaîne et un entier duplique la chaîne 4 fois au lieu d'effectuer une multiplication arithmétique.  
3. Correction :
```python
total = float(prix_unitaire) * quantite  # vaut 62.0
```

#### Exercice 1.3 — Décomposition de temps (Division entière & Modulo)
* $H = \text{secondes } // 3600$ *(ex: $7385 // 3600 = 2\text{ h}$)*
* $\text{secondes\_restantes} = \text{secondes } \% 3600$ *(ex: $7385 \% 3600 = 185\text{ s}$)*
* $M = \text{secondes\_restantes } // 60$ *(ex: $185 // 60 = 3\text{ min}$)*
* $R = \text{secondes\_restantes } \% 60$ *(ex: $185 \% 60 = 5\text{ s}$)*

---

### 💻 Partie B : Solution Machine

```python
def decomposer_secondes(secondes: int) -> tuple[int, int, int]:
    """Prend un nombre entier de secondes et retourne (heures, minutes, secondes_restantes)."""
    heures = secondes // 3600
    secondes_restantes = secondes % 3600
    minutes = secondes_restantes // 60
    reste = secondes_restantes % 60
    return (heures, minutes, reste)
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 2 : Affichage, Formatage et f-strings (Ch. 3)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 2.1 — Comportement de `print()`
1. `print("192", "168", "1", "10", sep=".")`  
   *Affichage exact :* **`192.168.1.10`**
2. `print("Vitesse", end=" : ") ; print(100, "km/h")`  
   *Affichage exact :* **`Vitesse : 100 km/h`**

#### Exercice 2.2 — Spécifications de format dans les f-strings
| Expression f-string | Rendu texte exact | Description du formatage |
| :--- | :--- | :--- |
| `f"{taux:.2%}"` | **`19.65%`** | Pourcentage avec 2 décimales. |
| `f"{valeur:05d}"` | **`00042`** | Entier complété par des zéros sur 5 caractères. |
| `f"{libelle:>10s}"` | **`   Serveur`** | Cadré à droite sur 10 caractères (3 espaces + 7 lettres). |
| `f"{libelle:*^12s}"` | **`**Serveur***`** | Centré sur 12 caractères avec remplissage `*`. |
| `f"{1234567:.2e}"` | **`1.23e+06`** | Notation scientifique avec 2 décimales. |

#### Exercice 2.3 — Alignement d'un tableau de bord
```python
ligne_formatee = f"{hote:<15s} | {port:>6d} | {statut:^10s}"
```

---

### 💻 Partie B : Solution Machine

```python
def formater_ligne_service(hote: str, port: int, statut: str) -> str:
    """Retourne une chaîne formatée : hôte cadré à gauche (15c), port à droite (6c), statut centré (10c)."""
    return f"{hote:<15s} | {port:>6d} | {statut:^10s}"
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 3 : Listes, Indexation, Slicing & Gestion Mémoire (Ch. 4)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 3.1 — Découpage par tranches (*Slicing*)
Soit `ip = [192, 168, 10, 254, 80, 443, 22]` ($N=7$) :
1. `ip[0]` : **`192`** | `ip[-1]` : **`22`** | `ip[-3]` : **`80`**
2. `ip[0:4]` : **`[192, 168, 10, 254]`**
3. `ip[4:]` : **`[80, 443, 22]`**
4. `ip[::2]` : **`[192, 10, 80, 22]`** *(éléments aux indices 0, 2, 4, 6)*
5. `ip[::-1]` : **`[22, 443, 80, 254, 10, 168, 192]`** *(inversion complète)*

#### Exercice 3.2 — Le piège de la copie mémoire par référence
1. **Schéma mémoire :**
```text
[Espace des Noms]                       [Espace Mémoire]
    L1  -------------------+--------->    [ 99 , 20 , 30 ]  (Objet A modifié)
    L2  -------------------+
    L3  ----------------------------->    [ 10 , 20 , 30 ]  (Objet B distinct)
```
2. Valeurs après `L1[0] = 99` :
   * `L1` : **`[99, 20, 30]`**
   * `L2` : **`[99, 20, 30]`** *(copie par référence : pointe vers le même objet)*
   * `L3` : **`[10, 20, 30]`** *(copie défensive indépendante via `list()`)*
3. Vérification d'adresse mémoire : **`id(L1) == id(L2)`** ou l'opérateur d'identité **`L1 is L2`** (retourne `True`).

---

### 💻 Partie B : Solution Machine

```python
def dupliquer_sans_effet_de_bord(liste_source: list) -> list:
    """Retourne une copie superficielle indépendante de la liste passée en argument."""
    return list(liste_source)
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 4 : Boucles `for`, `while` & Parcours d'Itérables (Ch. 5)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 4.1 — Déroulement d'un accumulateur sur table
Soit `releves = [12, 18, 5, 25, 8]` :

| Tour | Variable `v` | Test `v >= 10` | Nouveau `cumul` | Nouveau `nb_depassements` |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 12 | VRAI | 12 | 1 |
| 2 | 18 | **VRAI** | **30** | **2** |
| 3 | 5 | **FAUX** | **30** | **2** |
| 4 | 25 | **VRAI** | **55** | **3** |
| 5 | 8 | **FAUX** | **55** | **3** |

#### Exercice 4.2 — Conception de motif géométrique simple
1. Pseudo-code :
```text
Procédure triangle(entier n)
    Pour i de 1 à n :
        Afficher i fois le caractère '*'
    Fin Pour
Fin Procédure
```
2. Opération concise : **`"*" * i`** *(duplication de chaîne par un entier)*.

---

### 💻 Partie B : Solution Machine

```python
def calculer_somme_et_moyenne(valeurs: list[float | int]) -> tuple[float, float]:
    """Calcule et renvoie la somme totale et la moyenne arithmétique avec une boucle for."""
    if not valeurs:
        return (0.0, 0.0)
    total = 0.0
    for v in valeurs:
        total += float(v)
    moyenne = total / len(valeurs)
    return (total, moyenne)

def generer_lignes_triangle(n: int) -> list[str]:
    """Génère la liste des n lignes du triangle rectangle d'étoiles."""
    return ["*" * i for i in range(1, n + 1)]
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 5 : Conditions, Tests Avancés & Précision des Floats (Ch. 6)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 5.1 — Tables de vérité et tests multiples
* `(10 > 5) and (3 == 4)` $\to$ **`False`** *(Vrai ET Faux = Faux)*
* `(10 > 5) or (3 == 4)` $\to$ **`True`** *(Vrai OU Faux = Vrai)*
* `not (7 in [1, 2, 3])` $\to$ **`True`** *(NON Faux = Vrai)*
* `(5 > 2) and not (4 < 1)` $\to$ **`True`** *(Vrai ET (NON Faux) = Vrai ET Vrai = Vrai)*

#### Exercice 5.2 — L'énigme des nombres flottants
1. **Explication :** La norme IEEE-754 code les nombres en virgule flottante en base 2 binaire. Les nombres $0.1$ et $0.2$ ont un développement binaire infini périodique et ne peuvent pas être représentés de manière exacte en mémoire. L'addition produit $0.30000000000000004$, qui est strictement différent de $0.3$.
2. **Formule en Python :** `abs(a - b) < 1e-5`
3. **Fonction `math` :** `math.isclose(a, b, abs_tol=1e-5)`

---

### 💻 Partie B : Solution Machine

```python
import math

def categoriser_valeur(valeur: float, seuil_bas: float, seuil_haut: float) -> str:
    """Retourne 'BAS', 'NORMAL', ou 'CRITIQUE' selon les seuils (inclut tolérance 1e-5)."""
    tol = 1e-5
    if math.isclose(valeur, seuil_bas, abs_tol=tol) or math.isclose(valeur, seuil_haut, abs_tol=tol):
        return "NORMAL"
    if valeur < seuil_bas:
        return "BAS"
    if valeur > seuil_haut:
        return "CRITIQUE"
    return "NORMAL"
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 6 : Fichiers Texte, Sérialisation & Données JSON (Ch. 7)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 6.1 — Correspondance stricte Python $\leftrightarrow$ JSON
| Concept | En Python | En JSON strict (RFC 8259) |
| :--- | :---: | :---: |
| Valeur booléenne vraie | `True` | **`true`** |
| Valeur booléenne fausse | `False` | **`false`** |
| Absence d'information | `None` | **`null`** |
| Encadrement des chaînes | `'texte'` ou `"texte"` | **`"texte"`** *(Guillemets doubles obligatoires)* |
| Virgule après dernier élément | Tolérée | **Interdite** *(Erreur de syntaxe JSON)* |

#### Exercice 6.2 — Détection d'erreurs dans un extrait JSON
1. **Anomalie 1 :** `'titre'` utilise des guillemets simples `''` au lieu de guillemets doubles `""`.
2. **Anomalie 2 :** `True` possède une majuscule (syntaxe Python) au lieu du littéral `true`.
3. **Anomalie 3 :** Virgule traînante après `"HTTP"` dans `["SSH", "HTTP", ]`.

#### Exercice 6.3 — Gestionnaire de contexte `with open`
L'instruction `with open(...)` assure la fermeture automatique et déterministe du fichier dès la sortie du bloc indenté, même si une exception (`IOError`, `ValueError`) est levée pendant la lecture ou l'écriture, empêchant tout blocage ou fuite de descripteur système.

---

### 💻 Partie B : Solution Machine

```python
import json

def sauvegarder_donnees_json(chemin_fichier: str, donnees: list | dict) -> None:
    """Enregistre l'objet Python dans un fichier JSON avec indent=4 et encodage utf-8."""
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

def charger_donnees_json(chemin_fichier: str) -> list | dict:
    """Charge et retourne les données d'un fichier JSON."""
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return json.load(f)
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 7 : Dictionnaires, Tuples & Modélisation de Données (Ch. 8)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 7.1 — Traçage de dictionnaire
1. `equipement["nom"]` retourne **`"Passerelle"`**.
2. `equipement["vitesse"]` déclenche une exception **`KeyError: 'vitesse'`** (car la clé n'existe pas).
3. Méthode sécurisée : **`equipement.get("vitesse", 1000)`** (retourne `1000` sans planter).

#### Exercice 7.2 — Désempaquetage de Tuples (*Unpacking*)
```python
for nom, port in services:
    print(f"Service {nom} sur le port {port}")
```

#### Exercice 7.3 — Modélisation : Liste de Dictionnaires
```python
salaries = [
    { "nom": "Alice", "salaire": 1500.0 },
    { "nom": "Bob",   "salaire": 4500.0 }
]
```

---

### 💻 Partie B : Solution Machine

```python
def compter_frequences_elements(elements: list[str]) -> dict[str, int]:
    """Compte et retourne le nombre d'occurrences de chaque chaîne dans un dictionnaire."""
    frequences: dict[str, int] = {}
    for elt in elements:
        frequences[elt] = frequences.get(elt, 0) + 1
    return frequences
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 8 : Fonctions, Modularité, Paramètres & Portée (Ch. 10)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 8.1 — Analyse de la portée des variables (*Scope*)
1. *Affichage 1 :* **`Session ouverte pour Bob (n°1)`**
2. *Affichage 2 :* **`100`**
3. *Explication :* En vertu de la règle LGI (Local, Global, Interne), l'assignation `compteur = 1` à l'intérieur de `initialiser_session()` crée une variable **locale** propre à la fonction. La variable globale `compteur` du programme principal reste intacte à `100`.

#### Exercice 8.2 — Fonctions à retours multiples
En séparant les valeurs de retour par des virgules (`return mini, maxi`), Python les regroupe automatiquement dans un **tuple** `(mini, maxi)`. L'appelant peut ensuite désempaqueter le tuple à la volée : `val_min, val_max = ma_fonction(...)`.

---

### 💻 Partie B : Solution Machine

```python
def calculer_extremums_et_etendue(valeurs: list[float | int]) -> tuple[float, float, float]:
    """Retourne un tuple (minimum, maximum, etendue) où etendue = maximum - minimum."""
    if not valeurs:
        return (0.0, 0.0, 0.0)
    mini = float(min(valeurs))
    maxi = float(max(valeurs))
    return (mini, maxi, maxi - mini)
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 9 : Programmation Orientée Objet — Classes & Instances (Ch. 23)

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 9.1 — Le rôle fondamental de `self`
1. Le paramètre `self` représente l'instance d'objet sur laquelle la méthode est exécutée (son adresse/référence mémoire).
2. `self.salaire` est un attribut d'instance persistant dans l'objet et accessible par toutes les méthodes de la classe, alors qu'une variable `salaire` sans `self.` est une variable locale éphémère qui disparaît dès la fin de l'exécution de la méthode.

#### Exercice 9.2 — Conception de la classe `Salarie`
```python
class Salarie:
    def __init__(self, identifiant: int, nom: str, salaire: float):
        self.id = identifiant
        self.nom = nom
        self.salaire = float(salaire)

    def augmenter(self, pourcentage: float) -> None:
        """Augmente le salaire de pourcentage % (ex: 10 pour +10%)."""
        self.salaire = round(self.salaire * (1.0 + (pourcentage / 100.0)), 2)

    def to_dict(self) -> dict:
        """Convertit l'instance en dictionnaire standard pour export JSON."""
        return {
            "id": self.id,
            "nom": self.nom,
            "salaire": self.salaire
        }

    def __str__(self) -> str:
        """Représentation textuelle de l'objet pour print()."""
        return f"[{self.id}] {self.nom} : {self.salaire:.2f} €"
```

---

### 💻 Partie B : Solution Machine

```python
class Salarie:
    def __init__(self, identifiant: int, nom: str, salaire: float) -> None:
        self.id = int(identifiant)
        self.nom = str(nom)
        self.salaire = float(salaire)

    def augmenter(self, pourcentage: float) -> None:
        self.salaire = round(self.salaire * (1.0 + (pourcentage / 100.0)), 2)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "nom": self.nom,
            "salaire": self.salaire
        }

    def __str__(self) -> str:
        return f"[{self.id}] {self.nom} : {self.salaire:.2f} €"
```

---

<!-- PAGE BREAK -->
<div style="page-break-after: always;"></div>

## Module 10 : Grand Défi Synthèse — Pipeline de Traitement Itératif & JSON

### 📝 Partie A : Correction du Travail Débranché

#### Exercice 10.1 — Schéma synoptique du pipeline de données
* `[ 4 ]` Écriture du rapport agrégé dans un fichier `rapport_entreprise.json` avec `json.dump()`.
* `[ 1 ]` Ouverture et chargement du fichier source `employes_entree.json` avec `json.load()`.
* `[ 2 ]` Conversion de chaque dictionnaire chargé en instance de la classe `Salarie`.
* `[ 3 ]` Itération sur les instances : calcul de la somme des salaires, de la moyenne et sélection des salaires $\ge 2\,000\text{ €}$.

#### Exercice 10.2 — Remplissage de la table de trace du rapport
* **Effectif total** : **`3`**
* **Masse salariale totale** : $1\,500 + 4\,500 + 2\,200 =$ **`8 200.00 €`**
* **Salaire moyen** : $8\,200 / 3 \approx$ **`2 733.33 €`**
* **Nombre de salariés $\ge 2\,000\text{ €}$** : **`2`** *(Bob et Nicolas)*
* **Noms des salariés sélectionnés** : **`["Bob", "Nicolas"]`**

---

### 💻 Partie B : Solution Machine

```python
def traiter_pipeline_salaries(chemin_json_entree: str, chemin_json_sortie: str) -> dict[str, Any]:
    """Lit le JSON, instancie les Salarie, itère, calcule les stats et exporte le rapport JSON."""
    donnees_brutes = charger_donnees_json(chemin_json_entree)
    
    # Instanciation de la collection d'objets
    salaries = [Salarie(d["id"], d["nom"], d["salaire"]) for d in donnees_brutes]
    
    effectif = len(salaries)
    masse = 0.0
    qualifies = []
    
    # Itération métier
    for s in salaries:
        masse += s.salaire
        if s.salaire >= 2000.0:
            qualifies.append(s.to_dict())
            
    moyenne = round(masse / effectif, 2) if effectif > 0 else 0.0
    masse = round(masse, 2)
    
    rapport = {
        "effectif_total": effectif,
        "masse_salariale": masse,
        "salaire_moyen": moyenne,
        "seuil_qualification": 2000.0,
        "salaries_qualifies": qualifies
    }
    
    sauvegarder_donnees_json(chemin_json_sortie, rapport)
    return rapport
```
