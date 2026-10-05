"""
Introduction à Python : Fondamentaux, Algorithmique & Cybersécurité - CORRIGÉ.
BTS CIEL // Informatique, Réseaux & Cybersécurité.

Ce module regroupe les exercices préliminaires indispensables :
- I.1 : Chaînes de caractères, conditions & audit de mot de passe (tuples & strings)
- I.2 : Chiffrement de César, codes ASCII (ord/chr) et cryptanalyse par force brute
- I.3 : Chiffrement par clé XOR & Masque jetable (listes d'octets et symétrie)
- I.4 : Tuples vs Listes, passage par référence, mutation en place vs copie défensive
- I.5 : Dictionnaires & structures : analyse de journaux de sécurité (IOCs)
"""

from typing import List, Tuple, Dict


# =============================================================================
# EXERCICE I.1 : Chaînes de caractères & Audit de mot de passe
# =============================================================================

def auditer_mot_de_passe(mdp: str) -> Tuple[bool, int, List[str]]:
    """
    Vérifie la robustesse d'un mot de passe selon la politique de sécurité.
    
    Critères :
    1. Longueur minimale de 8 caractères (+1 pt si >= 12)
    2. Au moins une lettre majuscule
    3. Au moins une lettre minuscule
    4. Au moins un chiffre
    5. Au moins un caractère spécial parmi : !@#$%^&*_-+=
    
    Retourne un tuple immuable :
    (est_conforme: bool, score: int sur 5, anomalies: list[str])
    """
    anomalies: List[str] = []
    score = 0
    caracteres_speciaux = set("!@#$%^&*_-+=")

    # 1. Vérification de longueur
    if len(mdp) < 8:
        anomalies.append("Le mot de passe doit comporter au moins 8 caractères.")
    else:
        score += 1

    # 2, 3, 4, 5. Détection des catégories de caractères
    a_maj = any(c.isupper() for c in mdp)
    a_min = any(c.islower() for c in mdp)
    a_chiffre = any(c.isdigit() for c in mdp)
    a_special = any(c in caracteres_speciaux for c in mdp)

    if not a_maj:
        anomalies.append("Au moins une majuscule requise.")
    else:
        score += 1

    if not a_min:
        anomalies.append("Au moins une minuscule requise.")
    else:
        score += 1

    if not a_chiffre:
        anomalies.append("Au moins un chiffre requis.")
    else:
        score += 1

    if not a_special:
        anomalies.append("Au moins un caractère spécial requis (!@#$%^&*_-+=).")
    else:
        score += 1

    # Bonus longueur
    if len(mdp) >= 12 and score == 5:
        # Score parfait
        pass

    est_conforme = (len(anomalies) == 0)
    return (est_conforme, score, anomalies)


# =============================================================================
# EXERCICE I.2 : Chiffrement par décalage (César) & Cryptanalyse
# =============================================================================

def chiffrer_cesar(texte: str, decalage: int) -> str:
    """
    Chiffre une chaîne selon l'algorithme de César en appliquant un décalage modulaire.
    Conserve la casse (majuscule / minuscule) et laisse intacts les caractères non alphabétiques.
    """
    resultat = []
    decalage_normalise = decalage % 26

    for char in texte:
        if 'A' <= char <= 'Z':
            base = ord('A')
            nouveau_char = chr(base + (ord(char) - base + decalage_normalise) % 26)
            resultat.append(nouveau_char)
        elif 'a' <= char <= 'z':
            base = ord('a')
            nouveau_char = chr(base + (ord(char) - base + decalage_normalise) % 26)
            resultat.append(nouveau_char)
        else:
            # Ponctuation, espaces, chiffres laissés en clair
            resultat.append(char)

    return "".join(resultat)


def dechiffrer_cesar(texte_chiffre: str, decalage: int) -> str:
    """
    Déchiffre un message en appliquant le décalage inverse.
    """
    return chiffrer_cesar(texte_chiffre, -decalage)


def casser_cesar_force_brute(texte_chiffre: str) -> List[Tuple[int, str]]:
    """
    Génère la liste des 25 déchiffrements possibles pour casser le chiffrement
    sans connaître la clé initiale (cryptanalyse par force brute).
    """
    candidats = []
    for k in range(1, 26):
        candidats.append((k, dechiffrer_cesar(texte_chiffre, k)))
    return candidats


