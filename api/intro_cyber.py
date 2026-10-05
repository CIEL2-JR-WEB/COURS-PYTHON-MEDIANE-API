"""
Introduction à Python : Fondamentaux & Premiers Pas en Cybersécurité - ÉNONCÉ ÉLÈVE.
BTS CIEL // Informatique, Réseaux & Cybersécurité.

Exercice 0 :
- 0.1 : Chaînes de caractères & Chiffrement de César
- 0.2 : Chiffrement par clé XOR & Opérateur binaire
- 0.3 : Tuples vs Listes (Immutabilité & Données scellées)
- 0.4 : Mutation en place vs Copie de liste (Le piège des références)
- 0.5 : Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau CIEL-Guard)

Complétez les fonctions suivantes conformément aux consignes du README.md.
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
    # TODO: Exercice 0.1
    # 1. Normaliser le décalage avec % 26
    # 2. Parcourir chaque caractère du texte
    # 3. Si majuscule ('A' <= c <= 'Z') : décaler à partir de ord('A')
    # 4. Si minuscule ('a' <= c <= 'z') : décaler à partir de ord('a')
    # 5. Sinon : conserver le caractère tel quel
    # 6. Retourner la chaîne chiffrée
    pass


def dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str:
    """
    Déchiffre un message chiffré par César en appliquant le décalage opposé.
    """
    # TODO: Exercice 0.1
    # Astuce : Déchiffrer revient à appeler chiffrer_cesar avec -decalage
    pass


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
    # TODO: Exercice 0.2
    # 1. Vérifier que la clé n'est pas vide
    # 2. Pour chaque indice i de 0 à len(texte) - 1 :
    #    char_cle = cle[i % len(cle)]
    #    calculer ord(texte[i]) ^ ord(char_cle)
    # 3. Retourner la liste des entiers
    pass


def dechiffrer_xor(octets: List[int], cle: str) -> str:
    """
    Déchiffre une liste d'octets XOR en réappliquant la même clé.
    Propriété fondamentale : (A ^ K) ^ K == A.
    """
    # TODO: Exercice 0.2
    # 1. Pour chaque indice i de 0 à len(octets) - 1 :
    #    char_cle = cle[i % len(cle)]
    #    recalculer la valeur avec octets[i] ^ ord(char_cle)
    #    convertir en caractère avec chr()
    # 2. Retourner la chaîne reconstituée
    pass


# =============================================================================
# EXERCICE 0.3 : Tuples vs Listes (Immutabilité & Données scellées)
# =============================================================================

def creer_identifiant_scelle(login: str, uid: int, privilege: str) -> Tuple[str, int, str]:
    """
    Crée un enregistrement d'utilisateur sous forme de TUPLE immuable.
    """
    # TODO: Exercice 0.3
    # Retourner un tuple contenant (login, uid, privilege)
    pass


def tenter_modification_tuple(identifiant: Tuple) -> bool:
    """
    Démontre la sécurité du tuple : toute tentative d'affectation (identifiant[0] = ...)
    lève une exception TypeError.
    Retourne True si l'immutabilité a bien levé l'exception TypeError.
    """
    # TODO: Exercice 0.3
    # Utiliser try / except TypeError pour intercepter l'affectation interdite
    pass


# =============================================================================
# EXERCICE 0.4 : Mutation en place vs Copie de liste (Le piège des références)
# =============================================================================

def filtrer_ip_copie(liste_ips: List[str], ip_bannie: str) -> List[str]:
    """
    Filtre une liste d'adresses IP SANS modifier la liste d'origine.
    Garantit que la liste initiale passée par l'appelant conserve son intégrité.
    """
    # TODO: Exercice 0.4
    # 1. Créer une nouvelle liste ne contenant pas ip_bannie
    # 2. Ne jamais modifier liste_ips directement
    pass


# =============================================================================
# EXERCICE 0.5 : Projet Défi Anti-IA (Le Décodeur d'Artefact Réseau CIEL-Guard)
# =============================================================================

def decoder_ciel_guard(chemin_fichier: str = "mystere.payload") -> Tuple[str, int, int]:
    """
    Projet Défi Anti-IA :
    1. Ouvre et lit le fichier payload physique sur le disque.
    2. Parse la liste d'entiers séparés par des virgules.
    3. Calcule la clé dérivée dynamique : 'CIEL' + str(nombre_octets).
    4. Calcule le décalage César : somme des chiffres de l'année 2026 (10).
    5. Déchiffre la séquence selon la règle d'alternance :
       - Indice pair : XOR avec le caractère de la clé à la position (i // 2) % len(cle)
       - Indice impair : César inverse (-10)
    6. Retourne un tuple scellé : (message_restaure, total_octets, checksum_somme)
    """
    # TODO: Exercice 0.5
    # Implémentez la lecture du fichier et le déchiffrement alterné
    pass


if __name__ == '__main__':
    print("BTS CIEL // Tests de l'Introduction à Python (Exercice 0.1 à 0.5)")
    print("Complétez les fonctions ci-dessus pour valider les exercices et le Défi CIEL-Guard !")
