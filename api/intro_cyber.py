"""
BTS CIEL // Introduction à Python : Fondamentaux & Cybersécurité - ÉNONCÉ ÉLÈVE.
Architecture pédagogique progressive (Exercice 0 : 0.1 à 0.6).

Complétez les fonctions ci-dessous conformément aux consignes détaillées dans le README.md.

Sommaire :
- 0.1 : Fonctions, Variables & Types de base (def, return, int, float, bool, if/else)
- 0.2 : Chaînes de caractères (str : indexation, slicing, strip, split, replace)
- 0.3 : Listes (list : création, parcours for, append, calculs sum/len/min/max)
- 0.4 : Tuples & Dictionnaires (tuple immuable, unpacking, dict clé-valeur)
- 0.5 : Références en mémoire & Copie défensive (alias vs copy)
- 0.6 : Algorithmes de Chiffrement & Défi Anti-IA (César, XOR, Décodeur CIEL-Guard)
"""

import os
from typing import List, Tuple, Dict


# =============================================================================
# EXERCICE 0.1 : Fonctions, Variables & Types fondamentaux
# =============================================================================

def analyser_port(port: int) -> str:
    """
    Catégorise un numéro de port réseau selon les standards IANA :
    - < 0 ou > 65535 : "Invalide"
    - 0 à 1023      : "Privilégié / Système" (ex: SSH 22, HTTP 80, HTTPS 443)
    - 1024 à 49151  : "Enregistré / Utilisateur" (ex: MySQL 3306, Flask 5000)
    - 49152 à 65535 : "Dynamique / Privé" (ports éphémères de connexion cliente)
    """
    # TODO: Exercice 0.1
    # 1. Vérifier si port n'est pas un entier ou s'il est en dehors de [0, 65535] -> "Invalide"
    # 2. Si port <= 1023 -> "Privilégié / Système"
    # 3. Si port <= 49151 -> "Enregistré / Utilisateur"
    # 4. Sinon -> "Dynamique / Privé"
    pass


def calculer_debit(octets: int, duree_secondes: float) -> float:
    """
    Calcule le débit réseau en octets par seconde (octets / s).
    Gère la division par zéro et les entrées négatives en retournant 0.0.
    """
    # TODO: Exercice 0.1
    # 1. Si duree_secondes <= 0 ou octets < 0 -> retourner 0.0
    # 2. Sinon, retourner round(octets / duree_secondes, 2)
    pass


# =============================================================================
# EXERCICE 0.2 : Les Chaînes de caractères (str)
# =============================================================================

def normaliser_identifiant(login_brut: str) -> str:
    """
    Nettoie et normalise un login utilisateur :
    - Retire les espaces en début/fin avec .strip()
    - Convertit en minuscules avec .lower()
    - Remplace les espaces internes par des tirets bas avec .replace()
    """
    # TODO: Exercice 0.2
    pass


def masquer_mot_de_passe(mdp: str) -> str:
    """
    Masque un mot de passe pour affichage sécurisé dans un journal :
    - Longueur <= 2 : retourne autant d'étoiles que de caractères
    - Longueur > 2  : conserve le 1er et le dernier caractère, masque l'intérieur avec '*'
    Démontre l'indexation s[0], s[-1], len() et le slicing / répétition de chaînes.
    """
    # TODO: Exercice 0.2
    pass


def extraire_champs_log(ligne_log: str, separateur: str = "|") -> List[str]:
    """
    Découpe une ligne de journal selon un séparateur et nettoie chaque segment.
    Démontre l'usage de .split() et de la compréhension de liste avec .strip().
    """
    # TODO: Exercice 0.2
    pass


# =============================================================================
# EXERCICE 0.3 : Les Listes (list)
# =============================================================================

def filtrer_ports_actifs(ports: List[int]) -> List[int]:
    """
    Filtre une liste de ports pour ne conserver que les ports strictement positifs (> 0).
    Démontre la création d'une liste vide, la boucle for et la méthode .append().
    """
    # TODO: Exercice 0.3
    pass


def statistiques_latences(pings: List[float]) -> Tuple[float, float, float]:
    """
    Calcule sans module externe le minimum, le maximum et la moyenne des latences ping.
    Retourne un tuple : (min, max, moyenne). Si vide, retourne (0.0, 0.0, 0.0).
    """
    # TODO: Exercice 0.3
    # Astuce : sum(), min(), max(), len() et round(..., 2)
    pass


