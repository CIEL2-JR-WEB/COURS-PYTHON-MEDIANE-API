# Support de cours & Exercices pratiques : Les bases de Flask
**BTS CIEL (Option Informatique et Réseaux) — Module Développement Web & API REST**

Ce document est un **guide pratique pas à pas** pour débuter avec Flask. Il a été conçu pour vous faire pratiquer de manière **très progressive, concrète et directe**. À la fin de cette séquence, vous aurez toutes les clés pour réussir l'**Exercice 4.2** du TP.

---

## 1. Où coder et comment lancer Flask ?

### 📁 Où coder ?
Dans le dossier du projet, tout le code de l'API se trouve dans le sous-dossier `api/` :
- **Fichier principal de travail :** [`api/app.py`](api/app.py).  
  C'est dans ce fichier que vous ajoutez vos routes.

### 🚀 Comment lancer Flask ?

#### Méthode avec Docker (Recommandée — Environnement officiel du TP)
1. Ouvrez un terminal à la racine du projet et lancez les conteneurs :
   ```bash
   docker compose up -d
   ```
2. **Rechargement automatique (Hot-Reload) :**  
   Flask est configuré en mode débogage (`debug=True`). Dès que vous modifiez et enregistrez [`api/app.py`](api/app.py), **Flask recharge votre code instantanément**. Vous n'avez pas besoin de relancer Docker !
3. Pour voir les erreurs éventuelles ou vos `print()` en direct :
   ```bash
   docker compose logs -f api
   ```
4. Vos routes sont directement accessibles dans votre navigateur ou via `curl` sur :  
   `http://localhost/api/...` (ou `http://localhost:5000/api/...`).

#### Méthode en local autonome (sans Docker)
```bash
cd api
pip install -r requirements.txt
flask --app app.py run --debug
```
Le serveur écoute alors sur `http://localhost:5000/`.

---

## 2. Les 7 étapes d'initiation (très progressives et concrètes)

---

### Étape 0 : Votre première route Flask (Réponse fixe)

Une route Flask associe une **URL** à une **fonction Python** à l'aide d'un décorateur `@app.route`.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"reponse": "pong"}), 200
```

#### ✏️ Exercice 0 :
Créez la route `GET /api/info` qui renvoie en JSON votre promotion et la spécialité :
- **Sortie attendue :** `{"promotion": "BTS CIEL 2", "specialite": "IR"}`
- **Test curl :**
  ```bash
  curl "http://localhost/api/info"
  ```

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/info', methods=['GET'])
def route_info():
    return jsonify({
        "promotion": "BTS CIEL 2",
        "specialite": "IR"
    }), 200
```
</details>

---

### Étape 1 : Récupérer un paramètre texte dans l'URL (`request.args.get`)

Quand un client appelle une URL avec un point d'interrogation (ex : `/api/saluer?nom=Alice`), les variables situées après `?` forment la **Query String**.  
On récupère leur valeur avec : `request.args.get('cle', 'valeur_par_defaut')`.

#### ✏️ Exercice 1 :
Créez la route `GET /api/saluer` qui lit le paramètre `nom` et renvoie une salutation personnalisée.  
Si aucun nom n'est fourni, utilisez `'etudiant'` par défaut.

- **Test avec paramètre :**
  ```bash
  curl "http://localhost/api/saluer?nom=Thomas"
  ```
  *Sortie attendue :* `{"message": "Bonjour Thomas !"}`

- **Test sans paramètre :**
  ```bash
  curl "http://localhost/api/saluer"
  ```
  *Sortie attendue :* `{"message": "Bonjour etudiant !"}`

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/saluer', methods=['GET'])
def route_saluer():
    nom = request.args.get('nom', 'etudiant')
    return jsonify({
        "message": f"Bonjour {nom} !"
    }), 200
