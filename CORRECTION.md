# Guide de Correction et Validation Technique - BTS CIEL

Ce document récapitule les commandes de test unitaires et d'intégration permettant de valider instantanément chaque exercice dans les conteneurs Docker.

---

## 1. Démarrage de l'environnement

```bash
docker compose up -d
```

---

## 2. Commandes de test par exercice et sorties attendues

### Exercice 0.1 & 0.2 : Statistiques et Problème de Nicolas
```bash
docker compose exec api python main.py
```
**Sortie attendue :**
```text
=== EXERCICE 0.1 & 0.2 : Statistiques et Problème de Nicolas ===
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

### Exercice 4.2 : Route API Tri
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

---

### Exercice 5 : Fusion de tableaux
```bash
curl -s "http://localhost/api/fusion?t1=12,18,5&t2=20,8,14"
```
**Sortie attendue :**
```json
{
  "fusion": [12, 18, 5, 20, 8, 14],
  "mediane": 13.0,
  "tri": [5, 8, 12, 14, 18, 20]
}
```

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
