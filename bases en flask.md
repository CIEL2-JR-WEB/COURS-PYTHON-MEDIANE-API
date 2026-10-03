# Support de cours & Exercices pratiques : Les bases de Flask
**BTS CIEL (Option Informatique et Réseaux) — Module Développement Web & API REST**

Ce support prépare directement à l'**Exercice 4.2** (puis aux exercices 4.3, 5 et 6). Il vous apprend comment fonctionne un micro-framework web en Python, où écrire votre code, comment démarrer le serveur, et comment manipuler des **chaînes de caractères**, des **paramètres d'URL** et des **payloads JSON (POST)**.

---

## 1. Où coder et comment lancer Flask ?

### Où se trouvent les fichiers dans le projet ?
Dans l'arborescence du dépôt :
```text
tp-python-flask-ciel/
├── api/                  <── DOSSIER BACKEND FLASK
│   ├── app.py            <── FICHIER PRINCIPAL de l'API Flask (vous codez ici !)
│   ├── statistique.py    <── Vos fonctions moyenne() et mediane()
│   ├── tri_selection.py  <── Votre algorithme de tri par sélection
│   ├── db.py             <── Module de connexion MySQL (pour l'exercice 6)
│   └── requirements.txt  <── Dépendances Python (flask, mysql-connector-python)
├── nginx/                <── Serveur web et reverse proxy
└── docker-compose.yml    <── Orchestration des conteneurs
```

> 🎯 **Règle pratique :**  
> Toutes vos routes Flask doivent être écrites dans le fichier [`api/app.py`](api/app.py).

---

### Comment lancer et tester Flask ?

Deux méthodes s'offrent à vous :

#### Méthode 1 : Avec Docker Compose (Recommandé — Environnement du TP)
Ouvrez un terminal à la racine du projet et démarrez les conteneurs :
```bash
docker compose up -d
```

- Le conteneur `api` démarre automatiquement Flask avec le rechargement à chaud (**Hot-Reload**) activé (`debug=True`).
- **Vous n'avez pas besoin de redémarrer le conteneur à chaque modification :** dès que vous enregistrez [`api/app.py`](api/app.py), Flask détecte la sauvegarde et recharge votre code instantanément !
- Pour observer les messages du serveur et voir vos éventuelles erreurs Python en temps réel :
  ```bash
  docker compose logs -f api
  ```
- Vos routes sont accessibles :
  - Soit via Nginx sur le port standard : `http://localhost/api/...`
  - Soit directement sur le port Flask : `http://localhost:5000/api/...`

#### Méthode 2 : En local autonome (sans Docker)
Si vous souhaitez tester directement sur votre machine hôte :
```bash
# 1. Se déplacer dans le dossier api
cd api

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Démarrer Flask en mode débogage
flask --app app.py run --debug
```
Le serveur écoute sur `http://localhost:5000/`.

---

## 2. Qu'est-ce qu'une route et comment fonctionne Flask ?

Une API REST associe une **URL** et une **méthode HTTP** (`GET`, `POST`, etc.) à une fonction Python.

```python
from flask import Flask, jsonify, request

# Création de l'application
app = Flask(__name__)

# Déclaration d'une route avec un décorateur
@app.route('/api/status', methods=['GET'])
def get_status():
    # Retour d'un dictionnaire sérialisé en JSON avec le code HTTP 200 OK
    return jsonify({
        "etat": "operationnel",
        "service": "API Flask BTS CIEL"
    }), 200
```

---

## 3. Série d'exercices progressifs

---

### Niveau 1 : Première route et manipulation de chaînes de caractères

Dans ce premier niveau, nous allons créer des routes qui manipulent des chaînes de caractères (*strings*).

#### Notion : Récupérer une chaîne dans l'URL (`request.args.get`)
Lorsqu'un client émet une requête `GET /api/salutation?prenom=Nicolas` :
- `request.args.get('prenom', 'Inconnu')` récupère la valeur `'Nicolas'`.
- Si le paramètre n'est pas fourni dans l'URL, la valeur par défaut `'Inconnu'` est utilisée.

```python
@app.route('/api/salutation', methods=['GET'])
def salutation():
    prenom = request.args.get('prenom', 'etudiant')
    message = f"Bienvenue en BTS CIEL, {prenom.capitalize()} !"
    return jsonify({
        "prenom": prenom,
        "message": message
    }), 200
```