def compter_occurrences(historique: List[str], cible: str) -> int:
    """
    Compte manuellement le nombre d'occurrences d'une valeur dans une liste.
    Démontre une boucle for avec accumulateur.
    """
    # TODO: Exercice 0.3
    pass


# =============================================================================
# EXERCICE 0.4 : Tuples & Dictionnaires (tuple, dict)
# =============================================================================

def creer_enregistrement_scelle(ip: str, port: int, protocole: str) -> Tuple[str, int, str]:
    """
    Crée un enregistrement réseau sous forme de TUPLE immuable.
    """
    # TODO: Exercice 0.4
    pass


def verifier_immutabilite_tuple(donnees: Tuple) -> bool:
    """
    Démontre l'immutabilité du tuple : toute tentative d'affectation lève TypeError.
    Retourne True si l'immutabilité a protégé l'objet.
    """
    # TODO: Exercice 0.4
    # Utiliser un bloc try / except TypeError pour tester : donnees[0] = "pirate"
    pass


def creer_rapport_incident(id_incident: int, source_ip: str, criticite: str) -> Dict:
    """
    Construit une fiche d'incident de sécurité sous forme de DICTIONNAIRE clé-valeur.
    Initialise la clé 'resolu' à False.
    """
    # TODO: Exercice 0.4
    pass


def analyser_frequence_alertes(journal_alertes: List[str]) -> Dict[str, int]:
    """
    Compte la fréquence d'apparition de chaque type d'alerte via un dictionnaire.
    Démontre l'utilisation de .get() pour accumuler les valeurs.
    """
    # TODO: Exercice 0.4
    pass


# =============================================================================
# EXERCICE 0.5 : Références en mémoire & Copie défensive (.copy)
# =============================================================================

def filtrer_ip_copie(liste_ips: List[str], ip_bannie: str) -> List[str]:
    """
    Filtre une liste d'adresses IP SANS modifier la liste originale.
    Garantit l'intégrité de la liste passée par l'appelant.
    """
    # TODO: Exercice 0.5
    pass


def dupliquer_et_nettoyer(ports: List[int]) -> Tuple[List[int], List[int]]:
    """
    Démontre la copie défensive et l'élimination des doublons :
    - Conserve la liste originale strictement intacte
    - Retourne (liste_originale_intacte, copie_sans_doublons)
    """
    # TODO: Exercice 0.5
    pass


# =============================================================================
# EXERCICE 0.6 : Algorithmes de Chiffrement & Défi Anti-IA (CIEL-Guard)
# =============================================================================

def chiffrer_cesar(texte: str, decalage: int) -> str:
    """
    Chiffre une chaîne en décalant chaque lettre dans l'alphabet (modulo 26).
    Conserve la casse et préserve les autres caractères (espaces, ponctuation).
    """
    # TODO: Exercice 0.6
    pass


def dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str:
    """
    Déchiffre un message César en appliquant le décalage opposé.
    """
    # TODO: Exercice 0.6
    pass


def chiffrer_xor(texte: str, cle: str) -> List[int]:
    """
    Chiffre un texte avec une clé secrète via l'opérateur XOR (^).
    Chaque caractère est combiné avec le caractère correspondant de la clé cyclique.
    """
    # TODO: Exercice 0.6
    pass


def dechiffrer_xor(octets: List[int], cle: str) -> str:
    """
    Déchiffre une liste d'octets XOR en réappliquant la même clé.
    Propriété : (A ^ K) ^ K == A.
    """
    # TODO: Exercice 0.6
    pass


def decoder_ciel_guard(chemin_fichier: str = "mystere.payload") -> Tuple[str, int, int]:
    """
    Projet Défi Anti-IA CIEL-Guard :
    1. Lit le fichier physique sur disque.
    2. Dérive la clé dynamique : 'CIEL' + str(nombre_octets).
    3. Décalage César : somme des chiffres de 2026 (10).
    4. Déchiffre selon la règle d'alternance (indices pairs : XOR, impairs : César -10).
    5. Retourne un tuple scellé : (message_restaure, nombre_octets, checksum).
    """
    # TODO: Exercice 0.6
    pass


if __name__ == '__main__':
    print("=" * 76)
    print("BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON (ÉNONCÉ ÉLÈVE)")
    print("=" * 76)
    print("Complétez les fonctions des exercices 0.1 à 0.6 pour valider les tests !")
    print("Consultez le fichier README.md pour les explications détaillées et consignes.")
