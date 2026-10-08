# Guide de Correction et Validation Technique - BTS CIEL

Ce document récapitule les commandes de test unitaires et d'intégration permettant de valider instantanément chaque exercice dans les conteneurs Docker.

---

## 1. Démarrage de l'environnement

```bash
docker compose up -d
```

---

## 2. Commandes de test par exercice et sorties attendues

### Exercice 0 : Fondamentaux Python (Bases Concrètes) & Statistiques (0.1 à 0.7)

#### Exercices 0.1 à 0.6 : Chaînes (str), Listes (append), Dictionnaires (dict) & Image Cachée
```bash
docker compose exec api python intro_base.py
# ou alternativement :
docker compose exec api python main.py intro
```
**Sortie attendue :**
```text
========================================================================
BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON (BASES CONCRÈTES)
========================================================================

--- [Exercice 0.1] Les Chaînes de caractères (str) & Slicing ---
Saisie brute       : '   BTS CIEL 2026   '
Texte nettoyé      : 'bts ciel 2026'
'radar' est palindrome ? True
'python' est palindrome ? False
'kayak' est palindrome ? True
Villes découpées   : ['Paris', 'Lyon', 'Marseille', 'Toulouse']

--- [Exercice 0.2] Les Listes (list) & Accumulateur .append() (push JS) ---
Liste initiale     : [12, 5, 8, 21, 14, 3, 30]
Pairs (avec .append) : [12, 8, 14, 30]
Somme = 93.0 | Moyenne = 13.29

--- [Exercice 0.3] Les Dictionnaires (dict) & Liste de fiches ---
Nombre d'élèves    : 4
Moyenne de classe  : 11.75/20
Élèves admis       : ['Alice', 'Nicolas']

--- [Exercices 0.4 & 0.5] Traitement d'Image : Image Cachée dans une Image ---
Matrice apparente 8x8 (niveaux de gris) :
  [120, 135, 143, 110, 102, 187, 191, 104]
  [115, 133, 141, 127, 189, 175, 163, 147]
  [161, 179, 145, 137, 189, 177, 123, 145]
  ...

Révélation de l'image secrète par parité des pixels (pixel % 2 != 0) :
+--------+
| ##  ## |
|########|
|########|
|########|
| ###### |
|  ####  |
|   ##   |
|        |
+--------+
-> L'image secrète (un cœur) a été révélée avec succès !
========================================================================
```

---

#### Exercice 0.7 : Statistiques élémentaires et Problème de Nicolas
```bash
docker compose exec api python main.py
```
**Sortie attendue :**
```text
=== EXERCICE 0.7 : Statistiques élémentaires et Problème de Nicolas ===
Salaires de l'entreprise : [1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000]
Moyenne des salaires : 2500.00 €
Salaires triés       : [1500, 1500, 1700, 1800, 2000, 2200, 3300, 4000, 4500]
Médiane des salaires : 2000.00 €
Salaire de Nicolas   : 2200.00 €
-> Problématique : Nicolas gagne 2 200 € alors que le salaire moyen est de 2 500 €.
   Il affirme : "Je suis dans les moins bien payés de l'entreprise !"
-> Analyse : FAUX. Nicolas confond salaire moyen et salaire médian.
   La médiane réelle est de 2000.00 €. Avec 2200.00 €, Nicolas se situe
   au-dessus de la médiane (6e sur 9). Il fait partie des salariés les mieux rémunérés.
   La moyenne est tirée vers le haut par les salaires extrêmes (4000 € et 4500 €).
```

---

### Exercice 1 : Triangle console
```bash
docker compose exec api python triangle.py 4
```
**Sortie attendue :**
```text
*
**
***
****
```

---

### Exercice 2 : Table de multiplication
```bash
docker compose exec api python multiplication.py 4 5
```
**Sortie attendue :**
```text
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
```

---

### Exercice 3 : Récursivité vs Itération
```bash
docker compose exec api python recursion.py
```
**Sortie attendue :**
```text
Somme iterative(5)   : 15
Somme recursive(5)   : 15
Factorielle iter(5)  : 120
Factorielle recur(5) : 120
```

---

### Exercice 4.1 : Tri par sélection (Copie vs En place)
```bash
docker compose exec api python tri_selection.py
```
**Sortie attendue :**
```text
Tableau original : [15, 3, 22, 8, 19]
Après tri_selection_copie(t) -> [3, 8, 15, 19, 22]
Tableau original non modifié : [15, 3, 22, 8, 19]
Après tri_selection_en_place(t) -> t a été modifié directement : [3, 8, 15, 19, 22]
```

