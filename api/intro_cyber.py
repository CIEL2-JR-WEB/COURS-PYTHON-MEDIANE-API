"""
BTS CIEL // Introduction à Python : Fondamentaux & Cybersécurité - CORRIGÉ.
Architecture pédagogique progressive (Exercice 0 : 0.1 à 0.6).

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
    if not isinstance(port, int) or port < 0 or port > 65535:
        return "Invalide"
    elif port <= 1023:
        return "Privilégié / Système"
    elif port <= 49151:
        return "Enregistré / Utilisateur"
    else:
        return "Dynamique / Privé"


def calculer_debit(octets: int, duree_secondes: float) -> float:
    """
    Calcule le débit réseau en octets par seconde (octets / s).
    Gère la division par zéro et les entrées négatives en retournant 0.0.
    """
    if duree_secondes <= 0 or octets < 0:
        return 0.0
    return round(float(octets) / duree_secondes, 2)


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
    return login_brut.strip().lower().replace(" ", "_")


def masquer_mot_de_passe(mdp: str) -> str:
    """
    Masque un mot de passe pour affichage sécurisé dans un journal :
    - Longueur <= 2 : retourne autant d'étoiles que de caractères
    - Longueur > 2  : conserve le 1er et le dernier caractère, masque l'intérieur avec '*'
    Démontre l'indexation s[0], s[-1], len() et le slicing / répétition de chaînes.
    """
    if len(mdp) <= 2:
        return "*" * len(mdp)
    return mdp[0] + ("*" * (len(mdp) - 2)) + mdp[-1]


def extraire_champs_log(ligne_log: str, separateur: str = "|") -> List[str]:
    """
    Découpe une ligne de journal selon un séparateur et nettoie chaque segment.
    Démontre l'usage de .split() et de la compréhension de liste avec .strip().
    """
    return [morceau.strip() for morceau in ligne_log.split(separateur)]


# =============================================================================
# EXERCICE 0.3 : Les Listes (list)
# =============================================================================

def filtrer_ports_actifs(ports: List[int]) -> List[int]:
    """
    Filtre une liste de ports pour ne conserver que les ports strictement positifs (> 0).
    Démontre la création d'une liste vide, la boucle for et la méthode .append().
    """
    ouverts = []
    for p in ports:
        if p > 0:
            ouverts.append(p)
    return ouverts


def statistiques_latences(pings: List[float]) -> Tuple[float, float, float]:
    """
    Calcule sans module externe le minimum, le maximum et la moyenne des latences ping.
    Retourne un tuple : (min, max, moyenne). Si vide, retourne (0.0, 0.0, 0.0).
    """
    if not pings:
        return (0.0, 0.0, 0.0)
    lat_min = round(min(pings), 2)
    lat_max = round(max(pings), 2)
    lat_moy = round(sum(pings) / len(pings), 2)
    return (lat_min, lat_max, lat_moy)


def compter_occurrences(historique: List[str], cible: str) -> int:
    """
    Compte manuellement le nombre d'occurrences d'une valeur dans une liste.
    Démontre une boucle for avec accumulateur.
    """
    compteur = 0
    for item in historique:
        if item == cible:
            compteur += 1
    return compteur


# =============================================================================
# EXERCICE 0.4 : Tuples & Dictionnaires (tuple, dict)
# =============================================================================

def creer_enregistrement_scelle(ip: str, port: int, protocole: str) -> Tuple[str, int, str]:
    """
    Crée un enregistrement réseau sous forme de TUPLE immuable.
    """
    return (ip, port, protocole)


def verifier_immutabilite_tuple(donnees: Tuple) -> bool:
    """
    Démontre l'immutabilité du tuple : toute tentative d'affectation lève TypeError.
    Retourne True si l'immutabilité a protégé l'objet.
    """
    try:
        donnees[0] = "pirate"  # type: ignore
        return False
    except TypeError:
        return True


def creer_rapport_incident(id_incident: int, source_ip: str, criticite: str) -> Dict:
    """
    Construit une fiche d'incident de sécurité sous forme de DICTIONNAIRE clé-valeur.
    """
    return {
        "id": id_incident,
        "source": source_ip,
        "criticite": criticite,
        "resolu": False
    }


def analyser_frequence_alertes(journal_alertes: List[str]) -> Dict[str, int]:
    """
    Compte la fréquence d'apparition de chaque type d'alerte via un dictionnaire.
    Démontre l'utilisation de .get() pour accumuler les valeurs.
    """
    frequences: Dict[str, int] = {}
    for alerte in journal_alertes:
        frequences[alerte] = frequences.get(alerte, 0) + 1
    return frequences


# =============================================================================
# EXERCICE 0.5 : Références en mémoire & Copie défensive (.copy)
# =============================================================================

def filtrer_ip_copie(liste_ips: List[str], ip_bannie: str) -> List[str]:
    """
    Filtre une liste d'adresses IP SANS modifier la liste originale.
    Garantit l'intégrité de la liste passée par l'appelant.
    """
    return [ip for ip in liste_ips if ip != ip_bannie]


def dupliquer_et_nettoyer(ports: List[int]) -> Tuple[List[int], List[int]]:
    """
    Démontre la copie défensive et l'élimination des doublons :
    - Conserve la liste originale strictement intacte
    - Retourne (liste_originale_intacte, copie_sans_doublons)
    """
    copie = ports.copy()
    uniques = []
    for p in copie:
        if p not in uniques:
            uniques.append(p)
    return (ports, uniques)


# =============================================================================
# EXERCICE 0.6 : Algorithmes de Chiffrement & Défi Anti-IA (CIEL-Guard)
# =============================================================================

def chiffrer_cesar(texte: str, decalage: int) -> str:
    """
    Chiffre une chaîne en décalant chaque lettre dans l'alphabet (modulo 26).
    Conserve la casse et préserve les autres caractères (espaces, ponctuation).
    """
    resultat = []
    k = decalage % 26
    for char in texte:
        if 'A' <= char <= 'Z':
            base = ord('A')
            resultat.append(chr(base + (ord(char) - base + k) % 26))
        elif 'a' <= char <= 'z':
            base = ord('a')
            resultat.append(chr(base + (ord(char) - base + k) % 26))
        else:
            resultat.append(char)
    return "".join(resultat)


def dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str:
    """
    Déchiffre un message César en appliquant le décalage opposé.
    """
    return chiffrer_cesar(texte_chiffre, -decalage)


def chiffrer_xor(texte: str, cle: str) -> List[int]:
    """
    Chiffre un texte avec une clé secrète via l'opérateur XOR (^).
    Chaque caractère est combiné avec le caractère correspondant de la clé cyclique.
    """
    if not cle:
        raise ValueError("La clé ne peut pas être vide.")
    octets = []
    for i in range(len(texte)):
        char_texte = texte[i]
        char_cle = cle[i % len(cle)]
        octets.append(ord(char_texte) ^ ord(char_cle))
    return octets


def dechiffrer_xor(octets: List[int], cle: str) -> str:
    """
    Déchiffre une liste d'octets XOR en réappliquant la même clé.
    Propriété : (A ^ K) ^ K == A.
    """
    if not cle:
        raise ValueError("La clé ne peut pas être vide.")
    caracteres = []
    for i in range(len(octets)):
        valeur = octets[i]
        char_cle = cle[i % len(cle)]
        caracteres.append(chr(valeur ^ ord(char_cle)))
    return "".join(caracteres)


def dechiffrer_sequence_ciel_guard(octets: List[int], cle: str, decalage: int) -> str:
    """
    Moteur de déchiffrement propriétaire CIEL-Guard :
    - Indice pair   : Déchiffrement XOR avec la clé à (i // 2) % len(cle)
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
    Projet Défi Anti-IA CIEL-Guard :
    1. Lit le fichier physique sur disque.
    2. Dérive la clé dynamique : 'CIEL' + str(nombre_octets).
    3. Décalage César : somme des chiffres de 2026 (10).
    4. Déchiffre selon la règle d'alternance.
    5. Retourne un tuple scellé : (message_restaure, nombre_octets, checksum).
    """
    if not os.path.exists(chemin_fichier):
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
    print("=" * 76)
    print("BTS CIEL // EXERCICE 0 : FONDAMENTAUX DE PYTHON & CYBERSÉCURITÉ")
    print("=" * 76)

    # 0.1 Fonctions & Types
    print("\n--- [Exercice 0.1] Fonctions, Variables & Types fondamentaux ---")
    ports_test = [22, 5000, 55000, 99999]
    for p in ports_test:
        print(f"Port {p:5d} -> Catégorie : {analyser_port(p)}")
    debit = calculer_debit(10_000_000, 2.5)
    print(f"Débit calculé pour 10 Mo en 2.5s : {debit} octets/s ({debit / 1_000_000:.2f} Mo/s)")

    # 0.2 Chaînes (str)
    print("\n--- [Exercice 0.2] Les Chaînes de caractères (str) ---")
    login = normaliser_identifiant("  Admin Reseau 2026  ")
    print(f"Login normalisé      : '{login}'")
    mdp_masque = masquer_mot_de_passe("SuperSecretPass2026!")
    print(f"Mot de passe masqué  : {mdp_masque}")
    log_champs = extraire_champs_log("2026-10-05 14:30:00 | 192.168.1.50 | AUTH_SUCCESS | SSH")
    print(f"Champs de log extraits: {log_champs}")

    # 0.3 Listes (list)
    print("\n--- [Exercice 0.3] Les Listes (list) ---")
    ports_bruts = [22, -1, 80, 0, 443, -8080, 3306]
    actifs = filtrer_ports_actifs(ports_bruts)
    print(f"Ports bruts          : {ports_bruts}")
    print(f"Ports actifs filtrés : {actifs}")
    pings = [12.4, 8.1, 15.6, 9.8, 22.0]
    p_min, p_max, p_moy = statistiques_latences(pings)
    print(f"Pings analysés       : {pings}")
    print(f"Statistiques ping    : Min = {p_min} ms | Max = {p_max} ms | Moyenne = {p_moy} ms")
    ips_log = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "192.168.1.1"]
    nb_occ = compter_occurrences(ips_log, "192.168.1.1")
    print(f"Occurrences de 192.168.1.1 : {nb_occ} fois")

    # 0.4 Tuples & Dictionnaires
    print("\n--- [Exercice 0.4] Tuples & Dictionnaires (tuple, dict) ---")
    socket_scelle = creer_enregistrement_scelle("192.168.1.1", 443, "TCP")
    print(f"Socket scellé (tuple): {socket_scelle}")
    est_protege = verifier_immutabilite_tuple(socket_scelle)
    print(f"Tentative d'altération en mémoire bloquée : {est_protege} (TypeError capturé)")
    incident = creer_rapport_incident(101, "198.51.100.42", "CRITIQUE")
    print(f"Fiche d'incident     : {incident}")
    alertes = ["BRUTE_FORCE", "SQLI", "BRUTE_FORCE", "XSS", "BRUTE_FORCE", "SQLI"]
    frequences = analyser_frequence_alertes(alertes)
    print(f"Fréquences alertes   : {frequences}")

    # 0.5 Références & Copies (.copy)
    print("\n--- [Exercice 0.5] Références en mémoire & Copie défensive (.copy) ---")
    ips_sources = ["192.168.1.10", "10.0.0.99", "192.168.1.20"]
    ips_filtrees = filtrer_ip_copie(ips_sources, "10.0.0.99")
    print(f"Liste source (intacte)      : {ips_sources} (id: {id(ips_sources)})")
    print(f"Liste filtrée (nouvel objet): {ips_filtrees} (id: {id(ips_filtrees)})")
    ports_avec_doublons = [80, 443, 80, 22, 443, 8080]
    orig, dedup = dupliquer_et_nettoyer(ports_avec_doublons)
    print(f"Déduplication défensive     : {dedup} (source intacte : {orig == ports_avec_doublons})")

    # 0.6 Chiffrement & Défi CIEL-Guard
    print("\n--- [Exercice 0.6] Algorithmes de Chiffrement & Défi Anti-IA ---")
    msg_clair = "ALERTE INTRUSION 2026 !"
    c_cesar = chiffrer_cesar(msg_clair, 4)
    print(f"César chiffré (+4)   : '{c_cesar}' -> Restauré : '{dechiffrer_cesar(c_cesar, 4)}'")
    secret_pass = "PASSWORD_SECRET"
    octets_xor = chiffrer_xor(secret_pass, "CYBER")
    print(f"XOR chiffré          : {octets_xor} -> Restauré : '{dechiffrer_xor(octets_xor, 'CYBER')}'")
    try:
        flag, nb, chk = decoder_ciel_guard("mystere.payload")
        print(f"Artefact 'mystere.payload' lu avec succès ({nb} octets, checksum={chk})")
        print(f"-> MESSAGE SECRET DÉCODÉ : \033[92m{flag}\033[0m")
        print("-> Validation du Défi CIEL-Guard : SUCCÈS TOTAL !")
    except Exception as e:
        print(f"Erreur défi : {e}")

    print("=" * 76)


if __name__ == '__main__':
    run_introduction()
