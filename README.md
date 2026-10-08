# BTS CIEL // Algorithmique, Python & API REST avec Flask

Bienvenue dans ce cycle de travaux pratiques dédié à l'apprentissage de **Python 3**, des algorithmes statistiques et au développement d'une **API REST avec Flask** adossée à une base de données **MySQL**.

---

## 🛠️ Démarrage rapide de l'environnement

Le projet s'exécute dans une architecture de conteneurs Docker (Nginx, Python 3.12 Flask, MySQL 8.0) :

```bash
# 1. Lancement de la pile Docker
docker compose up -d

# 2. Vérifier que les conteneurs sont actifs
docker compose ps

# 3. Exécuter vos scripts console dans le conteneur Python
docker compose exec api python main.py

# 4. Accéder à l'interface web de test
# Ouvrez votre navigateur sur : http://localhost
```

---

## 📋 Progression des exercices

### Séquence Préparatoire : Des Fondations de Python au Seuil de l'API Flask

Cette séquence préparatoire amène tout étudiant (même débutant complet) de zéro en Python jusqu'au seuil de l'**Activité Finale** (API Flask adossée à MySQL avec interface web `fetch`).

Elle repose sur :
1. **Un apprentissage intensif des fondamentaux** : boucles, motifs géométriques, chaînes, slicing approfondi, parcours de listes, dictionnaires et listes de dictionnaires.
2. **Un travail sur table débranché systématique (15 min)** en tout début de chaque séance pour poser les concepts (schémas mémoire, tableaux de trace, trames HTTP) avant de coder sur machine.
3. **Le tri par sélection impératif obligatoire (sans `sorted()`)** pour comprendre physiquement la mutabilité et la référence mémoire avant de calculer la médiane et de l'exposer en API.
4. **Un fil rouge unique** : le même jeu de données des 9 salariés de l'entreprise (dont Nicolas).

---

#### 🧵 Le Fil Rouge : Les 9 Salariés de l'Entreprise
* **Alice** : 1 500 € | **Bob** : 4 500 € | **Nicolas** : 2 200 €
* **Chloé** : 1 500 € | **David** : 3 300 € | **Emma** : 1 800 €
* **Frank** : 1 700 € | **Grace** : 2 000 € | **Henri** : 4 000 €

---

#### 📊 Tableau de synthèse de la séquence préparatoire

