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

Avant d'aborder la programmation web et les bases de données, cette partie introductive pose les gammes indispensables du langage Python. **Aucun concept complexe ou cyber n'est requis** : nous manipulons du texte, des listes, des dictionnaires et une grille d'image dans la console.

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

#### 2. Entraînement : Chaînes de Caractères (`str`) & Slicing

```python
# Rappel Slicing : chaine[debut:fin:pas]
s = "PYTHON2026"
s[0]     # 'P' (premier caractère)
s[-1]    # '6' (dernier caractère)
s[:6]    # 'PYTHON' (du début à l'indice 6 exclu)
s[6:]    # '2026' (de l'indice 6 à la fin)
s[::-1]  # '6202NOHTYP' (inversion complète !)
```

* **Exercice 0.1 (Nettoyage & mise en forme de texte)** :  
  Écrivez une fonction `nettoyer_texte(s)` qui supprime les espaces inutiles au début et à la fin (`.strip()`) et convertit l'ensemble en minuscules (`.lower()`).
* **Exercice 0.2 (Slicing élémentaire & Palindrome)** :  
  Écrivez `est_palindrome(mot)` qui retourne `True` si un mot se lit identiquement dans les deux sens (ex: `"radar"`, `"kayak"`) en comparant simplement le mot à son inversion par slicing : `mot == mot[::-1]`.
* **Exercice 0.3 (Découpage & recomposition avec `.split()` et `.join()`)** :  
  À partir d'une chaîne `"Paris,Lyon,Marseille,Toulouse"`, découpez les éléments dans une liste Python avec `.split(",")`. Affichez chaque ville sur une ligne, puis recollez-les avec un tiret grâce à `"-".join(liste)`.

---

#### 3. Entraînement : Les Listes (`list`) & l'Accumulateur (`append` vs `push`)

* **Exercice 0.4 (Filtrage avec accumulateur `.append()`)** :  
  Soit une liste d'entiers `nombres = [12, 5, 8, 21, 14, 3, 30]`. En utilisant une boucle `for` et la méthode `.append()`, construisez une nouvelle liste `pairs` ne contenant que les nombres pairs (`n % 2 == 0`).
* **Exercice 0.5 (Calculs élémentaires sans fonction magique)** :  
  À partir d'une liste de notes `[12.5, 14.0, 9.0, 16.5, 11.0]`, écrivez une boucle calculant manuellement la somme totale et déduisez-en la moyenne arrondie à deux décimales avec `round(..., 2)`.

---

#### 4. Entraînement : Les Dictionnaires (`dict`) & Tableaux de Fiches

