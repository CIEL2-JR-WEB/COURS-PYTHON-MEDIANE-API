# Support de cours & Exercices pratiques : Les jointures SQL & la modélisation relationnelle
**BTS CIEL (Option Informatique et Réseaux) — Module Bases de données & API**

Ce support fait suite à [`bases en sql.md`](bases%20en%20sql.md) et prépare directement à l'**Exercice 7** du TP. Il aborde la transition d'une table plate unique vers un schéma relationnel normalisé, l'intégrité référentielle, ainsi que l'écriture de jointures (`INNER JOIN`), d'agrégations temporelles (`AVG`, `GROUP BY`) et de requêtes multi-tables.

---

## 1. Environnement de travail & Connexion à la base `CRUD2`

Pour ces exercices, nous utilisons la nouvelle base de données **`CRUD2`**, hébergée sur le même serveur MySQL dans le conteneur Docker `db`.

Pour vous connecter en ligne de commande avec le compte applicatif `eleve` / `eleve` à la base `CRUD2`, ouvrez un terminal à la racine du projet et lancez :

```bash
docker compose exec db mysql -u eleve -peleve CRUD2
```

> **Rappel des paramètres de connexion :**
> - Conteneur : `ciel_mysql_db` (service `db`)
> - Utilisateur : `eleve`
> - Mot de passe : `eleve`
> - Base active : `CRUD2`

Pour quitter le client MySQL à tout moment :
```sql
EXIT;
```

---

## 2. De la table plate aux tables relationnelles

### Situation initiale : La table `employees`
Dans l'Exercice 6 (base `CRUD`), toutes les données d'un employé étaient regroupées dans une seule table :

```text
+----+-------------------+--------------------------+--------+
| id | name              | address                  | salary |
+----+-------------------+--------------------------+--------+
|  1 | Roland Mendel     | C/ Araquil, 67, Madrid   |   5000 |
|  2 | Victoria Ashworth | 35 King George, London   |   6500 |
|  3 | Martin Blank      | 25, Rue Lauriston, Paris |   8000 |
+----+-------------------+--------------------------+--------+
```

