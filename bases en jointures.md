# Support de cours & Exercices pratiques : Les jointures SQL & la modélisation relationnelle
**BTS CIEL (Option Informatique et Réseaux) — Module Bases de données & API**

Ce support fait suite à [`bases en sql.md`](bases%20en%20sql.md) et prépare directement à l'**Exercice 7** du TP. Il aborde la transition d'une table plate unique vers un schéma relationnel normalisé, l'intégrité référentielle, ainsi que l'écriture de jointures (`INNER JOIN`), d'agrégations temporelles (`AVG`, `GROUP BY`) et de requêtes multi-tables.

---

## 1. Environnement de travail & Connexion avec MySQL Workbench (IHM)

Pour concevoir, tester et visualiser vos requêtes SQL dans une interface graphique conviviale (IHM), vous utiliserez **MySQL Workbench**, le client graphique officiel de référence.

### 1.1. Paramétrage de la connexion dans MySQL Workbench
Le conteneur Docker `db` (`ciel_mysql_db`) expose son port `3306` sur votre machine hôte.

1. Lancez **MySQL Workbench** sur votre poste.
2. Sur la page d'accueil (*MySQL Connections*), cliquez sur le bouton **`+`** à côté de *MySQL Connections* pour créer une nouvelle connexion.
3. Renseignez les champs suivants :
   - **Connection Name** : `Docker MySQL - CRUD2`
   - **Connection Method** : `Standard (TCP/IP)`
   - **Hostname** : `127.0.0.1` (ou `localhost`)
   - **Port** : `3306`
   - **Username** : `eleve`
   - **Password** : cliquez sur *Store in Vault...* et saisissez `eleve`
   - **Default Schema** : `CRUD2`
4. Cliquez sur **Test Connection**. Un message confirmant le succès de la connexion doit s'afficher :  
   `"Successfully made the MySQL connection"`.
5. Cliquez sur **OK** pour enregistrer la connexion, puis double-cliquez sur la tuile créée pour ouvrir l'espace de travail.

```text
+----------------------------------------------------------------------------------+
| MySQL Workbench - [Docker MySQL - CRUD2]                                         |
+-----------------------------------+----------------------------------------------+
| SCHEMAS                           |  Query 1                                     |
| 📁 CRUD                           |  SELECT * FROM employes;                     |
| 📂 CRUD2                          |                                              |
|    📂 Tables                      |  [ ⚡ Exécuter ]                             |
|       📄 employes                 +----------------------------------------------+
|       📄 salaires                 |  Result Grid                                 |
|       📄 employees                |  id | name              | address            |
|       📄 Customers                |  1  | Roland Mendel     | C/ Araquil, 67...  |
|       📄 Orders                   |  2  | Victoria Ashworth | 35 King George...  |
|       📄 Products                 |  3  | Martin Blank      | 25, Rue Laurist... |
+-----------------------------------+----------------------------------------------+
```

### 1.2. Prise en main de l'IHM MySQL Workbench
* **Panneau de gauche (SCHEMAS)** : Explorez l'arborescence de la base `CRUD2`. Déroulez `Tables` pour afficher la liste des tables créées par le script d'initialisation. Faites un clic droit sur une table $\rightarrow$ *Select Rows - Limit 1000* pour un aperçu instantané.
* **Éditeur central (SQL Query Tab)** : C'est ici que vous saisirez toutes vos requêtes SQL.
* **Bouton d'exécution (Éclair ⚡)** : Cliquez sur l'icône éclair (ou raccourci clavier `Ctrl + Entrée`) pour exécuter la requête sous votre curseur.
* **Panneau inférieur (Result Grid)** : Affiche les résultats sous forme de tableau ordonné, avec le nombre de lignes retournées et le temps d'exécution.

> 💡 **Alternative en ligne de commande (Terminal) :**  
> Si vous préférez le terminal, vous pouvez toujours vous connecter via :
> ```bash
> docker compose exec db mysql -u eleve -peleve CRUD2
> ```

---

## 2. De la table plate aux tables relationnelles

### Situation initiale : La table `employees`
Dans l'Exercice 6 (base `CRUD`), toutes les données d'un employé étaient regroupées dans une seule table plate :

```text
+----+-------------------+--------------------------+--------+
| id | name              | address                  | salary |
+----+-------------------+--------------------------+--------+
|  1 | Roland Mendel     | C/ Araquil, 67, Madrid   |   5000 |
|  2 | Victoria Ashworth | 35 King George, London   |   6500 |
|  3 | Martin Blank      | 25, Rue Lauriston, Paris |   8000 |
+----+-------------------+--------------------------+--------+
```