```
</details>

---

### Étape 2 : Manipuler une chaîne de caractères (Majuscules & Longueur)

Les valeurs retournées par `request.args.get()` sont **toujours du texte** (`str`). On peut donc leur appliquer toutes les fonctions Python usuelles sur les chaînes : `.upper()`, `.lower()`, `len()`, `.strip()`.

#### ✏️ Exercice 2 :
Créez la route `GET /api/texte/majuscule?mot=reseau`.  
Elle doit renvoyer le mot d'origine, le mot en majuscules et son nombre de lettres.

- **Test curl :**
  ```bash
  curl "http://localhost/api/texte/majuscule?mot=reseau"
  ```
  *Sortie attendue :*
  ```json
  {
    "original": "reseau",
    "majuscules": "RESEAU",
    "longueur": 6
  }
  ```

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/texte/majuscule', methods=['GET'])
def route_majuscule():
    mot = request.args.get('mot', '')
    return jsonify({
        "original": mot,
        "majuscules": mot.upper(),
        "longueur": len(mot)
    }), 200
```
</details>

---

### Étape 3 : Calcul arithmétique simple (Conversion `int()`)

⚠️ **Attention :** `request.args.get('valeur')` renvoie une chaîne de caractères (`"5"` et non `5`).  
Pour effectuer un calcul mathématique, la conversion explicite avec `int()` ou `float()` est obligatoire !

#### ✏️ Exercice 3.1 : Le carré d'un nombre
Créez la route `GET /api/calcul/carre?n=7` qui renvoie le nombre reçu et son carré ($n^2$).

- **Test curl :**
  ```bash
  curl "http://localhost/api/calcul/carre?n=7"
  ```
  *Sortie attendue :* `{"nombre": 7, "carre": 49}`

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/calcul/carre', methods=['GET'])
def route_carre():
    raw_n = request.args.get('n', '0')
    n = int(raw_n)
    return jsonify({
        "nombre": n,
        "carre": n * n
    }), 200
```
</details>

#### ✏️ Exercice 3.2 : Addition de deux paramètres (`a` et `b`)
Créez la route `GET /api/calcul/somme?a=12&b=8` qui calcule l'addition de deux valeurs reçues.

- **Test curl :**
  ```bash
  curl "http://localhost/api/calcul/somme?a=12&b=8"
  ```
  *Sortie attendue :* `{"a": 12, "b": 8, "somme": 20}`

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/calcul/somme', methods=['GET'])
def route_somme():
    a = int(request.args.get('a', '0'))
    b = int(request.args.get('b', '0'))
    return jsonify({
        "a": a,
        "b": b,
        "somme": a + b
    }), 200
```
</details>

---

### Étape 4 : Découper une chaîne en liste avec `.split(',')`

C'est le mécanisme exact dont vous aurez besoin pour l'**Exercice 4.2** (`/api/tri?t=15,3,8`) !  
Quand vous recevez une chaîne comme `"10,20,5"`, vous devez :
1. La découper avec `.split(',')` pour obtenir `["10", "20", "5"]`.
2. Convertir chaque sous-chaîne en entier : `int(x)`.

#### ✏️ Exercice 4 :
Créez la route `GET /api/liste/stats?valeurs=10,20,5`.  
Elle doit découper la chaîne, calculer le nombre d'éléments et la somme totale des nombres.

- **Test curl :**
  ```bash
  curl "http://localhost/api/liste/stats?valeurs=10,20,5"
  ```
  *Sortie attendue :*
  ```json
  {
    "elements": [10, 20, 5],
    "effectif": 3,
    "somme": 35
  }
  ```

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/liste/stats', methods=['GET'])
def route_liste_stats():
    raw_valeurs = request.args.get('valeurs', '')
    
    # Découpage et conversion en liste d'entiers
    tableau = []
    if raw_valeurs:
        for morceau in raw_valeurs.split(','):
            morceau_propre = morceau.strip()
            if morceau_propre:
                tableau.append(int(morceau_propre))
                
    return jsonify({
        "elements": tableau,
        "effectif": len(tableau),
        "somme": sum(tableau)
    }), 200