* **Exercice 0.6 (Fiche d'un étudiant & accès sécurisé `.get()`)** :  
  Créez un dictionnaire `eleve = {"nom": "Nicolas", "age": 19, "note": 14.5}`.  
  Ajoutez la clé `"ville": "Toulouse"`. Constatez ce qui se passe si vous demandez une clé inexistante `eleve["option"]` (`KeyError`). Sécurisez l'accès avec `eleve.get("option", "Aucune")`.
* **Exercice 0.7 (Parcours d'une liste de dictionnaires)** :  
  Soit la liste de 4 élèves :  
  ```python
  classe = [
      {"nom": "Alice", "note": 14.5},
      {"nom": "Bob", "note": 8.0},
      {"nom": "Nicolas", "note": 15.0},
      {"nom": "Chloé", "note": 9.5}
  ]
  ```
  1. Parcourez la liste pour calculer la moyenne générale de la classe.  
  2. Construisez avec `.append()` une nouvelle liste contenant uniquement les élèves admis (note $\ge 10.0$).

---

#### 5. Application Visuelle & Concrète : Traitement d'Image & L'Image Cachée

> 💡 **Démystifier une image numérique :**  
> Une image en noir et blanc n'est rien d'autre qu'une **grille 2D de pixels** (une liste de listes en Python) ! Chaque case contient une valeur lumineuse.

* **Exercice 0.8 (Afficher une image matricielle en console)** :  
  Soit une grille 2D de pixels $0$ (noir) et $1$ (blanc) :
  ```python
  dessin = [
      [0, 1, 1, 0],
      [1, 0, 0, 1],
      [1, 1, 1, 1],
      [1, 0, 0, 1]
  ]
  ```
  À l'aide d'une double boucle `for ligne in dessin:` et `for pixel in ligne:`, affichez l'image en remplaçant les `1` par le caractère `'#'` et les `0` par un espace `' '`. Vous observez la lettre **A** se dessiner dans la console !

* **Exercice 0.9 (Révéler une Image Cachée dans une Image)** :  
  Une image apparemment banale (matrice hôte $8 \times 8$) contient des niveaux de gris ordinaires compris entre 100 et 200 :
  ```python
  image_hote = [
      [120, 135, 143, 110, 102, 187, 191, 104],
      [115, 133, 141, 127, 189, 175, 163, 147],
      [161, 179, 145, 137, 189, 177, 123, 145],
      [155, 143, 177, 189, 135, 157, 179, 191],
      [134, 189, 177, 143, 159, 175, 123, 168],
      [112, 156, 189, 177, 123, 145, 180, 142],
      [176, 142, 156, 189, 177, 124, 168, 142],
      [104, 118, 144, 134, 188, 176, 124, 140]
  ]
  ```
  **Le secret de l'image cachée :**  
  La forme cachée est dissimulée dans la **parité** de chaque pixel :
  * Si la valeur du pixel est **impaire** (`pixel % 2 != 0`) : le pixel caché est allumé (`'#'`).
  * Si la valeur du pixel est **paire** (`pixel % 2 == 0`) : le pixel caché est éteint (`' '`).

  **Travail à réaliser :**  
  Écrivez la fonction `reveler_image_secrete(image_hote)` qui :
  1. Parcourt chaque ligne de `image_hote`.
  2. Initialise une liste vide `ligne_revelee = []`.
  3. Parcourt chaque pixel de la ligne, teste sa parité et ajoute `'#'` ou `' '` avec **`.append()`**.
  4. Affiche la ligne reconstituée avec `print("".join(ligne_revelee))`.
  5. Exécutez le script : admirez le dessin secret (un magnifique cœur) qui apparaît sous vos yeux !

* **Exercice 0.10 (Cacher son propre motif secret)** :  
  Écrivez la fonction inverse `cacher_motif(image_base, motif_binaire)` qui ajuste la valeur des pixels (en ajoutant ou retirant 1) pour que la parité corresponde exactement à votre propre motif secret.

---

### 📍 DÉTAIL DES 6 SÉANCES DE COURS & TP

---

#### 📍 SÉANCE 1 : Fondations Python & Structures de Données (2 h)

* **Objectif** : L'étudiant est capable de modéliser des employés sous forme de liste de dictionnaires en mémoire, de la parcourir avec une boucle `for`, et d'en extraire des données par filtrage conditionnel (`if`).

* **📝 Travail sur table préalable (15 min — Débranché)** :
  1. *Schéma mémoire* : Dessinez sur feuille la liste `employes` de 3 salariés (Alice 1500, Bob 4500, Nicolas 2200) avec ses cases d'indices `[0]`, `[1]`, `[2]` reliées à leurs dictionnaires respectifs.
  2. *Accès direct* : Écrivez l'expression Python accédant au salaire de Bob (`employes[1]["salaire"]`).
  3. *Tableau de trace* : Tracez pas à pas la boucle calculant la masse salariale (`total += emp["salaire"]`) et le filtrage des salaires $> 2\,000\text{ €}$.

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
  1. *Tableau de trace* : Déroulez l'algorithme sur $t = [15, 3, 8]$ ($n = 3$) en notant pour chaque étape $i$ la valeur de `min_idx`, l'échange effectué, et l'état du tableau.
  2. *Schéma Référence vs Copie* : Dessinez ce qui se passe en mémoire pour `b = t` (même adresse) vs `b = list(t)` (nouvel espace mémoire).
  3. *Formule de la médiane* : Calculez les formules d'indices pour $N=9$ (impair, indice $N // 2$) et $N=8$ (pair, moyenne de $N // 2 - 1$ et $N // 2$).

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
  1. *Correspondance des types* : Remplissez la grille (Python `True` $\rightarrow$ JSON `true`, `None` $\rightarrow$ `null`, guillemets doubles stricts `""`).
  2. *Chasse aux anomalies* : Identifiez les 3 erreurs de syntaxe dans un extrait JSON piégé (apostrophes, virgule finale en trop, majuscule à `True`).
  3. *Organigramme try/except* : Dessinez l'arbre de décision en cas de fichier introuvable.

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
  1. *Requêtes préparées vs Concaténation de chaînes* : Soit une variable Python `id_saisi = 3`. Pourquoi ne doit-on jamais concaténer de chaînes de caractères avec `f"SELECT * FROM employes WHERE id = {id_saisi}"` ? Réécrivez la requête de façon propre et robuste en utilisant le marqueur de substitution `%s` et le tuple de paramètres `(id_saisi,)`.
  2. *Du tuple SQL au dictionnaire Python* : Reconstituez le dictionnaire créé par `DictCursor` pour la ligne `(3, "Nicolas", 2200.0)`.

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
  1. *Trame de la Requête HTTP Postman* : Remplissez `GET /api/employes/3 HTTP/1.1`, `Host: localhost:5000`, `Accept: application/json`.
  2. *Trame de la Réponse HTTP Flask* : Remplissez `HTTP/1.1 200 OK`, `Content-Type: application/json`, corps JSON de Nicolas.
  3. *Gestion d'erreur* : Quel code statut et corps JSON renvoyer pour un employé inconnu (`404`, `{"error": "..."}`) ?

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
  1. *Anatomie de l'URL* : Découpez `http://localhost:5000/api/employes/filtre?min=2000`. Complétez l'instruction Flask : `seuil = float(request.args.get("min", 0))`.
  2. *Chronogramme séquentiel (1 à 5)* : Clic bouton $\rightarrow$ émission `fetch()` $\rightarrow$ réponse JSON Flask/MySQL $\rightarrow$ promesse `.json()` $\rightarrow$ injection DOM.

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
* **Consignes** :
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
* **Consignes** :
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
* **Consignes** :
  * Codez `somme_iterative(n)` puis `somme_recursive(n)` pour calculer $1 + 2 + \dots + n$.
  * Codez `factorielle_iterative(n)` puis `factorielle_recursive(n)` ($n! = 1 \times 2 \times \dots \times n$).
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
* **Consignes** :
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
* **Consignes** :
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
* **Éléments HTML fournis dans `index.html` (section `sec-random`) :**
  * `<button id="btn-random">` : bouton « Générer & Analyser ».
  * `<span id="span-brut">` : balise affichant les 9 salaires bruts générés aléatoirement en JavaScript.
  * `<span id="span-trie">` : balise affichant la liste triée retournée par l'API Flask.
  * `<span id="span-mediane">` : balise affichant la médiane retournée par l'API Flask.
* **Consignes dans `nginx/html/app.js` :**
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
* **Consignes** :
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
* **Consignes** :
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
* **Consignes** :
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

