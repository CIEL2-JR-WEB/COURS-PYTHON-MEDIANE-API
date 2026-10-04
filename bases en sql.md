# Support de cours & Exercices pratiques : Les bases de SQL
**BTS CIEL (Option Informatique et Réseaux) — Module Bases de données & API**

Ce support prépare directement à l'**Exercice 6** du TP. Il vous permet de maîtriser les requêtes SQL fondamentales nécessaires pour interroger la table `employees` de la base `CRUD` avant de manipuler ces données en Python avec Flask.

---

## 1. Environnement de travail & Connexion à MySQL

La base de données MySQL 8 s'exécute dans le conteneur Docker `db`.  
Pour vous connecter directement en ligne de commande au serveur MySQL et exécuter des requêtes interactives, ouvrez un terminal à la racine du projet et lancez :

```bash
docker compose exec db mysql -u eleve -peleve CRUD
```

> **Explication de la commande :**
> - `docker compose exec db` : exécute une commande dans le conteneur du service `db`.
> - `mysql` : lance le client interactif MySQL en ligne de commande.
> - `-u eleve` : utilisateur applicatif du TP.
> - `-peleve` : mot de passe associé (`eleve`).
> - `CRUD` : nom de la base de données sélectionnée par défaut.

Pour quitter le client MySQL à tout moment, tapez :
```sql
EXIT;
```

---

## 2. Découverte de la table `employees`

### Structure de la table
Pour inspecter la structure d'une table, utilisez la commande `DESCRIBE` :
```sql
DESCRIBE employees;
```

**Résultat attendu :**
```text
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| id      | int          | NO   | PRI | NULL    |       |
| name    | varchar(100) | NO   |     | NULL    |       |
| address | varchar(255) | NO   |     | NULL    |       |
| salary  | int          | NO   |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
```

*Analyse des colonnes :*
- `id` : entier (`INT`), clé primaire (`PRI`), identifiant unique non nul (`NOT NULL`).
- `name` : chaîne de caractères de taille maximale 100 (`VARCHAR(100)`), stocke le nom complet de l'employé.
- `address` : chaîne de caractères (`VARCHAR(255)`), adresse postale de l'employé.
- `salary` : entier (`INT`), montant du salaire mensuel brut en euros (€).

---

## 3. Série d'exercices très progressifs

---

### Niveau 1 : Projection et sélection globale (`SELECT ... FROM`)

La commande de base pour lire des données en SQL est `SELECT`.

#### Syntaxe :
```sql
SELECT colonne1, colonne2 FROM nom_table;
-- ou pour toutes les colonnes :
SELECT * FROM nom_table;
```

#### Mini-Exercice 1.1 : Lecture complète
Affichez la totalité des colonnes et des lignes de la table `employees`.

*Requête à saisir :*
```sql
SELECT * FROM employees;
```

**Sortie attendue :**
```text
+----+-------------------+--------------------------+--------+
| id | name              | address                  | salary |
+----+-------------------+--------------------------+--------+
|  2 | Victoria Ashworth | 35 King George, London   |   6500 |
|  3 | Martin Blank      | 25, Rue Lauriston, Paris |   8000 |
|  4 | Alain Gouiri      | 3 allee du Paradis       |   1200 |
|  8 | Thomas Demarcy    | 9 rue du Louvre          |  25000 |
| 20 | test              | test                     | 100000 |
| 21 | testo             | tosta                    |  40000 |
+----+-------------------+--------------------------+--------+
6 rows in set (0.00 sec)
```

#### Mini-Exercice 1.2 : Projection ciblée (Préparation à `get_all_salaries()`)
Pour l'Exercice 6, votre code Python n'aura besoin que des salaires pour calculer la moyenne et la médiane.  
Écrivez la requête qui n'extrait **que** la colonne `salary` de la table `employees`.

*Requête à saisir :*
```sql
SELECT salary FROM employees;
```

**Sortie attendue :**
```text
+--------+
| salary |
+--------+
|   6500 |
|   8000 |
|   1200 |
|  25000 |
| 100000 |
|  40000 |
+--------+
```

---

### Niveau 2 : Filtrage avec conditions (`WHERE`)

La clause `WHERE` permet de restreindre les résultats aux lignes vérifiant une condition logique.

#### Opérateurs usuels :
- Égalité : `=`
- Différent : `<>` ou `!=`
- Comparaisons : `>`, `<`, `>=`, `<=`
- Combinaisons : `AND`, `OR`, `NOT`

#### Mini-Exercice 2.1 : Recherche par identifiant (Préparation à `get_employee_by_id()`)
Affichez toutes les informations de l'employé dont l'identifiant `id` est égal à `3`.

*Requête à saisir :*
```sql
SELECT id, name, address, salary FROM employees WHERE id = 3;
```

**Sortie attendue :**
```text
+----+--------------+--------------------------+--------+
| id | name         | address                  | salary |
+----+--------------+--------------------------+--------+
|  3 | Martin Blank | 25, Rue Lauriston, Paris |   8000 |
+----+--------------+--------------------------+--------+
1 row in set (0.00 sec)
```