**Limites majeures de cette structure :**
1. Un employé ne peut avoir qu'un seul salaire enregistré à un instant $T$.
2. Impossible d'historiser les augmentations ou de calculer des moyennes au fil du temps sans écraser la donnée précédente.
3. Si l'on dupliquait les lignes de l'employé pour chaque nouveau salaire, son adresse et son nom seraient répétés inutilement (redondance et risque d'incohérence).

---

### Question 1 : Modélisation en deux tables (`employes` et `salaires`)

Pour séparer l'identité de l'employé de son historique financier, nous créons deux tables distinctes reliées par une **clé étrangère** (*Foreign Key*) :

```text
  +------------------+             +----------------------+
  |     employes     |             |       salaires       |
  +------------------+ 1       1..*+----------------------+
  | PK id            |<------------| FK employes_id       |
  |    name          |             | PK idsalaires        |
  |    address       |             |    salary            |
  +------------------+             +----------------------+
```

#### À vous de jouer :
1. Observez la structure des tables `employes` et `salaires` dans le panneau *SCHEMAS* de MySQL Workbench (ou avec `DESCRIBE employes;` et `DESCRIBE salaires;`).
2. Quelle est la clé primaire (*Primary Key*) de chaque table ?
3. Quelle colonne de la table `salaires` assure la relation avec `employes` ? Quel est son rôle ?
4. Que signifie la contrainte `ON DELETE CASCADE` définie sur la clé étrangère ?

---

### Le paradoxe de l'œuf et de la poule : Quelle table peupler en premier ?

Dans une base de données relationnelle, les tables ne sont pas indépendantes.

#### À vous de jouer :
1. Selon vous, quelle table doit être peuplée en premier : `salaires` ou `employes` ? Pourquoi ?
2. **Test pratique dans MySQL Workbench :**  
   Dans un onglet SQL de Workbench, essayez d'exécuter la requête suivante qui tente d'enregistrer un salaire pour un employé inexistant (`employes_id = 99`) :
   ```sql
   INSERT INTO salaires (salary, employes_id) VALUES (4000, 99);
   ```
   *Quel message d'erreur MySQL retourne-t-il dans l'onglet Output en bas ?*

> 📌 **Règle d'or de l'intégrité référentielle :**  
> La table parente (`employes`) **doit obligatoirement être peuplée avant** la table enfant (`salaires`).  
> Si la valeur de `employes_id` n'existe pas encore dans la table `employes`, MySQL bloque l'opération avec l'erreur `Error 1452 (Cannot add or update a child row: a foreign key constraint fails)`.

---

### Questions 2 & 3 : Insertion des données initiales

#### À vous de jouer :
1. **Question 2 :** Rédigez la requête SQL `INSERT INTO employes ...` permettant d'insérer les 3 employés suivants :
   - ID 1 : `Roland Mendel`, résidant `C/ Araquil, 67, Madrid`
   - ID 2 : `Victoria Ashworth`, résidant `35 King George, London`
   - ID 3 : `Martin Blank`, résidant `25, Rue Lauriston, Paris`
2. **Question 3 :** Rédigez ensuite la requête SQL `INSERT INTO salaires ...` pour leur attribuer leur salaire initial :
   - Employé 1 $\rightarrow$ 5000 €
   - Employé 2 $\rightarrow$ 6500 €
   - Employé 3 $\rightarrow$ 8000 €
3. Exécutez `SELECT * FROM employes;` puis `SELECT * FROM salaires;` dans MySQL Workbench pour vérifier vos insertions.

*(Note : ces données sont déjà pré-insérées dans la base `CRUD2` fournie avec le projet).*

---

## 3. Les jointures internes (`INNER JOIN`) et les alias

### Question 4 : Employés avec un salaire supérieur ou égal à 5000 €

Pour afficher ensemble des informations réparties sur deux tables différentes (ici le nom dans `employes` et le salaire dans `salaires`), on utilise une **jointure interne** (`INNER JOIN`).

#### Rappel de syntaxe :
```sql
SELECT table1.colonneA, table2.colonneB
FROM table1
INNER JOIN table2 ON table1.cle_primaire = table2.cle_etrangere
WHERE condition
ORDER BY colonne;
```

#### À vous de jouer :
Écrivez la requête SQL permettant d'afficher le **nom** de l'employé et son **salaire** pour tous les employés ayant un salaire **supérieur ou égal à 5000 €**, classés par **salaire croissant**.

*Indices :*
- Projetez `employes.name` et `salaires.salary`.
- Effectuez la jointure `INNER JOIN salaires ON employes.id = salaires.employes_id`.
- Filtrez avec `WHERE salaires.salary >= 5000`.
- Triez avec `ORDER BY salaires.salary ASC`.

#### Résultat attendu dans le Result Grid de Workbench :
```text
+-------------------+--------+
| name              | salary |
+-------------------+--------+
| Roland Mendel     |   5000 |
| Victoria Ashworth |   6500 |
| Martin Blank      |   8000 |
+-------------------+--------+
3 rows returned
```

---

### Question 5 : Alias de tables et de colonnes

Dans une requête complexe, préfixer chaque colonne par le nom complet de la table alourdit la syntaxe.  
On utilise des **alias de tables** (`FROM employes e INNER JOIN salaires s`) et des **alias de colonnes** (`SELECT e.name AS nom_employe`).

#### À vous de jouer :
Reprenez la requête de la Question 4 et adaptez-la en respectant les consignes suivantes :
1. Définissez l'alias `e` pour la table `employes` et l'alias `s` pour la table `salaires`.
2. Renommez la colonne `name` en `nom_employe` dans le résultat affiché.
3. Renommez la colonne `salary` en `salaire_mensuel`.
4. Effectuez le tri croissant directement sur l'alias `salaire_mensuel`.

#### Résultat attendu dans le Result Grid de Workbench :
```text
+-------------------+-----------------+
| nom_employe       | salaire_mensuel |
+-------------------+-----------------+
| Roland Mendel     |            5000 |
| Victoria Ashworth |            6500 |
| Martin Blank      |            8000 |
+-------------------+-----------------+
3 rows returned
```

---

## 4. Dimension temporelle & Agrégation (`AVG`, `GROUP BY`)

### Question 6 : Historisation des rémunérations

Dans la vie réelle, la rémunération d'un collaborateur évolue au cours de sa carrière (augmentations annuelles, primes, promotions).

#### À vous de jouer :
1. Quelle information indispensable manque-t-il dans la structure actuelle de la table `salaires` pour savoir à quelle période correspond un montant donné ?
2. Quel type de données SQL standard permet d'enregistrer une date au format `AAAA-MM-JJ` ?
3. Écrivez la commande SQL `ALTER TABLE` qui permet d'ajouter une colonne `date` obligatoire dans la table `salaires`.

*(Note : cette colonne `date` est déjà présente dans la base `CRUD2` du TP).*

---

### Question 7 : Moyennes temporelles par employé

Dans la base `CRUD2`, chaque employé possède désormais un historique de salaires étalé entre 2021 et 2023 :
- **Roland Mendel (id=1)** : 5 salaires (4800 € en 2021, 5000 € en 2021, 5200 € en janv. 2022, 5400 € en juil. 2022, 5600 € en 2023).
- **Victoria Ashworth (id=2)** : 4 salaires (6200 € en 2021, 6500 € en 2022, 6700 € en 2022, 7000 € en 2023).
- **Martin Blank (id=3)** : 4 salaires (7500 € en 2021, 7800 € en 2022, 8200 € en 2022, 8500 € en 2023).

#### Rappel de syntaxe pour les agrégations :
```sql
SELECT e.id, AVG(s.salary) AS moyenne
FROM employes e
INNER JOIN salaires s ON e.id = s.employes_id
GROUP BY e.id;
```
> La clause `GROUP BY e.id` rassemble toutes les lignes associées à un même employé pour que la fonction `AVG()` calcule la moyenne de son groupe de lignes. La fonction `ROUND(valeur, 2)` permet d'arrondir à 2 décimales.

---

#### 7.1. Salaire moyen de chaque employé depuis son embauche
Écrivez la requête SQL affichant :
- L'identifiant de l'employé (`id`)
- Le nom complet de l'employé (`name`)
- La moyenne de ses salaires historiques arrondie à deux décimales sous l'intitulé `salaire_moyen`
Triez le résultat par `id` croissant.

#### Résultat attendu dans Workbench :
```text
+----+-------------------+---------------+
| id | name              | salaire_moyen |
+----+-------------------+---------------+
|  1 | Roland Mendel     |       5200.00 |
|  2 | Victoria Ashworth |       6600.00 |
|  3 | Martin Blank      |       8000.00 |
+----+-------------------+---------------+
3 rows returned
```

---

#### 7.2. Salaire moyen de Roland Mendel sur l'année 2022
Écrivez la requête SQL calculant le salaire moyen perçu uniquement par **Roland Mendel** sur l'ensemble de l'année **2022** (du `2022-01-01` au `2022-12-31` inclus).

*Indices :*
- Combinez la jointure avec une clause `WHERE`.
- Filtrez sur le nom (`e.name = 'Roland Mendel'`) ou son identifiant (`e.id = 1`).
- Filtrez sur les dates avec `s.date BETWEEN '2022-01-01' AND '2022-12-31'` (ou avec `>=` et `<=`).

#### Résultat attendu dans Workbench :
```text
+---------------+--------------------+
| name          | salaire_moyen_2022 |
+---------------+--------------------+
| Roland Mendel |            5300.00 |
+---------------+--------------------+
1 row returned
```
*(Calcul de vérification : en 2022, Roland a perçu 5200 € le 15/01 et 5400 € le 15/07. La moyenne est bien $(5200 + 5400) / 2 = 5300.00$ €).*

---

## 5. Jointure sur plus de deux tables (Question 10)

Dans une application réelle (e-commerce, logistique, billetterie), l'information est fréquemment distribuée sur 3 tables ou davantage.

Dans la base `CRUD2`, ouvrez les 3 tables `Customers`, `Products` et `Orders` dans Workbench :
* **`Products`** : `product_id`, `product_name`, `price` (ex: Burger à 10 €, Sandwich à 15 €).
* **`Customers`** : `customer_id`, `customer_name`, `email` (Alice, Bob).
* **`Orders`** : `order_id`, `customer_id`, `product_id` (table d'association contenant les commandes passées).

#### À vous de jouer (Question 10) :
Rédigez la requête SQL avec jointures successives permettant d'obtenir le récapitulatif des commandes passées avec :
1. Le numéro de la commande (`order_id`)
2. Le nom du produit commandé (`product_name`)
3. Le nom du client ayant passé la commande (`customer_name`)
4. Le prix unitaire (`price`)
Triez par numéro de commande (`order_id`) croissant.

*Indices :*
- Démarrez votre sélection depuis la table `Orders o`.
- Faites une première jointure `INNER JOIN Customers c ON o.customer_id = c.customer_id`.
- Enchaînez une seconde jointure `INNER JOIN Products p ON o.product_id = p.product_id`.

#### Résultat attendu dans Workbench :
```text
+----------+--------------+---------------+-------+
| order_id | product_name | customer_name | price |
+----------+--------------+---------------+-------+
|        1 | Burger       | Alice         |    10 |
|        2 | Sandwich     | Alice         |    15 |
|        3 | Burger       | Bob           |    10 |
+----------+--------------+---------------+-------+
3 rows returned
```

---

## 6. Démarche inverse : Rétro-ingénierie d'une requête SQL (Question 11)

En entreprise, un développeur doit régulièrement analyser du code SQL existant pour comprendre les liaisons entre entités et reconstituer le modèle relationnel.

### Exercice 11.1 : Campagne marketing & Webinaires
Analysez la requête suivante :

```sql
SELECT sub.EmailAddress, de.CampaignName, web.AttendanceStatus
FROM _Subscribers AS sub
INNER JOIN DataExtension AS de 
  ON de.SubscriberKey = sub.SubscriberKey
INNER JOIN WebinarParticipants AS web 
  ON web.SubscriberKey = sub.SubscriberKey;
```

#### Questions :
1. Quelles sont les **trois tables** interrogées par cette requête et quels alias leur sont attribués ?
2. Quelle est la **clé de liaison commune** utilisée pour relier ces tables entre elles ?
3. Quelles colonnes finales sont projetées et affichées pour l'utilisateur ?
4. Expliquez en une phrase ce que permet d'extraire cette requête pour le service marketing.
5. Esquissez le schéma relationnel correspondant (tables, clés primaires et clés étrangères).

---

### Exercice 11.2 : Base de données Cinéma
Analysez la requête suivante :

```sql
SELECT f.titre
FROM Film AS f, Role AS r, Artiste AS a1, Artiste AS a2
WHERE f.idFilm = r.idFilm
  AND r.idActeur = a1.idArtiste
  AND f.idRealisateur = a2.idArtiste
  AND a2.nom = 'Burton'
  AND a1.nom = 'Depp';
```

#### Questions :
1. Combien de tables différentes sont interrogées ? Pourquoi la table `Artiste` est-elle mentionnée deux fois avec les alias `a1` et `a2` ?
2. Identifiez les conditions de jointures exprimées dans la clause `WHERE` (quelles sont les clés étrangères et vers quelles clés primaires pointent-elles) ?
3. Que recherche précisément cette requête en français ? Donnez un exemple de titre de film susceptible de figurer dans le résultat.
4. Réécrivez cette même requête en utilisant la norme moderne avec le mot-clé explicite `INNER JOIN ... ON ...`.

---

> 🚀 **Vous maîtrisez désormais les jointures et l'agrégation SQL dans MySQL Workbench !**  
> Vous pouvez maintenant passer à l'**Exercice 7 dans le `README.md`** pour concevoir l'API Flask de calcul de salaire médian sur période.
