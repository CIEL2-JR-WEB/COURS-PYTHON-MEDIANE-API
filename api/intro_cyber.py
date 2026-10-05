"""
Introduction à Python : Fondamentaux & Premiers Pas en Cybersécurité - CORRIGÉ.
BTS CIEL // Informatique, Réseaux & Cybersécurité.

Exercice 0 :
- 0.1 : Chaînes de caractères & Chiffrement de César
- 0.2 : Chiffrement par clé XOR & Opérateur binaire
- 0.3 : Tuples vs Listes (Immutabilité & Données scellées)
- 0.4 : Mutation en place vs Copie de liste (Le piège des références)
- 0.5 : Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau CIEL-Guard)
"""

import os
from typing import List, Tuple


# =============================================================================
# EXERCICE 0.1 : Chaînes de caractères & Chiffrement de César
# =============================================================================

def chiffrer_cesar(texte: str, decalage: int) -> str:
    """
    Chiffre une chaîne en décalant chaque lettre dans l'alphabet (modulo 26).
    Conserve la casse (majuscule / minuscule) et préserve les autres caractères (espaces, ponctuation).
    """
    resultat = []
    decalage_normalise = decalage % 26

    for char in texte:
        if 'A' <= char <= 'Z':
            base = ord('A')
            nouveau = chr(base + (ord(char) - base + decalage_normalise) % 26)
            resultat.append(nouveau)
        elif 'a' <= char <= 'z':
            base = ord('a')
            nouveau = chr(base + (ord(char) - base + decalage_normalise) % 26)
            resultat.append(nouveau)
        else:
            resultat.append(char)

    return "".join(resultat)


def dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str:
    """
    Déchiffre un message chiffré par César en appliquant le décalage opposé.
    """
    return chiffrer_cesar(texte_chiffre, -decalage)


# =============================================================================
# EXERCICE 0.2 : Chiffrement par clé XOR & Opérateur binaire
# =============================================================================

def chiffrer_xor(texte: str, cle: str) -> List[int]:
    """
    Chiffre un texte avec une clé secrète via l'opérateur bit-à-bit XOR (^).
    Chaque caractère du texte est combiné avec le caractère correspondant de la clé
    (répétée cycliquement via l'opérateur modulo).
    
    Retourne la liste des entiers (octets chiffrés).
    """
    if not cle:
        raise ValueError("La clé ne peut pas être vide.")

    octets = []
    for i in range(len(texte)):
        caractere = texte[i]
        caractere_cle = cle[i % len(cle)]
        valeur_xor = ord(caractere) ^ ord(caractere_cle)
        octets.append(valeur_xor)

    return octets


def dechiffrer_xor(octets: List[int], cle: str) -> str:
    """
    Déchiffre une liste d'octets XOR en réappliquant la même clé.
    Propriété fondamentale : (A ^ K) ^ K == A.
    """
    if not cle:
        raise ValueError("La clé ne peut pas être vide.")

    caracteres = []
    for i in range(len(octets)):
        valeur_octet = octets[i]
        caractere_cle = cle[i % len(cle)]
        valeur_originale = valeur_octet ^ ord(caractere_cle)
        caracteres.append(chr(valeur_originale))

    return "".join(caracteres)


# =============================================================================
# EXERCICE 0.3 : Tuples vs Listes (Immutabilité & Données scellées)
# =============================================================================

def creer_identifiant_scelle(login: str, uid: int, privilege: str) -> Tuple[str, int, str]:
    """
    Crée un enregistrement d'utilisateur sous forme de TUPLE immuable.
    Contrairement à une liste, un tuple garantit qu'aucun élément ne peut être altéré en mémoire.
    """
    return (login, uid, privilege)


def tenter_modification_tuple(identifiant: Tuple) -> bool:
    """
    Démontre la sécurité du tuple : toute tentative d'affectation (identifiant[0] = ...)
    lève une exception TypeError.
    Retourne True si l'immutabilité a bien protégé l'objet.
    """
    try:
        # En Python, cette ligne est formellement interdite sur un tuple :
        identifiant[0] = "pirate"  # type: ignore
        return False
    except TypeError:
        return True


# =============================================================================
# EXERCICE 0.4 : Mutation en place vs Copie de liste (Le piège des références)
# =============================================================================

def filtrer_ip_copie(liste_ips: List[str], ip_bannie: str) -> List[str]:
    """
    Filtre une liste d'adresses IP SANS modifier la liste d'origine.
    1. Crée une copie indépendante avec .copy() ou une compréhension de liste.
    2. Garantit que la liste initiale passée par l'appelant conserve son intégrité.
    """
    copie_securisee = [ip for ip in liste_ips if ip != ip_bannie]
    return copie_securisee


# =============================================================================
# EXERCICE 0.5 : Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau CIEL-Guard)
# =============================================================================