---

### Exercice 4.2 : Route API Tri & IHM Saisie Dynamique
* **Vidéo de référence** : https://drive.google.com/file/d/1_iikt1uk9Wx-tPY79woa0aJHjuJ83r5l/view?usp=drive_link (ou ressource locale : `resources/video_saisie_tri_ex4_2.mp4`)
* **Validation API (curl)** :
```bash
curl -s "http://localhost/api/tri?t=1500,4500,2200,1500,3300,1800,1700,2000,4000"
```
**Sortie attendue :**
```json
{
  "mediane": 2000.0,
  "original": [1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000],
  "tri": [1500, 1500, 1700, 1800, 2000, 2200, 3300, 4000, 4500]
}
```

* **Validation Web & DOM** :
  1. Ouvrir `http://localhost`.
  2. Saisie manuelle : saisir des entiers > 0 dans le champ et cliquer sur **« Ajouter (push) »** (ou touche Entrée). Le tableau `[val1, val2, ...]` se remplit en direct.
  3. Saisir une valeur <= 0 (ex: 0 ou -1) : la condition d'arrêt déclenche automatiquement la requête `fetch` vers `/api/tri?t=...`.
  4. Constater l'affichage dans le DOM du tableau original, du tableau trié et de la médiane.
  5. Ou cliquer sur **« Saisie via prompt() »** pour exécuter la saisie en boucle dialoguée conforme à la vidéo.

---

### Exercice 5 : Fusion de tableaux (API & Client Web DOM)
* **Vidéo de référence** : https://www.youtube.com/watch?v=aGkpJFJ9t4k (ou ressource locale : `resources/video_cahier_des_charges_ex5.mp4`)
* **Validation API (curl)** :
```bash
curl -s "http://localhost/api/fusion?t1=12,18,5&t2=20,8,14"
```
**Sortie attendue :**
```json
{
  "t1": [12, 18, 5],
  "t2": [20, 8, 14],
  "fusion": [12, 18, 5, 20, 8, 14],
  "tri": [5, 8, 12, 14, 18, 20],
  "mediane": 13.0
}
```

* **Validation Web & DOM** :
  1. Ouvrir `http://localhost`.
  2. Renseigner `Tableau 1` et `Tableau 2` ou conserver les valeurs par défaut.
  3. Cliquer sur **« Envoyer, Fusionner & Afficher dans le DOM »**.
  4. Constater la mise à jour immédiate des champs `span-t1`, `span-t2`, `span-fusion`, `span-fusion-tri` et `span-fusion-mediane` dans le DOM.

**Réponse à la question théorique de l'exercice 5 :**
Pour transmettre 3 tableaux, il existe deux manières idiomatiques :
1. Via des paramètres nommés distincts : `GET /api/fusion?t1=1,2&t2=3,4&t3=5,6`
2. Via la répétition du même paramètre intercepté par `request.args.getlist('t')` : `GET /api/fusion?t=1,2&t=3,4&t=5,6`

---

### Exercice 6 : Base de données MySQL

#### 1. Statistiques globales
```bash
curl -s "http://localhost/api/salaires/stats"
```
**Sortie attendue :**
```json
{
  "mediane": 16500.0,
  "moyenne": 30116.67,
  "nombre_employes": 6,
  "salaires_bruts": [6500, 8000, 1200, 25000, 100000, 40000],
  "salaires_tries": [1200, 6500, 8000, 25000, 40000, 100000]
}
```

#### 2. Comparaison d'un employé (Martin Blank - ID 3, 8000 €)
```bash
curl -s "http://localhost/api/employees/3/comparaison"
```
**Sortie attendue :**
```json
{
  "employe": {
    "address": "25, Rue Lauriston, Paris",
    "id": 3,
    "name": "Martin Blank",
    "salary": 8000
  },
  "statistiques_globales": {
    "mediane": 16500.0,
    "moyenne": 30116.67
  },
  "situation": {
    "par_rapport_a_la_mediane": "inférieur",
    "par_rapport_a_la_moyenne": "inférieur"
  }
}
```

#### 3. Test de gestion d'erreur (ID inconnu)
```bash
curl -s -w "\nHTTP Code: %{http_code}\n" "http://localhost/api/employees/999/comparaison"
```
**Sortie attendue :**
```json
{"erreur": "Employé introuvable"}
HTTP Code: 404
```