**Limites de cette structure :**
1. Un employé ne peut avoir qu'un seul salaire enregistré à un instant $T$.
2. Impossible d'historiser les augmentations ou de calculer des moyennes au fil du temps sans écraser la donnée précédente.
3. Si l'on dupliquait les lignes de l'employé pour chaque nouveau salaire, son adresse et son nom seraient répétés inutilement (redondance et risque d'incohérence).

---

### Question 1 : Décomposition en deux tables (`employes` et `salaires`)

Pour séparer l'identité de l'employé de son historique financier, nous créons deux tables distinctes reliées par une **clé étrangère** (*Foreign Key*) :

1. **Table `employes` (Entité parent)** :
   - `id` : identifiant unique de l'employé (`INT AUTO_INCREMENT PRIMARY KEY`).
   - `name` : nom et prénom (`VARCHAR(100)`).
   - `address` : adresse postale (`VARCHAR(255)`).

2. **Table `salaires` (Entité enfant)** :
   - `idsalaires` : identifiant unique de la fiche de paie (`INT AUTO_INCREMENT PRIMARY KEY`).
   - `salary` : montant du salaire perçu (`INT`).
   - `employes_id` : référence vers l'employé concerné (`INT`, clé étrangère pointant sur `employes(id)`).

```text
  +------------------+             +----------------------+
  |     employes     |             |       salaires       |
  +------------------+ 1       1..*+----------------------+
  | PK id            |<------------| FK employes_id       |
  |    name          |             | PK idsalaires        |
  |    address       |             |    salary            |
  +------------------+             +----------------------+
```

*Définition SQL des tables :*
```sql
CREATE TABLE employes (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE salaires (
    idsalaires INT NOT NULL AUTO_INCREMENT,
    salary INT NOT NULL,
    employes_id INT NOT NULL,
    PRIMARY KEY (idsalaires),
    FOREIGN KEY (employes_id) REFERENCES employes(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

### Le paradoxe de l'œuf et de la poule : Quelle table peupler en premier ?

> ❓ **Question :** Dans quel ordre devez-vous insérer vos données : la table `salaires` ou la table `employes` ? Pourquoi ?

**Explication & Règle d'or des SGBD relationnels :**
* La table **`employes` doit impérativement être peuplée en premier**.
* **Pourquoi ?** La table `salaires` possède une contrainte d'**intégrité référentielle** (`FOREIGN KEY (employes_id) REFERENCES employes(id)`). Le moteur MySQL vérifie qu'à chaque insertion dans `salaires`, la valeur passée dans `employes_id` existe déjà dans la table `employes`.
* Si vous essayez d'insérer un salaire en premier, MySQL rejettera la requête avec l'erreur `Error 1452: Cannot add or update a child row: a foreign key constraint fails`.

---

### Question 2 : Insertion dans la table `employes`

Insérez les 3 employés initiaux dans la table `employes` :

```sql
INSERT INTO employes (id, name, address) VALUES
(1, 'Roland Mendel', 'C/ Araquil, 67, Madrid'),
(2, 'Victoria Ashworth', '35 King George, London'),
(3, 'Martin Blank', '25, Rue Lauriston, Paris');
```

Vérifiez le contenu :
```sql
SELECT * FROM employes;
```

---

### Question 3 : Insertion dans la table `salaires`

Une fois les employés créés, insérez leurs salaires correspondants en renseignant la clé étrangère `employes_id` :

```sql
INSERT INTO salaires (idsalaires, salary, employes_id) VALUES
(1, 5000, 1),
(2, 6500, 2),
(3, 8000, 3);
```

Vérifiez le contenu :
```sql
SELECT * FROM salaires;
```

---

## 3. Les jointures internes (`INNER JOIN`) et les alias

### Question 4 : Récupérer les employés ayant un salaire $\ge 5000$ €

Pour rapprocher le nom d'un employé (stocké dans `employes`) et son salaire (stocké dans `salaires`), on effectue une **jointure interne** (`INNER JOIN`) sur la condition `employes.id = salaires.employes_id`.

#### Objectif :
Afficher le nom et le salaire des employés gagnant au moins 5000 €, triés par ordre croissant de salaire.

*Requête SQL :*
```sql
SELECT employes.name, salaires.salary
FROM employes
INNER JOIN salaires ON employes.id = salaires.employes_id
WHERE salaires.salary >= 5000
ORDER BY salaires.salary ASC;
```

**Sortie attendue :**
```text
+-------------------+--------+
| name              | salary |
+-------------------+--------+
| Roland Mendel     |   5000 |
| Victoria Ashworth |   6500 |
| Martin Blank      |   8000 |
+-------------------+--------+
3 rows in set (0.00 sec)
```

---

### Question 5 : Utilisation des alias de tables et de colonnes

Dans une requête complexe, préfixer chaque colonne par le nom complet de la table alourdit l'écriture.  
On utilise des **alias de tables** (`e` pour `employes`, `s` pour `salaires`) et des **alias de colonnes** (`AS nom_employe`, `AS salaire_mensuel`) pour clarifier le résultat.

#### Objectif :
Réécrire la requête précédente avec les alias `e` et `s`, et afficher les intitulés de colonnes en français.

*Requête SQL :*
```sql
SELECT e.name AS nom_employe, s.salary AS salaire_mensuel
FROM employes e
INNER JOIN salaires s ON e.id = s.employes_id
WHERE s.salary >= 5000
ORDER BY salaire_mensuel ASC;
```

**Sortie attendue :**
```text
+-------------------+-----------------+
| nom_employe       | salaire_mensuel |
+-------------------+-----------------+
| Roland Mendel     |            5000 |
| Victoria Ashworth |            6500 |
| Martin Blank      |            8000 |
+-------------------+-----------------+
```

---

## 4. Dimension temporelle & Agrégation (`AVG`, `GROUP BY`)

### Question 6 : Historisation des salaires

Dans une entreprise, le salaire affiché sur un tableau de bord annuel est généralement une **moyenne des rémunérations** perçues sur une période donnée (primes d'été, revalorisations, fin d'année).

> ❓ **Question :** Quelle information indispensable faut-il introduire dans notre modèle pour gérer cet historique ?

**Réponse :**  
Il faut ajouter une colonne temporelle dans la table `salaires`, par exemple **`date DATE`** (au format standard SQL `AAAA-MM-JJ`), indiquant la date de versement ou d'application du salaire.

*Évolution de la table `salaires` :*
```sql
ALTER TABLE salaires ADD COLUMN date DATE NOT NULL;
```

Grâce à cette colonne, un même employé (`employes_id = 1`) peut avoir plusieurs enregistrements de salaires à des dates différentes.

---

### Question 7 : Calculs de moyennes par employé et filtrage temporel

Dans la base `CRUD2` fournie, plusieurs salaires ont été enregistrés entre 2021 et 2023 pour chaque employé :
- **Roland Mendel (id=1)** :
  - `2021-01-15` : 4800 €
  - `2021-07-15` : 5000 €
  - `2022-01-15` : 5200 €
  - `2022-07-15` : 5400 €
  - `2023-01-15` : 5600 €
- **Victoria Ashworth (id=2)** :
  - `2021-03-01` : 6200 €
  - `2022-03-01` : 6500 €
  - `2022-09-01` : 6700 €
  - `2023-03-01` : 7000 €
- **Martin Blank (id=3)** :
  - `2021-06-01` : 7500 €
  - `2022-02-01` : 7800 €
  - `2022-08-01` : 8200 €
  - `2023-05-01` : 8500 €

---

#### 7.1. Salaire moyen de chaque employé depuis son embauche (`GROUP BY`)
Pour calculer la moyenne de chaque employé, on utilise la fonction d'agrégation `AVG()` combinée avec la clause `GROUP BY` :

*Requête SQL :*
```sql
SELECT e.id, e.name, ROUND(AVG(s.salary), 2) AS salaire_moyen
FROM employes e
INNER JOIN salaires s ON e.id = s.employes_id
GROUP BY e.id, e.name
ORDER BY e.id ASC;
```

**Sortie attendue :**
```text
+----+-------------------+---------------+
| id | name              | salaire_moyen |
+----+-------------------+---------------+
|  1 | Roland Mendel     |       5200.00 |
|  2 | Victoria Ashworth |       6600.00 |
|  3 | Martin Blank      |       8000.00 |
+----+-------------------+---------------+
```

---

#### 7.2. Salaire moyen de Roland Mendel sur l'année 2022
Pour restreindre le calcul à une personne et à une période précise, on ajoute des conditions dans la clause `WHERE` :

*Requête SQL :*
```sql
SELECT e.name, ROUND(AVG(s.salary), 2) AS salaire_moyen_2022
FROM employes e
INNER JOIN salaires s ON e.id = s.employes_id
WHERE e.name = 'Roland Mendel'
  AND s.date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY e.id, e.name;
```

**Sortie attendue :**
```text
+---------------+--------------------+
| name          | salaire_moyen_2022 |
+---------------+--------------------+
| Roland Mendel |            5300.00 |
+---------------+--------------------+
```
*(Calcul de vérification : $(5200 + 5400) / 2 = 5300.00$ €)*

---

## 5. Jointure sur plus de deux tables (Question 10)

Dans une application réelle (e-commerce, logistique, billetterie), l'information est souvent répartie sur 3 tables ou plus.

### Exemple e-commerce : `Customers`, `Products` et `Orders`
Considérons les trois tables créées dans `CRUD2` :

* **`Products`** :
```text
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
|          1 | Burger       |    10 |
|          2 | Sandwich     |    15 |
+------------+--------------+-------+
```

* **`Customers`** :
```text
+-------------+---------------+-----------------+
| customer_id | customer_name | email           |
+-------------+---------------+-----------------+
|           1 | Alice         | alice@alice.com |
|           2 | Bob           | bob@bob.com     |
+-------------+---------------+-----------------+
```

* **`Orders`** (table de liaison avec clés étrangères) :
```text
+----------+-------------+------------+
| order_id | customer_id | product_id |
+----------+-------------+------------+
|        1 |           1 |          1 |
|        2 |           1 |          2 |
|        3 |           2 |          1 |
+----------+-------------+------------+
```

#### Objectif de la Question 10 :
Écrire la requête avec jointures permettant d'obtenir le récapitulatif complet des commandes avec l'identifiant de commande, le nom du produit, le nom du client et le prix.

*Requête SQL :*
```sql
SELECT o.order_id, p.product_name, c.customer_name, p.price
FROM Orders o
INNER JOIN Customers c ON o.customer_id = c.customer_id
INNER JOIN Products p ON o.product_id = p.product_id
ORDER BY o.order_id ASC;
```

**Sortie attendue :**
```text
+----------+--------------+---------------+-------+
| order_id | product_name | customer_name | price |
+----------+--------------+---------------+-------+
|        1 | Burger       | Alice         |    10 |
|        2 | Sandwich     | Alice         |    15 |
|        3 | Burger       | Bob           |    10 |
+----------+--------------+---------------+-------+
3 rows in set (0.00 sec)
```

---

## 6. Démarche inverse : Rétro-ingénierie d'une requête SQL (Question 11)

En entreprise, un développeur doit régulièrement analyser des requêtes SQL existantes pour en déduire le modèle de données sous-jacent.

### Requête 1 (Étude de cas Marketing) :
```sql
SELECT sub.EmailAddress, de.CampaignName, web.AttendanceStatus
FROM _Subscribers AS sub
INNER JOIN DataExtension AS de 
  ON de.SubscriberKey = sub.SubscriberKey
INNER JOIN WebinarParticipants AS web 
  ON web.SubscriberKey = sub.SubscriberKey;
```

#### Déduction du schéma :
1. **Tables en jeu** :
   - `_Subscribers` (alias `sub`)
   - `DataExtension` (alias `de`)
   - `WebinarParticipants` (alias `web`)
2. **Clés de jointure** :
   - `SubscriberKey` est la clé commune reliant `_Subscribers` à `DataExtension` et `WebinarParticipants`.
3. **Attributs identifiés** :
   - `_Subscribers` : `SubscriberKey`, `EmailAddress`
   - `DataExtension` : `SubscriberKey`, `CampaignName`
   - `WebinarParticipants` : `SubscriberKey`, `AttendanceStatus`

---

### Requête 2 (Étude de cas Cinéma) :
```sql
SELECT f.titre
FROM Film AS f, Role AS r, Artiste AS a1, Artiste AS a2
WHERE f.idFilm = r.idFilm
  AND r.idActeur = a1.idArtiste
  AND f.idRealisateur = a2.idArtiste
  AND a2.nom = 'Burton'
  AND a1.nom = 'Depp';
```

#### Déduction du schéma relationnel :
1. **Tables & Clés primaires/étrangères** :
   - **`Film`** : `idFilm` (PK), `titre`, `idRealisateur` (FK vers `Artiste.idArtiste`).
   - **`Artiste`** : `idArtiste` (PK), `nom`. (Notez qu'elle apparaît deux fois via les alias `a1` pour l'acteur et `a2` pour le réalisateur).
   - **`Role`** : `idFilm` (FK vers `Film`), `idActeur` (FK vers `Artiste`).
2. **Sens de la requête** :
   - Cette requête sélectionne les titres des films réalisés par **Tim Burton** dans lesquels joue **Johnny Depp** (ex: *Edward aux mains d'argent*, *Sleepy Hollow*, *Charlie et la chocolaterie*).

---

> 🚀 **Vous maîtrisez désormais les jointures et l'agrégation SQL !**  
> Vous pouvez maintenant passer à l'**Exercice 7 dans le `README.md`** pour concevoir l'API Flask de calcul de salaire médian sur période.