def dechiffrer_sequence_ciel_guard(octets: List[int], cle: str, decalage: int) -> str:
    """
    Moteur de déchiffrement propriétaire du protocole CIEL-Guard :
    - Indice pair   : Déchiffrement XOR avec le caractère de la clé à la position (i // 2) % len(cle)
    - Indice impair : Déchiffrement César inverse avec décalage
    """
    caracteres = []
    for i, val in enumerate(octets):
        if i % 2 == 0:
            char_cle = cle[(i // 2) % len(cle)]
            caracteres.append(chr(val ^ ord(char_cle)))
        else:
            if 65 <= val <= 90:
                caracteres.append(chr((val - 65 - decalage) % 26 + 65))
            elif 97 <= val <= 122:
                caracteres.append(chr((val - 97 - decalage) % 26 + 97))
            else:
                caracteres.append(chr(val))
    return "".join(caracteres)


def decoder_ciel_guard(chemin_fichier: str = "mystere.payload") -> Tuple[str, int, int]:
    """
    Projet Défi Anti-IA :
    1. Ouvre et lit le fichier payload physique sur le disque.
    2. Parse la liste d'entiers séparés par des virgules.
    3. Calcule la clé dérivée dynamique : 'CIEL' + str(nombre_octets).
    4. Calcule le décalage César : somme des chiffres de l'année 2026 (2+0+2+6 = 10).
    5. Déchiffre la séquence et retourne un tuple scellé :
       (message_restaure, total_octets, checksum_somme)
    """
    if not os.path.exists(chemin_fichier):
        # Chercher également dans le dossier courant ou api/
        alternatif = os.path.join(os.path.dirname(__file__), chemin_fichier)
        if os.path.exists(alternatif):
            chemin_fichier = alternatif
        else:
            raise FileNotFoundError(f"Fichier introuvable : {chemin_fichier}")

    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read().strip()

    octets = [int(x.strip()) for x in contenu.split(',') if x.strip()]
    nombre_octets = len(octets)
    cle = f"CIEL{nombre_octets}"
    decalage = 10

    message_restaure = dechiffrer_sequence_ciel_guard(octets, cle, decalage)
    checksum = sum(octets)

    return (message_restaure, nombre_octets, checksum)


# =============================================================================
# Validation et Démonstration Console
# =============================================================================

def run_introduction():
    print("=" * 72)
    print("BTS CIEL // INTRODUCTION À PYTHON : FONDAMENTAUX & CYBERSÉCURITÉ")
    print("=" * 72)

    # 0.1 César
    print("\n--- [Exercice 0.1] Chaînes de caractères & Chiffrement de César ---")
    message = "ALERTE INTRUSION 2026 !"
    k = 4
    chiffre = chiffrer_cesar(message, k)
    clair = dechiffrer_cesar(chiffre, k)
    print(f"Original : {message}")
    print(f"Chiffré  : {chiffre} (décalage = {k})")
    print(f"Restauré : {clair}")

    # 0.2 XOR
    print("\n--- [Exercice 0.2] Chiffrement par clé XOR & Opérateur binaire ---")
    secret = "PASSWORD_SECRET"
    cle = "CYBER"
    octets = chiffrer_xor(secret, cle)
    recupere = dechiffrer_xor(octets, cle)
    print(f"Secret   : {secret}")
    print(f"Clé      : {cle}")
    print(f"Octets   : {octets}")
    print(f"Restauré : {recupere}")

    # 0.3 Tuples
    print("\n--- [Exercice 0.3] Tuples vs Listes (Immutabilité & Données scellées) ---")
    user = creer_identifiant_scelle("admin_root", 1001, "SUPERADMIN")
    print(f"Identifiant scellé (tuple) : {user}")
    est_protege = tenter_modification_tuple(user)
    print(f"Tentative d'altération en mémoire bloquée : {est_protege} (TypeError capturé)")

    # 0.4 Copie vs En place
    print("\n--- [Exercice 0.4] Mutation en place vs Copie de liste (Le piège des références) ---")
    ips_originales = ["192.168.1.1", "10.0.0.99", "192.168.1.50"]
    ips_filtrees = filtrer_ip_copie(ips_originales, "10.0.0.99")
    print(f"Liste originale (intacte)   : {ips_originales} (id: {id(ips_originales)})")
    print(f"Liste filtrée (nouvel objet): {ips_filtrees} (id: {id(ips_filtrees)})")

    # 0.5 Projet Défi Anti-IA
    print("\n--- [Exercice 0.5] Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau CIEL-Guard) ---")
    try:
        msg_resolu, nb, chk = decoder_ciel_guard("mystere.payload")
        print(f"Artefact 'mystere.payload' lu avec succès ({nb} octets, checksum={chk})")
        print(f"-> MESSAGE SECRET DÉCODÉ : \033[92m{msg_resolu}\033[0m")
        print("-> Validation du Défi : SUCCÈS TOTAL !")
    except Exception as e:
        print(f"Erreur lors du décodage du défi : {e}")

    print("=" * 72)


if __name__ == '__main__':
    run_introduction()