#### Mini-Exercice 1.1 : Analyseur de texte (Chaînes de caractères)
Écrivez dans `api/app.py` une route `GET /api/texte/analyse` qui reçoit un paramètre `mot` dans l'URL et renvoie :
1. Le mot en majuscules (`.upper()`).
2. Le mot inversé (`mot[::-1]`).
3. Le nombre de caractères (`len(mot)`).
4. Un booléen indiquant si le mot est un palindrome (s'il se lit de la même façon dans les deux sens).

*Exemple de code à tester :*
```python
@app.route('/api/texte/analyse', methods=['GET'])
def analyse_texte():
    mot = request.args.get('mot', '')
    if not mot:
        return jsonify({"erreur": "Veuillez fournir un mot via ?mot=..."}), 400

    mot_nettoye = mot.strip().lower()
    est_palindrome = (mot_nettoye == mot_nettoye[::-1])

    return jsonify({
        "original": mot,
        "majuscules": mot.upper(),
        "longueur": len(mot),
        "inverse": mot[::-1],
        "palindrome": est_palindrome
    }), 200
```

*Commandes de test dans votre terminal :*
```bash
curl "http://localhost/api/texte/analyse?mot=radar"
# Réponse : {"longueur":5,"majuscules":"RADAR","original":"radar","palindrome":true,"inverse":"radar"}

curl "http://localhost/api/texte/analyse?mot=informatique"
# Réponse : {"longueur":12,"majuscules":"INFORMATIQUE","original":"informatique","palindrome":false,"inverse":"euqitamrofni"}
```

---

### Niveau 2 : Traitement de Payloads JSON simples (Requêtes POST)

#### Pourquoi utiliser la méthode `POST` et un Payload ?
- Avec la méthode `GET`, les données transitent dans l'URL (**Query String**). C'est parfait pour rechercher ou filtrer, mais inadapté pour envoyer des données volumineuses, confidentielles ou des objets structurés.
- Avec la méthode `POST`, les données sont transmises dans le **corps de la requête** (*request body* ou **payload**), le plus souvent au format **JSON**.

#### Comment lire un payload JSON dans Flask ?
On utilise la fonction `request.get_json()` :
```python
@app.route('/api/echo', methods=['POST'])
def echo():
    # Récupère le payload JSON envoyé par le client sous forme de dictionnaire Python
    donnees = request.get_json()

    # Si le client n'a pas envoyé de JSON valide
    if not donnees:
        return jsonify({"erreur": "Payload JSON manquant ou invalide"}), 400

    return jsonify({
        "statut": "donnees_recues",
        "contenu": donnees
    }), 200
```

#### Mini-Exercice 2.1 : Message utilisateur avec validation de payload
Créez une route `POST /api/message` qui attend un payload JSON contenant le nom d'un auteur et un message :
```json
{
  "auteur": "Thomas",
  "texte": "Bonjour le réseau CIEL !"
}
```
La fonction doit :
1. Vérifier la présence des clés `"auteur"` et `"texte"`.
2. Calculer le nombre de mots du message (`len(texte.split())`).
3. Renvoyer une confirmation avec le code HTTP `201 Created`.

*Exemple de code à ajouter dans `api/app.py` :*
```python
@app.route('/api/message', methods=['POST'])
def creer_message():
    donnees = request.get_json()
    if not donnees:
        return jsonify({"erreur": "Format JSON attendu."}), 400

    auteur = donnees.get('auteur', '').strip()
    texte = donnees.get('texte', '').strip()

    if not auteur or not texte:
        return jsonify({"erreur": "Les champs 'auteur' et 'texte' sont obligatoires."}), 400

    nombre_mots = len(texte.split())

    return jsonify({
        "statut": "Message enregistre",
        "auteur": auteur,
        "texte": texte,
        "nombre_mots": nombre_mots,
        "accuse_reception": f"Merci {auteur}, votre message de {nombre_mots} mot(s) a bien ete traite."
    }), 201
```

*Test avec la commande `curl` (envoi d'un payload JSON avec l'en-tête `Content-Type`) :*
```bash
curl -X POST "http://localhost/api/message" \
     -H "Content-Type: application/json" \
     -d "{\"auteur\": \"Thomas\", \"texte\": \"Bonjour le reseau CIEL\"}"
```

**Sortie attendue :**
```json
{
  "accuse_reception": "Merci Thomas, votre message de 4 mot(s) a bien ete traite.",
  "auteur": "Thomas",
  "nombre_mots": 4,
  "statut": "Message enregistre",
  "texte": "Bonjour le reseau CIEL"
}
```

> 💡 **Avec Postman :**  
> Sélectionnez la méthode **POST**, entrez l'URL `http://localhost/api/message`, allez dans l'onglet **Body**, cochez **raw**, sélectionnez **JSON** dans la liste déroulante et collez votre payload.

---

### Niveau 3 : De la chaîne de caractères à la liste de nombres

Dans l'**Exercice 4.2**, le client transmet une série de nombres sous forme d'une chaîne de caractères dans la Query String :  
`GET /api/tri?t=15,3,22,8`

#### La fonction utilitaire de découpage : `parse_int_list`
Pour transformer `'15,3,22,8'` en une liste Python d'entiers `[15, 3, 22, 8]`, nous créons une fonction réutilisable :

```python
def parse_int_list(raw_string: str) -> list:
    """
    Convertit une chaîne de type '15, 3, 22' en liste Python [15, 3, 22].
    Lève ValueError si un élément n'est pas un entier valide.
    """
    if not raw_string:
        return []
    resultat = []
    for item in raw_string.split(','):
        element_propre = item.strip()
        if element_propre:
            resultat.append(int(element_propre))
    return resultat
```

#### Mini-Exercice 3.1 : Route de calcul sur une chaîne numérique
Créez une route `GET /api/somme` qui prend une série `t` dans l'URL, la convertit en liste d'entiers et renvoie la somme et le nombre d'éléments.

*Exemple de code :*
```python
@app.route('/api/somme', methods=['GET'])
def calculer_somme():
    raw_t = request.args.get('t', '')
    if not raw_t:
        return jsonify({"erreur": "Parametre 't' manquant (ex: /api/somme?t=10,20,5)"}), 400

    try:
        nombres = parse_int_list(raw_t)
        total = sum(nombres)
        return jsonify({
            "nombres_recus": nombres,
            "effectif": len(nombres),
            "somme": total
        }), 200
    except ValueError:
        return jsonify({"erreur": "La serie 't' doit contenir uniquement des entiers separes par des virgules."}), 400
```

*Test curl :*
```bash
curl "http://localhost/api/somme?t=10,20,5"
# Réponse : {"effectif": 3, "nombres_recus": [10, 20, 5], "somme": 35}

curl "http://localhost/api/somme?t=10,erreur,5"
# Réponse HTTP 400 : {"erreur": "La serie 't' doit contenir uniquement des entiers..."}
```

---

### Niveau 4 : Paramètres dans le chemin d'URL (*Path parameters*)

Pour préparer l'**Exercice 6** (`/api/employees/<id>/comparaison`), on utilise parfois des variables directement dans le chemin de la route.

```python
@app.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    # La variable article_id est automatiquement convertie en int par Flask
    return jsonify({
        "id": article_id,
        "titre": f"Article reference #{article_id}",
        "disponible": True
    }), 200
```

*Test curl :*
```bash
curl "http://localhost/api/articles/42"
# Réponse : {"disponible": true, "id": 42, "titre": "Article reference #42"}
```

---

## 4. Synthèse des mécanismes à retenir

| Besoin | Syntaxe Flask | Exemple d'utilisation |
| :--- | :--- | :--- |
| **Lire un paramètre d'URL (GET)** | `request.args.get('cle', defaut)` | `/api/tri?t=12,5` (Ex 4.2 & 5) |
| **Lire un payload JSON (POST)** | `donnees = request.get_json()` | Validation de formulaires / IHM |
| **Lire un paramètre de chemin** | `@app.route('/.../<int:id>')` | `/api/employees/3/...` (Ex 6) |
| **Envoyer du JSON** | `return jsonify(dict), code_http` | Réponse à toutes les requêtes |
| **Rejet d'entrée invalide** | `return jsonify({"erreur": ...}), 400` | Sécurité et robustesse API |

---

## 5. Vous êtes prêt pour l'Exercice 4.2 !

Vous savez désormais où coder (`api/app.py`), comment Flask recharge automatiquement vos modifications avec Docker, et comment recevoir et renvoyer des données en JSON.

👉 **Reprenez le sujet principal pour implémenter l'Exercice 4.2 :**  
[Retour au README.md — Exercice 4.2 : API REST Flask pour le tri](README.md#exercice-42--api-rest-flask-pour-le-tri)