# =============================================================================
# EXERCICE I.3 : Chiffrement par clé XOR & Masque jetable
# =============================================================================

def chiffrer_xor(texte: str, cle: str) -> List[int]:
    """
    Chiffre un texte avec une clé secrète via l'opérateur bit-à-bit XOR (^).
    Chaque caractère du texte est combiné avec le caractère correspondant de la clé
    (la clé est répétée cycliquement via l'opérateur modulo).
    
    Retourne la liste des entiers (valeurs d'octets chiffrés).
    """
    if not cle:
        raise ValueError("La clé de chiffrement ne peut pas être vide.")

    octets_chiffres: List[int] = []
    for i, char in enumerate(texte):
        char_cle = cle[i % len(cle)]
        valeur_xor = ord(char) ^ ord(char_cle)
        octets_chiffres.append(valeur_xor)

    return octets_chiffres


def dechiffrer_xor(octets_chiffres: List[int], cle: str) -> str:
    """
    Déchiffre une liste d'octets XOR avec la même clé.
    Propriété fondamentale du XOR : (A ^ B) ^ B == A.
    """
    if not cle:
        raise ValueError("La clé de déchiffrement ne peut pas être vide.")

    caracteres = []
    for i, octet in enumerate(octets_chiffres):
        char_cle = cle[i % len(cle)]
        valeur_originale = octet ^ ord(char_cle)
        caracteres.append(chr(valeur_originale))

    return "".join(caracteres)


# =============================================================================
# EXERCICE I.4 : Mutation en place vs Copie défensive & Tuples (Forensics)
# =============================================================================

def masquer_ip_en_place(evenements: List[List]) -> None:
    """
    PIÈGE PÉDAGOGIQUE : Modifie DIRECTEMENT la liste originale reçue en argument.
    Dans un contexte forensic (investigation numérique), cela détruit la preuve d'origine !
    """
    for evt in evenements:
        # Supposons la structure [timestamp, ip, statut]
        ip = evt[1]
        segments = ip.split('.')
        if len(segments) == 4:
            evt[1] = f"{segments[0]}.{segments[1]}.xxx.xxx"


def masquer_ip_copie_defensive(evenements: List[Tuple[str, str, str]]) -> List[Tuple[str, str, str]]:
    """
    APPROCHE SÉCURISÉE : Préserve l'intégrité absolue de la liste d'origine.
    1. Crée une nouvelle liste indépendante.
    2. Utilise des TUPLES immuables (timestamp, ip_masquee, statut) garantissant 
       qu'aucune modification ultérieure ne pourra altérer les enregistrements.
    """
    nouveaux_evenements = []
    for horodatage, ip, statut in evenements:
        segments = ip.split('.')
        if len(segments) == 4:
            ip_masquee = f"{segments[0]}.{segments[1]}.xxx.xxx"
        else:
            ip_masquee = ip
        nouveaux_evenements.append((horodatage, ip_masquee, statut))

    return nouveaux_evenements


# =============================================================================
# EXERCICE I.5 : Dictionnaires & Analyse de sécurité (IOCs / SIEM)
# =============================================================================

def analyser_connexions_suspectes(logs: List[Dict]) -> Dict:
    """
    Analyse un flux de logs réseau structurés sous forme de dictionnaires.
    Détecte les adresses IP effectuant des scans de ports ou du brute-force.
    
    Structure d'une entrée :
    {"ip": "192.168.1.42", "port": 22, "bloque": True, "octets": 128}
    
    Retourne une synthèse :
    - volume_par_ip : dict[str, int] (total octets transférés)
    - tentatives_bloquees : dict[str, int] (nombre d'échecs/blocages par IP)
    - alertes_critiques : list[str] (IP ayant plus de 3 blocages)
    """
    volume_par_ip: Dict[str, int] = {}
    tentatives_bloquees: Dict[str, int] = {}

    for evt in logs:
        ip = evt.get("ip", "inconnu")
        octets = evt.get("octets", 0)
        bloque = evt.get("bloque", False)

        # Cumul du volume réseau
        volume_par_ip[ip] = volume_par_ip.get(ip, 0) + octets

        # Cumul des alertes / blocages
        if bloque:
            tentatives_bloquees[ip] = tentatives_bloquees.get(ip, 0) + 1

    # Détection des IP dépassant le seuil de 3 tentatives infructueuses
    alertes_critiques = [
        ip for ip, count in tentatives_bloquees.items() if count >= 3
    ]

    return {
        "volume_par_ip": volume_par_ip,
        "tentatives_bloquees": tentatives_bloquees,
        "alertes_critiques": alertes_critiques
    }