```
</details>

---

### Étape 5 : Réception d'un Payload JSON simple (Méthode `POST`)

#### Pourquoi la méthode POST ?
- En `GET`, les données sont visibles dans l'URL (taille restreinte, pas adapté pour transmettre des formulaires complets).
- En `POST`, les données sont envoyées dans le **corps de la requête** (**Payload JSON**).
- Dans Flask, on lit ce payload simplement avec : `donnees = request.get_json()`.

#### ✏️ Exercice 5 : Enregistrer un contact
Créez la route `POST /api/contact` qui reçoit un payload JSON contenant le `nom`, la `ville` et l'`annee_naissance` :
```json
{
  "nom": "Martin",
  "ville": "Paris",
  "annee_naissance": 2005
}
```
La route doit calculer l'âge approximatif ($2026 - \text{annee\_naissance}$) et renvoyer une confirmation :
```json
{
  "statut": "enregistre",
  "nom": "Martin",
  "ville": "Paris",
  "age": 21
}
```

- **Test avec la commande curl (envoi d'un payload JSON avec `-X POST` et `-H "Content-Type: application/json"`) :**
  ```bash
  curl -X POST "http://localhost/api/contact" \
       -H "Content-Type: application/json" \
       -d "{\"nom\": \"Martin\", \"ville\": \"Paris\", \"annee_naissance\": 2005}"
  ```

- **Test avec Postman :**
  1. Choisissez la méthode **POST**.
  2. Saisissez l'URL : `http://localhost/api/contact`.
  3. Allez dans l'onglet **Body**, cochez **raw**, et sélectionnez **JSON** dans la liste déroulante.
  4. Collez le JSON et cliquez sur **Send**.

<details>
<summary>👀 Voir la solution</summary>

```python
@app.route('/api/contact', methods=['POST'])
def route_contact():
    # Lecture du payload JSON envoyé dans la requête
    donnees = request.get_json()
    
    if not donnees:
        return jsonify({"erreur": "Payload JSON attendu"}), 400
        
    nom = donnees.get('nom', 'Inconnu')
    ville = donnees.get('ville', 'Inconnue')
    annee = int(donnees.get('annee_naissance', 2026))
    
    age = 2026 - annee
    
    return jsonify({
        "statut": "enregistre",
        "nom": nom,
        "ville": ville,
        "age": age
    }), 201
```
</details>

---

### Étape 6 : Gérer les erreurs avec le code HTTP `400 Bad Request`

Une API robuste ne doit jamais planter si l'utilisateur oublie un paramètre ou tape des lettres à la place d'un chiffre. On utilise un bloc `try / except ValueError` et on retourne un code `400` :

```python
@app.route('/api/division', methods=['GET'])
def route_division():
    raw_a = request.args.get('a')
    raw_b = request.args.get('b')
    
    # 1. Vérification de présence
    if not raw_a or not raw_b:
        return jsonify({"erreur": "Les deux parametres 'a' et 'b' sont obligatoires"}), 400
        
    # 2. Vérification des conversions et division par zéro
    try:
        a = float(raw_a)
        b = float(raw_b)
        if b == 0:
            return jsonify({"erreur": "Division par zero impossible"}), 400
            
        return jsonify({"resultat": a / b}), 200
    except ValueError:
        return jsonify({"erreur": "Les parametres 'a' et 'b' doivent etre des nombres"}), 400
```

- **Test avec une erreur (lettres au lieu de nombres) :**
  ```bash
  curl -i "http://localhost/api/division?a=10&b=texte"
  # Réponse : HTTP/1.1 400 BAD REQUEST -> {"erreur": "Les parametres 'a' et 'b' doivent etre des nombres"}
  ```

---

## 3. Synthèse des 4 réflexes pour l'Exercice 4.2

Pour réussir l'**Exercice 4.2** (`GET /api/tri?t=...`), vous combinerez exactement les notions vues ici :

| Étape de l'Exercice 4.2 | Notions pratiquées |
| :--- | :--- |
| **1. Déclarer la route** | `@app.route('/api/tri', methods=['GET'])` (Étape 0) |
| **2. Récupérer la série** | `raw_t = request.args.get('t', '')` (Étape 1 & 2) |
| **3. Découper et convertir** | `.split(',')` et `int()` dans un bloc `try/except` (Étape 3 & 4 & 6) |
| **4. Trier et calculer** | `tri_selection_copie(t)` et `mediane(t)` puis `jsonify(...)` (Étape 0) |

---

## 4. Vous avez toutes les bases !

Vous maîtrisez maintenant le cycle complet d'une route Flask, de l'URL au JSON.

👉 **Rendez-vous sur l'Exercice 4.2 du sujet principal :**  
[Retour au README.md — Exercice 4.2 : API REST Flask pour le tri](README.md#exercice-42--api-rest-flask-pour-le-tri)
