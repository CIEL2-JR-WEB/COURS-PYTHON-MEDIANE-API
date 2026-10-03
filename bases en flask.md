# Support de cours & Exercices pratiques : Les bases de Flask
**BTS CIEL (Option Informatique et Réseaux) — Module Développement Web & API REST**

Ce support prépare directement à l'**Exercice 4.2** (et aux exercices suivants 4.3, 5 et 6) du TP. Il vous permet de comprendre le fonctionnement d'un micro-framework web en Python, la création de routes HTTP, la récupération des paramètres et l'émission de réponses au format JSON.

---

## 1. Qu'est-ce que Flask & Une API REST ?

### Le rôle de Flask
**Flask** est un micro-framework web écrit en Python. Il fournit les mécanismes essentiels pour :
1. Écouter des requêtes HTTP émises par un client (navigateur web, script JavaScript `fetch`, application mobile, commande `curl` ou Postman).
2. Associer une URL demandée à une fonction Python dédiée : c'est le principe du **routage** (*routing*).
3. Renvoyer une réponse au client, généralement au format textuel standardisé **JSON** (*JavaScript Object Notation*).

### Le cycle d'une requête dans notre architecture Docker
Dans ce TP, l'architecture se compose de :
```text
[ Client (Navigateur / curl) ]
               │
               ▼  (Port 80)
      [ Reverse Proxy Nginx ]
               │
        /api/* │ (Redirection interne port 5000)
               ▼
     [ API Python / Flask ]  <──────> [ Base MySQL (CRUD) ]
```
Le serveur Flask s'exécute dans le conteneur `api`. Il recharge automatiquement son code dès que vous sauvegardez vos fichiers (`debug=True`).

---

## 2. Structure minimale d'une application Flask

Une application Flask minimale tient en quelques lignes :

```python
from flask import Flask, jsonify

# 1. Instanciation de l'application Flask
app = Flask(__name__)

# 2. Définition d'une route avec un décorateur
@app.route('/api/bienvenue', methods=['GET'])
def bienvenue():
    # 3. Retour d'un dictionnaire converti en JSON
    return jsonify({
        "message": "Bienvenue sur l'API Flask du BTS CIEL !",
        "version": "1.0"
    }), 200

# 4. Point d'entrée pour démarrer le serveur (en écoute sur toutes les interfaces)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

> **Points clés :**
> - `@app.route('/chemin', methods=['GET'])` : ce décorateur indique à Flask d'appeler la fonction `bienvenue()` lorsque l'URL `/api/bienvenue` est sollicitée avec le verbe HTTP `GET`.
> - `jsonify(dictionnaire)` : sérialise un dictionnaire Python en une chaîne JSON valide avec l'en-tête HTTP `Content-Type: application/json`.
> - `, 200` : code de statut HTTP (*200 OK*).

---

## 3. Série d'exercices très progressifs

---

### Niveau 1 : Route simple et réponse JSON

#### Syntaxe :
```python
@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "service": "api-ciel"}), 200
```

#### Mini-Exercice 1.1 : Test de la route
Testez cette route depuis votre terminal avec `curl` :
```bash
curl -i "http://localhost/api/ping"
```

**Sortie attendue :**
```text
HTTP/1.1 200 OK
Content-Type: application/json

{"service":"api-ciel","status":"ok"}
```

---

### Niveau 2 : Passage de paramètres via la Query String (`request.args`)

C'est la méthode de transmission utilisée dans l'**Exercice 4.2** (`/api/tri?t=15,3,8`) et l'**Exercice 5** (`/api/fusion?t1=12,5&t2=8,20`).

#### Principe de la Query String :
Dans l'URL `http://localhost/api/saluer?nom=Alice&annee=2026` :
- Le point d'interrogation `?` marque le début des paramètres.
- Les couples `cle=valeur` sont séparés par des esperluettes `&`.
- Dans Flask, ces valeurs sont accessibles via l'objet `request.args`.

```python
from flask import request

@app.route('/api/saluer', methods=['GET'])
def saluer():
    # request.args.get('cle', valeur_par_defaut)
    nom = request.args.get('nom', 'Anonyme')
    return jsonify({
        "salutation": f"Bonjour {nom} !",
        "destinataire": nom
    }), 200
```

> ⚠️ **Attention cruciale aux types de données :**  
> `request.args.get()` renvoie **toujours une chaîne de caractères** (`str`), jamais un entier ou un flottant !  
> Si vous attendez un nombre, vous devez le convertir explicitement avec `int()` ou `float()`.

#### Mini-Exercice 2.1 : Route d'addition de deux entiers
Observez comment extraire et additionner deux nombres transmis dans l'URL :

```python
@app.route('/api/addition', methods=['GET'])
def addition():
    # Récupération des deux paramètres sous forme de chaînes
    raw_a = request.args.get('a', '0')
    raw_b = request.args.get('b', '0')
    
    # Conversion en entiers
    a = int(raw_a)
    b = int(raw_b)
    
    return jsonify({
        "a": a,
        "b": b,
        "somme": a + b
    }), 200
```

*Test curl :*
```bash
curl "http://localhost/api/addition?a=12&b=8"
# Réponse attendue : {"a": 12, "b": 8, "somme": 20}
```

---

### Niveau 3 : Transmission et découpage d'une liste de nombres

