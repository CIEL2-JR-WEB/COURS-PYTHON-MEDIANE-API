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

### Exercice 0 : Introduction à Python, Cybersécurité & Statistiques fondamentales

L'**Exercice 0** regroupe les prérequis fondamentaux indispensables pour aborder sereinement les exercices suivants du TP. Il est structuré en **deux volets progressifs** :
1. **Les bases algorithmiques & cybersécurité (0.1 à 0.5)** : manipulation de chaînes, chiffrement de César, opérateur XOR, tuples immuables, copies en mémoire et mini-projet défi anti-IA.
2. **Les calculs statistiques élémentaires (0.6 et 0.7)** : calcul de moyenne, ordonnancement et résolution du problème de Nicolas sur le salaire médian.

---

#### Exercice 0.1 : Chaînes de caractères & Chiffrement de César

* **Objectif pédagogique** :  
  Créer sa première fonction (`def`), parcourir une chaîne caractère par caractère avec une boucle `for`, convertir des lettres en codes numériques avec `ord()` et `chr()`, et appliquer l'arithmétique modulaire (`% 26`).
* **Mise en situation Cybersécurité** :  
  Le chiffrement de Jules César est le premier système de chiffrement symétrique de l'histoire. Vous devez concevoir la fonction qui décale chaque lettre de l'alphabet d'un nombre fixe $k$ de positions.