#### Mini-Exercice 2.2 : Filtrage sur les salaires élevés
Affichez le nom et le salaire des employés gagnant **strictement plus de 20 000 €**.

*Requête à saisir :*
```sql
SELECT name, salary FROM employees WHERE salary > 20000;
```

**Sortie attendue :**
```text
+----------------+--------+
| name           | salary |
+----------------+--------+
| Thomas Demarcy |  25000 |
| test           | 100000 |
| testo          |  40000 |
+----------------+--------+
```

---

### Niveau 3 : Tri des données (`ORDER BY`)

Pour observer l'ordre des salaires et appréhender le calcul de la médiane, on utilise la clause `ORDER BY`.

#### Syntaxe :
```sql
SELECT ... FROM nom_table ORDER BY nom_colonne ASC;  -- Croissant (par défaut)
SELECT ... FROM nom_table ORDER BY nom_colonne DESC; -- Décroissant
```

#### Mini-Exercice 3.1 : Salaires par ordre croissant
Affichez le nom et le salaire de tous les employés, triés du plus bas salaire au plus élevé.

*Requête à saisir :*
```sql
SELECT name, salary FROM employees ORDER BY salary ASC;
```

**Sortie attendue :**
```text
+-------------------+--------+
| name              | salary |
+-------------------+--------+
| Alain Gouiri      |   1200 |
| Victoria Ashworth |   6500 |
| Martin Blank      |   8000 |
| Thomas Demarcy    |  25000 |
| testo             |  40000 |
| test              | 100000 |
+-------------------+--------+
```

> 💡 **Observation pour la médiane :**  
> L'effectif total est $N = 6$ (pair).  
> Les deux valeurs centrales aux positions 3 et 4 sont **8 000 €** et **25 000 €**.  
> La médiane vaut donc : $(8000 + 25000) / 2$ = **16 500 €**.

---

### Niveau 4 : Fonctions d'agrégation statistiques (`COUNT`, `AVG`, `MIN`, `MAX`)

Le moteur SQL sait effectuer des calculs statistiques globaux sans transférer toutes les lignes au client.

#### Fonctions principales :
- `COUNT(*)` : compte le nombre total de lignes.
- `SUM(colonne)` : somme des valeurs de la colonne.
- `AVG(colonne)` : moyenne arithmétique de la colonne.
- `MIN(colonne)` / `MAX(colonne)` : valeur minimale / maximale.

#### Mini-Exercice 4.1 : Synthèse statistique en une seule requête
Calculez en SQL le nombre d'employés, la moyenne des salaires, ainsi que les salaires minimum et maximum.

*Requête à saisir :*
```sql
SELECT 
    COUNT(*) AS total_salaries,
    AVG(salary) AS salaire_moyen,
    MIN(salary) AS salaire_min,
    MAX(salary) AS salaire_max
FROM employees;
```

**Sortie attendue :**
```text
+----------------+---------------+-------------+-------------+
| total_salaries | salaire_moyen | salaire_min | salaire_max |
+----------------+---------------+-------------+-------------+
|              6 |    30116.6667 |        1200 |      100000 |
+----------------+---------------+-------------+-------------+
```

---

### Niveau 5 : Passage de SQL à Python & Sécurité (Injections SQL)

Dans l'Exercice 6, vous utiliserez le connecteur Python `mysql.connector`.

#### Règle absolue de cybersécurité :
❌ **NE JAMAIS concaténer une variable utilisateur dans une chaîne SQL :**
```python
# FAILLE DE SÉCURITÉ CRITIQUE (Injection SQL) :
emp_id = request.args.get("id")
curseur.execute(f"SELECT * FROM employees WHERE id = {emp_id}")
```

✅ **Toujours utiliser une requête paramétrée avec `%s` :**
```python
# CODE SÉCURISÉ (Requête préparée) :
emp_id = request.args.get("id")
curseur.execute(
    "SELECT id, name, address, salary FROM employees WHERE id = %s",
    (emp_id,)
)
resultat = curseur.fetchone()
```
Le connecteur se charge d'échapper et de typer la variable, neutralisant toute tentative d'injection SQL.

---

## 4. Synthèse des requêtes indispensables pour l'Exercice 6

| Objectif Python dans `api/db.py` | Requête SQL correspondante |
| :--- | :--- |
| **Lister tous les salaires** (`get_all_salaries`) | `SELECT salary FROM employees;` |
| **Rechercher un employé par son ID** (`get_employee_by_id`) | `SELECT id, name, address, salary FROM employees WHERE id = %s;` |
| **Vérifier les données en direct** | `SELECT * FROM employees;` |

---

## 5. Prêt pour l'Exercice 6 !

Vous disposez maintenant de toutes les notions SQL nécessaires.

👉 **Reprenez le sujet principal du TP pour réaliser l'Exercice 6 :**  
[Retour au README.md — Exercice 6 : Connexion MySQL & Comparaison de salaire](README.md#exercice-6--connexion-mysql--comparaison-de-salaire)