Dans l'**Exercice 4.2**, l'utilisateur transmet une liste de nombres séparés par des virgules dans le paramètre `t` :  
Exemple : `GET /api/tri?t=1500,4500,2200,1800`

#### Comment transformer cette chaîne en liste d'entiers en Python ?
On utilise la méthode `.split(',')` combinée au nettoyage des espaces `.strip()` :

```python
def parse_int_list(raw_string: str) -> list:
    """Convertit '15, 3, 22' en [15, 3, 22]."""
    if not raw_string:
        return []
    result = []
    for item in raw_string.split(','):
        clean = item.strip()
        if clean:
            result.append(int(clean))
    return result
```

#### Mini-Exercice 3.1 : Route de calcul de statistiques sur une liste
```python
from statistique import moyenne, mediane
from tri_selection import tri_selection_copie

@app.route('/api/demo-stats', methods=['GET'])
def demo_stats():
    raw_t = request.args.get('t', '')
    liste_entiers = parse_int_list(raw_t)
    
    liste_triee = tri_selection_copie(liste_entiers)
    val_mediane = mediane(liste_triee)
    
    return jsonify({
        "original": liste_entiers,
        "tri": liste_triee,
        "mediane": val_mediane
    }), 200
```

*Test curl :*
```bash
curl "http://localhost/api/demo-stats?t=15,3,22,8"
# Réponse attendue : {"mediane": 11.5, "original": [15, 3, 22, 8], "tri": [3, 8, 15, 22]}
```

---

### Niveau 4 : Gestion des erreurs & Codes HTTP (`400 Bad Request`)

Une API professionnelle doit être **robuste** et rejeter les requêtes invalides avec des codes de statut HTTP explicites :
- `200 OK` : traitement réussi.
- `400 Bad Request` : paramètre obligatoire manquant ou type incorrect (ex: du texte au lieu de nombres).
- `404 Not Found` : ressource demandée inexistante.
- `500 Internal Server Error` : erreur non interceptée côté serveur.

#### Exemple de validation rigoureuse :
```python
@app.route('/api/tri-securise', methods=['GET'])
def tri_securise():
    raw_t = request.args.get('t')
    
    # 1. Vérification de présence
    if not raw_t:
        return jsonify({
            "erreur": "Le paramètre 't' est obligatoire (ex: /api/tri?t=12,5,8)"
        }), 400

    # 2. Vérification du format numérique avec bloc try/except
    try:
        nombres = parse_int_list(raw_t)
        if len(nombres) == 0:
            return jsonify({"erreur": "La liste transmise est vide."}), 400
            
        tri = tri_selection_copie(nombres)
        med = mediane(tri)
        return jsonify({"original": nombres, "tri": tri, "mediane": med}), 200
        
    except ValueError:
        return jsonify({
            "erreur": "Le paramètre 't' doit contenir uniquement des entiers séparés par des virgules."
        }), 400
```

*Test d'une requête erronée :*
```bash
curl -i "http://localhost/api/tri-securise?t=12,abc,15"
# Réponse : HTTP/1.1 400 BAD REQUEST -> {"erreur": "Le paramètre 't' doit contenir uniquement des entiers..."}
```

---

### Niveau 5 : Paramètres dans le chemin d'URL (*Path parameters*)

Dans l'**Exercice 6**, pour consulter la fiche d'un employé selon son identifiant unique, on n'utilise pas la Query String mais une variable directement dans le chemin de l'URL :  
Exemple : `GET /api/employees/3/comparaison`

#### Syntaxe Flask avec convertisseur de type :
```python
# <int:emp_id> capture la partie correspondante de l'URL et la convertit automatiquement en entier
@app.route('/api/employees/<int:emp_id>', methods=['GET'])
def get_employe(emp_id):
    # La variable emp_id est transmise comme argument à la fonction !
    if emp_id == 3:
        return jsonify({
            "id": 3,
            "name": "Martin Blank",
            "salary": 8000
        }), 200
    else:
        # Ressource non trouvée
        return jsonify({"erreur": f"Employé avec l'ID {emp_id} introuvable."}), 404
```

---

## 4. Synthèse des mécanismes Flask du TP

| Notion Flask | Syntaxe | Exercice cible |
| :--- | :--- | :--- |
| **Création d'une route GET** | `@app.route('/api/...', methods=['GET'])` | Exercices 4.2, 4.3, 5, 6 |
| **Lecture Query String unique** | `request.args.get('t')` | Exercice 4.2 & 4.3 |
| **Lecture de paramètres multiples** | `request.args.get('t1')`, `request.args.get('t2')` | Exercice 5 |
| **Répétition d'un paramètre** | `request.args.getlist('t')` | Exercice 5 (Amélioration) |
| **Paramètre dans le chemin (ID)** | `@app.route('/api/employees/<int:emp_id>')` | Exercice 6 |
| **Réponse JSON & Statut HTTP** | `return jsonify(donnees), 200` ou `400` | Tous les exercices d'API |

---

## 5. Prêt pour l'Exercice 4.2 !

Vous comprenez désormais le rôle des routes Flask, de la Query String et du format JSON.

👉 **Rendez-vous sur l'Exercice 4.2 du sujet principal pour connecter votre premier algorithme à une API REST :**  
[Retour au README.md — Exercice 4.2 : API REST Flask pour le tri](README.md#exercice-42--api-rest-flask-pour-le-tri)