| Séance | Durée | Objectif (« L'étudiant est capable de… ») | Notions clés | Production attendue |
| :---: | :---: | :--- | :--- | :--- |
| **S1** | 2 h | Structurer et manipuler des données d'employés en mémoire. | Types primitifs (`int`, `str`, `float`), listes `[]`, dictionnaires `{}`, listes de dictionnaires, boucle `for`, conditions `if`. | `employes.py` : création des 9 salariés, filtrage des salaires $> 2\,000\text{ €}$. |
| **S2** | 2 h | Coder le tri par sélection impératif (Valeur vs Référence) et calculer la médiane (**Activité 0.7**). | Pseudo-code officiel, boucles imbriquées, permutation `t[i], t[min] = t[min], t[i]`, mutabilité (`list(t)`), calcul de médiane **sans `sorted()`**. | `tri_selection.py`, `read_tab.py`, `statistique.py` : tri par sélection et résolution du cas de Nicolas. |
| **S3** | 2 h | Sérialiser et désérialiser des données en JSON avec gestion d'erreurs. | Module `json` (`load`, `dump`), gestion de fichier (`with open`), exceptions (`try / except`, `FileNotFoundError`). | `gestion_json.py` : persistance de `employes.json` et gestion des cas d'erreur sans crash. |
| **S4** | 2 h | Interroger MySQL de façon sécurisée et convertir les résultats. | Connecteur MySQL (`pymysql`), curseur dictionnaire (`DictCursor`), requêtes paramétrées (`%s`), variables d'environnement. | `bdd.py` : extraction sécurisée des employés et salaires depuis la base `CRUD`. |
| **S5** | 2 h | Créer une API REST avec Flask et tester ses routes sous Postman. | Instance Flask, décorateur `@app.route`, méthodes HTTP (`GET`), `jsonify()`, codes HTTP (`200`, `404`), CORS, Postman. | `app.py` : serveur API exposant `/api/employes` et `/api/employes/<id>` validé avec Postman. |
| **S6** | 2 h | Filtrer via paramètres d'URL et afficher dans le DOM via `fetch()`. | Paramètres de requête (`request.args`), requête asynchrone JS (`fetch`), injection DOM (`innerHTML`, `textContent`). | `index.html` : interface web interrogeant l'API et affichant dynamiquement la médiane et les filtres. |

---

### 🟢 Partie 0 : Prise en main Fondamentale de Python (Les Bases Concrètes)

Avant d'aborder la programmation web et les bases de données, cette partie introductive pose les gammes indispensables du langage Python. **Chaque exercice sur machine est systématiquement précédé d'un exercice écrit sur table**, vous permettant de poser le problème, tracer les variables et concevoir le pseudo-code avant de toucher au clavier.

---

#### 1. Fiche Essentielle : Le pont JavaScript $\leftrightarrow$ Python & les Patrons de Base

Pour un étudiant venant du développement web (JavaScript / HTML), les équivalences sont immédiates :

| Concept | En JavaScript | En Python (Strict équivalent) |
| :--- | :--- | :--- |
| **Affichage console** | `console.log("Bonjour");` | `print("Bonjour")` |
| **Ajout en fin de tableau** | `tableau.push(element);` | **`liste.append(element)`** *(capital !)* |
| **Taille / Longueur** | `tableau.length` ou `chaine.length` | `len(liste)` ou `len(chaine)` |
| **Objet / Dictionnaire** | `{ nom: "Alice", age: 20 }` | `{"nom": "Alice", "age": 20}` |
| **Parcours par élément** | `for (const x of liste) { ... }` | `for x in liste:` |
| **Parcours par indice** | `for (let i = 0; i < tab.length; i++)` | `for i in range(len(liste)):` |

```python
# PATRON 1 : Parcours direct par élément
for val in salaires:
    print(val)

# PATRON 2 : Parcours par indice (pour modifier une liste en place)
for i in range(len(salaires)):
    salaires[i] = salaires[i] + 100

# PATRON 3 : Accumulateur avec .append() (l'analogue strict de .push() en JS)
selection = []
for val in salaires:
    if val >= 2000:
        selection.append(val)

# PATRON 4 : Parcours dictionnaire clés et valeurs
for cle, val in fiche_emp.items():
    print(f"{cle} => {val}")

# PATRON 5 : Parcours d'une liste de dictionnaires (le format JSON et SQL)
for emp in liste_employes:
    print(f"{emp['nom']} gagne {emp['salaire']} €")
```

---

#### 2. Les Exercices Fondamentaux d'Algorithmique & Structures de Données

---

* **Exercice 0.1 : Indice du minimum d'une liste (Recherche d'extremum)**
  * **Énoncé** : Écrire une fonction prenant en entrée une liste et qui retourne l'indice où se trouve son minimum.  
    *Exemple* : Pour `L = [15, 3, 22, 8]`, la fonction retourne `1` (car le minimum 3 est à l'indice 1).
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Déroulez manuellement l'algorithme sur la liste $L = [15, 3, 22, 8]$ :
    >    | Indice $i$ | Valeur $L[i]$ | Indice $min\_idx$ avant test | Test $L[i] < L[min\_idx]$ | Action sur $min\_idx$ | Nouveau $min\_idx$ |
    >    | :---: | :---: | :---: | :---: | :--- | :---: |
    >    | 0 | 15 | 0 | Initialisation | - | 0 |
    >    | 1 | 3 | 0 | $3 < 15$ (VRAI) | $min\_idx \leftarrow 1$ | 1 |
    >    | 2 | 22 | 1 | $22 < 3$ (FAUX) | Aucun changement | 1 |
    >    | 3 | 8 | 1 | `____________________` | `____________________` | `____` |
    > 2. Complétez le pseudo-code officiel :
    >    ```text
    >    fonction indice_minimum(L : liste) -> entier
    >        min_idx ← 0
    >        pour i de 1 à longueur(L) - 1 :
    >            si L[i] < L[min_idx] alors :
    >                min_idx ← ____________
    >        retourner min_idx
    >    fin fonction
    >    ```
    > 3. Si le minimum apparaît plusieurs fois (ex: `[7, 3, 9, 3]`), quel indice votre fonction retourne-t-elle ? Pourquoi ?  
    >    *Réponse :* `____________________________________________________________________`
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez la fonction `indice_minimum(L)`. Testez avec `python api/intro_base.py`.

---

* **Exercice 0.2 : Somme des entiers de 1 à n (Itératif vs Récursif)**
  * **Énoncé** : Écrire une fonction calculant la somme des entiers de $1$ à $n$ ($1 + 2 + \dots + n$) de deux manières :
    1. Version itérative `somme_iterative(n)` utilisant une boucle `for` ;
    2. Version récursive `somme_recursive(n)` utilisant la relation $somme(n) = n + somme(n - 1)$.
    * *Exemple* : Pour $n = 5$, les deux fonctions retournent `15` ($1+2+3+4+5=15$).
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Déroulez l'arbre des appels récursifs pour $n = 4$ :
    >    ```text
    >    somme(4) = 4 + somme(3)
    >             = 4 + (3 + somme(2))
    >             = 4 + (3 + (2 + somme(1)))
    >             = 4 + 3 + 2 + 1 = 10
    >    ```
    > 2. Identifiez les deux éléments fondamentaux de la récursivité :
    >    * **Cas de base (ou d'arrêt)** : Si $n \le 0$ (ou $n == 1$), la fonction retourne immédiatement $0$ (ou $1$) sans nouvel appel récursif.
    >    * **Cas récursif** : Pour $n > 1$, la fonction s'appelle elle-même avec un argument strictement décroissant : $n + \text{somme}(n - 1)$.
    > 3. Que se passerait-il en Python si l'on oubliait le cas de base ?  
    >    *Réponse :* Une boucle récursive infinie provoquant l'exception `RecursionError: maximum recursion depth exceeded`.
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `somme_iterative(n)` et `somme_recursive(n)`. Testez avec $n = 5$.

---

* **Exercice 0.3 : Puissance $x^n$ (Itératif vs Récursif — Exercice simple de même type)**
  * **Énoncé** : Écrire une fonction calculant $x^n$ ($x$ élevé à la puissance $n \ge 0$) de deux manières :
    1. Version itérative `puissance_iterative(x, n)` avec une boucle `for` ;
    2. Version récursive `puissance_recursive(x, n)` utilisant la relation $x^n = x \times x^{n-1}$.
    * *Exemple* : Pour $x = 2$ et $n = 4$, les deux fonctions retournent `16` ($2 \times 2 \times 2 \times 2 = 16$).
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Déroulez l'arbre des appels pour $x = 2$ et $n = 3$ ($2^3$) :
    >    ```text
    >    puissance(2, 3) = 2 * puissance(2, 2)
    >                    = 2 * (2 * puissance(2, 1))
    >                    = 2 * (2 * (2 * puissance(2, 0)))
    >                    = 2 * 2 * 2 * 1 = 8
    >    ```
    > 2. Définissez le cas de base :  
    >    *Cas d'arrêt :* Pour $n = 0$, $x^0 = 1$ $\rightarrow$ retourner `1`.
    > 3. Complétez le pseudo-code :
    >    ```text
    >    fonction puissance_recursive(x, n)
    >        si n == 0 alors :
    >            retourner 1
    >        sinon :
    >            retourner x * puissance_recursive(x, n - 1)
    >    fin fonction
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `puissance_iterative(x, n)` et `puissance_recursive(x, n)`. Testez avec $x = 2, n = 4$.

---

* **Exercice 0.4 : Taille totale d'une liste de listes**
  * **Énoncé** : Écrire une fonction prenant en entrée une liste de listes $L$ contenant des nombres et qui retourne la taille totale (nombre total d'éléments) de la liste $L$.  
    *Exemple* : La fonction retourne `7` pour la liste de listes `[[2, 5, 4], [3, 6], [4], [2]]`.
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Schématisez la liste de listes en mémoire (un tableau principal pointant vers 4 sous-listes) :
    >    ```text
    >    L -> [ [0] -> [2, 5, 4]  (taille 3)
    >           [1] -> [3, 6]     (taille 2)
    >           [2] -> [4]        (taille 1)
    >           [3] -> [2]        (taille 1) ]
    >    ```
    > 2. Tableau de trace du cumul :
    >    | Indice $k$ | Sous-liste | `len(sous_liste)` | Total cumulé |
    >    | :---: | :---: | :---: | :---: |
    >    | 0 | `[2, 5, 4]` | 3 | 3 |
    >    | 1 | `[3, 6]` | 2 | 5 |
    >    | 2 | `[4]` | 1 | 6 |
    >    | 3 | `[2]` | 1 | 7 |
    > 3. Pseudo-code officiel :
    >    ```text
    >    total ← 0
    >    Pour chaque sous_liste dans L :
    >        total ← total + longueur(sous_liste)
    >    Retourner total
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `taille_totale(L)`. Validez avec `assert taille_totale([[2, 5, 4], [3, 6], [4], [2]]) == 7`.

---

* **Exercice 0.5 : Somme et Maximum d'une liste de listes**
  * **Énoncé** :
    1. Écrire une fonction prenant en entrée une liste de listes $L$ contenant des nombres et qui retourne la somme de tous les nombres dans toutes les listes de $L$.  
       *Exemple* : Retourne `26` pour `[[2, 5, 4], [3, 6], [4], [2]]`.
    2. Écrire une fonction prenant en entrée une liste de listes $L$ contenant des nombres et qui retourne le plus grand nombre figurant dans $L$, sans le localiser.  
       *Exemple* : Retourne `6` pour `[[2, 5, 4], [3, 6], [4], [2]]`.
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Déroulez le calcul de la somme sur feuille :  
    >    $\text{Somme} = (2 + 5 + 4) + (3 + 6) + (4) + (2) = 11 + 9 + 4 + 2 = 26$.
    > 2. Pourquoi ne faut-il jamais initialiser `max_val = 0` ?  
    >    *Réponse :* Si la liste ne contient que des valeurs négatives (ex: `[[-5], [-2]]`), 0 donnerait un résultat erroné. Il faut initialiser au premier élément ou à `None`.
    > 3. Pseudo-code :
    >    ```text
    >    max_val ← None
    >    Pour chaque sous_liste dans L :
    >        Pour chaque val dans sous_liste :
    >            Si max_val est None ou val > max_val alors :
    >                max_val ← val
    >    Retourner max_val
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `somme_liste_de_listes(L)` et `maximum_liste_de_listes(L)`.

---

* **Exercice 0.6 : Création de Matrice 2D Régulière & Inversion Binaire**
  * **Énoncé** :
    1. Écrire une fonction `creer_matrice(nb_lignes, nb_colonnes, valeur_defaut=0)` qui crée une matrice $N \times P$ avec des lignes indépendantes construites avec `.append()`.
    2. Écrire une fonction `inverser_matrice_binaire(M)` qui prend une matrice de 0 et de 1 et retourne une nouvelle matrice où chaque 0 devient 1 et chaque 1 devient 0.
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. *Piège de la référence partagée en Python* :  
    >    Pourquoi `M = [[0] * 4] * 3` est-il interdit ?  
    >    *Réponse :* Les 3 lignes partagent la même adresse mémoire physique. Modifier `M[1][2] = 9` modifie les 3 lignes simultanément.
    > 2. Coordonnées dans la matrice :  
    >    `M[1][2]` désigne la ligne 1 (2e ligne) et la colonne 2 (3e colonne) en base 0.
    > 3. Inversion de `M = [[0, 1, 0], [1, 1, 0]]` :  
    >    *Résultat attendu :* `[[1, 0, 1], [0, 0, 1]]`.
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `creer_matrice(nb_lignes, nb_colonnes, valeur_defaut)` et `inverser_matrice_binaire(M)`.

---

* **Exercice 0.7 : Produit cartésien de deux listes (Génération de couples)**
  * **Énoncé** : Écrire une fonction prenant en entrée deux listes et qui retourne la liste de tous les couples formés d'un élément de la première liste et d'un élément de la deuxième liste.  
    *Exemple* : Pour `L1 = [0, 1]` et `L2 = [1, 4]`, la fonction retourne `[(0, 1), (0, 4), (1, 1), (1, 4)]`.
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Tableau cartésien pour $L_1 = [0, 1]$ et $L_2 = [1, 4]$ :
    >    | $a \in L_1 \backslash b \in L_2$ | **1** | **4** |
    >    | :---: | :---: | :---: |
    >    | **0** | `(0, 1)` | `(0, 4)` |
    >    | **1** | `(1, 1)` | `(1, 4)` |
    > 2. Cardinalité : Si $|L_1| = n$ et $|L_2| = p$, le résultat contient $n \times p$ couples.
    > 3. Pseudo-code avec double boucle :
    >    ```text
    >    couples ← []
    >    Pour chaque a dans L1 :
    >        Pour chaque b dans L2 :
    >            couples.append((a, b))
    >    Retourner couples
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `produit_cartesien(L1, L2)`.

---

* **Exercice 0.8 : Réorganisation ordonnée de couples selon un pivot (Permutation)**
  * **Énoncé** : Écrire une fonction prenant en entrée une liste `l` de couples et un indice `i` entre 0 (inclus) et la taille de `l` (exclue) et qui retourne une liste formant une permutation de la liste `l`, selon la règle suivante :
    1. D'abord on met le couple à l'indice `i` ;
    2. Puis les couples dans la liste dont le premier élément est égal à celui à l'indice `i` dans l'ordre dans lequel ils figurent dans `l` ;
    3. Puis tous les autres couples de `l` en préservant également leur ordre.  
    *Exemple* : Pour `l = [(2, 3), (1, 0), (2, 1), (3, 5), (3, 4), (3, 0), (2, 5)]` et `i = 4`, la fonction retourne :  
    `[(3, 4), (3, 5), (3, 0), (2, 3), (1, 0), (2, 1), (2, 5)]`.
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Pivot à l'indice $i = 4$ : `l[4] = (3, 4)`. Sa clé est `3`.
    > 2. Partition des couples restants :
    >    * Couples avec clé 3 : `[(3, 5), (3, 0)]`.
    >    * Autres couples : `[(2, 3), (1, 0), (2, 1), (2, 5)]`.
    > 3. Concaténation finale ordonnée :  
    >    `[(3, 4)] + [(3, 5), (3, 0)] + [(2, 3), (1, 0), (2, 1), (2, 5)]`.
    > 4. Pseudo-code :
    >    ```text
    >    pivot ← l[i]
    >    cle ← pivot[0]
    >    meme_cle ← [] ; autres ← []
    >    Pour k de 0 à longueur(l) - 1 :
    >        Si k ≠ i alors :
    >            Si l[k][0] == cle alors meme_cle.append(l[k])
    >            Sinon : autres.append(l[k])
    >    Retourner [pivot] + meme_cle + autres
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `reorganiser_couples(l, i)`.

---

* **Exercice 0.9 : Triangle d'étoiles simple (Boucle & Affichage console)**
  * **Énoncé** : Écrire une fonction `afficher_triangle_simple(n)` prenant en entrée un entier naturel $n \ge 1$ et imprimant un triangle rectangle simple de hauteur $n$.  
    Chaque ligne $i$ (pour $i$ allant de $1$ à $n$) contient exactement $i$ étoiles.  
    *Exemple pour $n = 4$* :
    ```text
    *
    **
    ***
    ****
    ```
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > 1. Remplissez le tableau de trace pour $n = 4$ :
    >    | Ligne $i$ | Nombre d'étoiles | Rendu console attendu |
    >    | :---: | :---: | :--- |
    >    | 1 | 1 | `*` |
    >    | 2 | 2 | `**` |
    >    | 3 | 3 | `***` |
    >    | 4 | 4 | `****` |
    > 2. Pseudo-code de la procédure :
    >    ```text
    >    procédure triangle_simple(entier n)
    >        pour i de 1 à n :
    >            afficher i fois le caractère '*'
    >    fin procédure
    >    ```
    > 3. En Python, quelle opération concise sur chaîne permet d'afficher $i$ étoiles sans boucle interne ?  
    >    *Réponse :* `print("*" * i)`.
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez `afficher_triangle_simple(n)`. Testez avec $n = 4$.

---

* **Exercice 0.10 : Objets & Dictionnaires (`dict`) & Statistiques de promotion**
  * **Énoncé** :
    1. Écrire `creer_fiche_etudiant(nom, note, age=None)` retournant un dictionnaire `{"nom": nom, "note": note, "age": age}`.
    2. Écrire `modifier_note(fiche, nouvelle_note)` qui modifie la note directement en mémoire.
    3. Écrire `statistiques_promo(etudiants)` prenant une liste de fiches d'étudiants et retournant un dictionnaire :
       `{"effectif": ..., "moyenne": ..., "note_max": ..., "admis": [...]}` (admis : note $\ge 10.0$).
  * **📝 Étape 1 : Travail sur table préalable (Débranché)** :
    > ✍️ **Cadre de réponse écrite (Travail sur table) :**
    > 
    > Soit la liste de 4 fiches d'étudiants :
    > ```python
    > promo = [
    >     {"nom": "Alice", "note": 14.5},
    >     {"nom": "Bob", "note": 8.0},
    >     {"nom": "Nicolas", "note": 15.0},
    >     {"nom": "Chloé", "note": 9.5}
    > ]
    > ```
    > 1. Calculez les résultats statistiques attendus sur feuille :
    >    * Effectif = `4`
    >    * Somme des notes = $14.5 + 8.0 + 15.0 + 9.5 = 47.0$ $\rightarrow$ Moyenne = $47.0 / 4 = 11.75$
    >    * Note maximale = `15.0`
    >    * Liste des admis (note $\ge 10.0$) : `["Alice", "Nicolas"]`.
    > 2. Pseudo-code pour le calcul et le filtrage :
    >    ```text
    >    admis ← []
    >    total ← 0.0
    >    Pour chaque e dans promo :
    >        total ← total + e["note"]
    >        Si e["note"] >= 10.0 alors :
    >            admis.append(e["nom"])
    >    moyenne ← total / longueur(promo)
    >    ```
  * **💻 Étape 2 : Implémentation sur machine** :  
    Dans `api/intro_base.py`, codez les fonctions associées. Validez avec la promotion de test.

---

### 📍 DÉTAIL DES 6 SÉANCES DE COURS & TP

---

#### 📍 SÉANCE 1 : Fondations Python & Structures de Données (2 h)

* **Objectif** : L'étudiant est capable de modéliser des employés sous forme de liste de dictionnaires en mémoire, de la parcourir avec une boucle `for`, et d'en extraire des données par filtrage conditionnel (`if`).

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Schéma mémoire d'une liste de dictionnaires* :  
  >    Dessinez sur feuille la structure de la variable `employes` de 3 salariés (Alice 1500, Bob 4500, Nicolas 2200).  
  >    ```text
  >    employes (liste) -> [ [0] -> {"id": 1, "nom": "Alice",   "salaire": 1500},
  >                          [1] -> {"id": 2, "nom": "Bob",     "salaire": 4500},
  >                          [2] -> {"id": 3, "nom": "Nicolas", "salaire": 2200} ]
  >    ```
  > 2. *Accès direct à une propriété imbriquée* :  
  >    Écrivez l'expression Python accédant au salaire de Bob :  
  >    *Réponse :* `employes[______][______]` *(donne 4500)*.
  > 3. *Tableau de trace de la boucle de calcul et filtrage* :  
  >    Remplissez le tableau pour la boucle calculant la masse salariale (`total += emp["salaire"]`) et testant `emp["salaire"] > 2000` :
  >    | Tour | Salarié | Salaire | Total cumulé | Condition `> 2000` | Affichage produit |
  >    | :---: | :---: | :---: | :---: | :---: | :--- |
  >    | 1 | Alice | 1500 | 1500 | FAUX | Aucun |
  >    | 2 | Bob | 4500 | 6000 | VRAI | `"Haut salaire : Bob (4500 €)"` |
  >    | 3 | Nicolas | 2200 | `____` | `____` | `"______________________________"` |

* **Exemple de code de cours (14 lignes)** :
  ```python
  employes = [
      {"id": 1, "nom": "Alice", "salaire": 1500},
      {"id": 2, "nom": "Bob", "salaire": 4500}
  ]
  total = 0
  for emp in employes:
      total += emp["salaire"]
      if emp["salaire"] > 2000:
          print(f"Haut salaire : {emp['nom']} ({emp['salaire']} €)")
  print(f"Masse salariale totale : {total} €")
  ```

* **Exercices sur machine** :
  * *1.1 (Guidé)* : Dans `employes.py`, complétez la liste avec Nicolas (2200) et Chloé (1500). Affichez chaque salarié.
  * *1.2 (Semi-guidé)* : Définissez les 9 salariés. Utilisez un accumulateur `.append()` pour extraire dans `bas_salaires` ceux qui gagnent $< 2\,000\text{ €}$.
  * *1.3 (Autonome)* : Demandez un nom avec `input()`, parcourez la liste (insensible à la casse avec `.lower()`) et affichez la fiche complète ou `"Employé introuvable"`.

* **Critère de validation** : Le script affiche exactement 4 employés ayant un salaire $< 2\,000\text{ €}$ (Alice, Chloé, Emma, Frank).

---

#### 📍 SÉANCE 2 : Tri par Sélection (Valeur vs Référence) & Médiane (2 h)

* **Objectif** : L'étudiant est capable de transcrire le pseudo-code officiel du tri par sélection en Python, de différencier le passage par référence (en place) du passage par valeur (copie défensive), et de calculer la médiane d'une série ordonnée **sans utiliser les fonctions natives `sorted()` ou `.sort()`**.

* **📺 Vidéo support de l'algorithme** :  
  👉 [Visualiser l'animation et le principe du Tri par Sélection](https://youtu.be/8u3Yq-5DTN8?si=749n7xBfh2mbJTXS) *(Observez comment le plus petit élément restant est recherché puis permuté avec l'élément courant)*.

* **Pseudo-code officiel imposé** :
  ```text
  procédure tri_selection(tableau t)
      n ← longueur(t)
      pour i de 0 à n - 2
          min ← i
          pour j de i + 1 à n - 1
              si t[j] < t[min], alors min ← j
          fin pour
          si min ≠ i, alors échanger t[i] et t[min]
      fin pour
  fin procédure
  ```

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Tableau de trace complet du Tri par Sélection sur $t = [15, 3, 8]$ ($n = 3$)* :
  >    | Étape $i$ | Indice $min$ initial | Indice $j$ | Comparaison $t[j] < t[min]$ | Nouveau $min$ | Échange $t[i] \leftrightarrow t[min]$ | État du tableau $t$ |
  >    | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  >    | 0 | 0 ($t[0]=15$) | 1 | $3 < 15$ (VRAI) | 1 | - | - |
  >    | 0 | 1 ($t[1]=3$) | 2 | $8 < 3$ (FAUX) | 1 | $t[0] \leftrightarrow t[1]$ | `[3, 15, 8]` |
  >    | 1 | 1 ($t[1]=15$) | 2 | $8 < 15$ (VRAI) | 2 | $t[1] \leftrightarrow t[2]$ | `[3, 8, 15]` |
  > 2. *Schéma mémoire : Passage par Référence vs Copie Défensive* :
  >    * Si `b = t` : `id(b) == id(t)`. `b` et `t` partagent le même emplacement. Modifier `b[0]` modifie aussi `t[0]`.
  >    * Si `b = list(t)` : `id(b) != id(t)`. Un clone distinct est créé. `t` reste strictement intact.
  > 3. *Formule d'indice de la médiane sur série triée de taille $N$* :
  >    * Si $N$ est impair ($N=9$) : `indice = N // 2` *(indice 4, soit le 5e élément)*.
  >    * Si $N$ est pair ($N=8$) : `mediane = (t[N // 2 - 1] + t[N // 2]) / 2` *(moyenne des indices 3 et 4)*.

* **Exemple de code de cours (18 lignes)** :
  ```python
  def permuter(t: list, i: int, j: int) -> None:
      t[i], t[j] = t[j], t[i]

  def tri_selection_en_place(t: list) -> None:
      n = len(t)
      for i in range(n - 1):
          min_idx = i
          for j in range(i + 1, n):
              if t[j] < t[min_idx]:
                  min_idx = j
          if min_idx != i:
              permuter(t, i, min_idx)

  salaires = [2200, 1500, 4500]
  tri_selection_en_place(salaires)
  print("Salaires modifiés en mémoire :", salaires)
  ```

* **Exercices sur machine** :
  * *2.1 (Guidé)* : Dans `api/tri_selection.py`, codez `tri_selection_en_place(t)` d'après le pseudo-code avec la permutation `t[i], t[min_idx] = t[min_idx], t[i]`.
  * *2.2 (Semi-guidé)* : Codez `tri_selection_copie(t)` qui travaille sur `copie = list(t)`. Utilisez `afficher_tableau(t)` de `read_tab.py` pour valider que `tab_init = [15, 3, 8]` reste inchangé.
  * *2.3 (Autonome — Activité 0.7 : Statistiques élémentaires & Problème de Nicolas)* :  
    ![Médiane d'une série statistique - Problématique de Nicolas](img/mediane_nicolas.png)  
    > **Problématique de Nicolas :**  
    > Dans une entreprise de **9 salariés**, le salaire mensuel moyen est de **2 500 €**. Nicolas travaille dans cette entreprise et gagne **2 200 €** par mois.  
    > Constatant que son salaire est inférieur au salaire moyen ($2\,200\text{ €} < 2\,500\text{ €}$), il affirme : *« Je suis dans les moins bien payés de l'entreprise ! »*. Que penser de cette affirmation ?  
    >  
    > *Élément d'analyse* : Nicolas confond salaire moyen et salaire médian. Quelques salaires élevés suffisent à tirer la moyenne vers le haut. Pour savoir s'il est réellement dans la tranche inférieure ou supérieure de l'entreprise, il faut ordonner la série et trouver la **médiane** qui sépare l'effectif en deux moitiés égales.  

    Dans `api/statistique.py` et `api/main.py`, codez les fonctions `moyenne(tab)` et `mediane(tab)` sur liste ordonnée (sans `sorted()` ni `.sort()`). Triez la liste des 9 salaires de l'entreprise avec votre fonction `tri_selection_copie()` et affichez les résultats dans la console pour conclure scientifiquement sur l'affirmation de Nicolas (2 200 € vs médiane réelle de 2 000 €).

* **Critère de validation** : L'exécution console affiche : `Moyenne = 2500.00 € | Médiane = 2000.00 €` et démontre que Nicolas a tort. Aucune mention de `sorted` ou `.sort` dans le code.

---

#### 📍 SÉANCE 3 : Persistance JSON & Gestion d'Erreurs (2 h)

* **Objectif** : L'étudiant est capable de sérialiser et désérialiser des listes de dictionnaires dans un fichier `.json` avec le module `json`, en encapsulant les opérations dans des blocs `try / except`.

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Grille de correspondance de syntaxe Python $\leftrightarrow$ JSON* :
  >    | Type / Valeur | En Python | En JSON strict |
  >    | :--- | :--- | :--- |
  >    | Booléen vrai | `True` | `true` |
  >    | Booléen faux | `False` | `false` |
  >    | Absence de valeur | `None` | `null` |
  >    | Chaîne de texte | `'texte'` ou `"texte"` | `"texte"` (guillemets doubles stricts) |
  > 2. *Chasse aux anomalies syntaxiques JSON* :  
  >    Identifiez et corrigez les 3 erreurs dans cet extrait invalide :
  >    ```json
  >    { 'nom': "Alice", "actif": True, "salaire": 1500, }
  >    ```
  >    *Erreur 1 :* `'nom'` $\rightarrow$ `"nom"` (guillemets simples interdits).  
  >    *Erreur 2 :* `True` $\rightarrow$ `true` (majuscule interdite).  
  >    *Erreur 3 :* `1500,` $\rightarrow$ `1500` (virgule finale interdite).
  > 3. *Organigramme try / except* :  
  >    Que fait le programme si `open("employes.json")` déclenche une `FileNotFoundError` ?  
  >    *Réponse :* Le bloc `except` intercepte l'erreur sans planter et retourne une liste vide `[]`.

* **Exemple de code de cours (17 lignes)** :
  ```python
  import json

  data = [{"id": 1, "nom": "Alice", "salaire": 1500}]
  with open("test.json", "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)

  try:
      with open("test.json", "r", encoding="utf-8") as f:
          charge = json.load(f)
          print(f"Employé chargé : {charge[0]['nom']}")
  except FileNotFoundError:
      print("Erreur : le fichier test.json n'existe pas.")
  ```

* **Exercices sur machine** :
  * *3.1 (Guidé)* : Dans `gestion_json.py`, écrivez `sauvegarder_employes(fichier, data)` pour enregistrer les 9 salariés dans `employes.json`.
  * *3.2 (Semi-guidé)* : Écrivez `augmenter_salaire(fichier, id_emp, pourcentage)` : chargez le JSON, appliquez $+10\,\%$ à Nicolas (2 420 €), réécrivez le fichier.
  * *3.3 (Autonome)* : Écrivez `charger_employes_securise(chemin)` interceptant `FileNotFoundError` et `json.JSONDecodeError` pour éviter tout crash.

* **Critère de validation** : `employes.json` est généré, contient un JSON valide de 9 enregistrements, et le test sur un fichier inexistant renvoie une liste vide sans planter.

---

#### 📍 SÉANCE 4 : Python & MySQL (Accès aux Données & Sécurité) (2 h)

* **Objectif** : L'étudiant est capable de connecter Python à MySQL, d'exécuter des requêtes paramétrées sécurisées (`%s`), et de récupérer les lignes de résultats sous forme de dictionnaires avec `DictCursor`.

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Requêtes préparées vs Concaténation de chaînes* :  
  >    Soit une variable Python `id_saisi = 3`. Pourquoi ne doit-on jamais concaténer de chaînes avec `f"SELECT * FROM employes WHERE id = {id_saisi}"` ?  
  >    *Réponse :* La concaténation ouvre la porte aux erreurs de syntaxe et aux corruptions si la saisie contient des caractères spéciaux. Réécriture robuste :
  >    ```python
  >    cur.execute("SELECT * FROM employes WHERE id = %s", (id_saisi,))
  >    ```
  > 2. *Du tuple SQL au dictionnaire Python avec DictCursor* :  
  >    Pour la ligne retournée `(3, "Nicolas", 2200.0)`, écrivez le dictionnaire généré par le curseur :  
  >    *Dictionnaire :* `{"id": 3, "nom": "Nicolas", "salaire": 2200.0}`.

* **Exemple de code de cours (19 lignes)** :
  ```python
  import os, pymysql
  from pymysql.cursors import DictCursor

  conn = pymysql.connect(
      host=os.environ.get("MYSQL_HOST", "db"),
      user=os.environ.get("MYSQL_USER", "root"),
      password=os.environ.get("MYSQL_PASSWORD", "root"),
      database=os.environ.get("MYSQL_DATABASE", "CRUD"),
      cursorclass=DictCursor
  )
  with conn.cursor() as cur:
      cur.execute("SELECT nom, salaire FROM employes WHERE salaire > %s", (2000,))
      resultats = cur.fetchall()
      print(f"Salariés trouvés : {len(resultats)}")
  conn.close()
  ```

* **Exercices sur machine** :
  * *4.1 (Guidé)* : Dans `api/bdd.py`, créez `get_connection()` vers la base `CRUD` et testez `SELECT COUNT(*) FROM employes;`.
  * *4.2 (Semi-guidé)* : Écrivez `get_employe_by_id(id_emp)` avec requête sécurisée `%s` et `cur.fetchone()`. Interdiction formelle de concaténer avec `f"..."`.
  * *4.3 (Autonome)* : Écrivez `get_statistiques_bdd()` qui extrait tous les salaires, les trie avec `tri_selection_copie()`, calcule la médiane, et retourne `{"effectif": 9, "moyenne": 2500.0, "mediane": 2000.0}`.

* **Critère de validation** : `docker compose exec api python bdd.py` se connecte sans erreur, extrait Nicolas pour l'ID 3 et calcule exactement 2 000.0 € de médiane.

---

#### 📍 SÉANCE 5 : Fondamentaux de Flask & API REST (2 h)

* **Objectif** : L'étudiant est capable de déclarer des routes Flask associées à la méthode HTTP `GET`, de formater des réponses avec `jsonify()`, d'associer des codes HTTP (`200`, `404`), et de tester les endpoints avec Postman.

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Trame de la Requête HTTP émise par le client (Postman)* :
  >    ```http
  >    GET /api/employes/3 HTTP/1.1
  >    Host: localhost:5000
  >    Accept: application/json
  >    ```
  > 2. *Trame de la Réponse HTTP renvoyée par Flask* :
  >    ```http
  >    HTTP/1.1 200 OK
  >    Content-Type: application/json
  >
  >    { "id": 3, "nom": "Nicolas", "salaire": 2200.0 }
  >    ```
  > 3. *Code d'état HTTP en cas d'employé inconnu* :  
  >    *Code statut :* `404 Not Found` | *Corps JSON :* `{"error": "Employé introuvable"}`.

* **Exemple de code de cours (16 lignes)** :
  ```python
  from flask import Flask, jsonify

  app = Flask(__name__)

  @app.route("/api/ping", methods=["GET"])
  def ping():
      return jsonify({"status": "ok", "message": "API opérationnelle"}), 200

  @app.route("/api/hello/<nom>", methods=["GET"])
  def saluer(nom):
      return jsonify({"message": f"Bonjour {nom}"}), 200

  if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000, debug=True)
  ```

* **Exercices sur machine** :
  * *5.1 (Guidé)* : Dans `api/app.py`, instanciez Flask avec `CORS(app)`. Créez la route `@app.route('/api/employes')` qui renvoie la liste complète des 9 salariés en JSON.
  * *5.2 (Semi-guidé)* : Créez la route `/api/employes/<int:id_emp>` : renvoie le salarié avec le code `200`, ou `jsonify({"error": "..."}), 404` si absent.
  * *5.3 (Autonome)* : Créez `/api/salaires/statistiques` appelant `get_statistiques_bdd()`. Ouvrez Postman et validez les requêtes pour l'employé 3 (`200 OK`), l'employé 99 (`404`), et les statistiques.

* **Critère de validation** : Les requêtes sous Postman renvoient du JSON valide avec un statut 200 pour Nicolas et 404 pour un ID inexistant.

---

#### 📍 SÉANCE 6 : Paramètres d'URL & Client Web `fetch()` (2 h)

* **Objectif** : L'étudiant est capable de récupérer des filtres dans Flask via `request.args`, et de concevoir une page HTML/JavaScript qui consomme l'API via `fetch()` pour mettre à jour le DOM sans rechargement.

* **📝 Travail sur table préalable (15 min — Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Anatomie d'une URL avec Query String* :  
  >    Soit l'URL `http://localhost:5000/api/employes/filtre?min=2000`.  
  >    * Paramètre extrait dans Flask : `request.args.get("min", 0)` (renvoie la chaîne `"2000"`).  
  >    * Conversion obligatoire en Python : `seuil = float(request.args.get("min", 0))`.
  > 2. *Chronogramme séquentiel (de 1 à 5)* :  
  >    * Étape 1 : L'utilisateur clique sur le bouton de l'interface web.  
  >    * Étape 2 : Le JavaScript émet la requête asynchrone `fetch('/api/employes/filtre?min=2000')`.  
  >    * Étape 3 : Flask exécute la requête SQL et renvoie la réponse HTTP en JSON.  
  >    * Étape 4 : Le navigateur résout la promesse avec `response.json()`.  
  >    * Étape 5 : Le script met à jour le DOM sans recharger la page (`innerHTML` ou `textContent`).

* **Exemple de code de cours (19 lignes)** :
  ```python
  # Côté Flask (Python)
  from flask import request, jsonify

  @app.route("/api/filtrer", methods=["GET"])
  def filtrer():
      valeur_min = float(request.args.get("min", 0))
      return jsonify({"seuil_recu": valeur_min}), 200
  ```
  ```javascript
  // Côté Client (JavaScript)
  fetch('/api/filtrer?min=2000')
      .then(response => response.json())
      .then(data => {
          document.getElementById('resultat').textContent = `Seuil : ${data.seuil_recu} €`;
      });
  ```

* **Exercices sur machine** :
  * *6.1 (Guidé)* : Dans `api/app.py`, ajoutez `/api/employes/filtre` lisant `request.args.get('min', 0)` et exécutant `SELECT * FROM employes WHERE salaire >= %s ORDER BY salaire ASC;`.
  * *6.2 (Semi-guidé)* : Dans `index.html`, écrivez `chargerStats()` appelant `/api/salaires/statistiques` pour actualiser `<span id="moyenne">` et `<span id="mediane">`.
  * *6.3 (Autonome)* : Ajoutez un champ `<input id="seuil">` et un bouton. Au clic, appelez l'API de filtrage et générez dynamiquement les lignes d'un tableau HTML `<table>`.

* **Critère de validation** : Sur `http://localhost`, cliquer sur le bouton affiche immédiatement la médiane (2 000.0 €), et filtrer avec `3000` affiche exactement les 3 employés concernés (David, Henri, Bob) sans rechargement de page.

---

### 🏁 Évaluation Diagnostique de Fin de Séquence (Mini-TP 30 min)

* **Énoncé** : « Le Micro-service de Prime Salariale »  
* **Objectif** : Écrire `calculer_mediane(salaires)` (sans `sorted`), calculer une prime ($500\text{ €}$ si $<$ médiane, $200\text{ €}$ si $\ge$ médiane), extraire les salaires de MySQL et exposer la route `GET /api/employes/<int:id_emp>/prime`.
* **Barème (/20)** : Médiane par sélection (/4), Logique prime (/2), Requête SQL paramétrée (/4), Extraction données (/2), Route typée Flask (/4), Réponse JSON & 404 (/4). *Seuil d'accès validé à l'activité finale : $\ge 12 / 20$.*

---

---

### Exercice 1 : Triangle console et arguments CLI
* **Objectif** : Lire des arguments en ligne de commande et pratiquer les boucles imbriquées ou l'opérateur de chaîne.
* **Fichiers** : `api/triangle.py`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. Pour $n = 4$, combien d'étoiles doit afficher chaque ligne $i$ (pour $i$ allant de $1$ à $n$) ?  
  >    *Réponse :* La ligne $i$ affiche exactement `i` étoiles.
  > 2. Remplissez le tableau de trace pour $n = 4$ :
  >    | Ligne $i$ | Nombre d'étoiles | Rendu console attendu |
  >    | :---: | :---: | :--- |
  >    | 1 | 1 | `*` |
  >    | 2 | 2 | `**` |
  >    | 3 | 3 | `***` |
  >    | 4 | 4 | `****` |
  > 3. Écrivez le pseudo-code officiel de la fonction :
  >    ```text
  >    procédure triangle(entier n)
  >        pour i de 1 à n :
  >            afficher i fois le caractère '*'
  >    fin procédure
  >    ```
  > 4. Comment accède-t-on au premier argument utilisateur passé dans le terminal via `sys.argv` ?  
  >    *Réponse :* `int(sys.argv[1])` *(attention, `sys.argv[0]` contient le nom du script lui-même)*.

* **💻 Étape 2 : Implémentation sur machine** :
  * Implémentez la fonction `triangle(n)` qui trace un triangle rectangle d'étoiles de hauteur $n$.
  * Récupérez la valeur de $n$ depuis le terminal via la liste `sys.argv`.
  * Lancez le script via `docker compose exec api python triangle.py 5`.
* **Exemple d'exécution** :
  ```text
  Entrée : 4
  Sortie attendue :
  *
  **
  ***
  ****
  ```
* **Amélioration** : Affichez un message d'aide clair si l'utilisateur oublie de renseigner l'argument sur la ligne de commande.

---

### Exercice 2 : Table de multiplication et alignement
* **Objectif** : Formater l'affichage console sans module tiers à l'aide des f-strings et de `.rjust()` pour aligner les colonnes.
* **Fichiers** : `api/multiplication.py`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. Remplissez la grille des valeurs pour $n = 3$ et $m = 4$ ($i \times j$) :
  >    | $i \backslash j$ | 1 | 2 | 3 | 4 |
  >    | :---: | :---: | :---: | :---: | :---: |
  >    | **1** | 1 | 2 | 3 | 4 |
  >    | **2** | 2 | 4 | 6 | 8 |
  >    | **3** | 3 | 6 | 9 | 12 |
  > 2. Pourquoi l'instruction naïve `print(i * j, end=" ")` produit-elle une grille décalée dès qu'un nombre dépasse 9 ?  
  >    *Réponse :* `________________________________________________` *(Les nombres à deux chiffres occupent 2 caractères au lieu d'un, ce qui décale les colonnes).*
  > 3. Donnez la syntaxe f-string pour forcer chaque nombre à occuper exactement 4 caractères de large alignés à droite :  
  >    *Réponse :* `print(f"{i * j:4d}", end="")`

* **💻 Étape 2 : Implémentation sur machine** :
  * Écrivez `multiplication_n_m(n, m)` qui affiche la table complète de $1 \times 1$ jusqu'à $n \times m$.
  * Alignez chaque nombre sur une largeur constante de 4 caractères pour obtenir une grille propre.
* **Exemple d'exécution** :
  ```text
  multiplication_n_m(3, 4)
     1   2   3   4
     2   4   6   8
     3   6   9  12
  ```
* **Amélioration** : Affichez automatiquement une ligne et une colonne d'en-tête séparées par des tirets.

---

### Exercice 3 : Somme et factorielle (Itératif vs Récursif)
* **Objectif** : Comprendre le principe de récursivité et l'empilement d'appels en Python.
* **Fichiers** : `api/recursion.py`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. Déroulez l'arbre des appels récursifs pour `somme_recursive(4)` :
  >    ```text
  >    somme(4) = 4 + somme(3)
  >             = 4 + (3 + somme(2))
  >             = 4 + (3 + (2 + somme(1)))
  >             = 4 + 3 + 2 + 1 = 10
  >    ```
  > 2. Déroulez l'arbre des appels pour `factorielle_recursive(4)` ($4!$) :
  >    ```text
  >    fact(4) = 4 * fact(3) = 4 * 6 = 24
  >    fact(3) = 3 * fact(2) = 3 * 2 = 6
  >    fact(2) = 2 * fact(1) = 2 * 1 = 2
  >    fact(1) = 1 (cas de base)
  >    ```
  > 3. Quel est le rôle vital du **cas d'arrêt** dans une fonction récursive ? Que se passe-t-il s'il est omis en Python ?  
  >    *Réponse :* `________________________________________________` *(Une boucle infinie d'appels provoquant l'exception RecursionError).*

* **💻 Étape 2 : Implémentation sur machine** :
  * Codez `somme_iterative(n)` puis `somme_recursive(n)` pour calculer $1 + 2 + \dots + n$.
  * Codez `factorielle_iterative(n)` puis `factorielle_recursive(n)` ($n! = 1 \times 2 \dots \times n$).
  * Fixez rigoureusement vos cas d'arrêt pour éviter la `RecursionError`.
* **Exemple d'exécution** :
  ```text
  somme_recursive(5) -> 15
  factorielle_recursive(5) -> 120
  ```
* **Amélioration** : Levez une exception `ValueError` explicite si un nombre négatif est transmis.

---

### Exercice 4.1 : Tri par sélection (Valeur vs Référence)
* **Objectif** : Coder un algorithme de tri impératif et maîtriser la mutabilité des listes en Python.
* **Fichiers** : `api/tri_selection.py`, `api/read_tab.py`.
* **Pseudo-code obligatoire** :
```text
procédure tri_selection(tableau t)
    n ← longueur(t)
    pour i de 0 à n - 2
        min ← i
        pour j de i + 1 à n - 1
            si t[j] < t[min], alors min ← j
        fin pour
        si min ≠ i, alors échanger t[i] et t[min]
    fin pour
fin procédure
```

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > Déroulez manuellement l'algorithme sur le tableau $t = [15, 3, 8]$ ($n = 3$) :
  > 
  > | Tour $i$ | Indice $min$ initial | Indice $j$ | Comparaison $t[j] < t[min]$ | Nouveau $min$ | Échange effectué | État du tableau $t$ |
  > | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  > | 0 | 0 ($t[0]=15$) | 1 | $3 < 15$ (VRAI) | 1 | - | - |
  > | 0 | 1 ($t[1]=3$) | 2 | $8 < 3$ (FAUX) | 1 | $t[0] \leftrightarrow t[1]$ | `[3, 15, 8]` |
  > | 1 | 1 ($t[1]=15$) | 2 | $8 < 15$ (VRAI) | 2 | $t[1] \leftrightarrow t[2]$ | `[3, 8, 15]` |
  > 
  > *Schéma mémoire :*
  > * Passage par référence : `tri_selection_en_place(t)` mute directement l'adresse mémoire de `t`.
  > * Copie défensive : `tri_selection_copie(t)` instancie `copie = list(t)` pour isoler les mutations.

* **💻 Étape 2 : Implémentation sur machine** :
  * Codez `tri_selection_copie(t)` qui retourne une **nouvelle** liste triée sans modifier la liste d'origine.
  * Codez `tri_selection_en_place(t)` qui modifie **directement** la liste en mémoire (passage par référence d'objet mutable).
  * Utilisez `afficher_tableau(t)` depuis `read_tab.py` pour valider l'absence d'effet de bord sur la version par copie.
* **Exemple d'exécution** :
  ```text
  tab_init = [15, 3, 8]
  tri_selection_copie(tab_init) -> retourne [3, 8, 15], tab_init vaut toujours [15, 3, 8]
  tri_selection_en_place(tab_init) -> ne retourne rien, tab_init vaut désormais [3, 8, 15]
  ```
* **Amélioration** : Mesurez le temps d'exécution (`time.perf_counter`) sur une liste de 1 000 entiers aléatoires.

---

### Prérequis à l'Exercice 4.2 : Les fondamentaux de Flask (Routes & Paramètres)

> 📖 **Support de cours & exercices préparatoires :**  
> C'est à ce stade du TP que vous passez des scripts console à une API Web. Avant d'exposer vos algorithmes en HTTP, vous devez maîtriser les mécanismes clés de Flask : instanciation, déclaration de routes avec `@app.route`, extraction des paramètres dans l'URL avec `request.args` et retour de données JSON avec `jsonify()`.  
> 👉 **Consultez le cours et réalisez les exercices progressifs dans : [`bases en flask.md`](bases%20en%20flask.md)**  
> *(Revenez ensuite ici pour réaliser l'Exercice 4.2)*

---

### Exercice 4.2 : API REST Flask pour le tri

[![Vidéo de démonstration : saisie et tri](img/video_ex4_2_thumbnail.jpg)](https://drive.google.com/file/d/1_iikt1uk9Wx-tPY79woa0aJHjuJ83r5l/view?usp=drive_link)

* **Objectif** : Concevoir une IHM web en JavaScript pour la saisie dynamique de valeurs, valider l'affichage DOM à l'aide d'un serveur Mock Postman, puis exposer le service web réel en Python avec Flask.
* **Fichiers** : `nginx/html/index.html`, `nginx/html/app.js`, `api/app.py`.
* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Extraction et conversion de la Query String dans Flask* :  
  >    Soit la requête HTTP reçue par Flask : `GET /api/tri?t=15,3,22,8`.  
  >    * Quel est le type et la valeur retournée par l'instruction `request.args.get("t")` ?  
  >      *Réponse :* Type `str`, valeur `"15,3,22,8"`.  
  >    * Écrivez l'instruction Python permettant de convertir cette chaîne en une véritable liste d'entiers `[15, 3, 22, 8]` :  
  >      *Réponse :* `t_liste = [int(x) for x in request.args.get("t").split(",")]`  
  > 2. *Calcul manuel de la médiane sur feuille pour $N = 4$ (effectif pair)* :  
  >    * Série triée par sélection : `[3, 8, 15, 22]`.  
  >    * Quels sont les deux indices centraux en base 0 pour $N = 4$ ?  
  >      *Réponse :* Indice `N // 2 - 1 = 1` ($valeur = 8$) et Indice `N // 2 = 2` ($valeur = 15$).  
  >    * Calculez la médiane exacte :  
  >      *Réponse :* $(8 + 15) / 2 = 23 / 2 = 11.5$.  
  > 3. *Contrat d'échange JSON de la réponse HTTP* :  
  >    Complétez la structure JSON attendue renvoyée par l'API :  
  >    ```json
  >    {
  >      "original": [15, 3, 22, 8],
  >      "tri": [3, 8, 15, 22],
  >      "mediane": 11.5
  >    }
  >    ```
  > 4. *Pseudo-code de la saisie séquentielle et condition d'arrêt côté client (JavaScript)* :  
  >    ```text
  >    tableau_saisi ← []
  >    Répéter :
  >        valeur ← demander_entier("Entrez un nombre (> 0) :")
  >        Si valeur > 0 alors :
  >            tableau_saisi.push(valeur)
  >            mettre_a_jour_affichage(tableau_saisi)
  >    Jusqu'à ce que valeur <= 0
  >    envoyer_requete_fetch(tableau_saisi)
  >    ```

* **💻 Étape 2 : Implémentation sur machine** :
  * **1. Simulation avec un serveur Mock Postman (définition du contrat d'API)** :
    * Avant de développer la page web ou le backend, définissez le contrat d'échange en créant un **Mock Server** dans Postman simulant la route `GET /api/tri`.
    * Configurez un exemple de réponse JSON de référence conforme au format attendu :
      ```json
      {
        "original": [15, 3, 22, 8],
        "tri": [3, 8, 15, 22],
        "mediane": 11.5
      }
      ```
    * Copiez l'URL publique générée par le Mock Postman (ex: `https://<mock-id>.mock.pstmn.io/api/tri`).
  * **2. Côté Frontend (IHM Web & JavaScript - `index.html`, `app.js`)** :
    * **Comprendre la structure HTML fournie :**  
      Ouvrez `nginx/html/index.html` (section `sec-tri`). Les éléments interactifs sont déjà créés et identifiés par leur attribut `id` :
      * **Contrôles de saisie :**
        * `<input id="input-valeur-tri">` : champ numérique pour saisir un entier.
        * `<button id="btn-push-tri">` : bouton « Ajouter (push) » déclenchant l'ajout au tableau JavaScript.
        * `<button id="btn-prompt-tri">` : bouton « Saisie via prompt() » (pour reproduire fidèlement la saisie séquentielle de la vidéo).
        * `<button id="btn-reset-tri">` : bouton de remise à zéro.
      * **Zones d'affichage dans le DOM (balises `<span>` et `<pre>`) :**
        * `<span id="span-saisie-cours">` : balise affichant le tableau en cours de constitution en JavaScript (ex: `[15, 3, 22]`).
        * `<span id="span-tri-original">` : balise affichant le tableau initial envoyé au service web.
        * `<span id="span-tri-trie">` : balise affichant le tableau trié reçu dans la réponse JSON (`data.tri`).
        * `<span id="span-tri-mediane">` : balise affichant la médiane calculée reçue (`data.mediane`).
        * `<pre id="output-tri">` : zone de texte pour afficher le JSON brut ou les messages d'état.
    * **Développement dans `nginx/html/app.js` :**
      * **Saisie entier + push** : demandez des entiers à l'utilisateur et ajoutez-les dans un tableau JavaScript avec `tableau.push(valeur)` tant que la valeur saisie est strictement supérieure à 0 (`valeur > 0`). Mettez à jour le texte de la balise `<span id="span-saisie-cours">` avec `document.getElementById('span-saisie-cours').textContent = ...`.
      * **Condition d'arrêt et appel réseau** : dès qu'une valeur inférieure ou égale à 0 est saisie ($\le 0$), transmettez le tableau de valeurs accumulées au service web via une requête `fetch(...)`.
      * **Validation immédiate avec le Mock Postman** : pointez temporairement votre requête `fetch()` vers l'URL générée par votre Mock Postman. Récupérez le JSON avec `await response.json()`, puis injectez les valeurs dans les balises correspondantes avec `document.getElementById('span-tri-original').textContent = ...`, `span-tri-trie` et `span-tri-mediane`.
      * Vous validez ainsi toute votre interface graphique et la manipulation du DOM sans attendre le backend !
  * **3. Côté Backend (Flask - `app.py`)** :
    * Développez maintenant la route réelle dans l'application Flask :
      * Créez la route `GET /api/tri`.
      * Récupérez la série passée dans la Query String `t` (ex: `/api/tri?t=1500,4500,2200`).
      * Triez le tableau avec votre fonction maison `tri_selection_copie` et calculez la médiane.
      * Renvoyez la réponse JSON structurée : `{"original": [...], "tri": [...], "mediane": 2000.0}`.
    * Dans `nginx/html/app.js`, remplacez l'URL du Mock Postman par l'URL locale `/api/tri?t=...` pour connecter votre interface au backend Flask réel.
* **Exemple de test curl** :
  ```bash
  curl "http://localhost/api/tri?t=15,3,22,8"
  ```
* **Amélioration** : Renvoyez un code d'erreur HTTP 400 si le paramètre `t` est manquant ou contient des caractères non numériques.

---

### Exercice 4.3 : Client Web Fetch & Salaires aléatoires
* **Objectif** : Connecter une interface web cliente à votre API Flask pour automatiser l'analyse de salaires aléatoires.
* **Fichiers** : `nginx/html/index.html`, `nginx/html/app.js`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Génération aléatoire d'un entier en JavaScript dans $[min, max]$* :  
  >    * Rappel : `Math.random()` génère un nombre décimal pseudo-aléatoire dans $[0, 1[$.  
  >    * Complétez la formule JS pour obtenir un entier aléatoire compris entre $1\,200$ et $5\,000$ inclus :  
  >      *Réponse :* `Math.floor(Math.random() * (5000 - 1200 + 1)) + 1200`  
  > 2. *Pseudo-code de constitution du tableau de salaires en JavaScript* :  
  >    ```text
  >    salaires ← []
  >    Pour i de 1 à 9 :
  >        valeur_aleatoire ← Math.floor(Math.random() * (5000 - 1200 + 1)) + 1200
  >        salaires.push(valeur_aleatoire)
  >    Fin Pour
  >    ```
  > 3. *Préparation de l'URL pour la requête `fetch()`* :  
  >    Comment convertir le tableau JavaScript `[2200, 1500, 3400]` en chaîne pour le paramètre d'URL `?t=...` ?  
  >    *Réponse :* `salaires.join(",")` *(produit `"2200,1500,3400"`)*.  
  > 4. *Chronogramme séquentiel de mise à jour asynchrone du DOM* :  
  >    * Étape 1 : Clic sur `<button id="btn-random">`.  
  >    * Étape 2 : Génération des 9 salaires aléatoires et affichage immédiat dans `<span id="span-brut">`.  
  >    * Étape 3 : Émission de la requête asynchrone `fetch('/api/tri?t=' + salaires.join(','))`.  
  >    * Étape 4 : Réception du JSON et injection de `data.tri` dans `<span id="span-trie">` et de `data.mediane` dans `<span id="span-mediane">`.

* **💻 Étape 2 : Implémentation sur machine** :
  * **Éléments HTML fournis dans `index.html` (section `sec-random`) :**
    * `<button id="btn-random">` : bouton « Générer & Analyser ».
    * `<span id="span-brut">` : balise affichant les 9 salaires bruts générés aléatoirement en JavaScript.
    * `<span id="span-trie">` : balise affichant la liste triée retournée par l'API Flask.
    * `<span id="span-mediane">` : balise affichant la médiane retournée par l'API Flask.
  * **Consignes de développement dans `nginx/html/app.js` :**
    * Dans le client web, écoutez le clic sur le bouton `document.getElementById('btn-random')`.
    * Générez une série de 9 entiers aléatoires compris entre 1200 et 5000 (représentant des salaires en €).
    * Affichez la série générée dans `<span id="span-brut">`.
    * Émettez la requête HTTP vers votre API Flask : `fetch('/api/tri?t=...')`.
    * À la réception du JSON, injectez la série triée dans `<span id="span-trie">` et la médiane dans `<span id="span-mediane">` sans rechargement de page.
* **Exemple d'exécution** :
  * Clic sur le bouton $\rightarrow$ Les salaires bruts s'affichent, l'API renvoie le tri et la médiane dans le DOM.
* **Amélioration** : Animez ou mettez en surbrillance la médiane dans la liste reçue.

---

### Exercice 5 : Fusion de listes (Concaténation)

[![Vidéo de démonstration](https://img.youtube.com/vi/aGkpJFJ9t4k/maxresdefault.jpg)](https://www.youtube.com/watch?v=aGkpJFJ9t4k)

* **Objectif** : Traiter plusieurs paramètres de requêtes, manipuler la concaténation de listes avec l'opérateur `+`, et connecter une interface web dynamique pour la saisie et l'affichage.
* **Fichiers** : `api/app.py`, `nginx/html/index.html`, `nginx/html/app.js`.
* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Concaténation de listes en Python & Immutabilité relative* :  
  >    Soit $t_1 = [12, 18, 5]$ et $t_2 = [20, 8, 14]$.  
  >    * Quelle est la valeur de la liste résultant de l'opération `fusion = t1 + t2` ?  
  >      *Réponse :* `[12, 18, 5, 20, 8, 14]`.  
  >    * L'opération `t1 + t2` modifie-t-elle les listes d'origine `t1` ou `t2` en mémoire ?  
  >      *Réponse :* Non, l'opérateur `+` alloue une nouvelle liste distincte en mémoire sans altérer les listes opérandes.  
  > 2. *Tri par sélection et Médiane sur table de la liste fusionnée ($N = 6$)* :  
  >    * Série brute fusionnée : `[12, 18, 5, 20, 8, 14]`  
  >    * Série ordonnée (après tri par sélection) : `[5, 8, 12, 14, 18, 20]`  
  >    * Puisque l'effectif $N=6$ est pair, quels sont les indices (base 0) et les valeurs des deux éléments centraux ?  
  >      * Indice `N // 2 - 1 = 2` $\rightarrow$ Valeur : $12$  
  >      * Indice `N // 2 = 3` $\rightarrow$ Valeur : $14$  
  >    * Calculez la médiane globale de la fusion :  
  >      *Réponse :* $(12 + 14) / 2 = 26 / 2 = 13.0$.  
  > 3. *Structure d'URL multi-paramètres et Question théorique* :  
  >    * Quel symbole sépare l'URL des paramètres de requête ? `?`  
  >    * Quel symbole sépare deux paramètres distincts entre eux ? `&`  
  >    * **Question théorique obligatoire** : Quelle URI et structure de requête devez-vous adopter pour transmettre et fusionner 3 tableaux $t_1$, $t_2$ et $t_3$ ?  
  >      *Réponse :* `/api/fusion?t1=12,18,5&t2=20,8,14&t3=1,2,3` *(les paramètres sont cumulés avec le séparateur `&`)*.  
  > 4. *Contrat d'échange JSON attendu* :  
  >    Remplissez le JSON que devra renvoyer l'API :  
  >    ```json
  >    {
  >      "t1": [12, 18, 5],
  >      "t2": [20, 8, 14],
  >      "fusion": [12, 18, 5, 20, 8, 14],
  >      "tri": [5, 8, 12, 14, 18, 20],
  >      "mediane": 13.0
  >    }
  >    ```

* **💻 Étape 2 : Implémentation sur machine** :
  * **1. Simulation avec un serveur Mock Postman (définition du contrat d'API)** :
    * Avant de coder l'interface ou le backend, créez dans Postman un **Mock Server** simulant la route `GET /api/fusion?t1=12,18,5&t2=20,8,14`.
    * Configurez la réponse JSON de référence conforme au cahier des charges de la vidéo :
      ```json
      {
        "t1": [12, 18, 5],
        "t2": [20, 8, 14],
        "fusion": [12, 18, 5, 20, 8, 14],
        "tri": [5, 8, 12, 14, 18, 20],
        "mediane": 13.0
      }
      ```
    * Copiez l'URL générée par le Mock Server.
  * **2. Côté Frontend (IHM Web & JavaScript - `index.html`, `app.js`)** :
    * **Comprendre la structure HTML fournie :**  
      Ouvrez `nginx/html/index.html` (section `sec-fusion`). Les balises suivantes sont déjà prêtes :
      * **Champs de saisie & bouton d'action :**
        * `<input id="input-t1">` : champ texte pour saisir le premier tableau (ex: `12, 18, 5`).
        * `<input id="input-t2">` : champ texte pour saisir le second tableau (ex: `20, 8, 14`).
        * `<button id="btn-fusion">` : bouton « Envoyer, Fusionner & Afficher dans le DOM ».
      * **Zones d'affichage du résultat dans le DOM (balises `<span>` et `<pre>`) :**
        * `<span id="span-t1">` : balise affichant le premier tableau saisi.
        * `<span id="span-t2">` : balise affichant le second tableau saisi.
        * `<span id="span-fusion">` : balise affichant la concaténation brute reçue (`data.fusion`).
        * `<span id="span-fusion-tri">` : balise affichant la liste fusionnée et triée reçue (`data.tri`).
        * `<span id="span-fusion-mediane">` : balise affichant la médiane globale calculée (`data.mediane`).
        * `<pre id="output-fusion">` : zone affichant la réponse JSON brute pour vérifier l'exactitude des données.
    * **Développement dans `nginx/html/app.js` :**
      * Écoutez l'événement `click` sur le bouton `<button id="btn-fusion">`.
      * Récupérez les valeurs saisies avec `document.getElementById('input-t1').value` et `document.getElementById('input-t2').value`.
      * Pointez temporairement votre requête `fetch()` vers l'URL de votre Mock Server Postman (`https://<mock-id>.mock.pstmn.io/api/fusion?t1=12,18,5&t2=20,8,14`).
      * À la réception du JSON, mettez à jour le contenu textuel (`.textContent`) de chaque balise cible du DOM :
        * `document.getElementById('span-t1').textContent = ...`
        * `document.getElementById('span-t2').textContent = ...`
        * `document.getElementById('span-fusion').textContent = ...`
        * `document.getElementById('span-fusion-tri').textContent = ...`
        * `document.getElementById('span-fusion-mediane').textContent = ...`
        * `document.getElementById('output-fusion').textContent = JSON.stringify(data, null, 2)`
      * Vérifiez dans votre navigateur que tous les éléments s'actualisent fidèlement à la vidéo de démonstration.
  * **3. Côté Backend (Flask - `app.py`)** :
    * Développez la route réelle `GET /api/fusion?t1=...&t2=...` dans Flask :
      * Récupérez les deux paramètres `t1` et `t2` depuis la Query String (`request.args.get`).
      * Découpez les chaînes avec `.split(',')` et convertissez les morceaux en entiers.
      * Concaténez les deux listes avec l'opérateur Python `+` : `fusion = liste1 + liste2`.
      * Triez la liste fusionnée et calculez sa médiane.
      * Renvoyez la réponse JSON structurée avec les clés `"t1"`, `"t2"`, `"fusion"`, `"tri"`, `"mediane"`.
    * Dans `nginx/html/app.js`, remplacez l'URL du Mock par l'URL locale `/api/fusion?t1=...&t2=...`.
* **Question théorique (à consigner dans votre compte-rendu)** :
  * *Quelle URI et structure de requête devez-vous adopter pour transmettre et fusionner 3 tableaux t1, t2 et t3 ?*
* **Exemple d'exécution** :
  * Requête : `GET /api/fusion?t1=12,18,5&t2=20,8,14`
  * Réponse JSON : `{"t1": [12, 18, 5], "t2": [20, 8, 14], "fusion": [12, 18, 5, 20, 8, 14], "tri": [5, 8, 12, 14, 18, 20], "mediane": 13.0}`
* **Amélioration** : Rendez votre route capable d'accepter une infinité de tableaux grâce à `request.args.getlist('t')`.

---

### Prérequis à l'Exercice 6 : Les fondamentaux de SQL

> 📖 **Support de cours & exercices préparatoires :**  
> Avant d'interagir avec la base de données depuis votre API Python/Flask, vous devez maîtriser les requêtes SQL indispensables sur la table `employees`.  
> 👉 **Consultez le cours et réalisez les exercices progressifs dans : [`bases en sql.md`](bases%20en%20sql.md)**  
> *(Revenez ensuite ici pour réaliser l'Exercice 6)*

---

### Exercice 6 : Connexion MySQL & Comparaison de salaire
* **Objectif** : Interagir avec une base de données MySQL dans un bloc `try/except` et implémenter des routes métier.
* **Démonstration en ligne de ce qui est attendu** :  
  * 🌐 **Lien vers la démonstration en ligne** : [Accéder au site de démonstration (Salaire médian)](http://51.210.151.13/btssnir/demo_cours/SQL/EXERCICES/1_MEDIANE_ET_MOYENNE/)  
    *(Lien miroir vers le Dashboard des employés : [http://51.210.151.13/btssnir/demo_cours/SQL/DASHBOARD%20EMPLOYES/](http://51.210.151.13/btssnir/demo_cours/SQL/DASHBOARD%20EMPLOYES/))*
  * **Fonctionnement illustré** :  
    Le site extrait les salaires de la table MySQL `employees`, affiche la série brute (`[6500, 8000, 1200, 25000, 100000, 40000]`), effectue le tri par sélection (`[1200, 6500, 8000, 25000, 40000, 100000]`), et détermine la médiane (**16 500.00 €**) ainsi que la moyenne (**~30 116.67 €**).  
    Sur la branche `correction`, une version équivalente développée en **Python avec Flask** a été implémentée et est accessible directement en local sur [`http://localhost/demo/mediane`](http://localhost/demo/mediane) et [`http://localhost/demo/dashboard`](http://localhost/demo/dashboard).
* **Fichiers** : `api/db.py`, `api/app.py`, `nginx/html/index.html`, `nginx/html/app.js`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Rédaction des requêtes SQL sur la table `employees`* :  
  >    * Requête pour extraire la colonne des salaires de l'ensemble du personnel :  
  >      ```sql
  >      SELECT salary FROM employees;
  >      ```
  >    * Requête paramétrée sécurisée pour extraire un employé spécifique selon son `id` :  
  >      ```sql
  >      SELECT id, name, address, salary FROM employees WHERE id = %s;
  >      ```
  > 2. *Calcul statistique sur table des données réelles de la BDD ($N = 6$)* :  
  >    * Salaires bruts en base : `[6500, 8000, 1200, 25000, 100000, 40000]`  
  >    * Ordonnez manuellement la série : `[1200, 6500, 8000, 25000, 40000, 100000]`  
  >    * Calculez la moyenne arithmétique :  
  >      $\text{Somme} = 1200 + 6500 + 8000 + 25000 + 40000 + 100000 = 180\,700\text{ €}$  
  >      $\text{Moyenne} = 180\,700 / 6 \approx 30\,116.67\text{ €}$  
  >    * Calculez la médiane (effectif pair $N=6$) :  
  >      Éléments centraux aux indices 2 et 3 ($8\,000$ et $25\,000$).  
  >      $\text{Médiane} = (8\,000 + 25\,000) / 2 = 33\,000 / 2 = 16\,500.00\text{ €}$.  
  > 3. *Analyse de situation de Martin Blank (ID 3, salaire 8 000 €)* :  
  >    * Salaire de Martin Blank : $8\,000\text{ €}$.  
  >    * Comparaison à la moyenne ($30\,116.67\text{ €}$) : Inférieur ($8\,000 < 30\,116.67$).  
  >    * Comparaison à la médiane ($16\,500.00\text{ €}$) : Inférieur ($8\,000 < 16\,500$).  
  >    * Conclusion sociologique : Martin Blank fait partie des $50\,\%$ des employés les moins bien payés de l'entreprise, bien que la moyenne de l'entreprise soit tirée vers le haut par deux salaires atypiques.  
  > 4. *Contrat d'échange JSON attendu pour Martin Blank* :  
  >    ```json
  >    {
  >      "employe": {"id": 3, "name": "Martin Blank", "salary": 8000},
  >      "statistiques_globales": {"moyenne": 30116.67, "mediane": 16500.0},
  >      "situation": {"par_rapport_a_la_moyenne": "inférieur", "par_rapport_a_la_mediane": "inférieur"}
  >    }
  >    ```

* **💻 Étape 2 : Implémentation sur machine** :
  * **1. Simulation avec un serveur Mock Postman (définition du contrat d'API)** :
    * Avant d'interfacer MySQL, créez dans Postman un **Mock Server** simulant les deux routes de l'exercice :
      * `GET /api/salaires/stats` simulant le retour global :
        ```json
        {
          "nombre_employes": 6,
          "salaires_bruts": [6500, 8000, 1200, 25000, 100000, 40000],
          "salaires_tries": [1200, 6500, 8000, 25000, 40000, 100000],
          "moyenne": 30116.67,
          "mediane": 16500.0
        }
        ```
      * `GET /api/employees/3/comparaison` simulant la situation de Martin Blank :
        ```json
        {
          "employe": {"id": 3, "name": "Martin Blank", "salary": 8000},
          "statistiques_globales": {"moyenne": 30116.67, "mediane": 16500.0},
          "situation": {"par_rapport_a_la_moyenne": "inférieur", "par_rapport_a_la_mediane": "inférieur"}
        }
        ```
  * **2. Côté Frontend (IHM Web & JavaScript - `index.html`, `app.js`)** :
    * **Comprendre la structure HTML fournie :**  
      Ouvrez `nginx/html/index.html` (section `sec-db`). Les éléments suivants sont mis à disposition :
      * **Partie 1 : Statistiques globales BDD :**
        * `<button id="btn-db-stats">` : bouton « Charger les statistiques BDD ».
        * `<pre id="output-db-stats">` : zone d'affichage pour la réponse JSON des statistiques.
      * **Partie 2 : Comparaison d'un employé par son ID :**
        * `<input id="input-emp-id">` : champ numérique pour saisir l'ID de l'employé (ex: `3`).
        * `<button id="btn-db-emp">` : bouton « Comparer ».
        * `<pre id="output-db-emp">` : zone d'affichage pour le résultat comparatif de l'employé.
    * **Développement dans `nginx/html/app.js` :**
      * Câblez les écouteurs d'événements `click` sur `btn-db-stats` et `btn-db-emp`.
      * Connectez temporairement vos requêtes `fetch()` vers votre Mock Postman pour valider que le JSON s'affiche proprement dans `<pre id="output-db-stats">` et `<pre id="output-db-emp">` via `output.textContent = JSON.stringify(data, null, 2)`.
  * **3. Côté Backend (MySQL & Flask - `api/db.py`, `api/app.py`)** :
    * Dans `db.py`, connectez-vous à la base `CRUD` avec le compte `eleve` / `eleve`.
    * Implémentez les requêtes SQL réelles (`SELECT salary FROM employees` et requête préparée `SELECT id, name, address, salary FROM employees WHERE id = %s`).
    * Créez les routes réelles dans Flask (`/api/salaires/stats` et `/api/employees/<id>/comparaison`).
    * Dans `app.js`, reconnectez les appels `fetch()` sur l'API Flask locale.
* **Données de référence BDD** :
  * 6 employés ($N=6$, pair) : 1200, 6500, 8000, 25000, 40000, 100000.
  * Moyenne attendue : **~30 116.67 €** | Médiane attendue : $(8000 + 25000) / 2$ = **16 500.00 €**.
* **Exemple d'exécution** :
  ```bash
  curl "http://localhost/api/employees/3/comparaison"
  # Martin Blank (8000 €) -> Inférieur à la moyenne et inférieur à la médiane.
  ```
* **Amélioration** : Renvoyez une réponse JSON avec code d'état HTTP 404 si l'employé demandé n'existe pas en BDD.

---

### Prérequis à l'Exercice 7 : Les jointures SQL & la modélisation relationnelle

> 📖 **Support de cours & exercices préparatoires :**  
> Avant d'interfacer l'API Flask avec des requêtes multi-tables et des calculs statistiques sur période, vous devez maîtriser les jointures relationnelles et les agrégations temporelles sur la base `CRUD2`.  
> 👉 **Consultez le cours et réalisez les exercices progressifs dans : [`bases en jointures.md`](bases%20en%20jointures.md)**  
> *(Revenez ensuite ici pour réaliser l'Exercice 7)*

---

### Exercice 7 : API Flask & Médiane sur une période (Jointures & BDD CRUD2)
* **Objectif** : Exposer un service web HTTP REST avec Flask interrogeant la base relationnelle `CRUD2` pour calculer des moyennes individuelles en SQL (`INNER JOIN` + `AVG` + `GROUP BY`) et la médiane globale des salaires moyens en Python.
* **Fichiers** : `api/db.py`, `api/app.py`, `nginx/html/index.html`, `nginx/html/app.js`.

* **📝 Étape 1 : Travail sur table préalable (Débranché)** :
  > ✍️ **Cadre de réponse écrite (Travail sur table) :**
  > 
  > 1. *Algorithme de décision des 4 cas selon les paramètres URL* :  
  >    Complétez les conditions en Python dans la vue Flask selon les variables `p`, `d1`, `d2` :  
  >    ```python
  >    if p and d1 and d2:
  >        cas = "employe_periode"
  >    elif p and (d1 or d2):
  >        cas = "employe_partir_de"
  >    elif not p and d1 and d2:
  >        cas = "mediane_periode"
  >    else:
  >        cas = "mediane_globale"
  >    ```
  > 2. *Rédaction des requêtes SQL avec Jointure relationnelle (`CRUD2`)* :  
  >    * *Cas 1 (Moyenne d'un employé entre d1 et d2)* :  
  >      ```sql
  >      SELECT e.id, e.name, AVG(s.salary) AS salaire_moyen
  >      FROM employes e
  >      INNER JOIN salaires s ON e.id = s.employe_id
  >      WHERE e.id = %s AND s.date BETWEEN %s AND %s
  >      GROUP BY e.id, e.name;
  >      ```
  >    * *Cas 3 (Moyenne de chaque employé sur période pour calcul médiane)* :  
  >      ```sql
  >      SELECT e.id, e.name, AVG(s.salary) AS salaire_moyen
  >      FROM employes e
  >      INNER JOIN salaires s ON e.id = s.employe_id
  >      WHERE s.date BETWEEN %s AND %s
  >      GROUP BY e.id, e.name
  >      ORDER BY e.id;
  >      ```
  >    * *Cas 4 (Moyenne historique globale de chaque employé)* :  
  >      ```sql
  >      SELECT e.id, e.name, AVG(s.salary) AS salaire_moyen
  >      FROM employes e
  >      INNER JOIN salaires s ON e.id = s.employe_id
  >      GROUP BY e.id, e.name
  >      ORDER BY e.id;
  >      ```
  > 3. *Calcul manuel sur table de la médiane des moyennes sur 2022 (`CRUD2`)* :  
  >    * Moyenne Roland Mendel (id 1) : $5\,300.00\text{ €}$  
  >    * Moyenne Victoria Ashworth (id 2) : $6\,600.00\text{ €}$  
  >    * Moyenne Martin Blank (id 3) : $8\,000.00\text{ €}$  
  >    * Liste ordonnée des moyennes : `[5300.0, 6600.0, 8000.0]` ($N = 3$, effectif impair).  
  >    * Indice médian : $3 // 2 = 1$.  
  >    * Médiane des moyennes = **6 600.00 €**.  
  > 4. *Pourquoi le calcul de la médiane est-il réalisé en Python et non directement en SQL ?* :  
  >    *Réponse :* SQL (et MySQL en particulier) ne possède pas de fonction d'agrégation native `MEDIAN()`. Les moyennes individuelles sont donc calculées efficacement par le moteur de base de données via `AVG()`, puis Python trie la liste des moyennes avec l'algorithme `tri_selection_copie()` pour en déduire la médiane exacte.

* **💻 Étape 2 : Implémentation sur machine** :
  * **1. Simulation avec un serveur Mock Postman (définition du contrat d'API)** :
    * La route à concevoir est `GET /api/salaires/periode`. Elle accepte trois paramètres optionnels dans la Query String :
      * `p` : identifiant entier (`id`) de l'employé.
      * `d1` : date de début au format standard `AAAA-MM-JJ`.
      * `d2` : date de fin au format standard `AAAA-MM-JJ`.
    * **Matrice de décision métier (4 cas) :**
      | `p` (Employé) | `d1` / `d2` (Période) | Réponse attendue de l'API | Exemple d'URL |
      |:---:|:---:|:---|:---|
      | **Présent** | **Les deux** | Salaire moyen de l'employé `p` entre `d1` et `d2` | `/api/salaires/periode?p=1&d1=2022-01-01&d2=2022-12-31` |
      | **Présent** | **Un seul (`d1` ou `d2`)** | Salaire moyen de l'employé `p` à partir de cette date | `/api/salaires/periode?p=1&d1=2022-01-01` |
      | **Absent** | **Les deux** | Médiane des salaires moyens des employés entre `d1` et `d2` | `/api/salaires/periode?d1=2022-01-01&d2=2022-12-31` |
      | **Absent** | **Aucun** | Médiane des salaires moyens de tous les employés (toutes dates) | `/api/salaires/periode` |

    * Avant de coder le backend, créez dans Postman un **Mock Server** simulant les 4 retours JSON de référence :
      * **Cas 1 (`?p=1&d1=2022-01-01&d2=2022-12-31`)** :
        ```json
        {
          "cas": "employe_periode",
          "employe_id": 1,
          "employe_nom": "Roland Mendel",
          "d1": "2022-01-01",
          "d2": "2022-12-31",
          "salaire_moyen": 5300.0
        }
        ```
      * **Cas 2 (`?p=1&d1=2022-01-01`)** :
        ```json
        {
          "cas": "employe_partir_de",
          "employe_id": 1,
          "employe_nom": "Roland Mendel",
          "date_debut": "2022-01-01",
          "salaire_moyen": 5400.0
        }
        ```
      * **Cas 3 (`?d1=2022-01-01&d2=2022-12-31`)** :
        ```json
        {
          "cas": "mediane_periode",
          "d1": "2022-01-01",
          "d2": "2022-12-31",
          "nombre_employes": 3,
          "moyennes_individuelles": [5300.0, 6600.0, 8000.0],
          "mediane_des_moyennes": 6600.0
        }
        ```
      * **Cas 4 (`/api/salaires/periode`)** :
        ```json
        {
          "cas": "mediane_globale",
          "nombre_employes": 3,
          "moyennes_individuelles": [5200.0, 6600.0, 8000.0],
          "mediane_des_moyennes": 6600.0
        }
        ```

  * **2. Côté Frontend (IHM Web & JavaScript - `index.html`, `app.js`)** :
    * **Comprendre la structure HTML fournie :**  
      Ouvrez `nginx/html/index.html` (section `sec-periode`). Les éléments suivants sont mis à disposition :
      * `<input id="input-periode-p">` : champ numérique pour l'identifiant employé `p` (optionnel).
      * `<input id="input-periode-d1">` : champ de date pour la date de début `d1`.
      * `<input id="input-periode-d2">` : champ de date pour la date de fin `d2`.
      * `<button id="btn-periode">` : bouton « Interroger l'API Période ».
      * `<button id="btn-periode-reset">` : bouton « Réinitialiser les filtres ».
      * Balises `<span>` d'affichage dans `#preview-periode` :
        * `<span id="span-periode-cas">` : cas détecté par l'API (`employe_periode`, `mediane_globale`, etc.).
        * `<span id="span-periode-employe">` : nom et ID de l'employé concerné (ou mention globale).
        * `<span id="span-periode-dates">` : période appliquée aux calculs.
        * `<span id="span-periode-moyennes">` : série des moyennes calculées pour chaque employé.
        * `<span id="span-periode-resultat">` : valeur statistique finale (salaire moyen ou médiane en €).
      * `<pre id="output-periode">` : zone d'affichage pour la réponse JSON brute formatée.
    * **Développement dans `nginx/html/app.js` :**
      * Câblez l'écouteur d'événements `click` sur `btn-periode`.
      * Récupérez les valeurs saisies et construisez dynamiquement la Query String avec `URLSearchParams` (en n'ajoutant que les paramètres renseignés).
      * Connectez temporairement votre `fetch()` vers votre Mock Postman pour valider que tous les éléments du DOM sont mis à jour proprement.

  * **3. Côté Backend (MySQL CRUD2 & Flask - `api/db.py`, `api/app.py`)** :
    * **Connexion à `CRUD2` (`api/db.py`) :**
      * Mettez à jour `get_db_connection(database=None)` pour qu'elle accepte un nom de base optionnel (par défaut `CRUD` pour préserver l'Exercice 6, ou `CRUD2` si passé en argument).
    * **Conception et validation de vos requêtes SQL dans MySQL Workbench :**
      * Avant d'écrire votre code Python dans `api/db.py`, connectez-vous à la base `CRUD2` avec **MySQL Workbench** (ou le client en ligne de commande Docker).
      * Pour chacun des 4 cas de la matrice de décision, vous devez concevoir et tester la requête SQL correspondante :
        * *Cas 1 (`p` présent, `d1` et `d2` renseignés)* :  
          Rédigez la requête avec jointure (`employes` et `salaires`) calculant la moyenne (`AVG(s.salary)`) pour l'employé d'identifiant `p` sur la période comprise entre `d1` et `d2`.  
          *Test dans Workbench :* Pour `p=1`, `d1='2022-01-01'` et `d2='2022-12-31'`, votre requête doit renvoyer la moyenne **5300.00 €** pour Roland Mendel.
        * *Cas 2 (`p` présent, une seule date `d1` ou `d2`)* :  
          Adaptez la clause de filtrage sur la date (`s.date >= ...`) pour calculer le salaire moyen à partir de la date fournie.  
          *Test dans Workbench :* Pour `p=1` et `d1='2022-01-01'`, votre requête doit renvoyer la moyenne **5400.00 €**.
        * *Cas 3 (`p` absent, `d1` et `d2` renseignés)* :  
          Rédigez la requête calculant la moyenne des salaires de **chaque employé** sur la période `d1` à `d2`. Quelle clause de regroupement (`GROUP BY`) devez-vous employer ?  
          *Test dans Workbench :* Sur l'année 2022, votre requête doit renvoyer 3 lignes correspondant aux moyennes respectives des 3 employés : `5300.00 €`, `6600.00 €` et `8000.00 €`.
        * *Cas 4 (`p`, `d1` et `d2` tous absents)* :  
          Rédigez la requête calculant le salaire moyen global de chaque employé, toutes dates confondues.  
          *Test dans Workbench :* Votre requête doit renvoyer les 3 moyennes historiques : `5200.00 €`, `6600.00 €` et `8000.00 €`.
      * Une fois vos requêtes validées dans MySQL Workbench, intégrez-les dans les fonctions de `api/db.py` en les sécurisant sous forme de **requêtes préparées** (remplacez les valeurs littérales par les marqueurs de substitution `%s` et passez les arguments dans le tuple de paramètres).
    * **Calcul de la médiane en Python (`api/app.py`) :**
      * MySQL ne dispose pas de fonction native standard `MEDIAN()`.
      * Les moyennes individuelles sont donc calculées en SQL avec `AVG()`, puis récupérées sous forme de liste Python `[moyenne1, moyenne2, ...]`.
      * Vous devez utiliser vos fonctions maison `tri_selection_copie()` et `mediane()` pour trier les moyennes et en extraire la médiane exacte.
    * **Route Flask (`/api/salaires/periode`) :**
      * Récupérez `request.args.get('p')`, `request.args.get('d1')` et `request.args.get('d2')`.
      * Déterminez le cas approprié parmi les 4 configurations.
      * Renvoyez la réponse JSON structurée avec `jsonify(...)`.
      * Dans `app.js`, reconnectez l'appel `fetch()` sur l'API Flask locale.

* **Données de référence BDD (`CRUD2`)** :
  * 3 employés ($N=3$, impair) :
    * **Roland Mendel (id=1)** : salaires 4800, 5000, 5200, 5400, 5600 €
      * Moyenne globale : **5200.00 €** | Moyenne 2022 : **5300.00 €** | Moyenne depuis 2022-01-01 : **5400.00 €**
    * **Victoria Ashworth (id=2)** : salaires 6200, 6500, 6700, 7000 €
      * Moyenne globale : **6600.00 €** | Moyenne 2022 : **6600.00 €**
    * **Martin Blank (id=3)** : salaires 7500, 7800, 8200, 8500 €
      * Moyenne globale : **8000.00 €** | Moyenne 2022 : **8000.00 €**
  * **Médiane globale (Cas 4)** : série triée `[5200.0, 6600.0, 8000.0]` $\rightarrow$ Médiane = **6600.00 €**.
  * **Médiane sur 2022 (Cas 3)** : série triée `[5300.0, 6600.0, 8000.0]` $\rightarrow$ Médiane = **6600.00 €**.

* **Exemples de tests curl** :
  ```bash
  # Cas 1 : Roland Mendel sur l'année 2022 (Attendu : 5300.0 €)
  curl "http://localhost/api/salaires/periode?p=1&d1=2022-01-01&d2=2022-12-31"

  # Cas 2 : Roland Mendel à partir du 2022-01-01 (Attendu : 5400.0 €)
  curl "http://localhost/api/salaires/periode?p=1&d1=2022-01-01"

  # Cas 3 : Médiane des employés sur 2022 (Attendu : 6600.0 €)
  curl "http://localhost/api/salaires/periode?d1=2022-01-01&d2=2022-12-31"

  # Cas 4 : Médiane globale toutes dates confondues (Attendu : 6600.0 €)
  curl "http://localhost/api/salaires/periode"
  ```

* **Améliorations** :
  * Renvoyez une erreur HTTP 400 (`Bad Request`) si le format des dates n'est pas `AAAA-MM-JJ` ou si `d1 > d2`.
  * Renvoyez une erreur HTTP 404 (`Not Found`) si l'employé `p` spécifié n'existe pas dans la base `CRUD2`.