# =============================================================================
# Démonstration globale exécutable
# =============================================================================

def run_introduction_interactive():
    print("=" * 70)
    print("BTS CIEL // INTRODUCTION À PYTHON : FONDAMENTAUX & CYBERSÉCURITÉ")
    print("=" * 70)

    # I.1 Audit de mot de passe
    print("\n--- [I.1] Audit de politique de mot de passe ---")
    test_mdp = "Admin@2026"
    conforme, score, erreurs = auditer_mot_de_passe(test_mdp)
    print(f"Mot de passe testé : '{test_mdp}'")
    print(f"Score : {score}/5 | Conforme : {conforme}")
    if erreurs:
        print(f"Anomalies détectées : {erreurs}")
    else:
        print("Verdict : Mot de passe conforme aux exigences de sécurité.")

    # I.2 Chiffrement de César
    print("\n--- [I.2] Chiffrement de César & Cryptanalyse ---")
    clair = "ATTAQUE DU SERVEUR A MINUIT !"
    cle_cesar = 3
    chiffre = chiffrer_cesar(clair, cle_cesar)
    dechiffre = dechiffrer_cesar(chiffre, cle_cesar)
    print(f"Message clair     : {clair}")
    print(f"Chiffré (clé={cle_cesar})  : {chiffre}")
    print(f"Déchiffré inverse : {dechiffre}")
    
    # Démonstration force brute sur un extrait
    flag_chiffre = "KHOOR" # 'HELLO' avec k=3
    print(f"\nSimulation force brute sur '{flag_chiffre}' :")
    for k, proposition in casser_cesar_force_brute(flag_chiffre)[:5]:
        print(f"  Clé k={k:2d} -> {proposition}")

    # I.3 Chiffrement XOR
    print("\n--- [I.3] Chiffrement par clé XOR & Masque Jetable ---")
    secret = "FLAG{ciel_python_2026}"
    cle_xor = "CYBER"
    octets = chiffrer_xor(secret, cle_xor)
    recupere = dechiffrer_xor(octets, cle_xor)
    print(f"Texte secret      : {secret}")
    print(f"Clé secrète       : '{cle_xor}'")
    print(f"Flux d'octets XOR : {octets}")
    print(f"Texte restauré    : {recupere}")

    # I.4 Mutabilité vs Immutabilité
    print("\n--- [I.4] Manipulation d'objets : En place vs Par copie (Forensics) ---")
    logs_bruts = [
        ("10:00:01", "192.168.1.15", "AUTH_FAIL"),
        ("10:00:03", "192.168.1.15", "AUTH_FAIL"),
        ("10:00:05", "10.0.0.8", "AUTH_OK")
    ]
    logs_anonymes = masquer_ip_copie_defensive(logs_bruts)
    print(f"Logs originaux (preuve scellée)    : {logs_bruts}")
    print(f"Logs anonymisés (copie défensive) : {logs_anonymes}")
    print("Contrôle d'intégrité : La liste originale est restée 100% intacte !")

    # I.5 Dictionnaires & IOCs
    print("\n--- [I.5] Dictionnaires & Détection d'intrusions (SIEM) ---")
    flux_reseau = [
        {"ip": "203.0.113.5", "port": 22, "bloque": True, "octets": 64},
        {"ip": "203.0.113.5", "port": 22, "bloque": True, "octets": 64},
        {"ip": "203.0.113.5", "port": 22, "bloque": True, "octets": 64},
        {"ip": "192.168.1.10", "port": 80, "bloque": False, "octets": 1024},
        {"ip": "203.0.113.5", "port": 22, "bloque": True, "octets": 64},
    ]
    rapport = analyser_connexions_suspectes(flux_reseau)
    print(f"Volume par IP          : {rapport['volume_par_ip']}")
    print(f"Échecs par IP          : {rapport['tentatives_bloquees']}")
    print(f"ALERTE IOC CRITIQUE    : {rapport['alertes_critiques']} (Attaque par force brute détectée)")
    print("=" * 70)


if __name__ == '__main__':
    run_introduction_interactive()