* **Fichiers** : `api/intro_cyber.py`.
* **Ressources vidéo recommandées** :  
  * 📺 [Python - Le chiffrement César avec ASCII (niveau débutant / intermédiaire)](https://www.youtube.com/watch?v=B5TOZY1oBy0) *(Explication lumineuse des fonctions `ord()` et `chr()`, du décalage avec modulo et de la mise en œuvre en Python)*.
* **💡 Notions clés & syntaxe Python** :
  ```python
  # Code ASCII vers caractère et inversement :
  ord('A')  # -> 65
  chr(65)   # -> 'A'

  # Décalage circulaire dans l'alphabet de 26 lettres :
  nouveau_char = chr(ord('A') + (ord(c) - ord('A') + decalage) % 26)
  ```
* **Consignes** :
  1. Écrivez `chiffrer_cesar(texte: str, decalage: int) -> str` en préservant la casse (majuscules/minuscules) et en laissant les espaces et la ponctuation intacts.
  2. Écrivez `dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str` (astuce : déchiffrer revient à chiffrer avec `-decalage`).
* **Exemple d'exécution** :
  ```text
  Original : ALERTE INTRUSION 2026 !
  Chiffré  : EPIVXI MRXVYWMSR 2026 !  (décalage = 4)
  Restauré : ALERTE INTRUSION 2026 !
  ```

---

#### Exercice 0.2 : Chiffrement par clé XOR & Opérateur binaire

* **Objectif pédagogique** :  
  Manipuler une liste de nombres entiers (`list[int]`), utiliser l'opérateur bit-à-bit XOR (`^`), répéter cycliquement une clé avec l'opérateur modulo (`i % len(cle)`), et vérifier la propriété fondamentale de réversibilité : $(A \oplus K) \oplus K = A$.
* **Mise en situation Cybersécurité** :  
  L'opération OU exclusif (XOR) est au cœur de la cryptographie moderne (masque jetable de Vernam, protocoles réseau, Wi-Fi WPA). Chiffrer et déchiffrer utilisent la même opération logique.
* **Fichiers** : `api/intro_cyber.py`.
* **Ressources vidéo recommandées** :  
  * 📺 [Qu'est-ce que la cryptographie symétrique ? (XOR et Masque jetable)](https://www.youtube.com/watch?v=EHCds8De34Q) *(Le rôle fondamental de l'opérateur XOR et du masque de Vernam en cryptographie)*.
* **💡 Notions clés & syntaxe Python** :
  ```python
  # Opérateur binaire XOR en Python :
  octet_chiffre = ord('A') ^ ord('K')  # Produit un entier (code de l'octet chiffré)
  
  # Répétition cyclique de la clé :
  char_cle = cle[i % len(cle)]
  ```
* **Consignes** :
  1. Écrivez `chiffrer_xor(texte: str, cle: str) -> list[int]` qui transforme chaque caractère du texte en entier chiffré par XOR avec le caractère correspondant de la clé.
  2. Écrivez `dechiffrer_xor(octets: list[int], cle: str) -> str` qui réapplique la même clé pour retrouver le texte d'origine.
* **Exemple d'exécution** :
  ```text
  Secret   : PASSWORD_SECRET
  Clé      : CYBER
  Octets   : [19, 24, 17, 22, 5, 12, 11, 6, 26, 1, 6, 26, 16, 0, 6]
  Restauré : PASSWORD_SECRET
  ```

---

#### Exercice 0.3 : Tuples vs Listes (Immutabilité & Données scellées)

* **Objectif pédagogique** :  
  Comprendre la différence vitale entre types **mutables** (`list` entre crochets `[...]`) et types **immuables** (`tuple` entre parenthèses `(...)`).
* **Mise en situation Cybersécurité** :  
  En sécurité des systèmes, des identifiants système ou des clés d'authentification (`admin_root`, `UID=1001`, `SUPERADMIN`) ne doivent jamais pouvoir être corrompus ou écrasés par un script tiers en cours d'exécution. Les stocker dans un **tuple** scelle les données en mémoire.
* **Fichiers** : `api/intro_cyber.py`.
* **Ressources vidéo recommandées** :  
  * 📺 [TUTO Python : Manipulation de chaînes de caractères et tuples](https://www.youtube.com/watch?v=DFcCc3zWrU0) *(Comprendre les structures de base et l'immuabilité)*.
* **💡 Notions clés & syntaxe Python** :
  ```python
  mon_tuple = ("admin", 1001, "RO")
  # Tenter de faire : mon_tuple[0] = "pirate"
  # Déclenche immédiatement : TypeError: 'tuple' object does not support item assignment
  ```
* **Consignes** :
  1. Écrivez `creer_identifiant_scelle(login: str, uid: int, privilege: str) -> tuple`.
  2. Écrivez `tenter_modification_tuple(identifiant: tuple) -> bool` utilisant un bloc `try / except TypeError` démontrant que Python interdit toute altération du tuple.
* **Exemple d'exécution** :
  ```text
  Identifiant scellé (tuple) : ('admin_root', 1001, 'SUPERADMIN')
  Tentative d'altération en mémoire bloquée : True (TypeError capturé avec succès)
  ```

---

#### Exercice 0.4 : Mutation en place vs Copie de liste (Le piège des références)

* **Objectif pédagogique** :  
  Démystifier le piège numéro 1 de Python : l'affectation `b = a` ne duplique PAS les données, elle copie simplement la **référence** (adresse mémoire) ! Apprendre à créer une copie indépendante avec `b = a.copy()`.
* **Mise en situation Cybersécurité** :  
  Lors du filtrage d'adresses IP suspectes pour un rapport d'audit, modifier la liste originale détruit la preuve d'origine. Vous devez garantir l'intégrité de la liste source.
* **Fichiers** : `api/intro_cyber.py`.
* **Ressources vidéo recommandées** :  
  * 📺 [Maîtriser les LISTES avec Python](https://www.youtube.com/watch?v=yK4CTsEP_B0) *(Comprendre la manipulation des listes, les méthodes de mutation et les bonnes pratiques)*.
* **⚠️ Le piège classique en Python** :
  ```python
  a = [10, 20, 30]
  b = a            # ATTENTION : 'b' et 'a' partagent le MÊME id en mémoire !
  b.append(40)     # 'a' est également altéré à votre insu : [10, 20, 30, 40]
  
  # La bonne pratique (Copie défensive) :
  b = a.copy()     # 'b' possède son propre espace mémoire indépendant
  ```
* **Consignes** :
  1. Écrivez `filtrer_ip_copie(liste_ips: list, ip_bannie: str) -> list`.
  2. Assurez-vous que la liste retournée est un **nouvel objet** et que la liste passée en argument reste rigoureusement identique.
* **Lien avec la suite du TP** :  
  Cette maîtrise est le prérequis direct de l'**Exercice 4.1** (`tri_selection_copie()` vs `tri_selection_en_place()`).

---

#### Exercice 0.5 : Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau « CIEL-Guard »)

> [!IMPORTANT]
> **Pourquoi ce défi est résistant au simple copier-coller d'IA ?**  
> Une IA générative en ligne (ChatGPT, Claude...) ne peut pas résoudre ce problème par un simple copier-coller de l'énoncé car :
> 1. **Dépendance à un artefact local réel** : Les données brutes se trouvent dans le fichier physique [api/mystere.payload](api/mystere.payload) présent dans votre conteneur Docker.
> 2. **Protocole composite propriétaire** : Ce n'est pas un chiffrement standardisé trouvé sur Internet, mais une combinaison alternée d'opérations bit-à-bit et modulaires.
> 3. **Validation dynamique anti-hardcoding** : Le script de test valide votre code sur le fichier réel ET sur un vecteur secret aléatoire généré en mémoire. Un code qui renvoie simplement une réponse statique échouera automatiquement.

* **Contexte de la mission (SOC Analyst)** :  
  Votre équipe a intercepté une transmission clandestine lors d'une attaque simulée. Les octets capturés ont été exportés dans le fichier [api/mystere.payload](api/mystere.payload).
  D'après l'analyse des rétro-ingénieurs, l'attaquant a employé le protocole **CIEL-Guard v1** :
  * La clé secrète est dérivée dynamiquement : la chaîne `"CIEL"` concaténée avec le nombre total d'octets du fichier (ex: `"CIEL44"`).
  * Le décalage de César est la somme des chiffres de l'année `2026` ($2 + 0 + 2 + 6 = 10$).
  * **Règle d'alternance** :
    * Les octets à **indice pair** ($0, 2, 4, \dots$) ont été chiffrés par XOR avec le caractère de la clé à l'indice $(i // 2) \pmod{\text{longueur clé}}$.
    * Les octets à **indice impair** ($1, 3, 5, \dots$) ont été chiffrés par décalage de César ($+10$).
* **Fichiers** : `api/mystere.payload`, `api/intro_cyber.py`.
* **Consignes** :
  1. Écrivez la fonction `decoder_ciel_guard(chemin_fichier: str = "mystere.payload") -> tuple[str, int, int]`.
  2. Ouvrez et lisez le fichier contenant les entiers séparés par des virgules.
  3. Déchiffrez la séquence selon la règle d'alternance CIEL-Guard.
  4. Renvoyez le résultat sous forme d'un **tuple** scellé : `(message_clair, nombre_octets, checksum_somme)`.
  5. Exécutez le script (`docker compose exec api python intro_cyber.py`) pour révéler le **FLAG** secret validant l'enquête.
* **Exemple de sortie attendue** :
  ```text
  Artefact 'mystere.payload' lu avec succès (44 octets, checksum=3419)
  -> MESSAGE SECRET DÉCODÉ : FLAG{ciel_python_2026_investigation_reussie}
  -> Validation du Défi : SUCCÈS TOTAL !
  ```

---

#### Exercice 0.6 : Moyenne et import de module
* **Objectif** : Manipuler une liste Python et créer son premier module réutilisable.
* **Fichiers** : `api/statistique.py`, `api/main.py`.
* **Consignes** :
  * Dans `statistique.py`, codez la fonction `moyenne(tab)`.
  * Ne pas utiliser le module `statistics` : calculez la somme et divisez par le nombre d'éléments.
  * Dans `main.py`, importez `moyenne` et testez-la avec la liste `notes = [12, 15, 8, 19, 10, 14]`.
* **Exemple d'exécution** :
  ```text
  Entrée : [12, 15, 8, 19, 10, 14]
  Sortie attendue : Moyenne = 13.0
  ```
* **Amélioration** : Gérez le cas où la liste passée en paramètre est vide (renvoyez `0.0` sans provoquer de division par zéro).

---

#### Exercice 0.7 : Médiane et problème de l'employé Nicolas

![Médiane d'une série statistique - Problématique de Nicolas](img/mediane_nicolas.png)

> **Problématique de Nicolas :**
> Dans une entreprise de **9 salariés**, le salaire mensuel moyen est de **2 500 €**. Nicolas travaille dans cette entreprise et gagne **2 200 €** par mois.
> Constatant que son salaire est inférieur au salaire moyen (2 200 € < 2 500 €), il affirme : *« Je suis dans les moins bien payés de l'entreprise ! »*.
> Que penser de cette affirmation ?
>
> *Élément d'analyse* : Nicolas commet la confusion fréquente entre **salaire moyen** et **salaire médian**. Quelques très hauts salaires suffisent à tirer la moyenne vers le haut. Pour savoir s'il est réellement dans la tranche inférieure ou supérieure de l'entreprise, il faut ordonner la série et trouver la **médiane** qui sépare l'effectif en deux moitiés égales.

* **Objectif** : Implémenter le calcul de la médiane sur une liste triée et résoudre ce cas concret.
* **Fichiers** : `api/statistique.py`, `api/main.py`.
* **Consignes** :
  * Dans `statistique.py`, codez la fonction `mediane(tab)` sur une série **supposée triée**.
  * Si $N$ est impair, retournez l'élément central à l'indice $N // 2$ ; si $N$ est pair, retournez la moyenne des deux éléments centraux.
  * Dans `main.py`, appliquez le calcul sur les salaires de l'entreprise : `[1500, 4500, 2200, 1500, 3300, 1800, 1700, 2000, 4000]`.
  * Répondez par affichage console : concluez formellement sur la validité de l'affirmation de Nicolas en comparant son salaire à la médiane.
* **Rappel du calcul** :
  * $N = 9$ (impair), série triée : `1500, 1500, 1700, 1800, [2000], 2200, 3300, 4000, 4500` $\rightarrow$ médiane = **2000 €**.
  * $N = 8$ (pair), série triée : `1500, 1700, 1800, [2000 | 2200], 3300, 4000, 4500` $\rightarrow$ médiane = $(2000 + 2200) / 2$ = **2100 €**.
* **Exemple d'exécution** :
  ```text
  Moyenne = 2500.0 € | Médiane = 2000.0 €
  Conclusion : Affirmation fausse (Nicolas gagne 2200 €, soit plus que la médiane de 2000 € ; il fait partie des 50 % les mieux payés).
  ```
* **Amélioration** : Ajoutez une assertion vérifiant que le résultat est identique que la médiane soit calculée sur des entiers ou des flottants.

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

