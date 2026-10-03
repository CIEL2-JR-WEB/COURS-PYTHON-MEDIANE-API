// BTS CIEL - Client JavaScript (fetch) - CORRIGÉ

// Exercice 4.2 : Saisie dynamique d'entiers (push tant que valeur > 0) puis appel à /api/tri
let tableauSaisieEx4 = [];

// Fonction utilitaire pour envoyer le tableau au service web (Mock Postman ou API Flask locale)
async function envoyerEtTraiterTableau(tableau) {
    const outputElem = document.getElementById('output-tri');
    if (!tableau || tableau.length === 0) {
        outputElem.textContent = "Aucune valeur saisie à envoyer.";
        return;
    }

    try {
        // Remarque : Pour l'Étape 2, cette URL peut pointer vers votre serveur Mock Postman
        // Exemple : const url = `https://<mock-id>.mock.pstmn.io/api/tri?t=${encodeURIComponent(tableau.join(','))}`;
        const url = `/api/tri?t=${encodeURIComponent(tableau.join(','))}`;
        const response = await fetch(url);
        const data = await response.json();

        if (!response.ok) {
            outputElem.textContent = "Erreur : " + (data.erreur || "Erreur de traitement");
            return;
        }

        // Mise à jour de l'IHM dans le DOM
        document.getElementById('span-tri-original').textContent = data.original.join(', ');
        document.getElementById('span-tri-trie').textContent = data.tri.join(', ');
        document.getElementById('span-tri-mediane').textContent = data.mediane;
        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputElem.textContent = "Erreur lors de l'appel API : " + err.message;
    }
}

// Option 1 : Saisie via champ de texte et bouton 'Ajouter (push)'
document.getElementById('btn-push-tri').addEventListener('click', async () => {
    const input = document.getElementById('input-valeur-tri');
    const rawVal = input.value.trim();
    if (rawVal === '') return;

    const val = parseInt(rawVal, 10);
    input.value = '';
    input.focus();

    if (val > 0) {
        // Remplissage du tableau tant que valeur > 0
        tableauSaisieEx4.push(val);
        document.getElementById('span-saisie-cours').textContent = `[${tableauSaisieEx4.join(', ')}]`;
    } else {
        // Valeur <= 0 : condition d'arrêt et traitement par le service web
        if (tableauSaisieEx4.length > 0) {
            await envoyerEtTraiterTableau(tableauSaisieEx4);
            tableauSaisieEx4 = [];
            document.getElementById('span-saisie-cours').textContent = '[] (traité)';
        } else {
            document.getElementById('output-tri').textContent = "Veuillez saisir au moins une valeur > 0 avant de terminer.";
        }
    }
});

// Validation par la touche 'Entrée' dans le champ de saisie
document.getElementById('input-valeur-tri').addEventListener('keyup', (e) => {
    if (e.key === 'Enter') {
        document.getElementById('btn-push-tri').click();
    }
});

// Option 2 : Saisie via boucle prompt() (conforme à la vidéo de démonstration)
document.getElementById('btn-prompt-tri').addEventListener('click', async () => {
    const tableauLocal = [];
    while (true) {
        const reponse = prompt("saisissez un nombre > 0");
        if (reponse === null) break; // Clic sur Annuler

        const nombre = parseInt(reponse.trim(), 10);
        if (isNaN(nombre) || nombre <= 0) {
            // Arrêt de la boucle quand valeur <= 0
            break;
        }

        tableauLocal.push(nombre);
        document.getElementById('span-saisie-cours').textContent = `[${tableauLocal.join(', ')}]`;
    }

    if (tableauLocal.length > 0) {
        await envoyerEtTraiterTableau(tableauLocal);
    }
});

// Réinitialisation
document.getElementById('btn-reset-tri').addEventListener('click', () => {
    tableauSaisieEx4 = [];
    document.getElementById('input-valeur-tri').value = '';
    document.getElementById('span-saisie-cours').textContent = '[]';
    document.getElementById('span-tri-original').textContent = '-';
    document.getElementById('span-tri-trie').textContent = '-';
    document.getElementById('span-tri-mediane').textContent = '-';
    document.getElementById('output-tri').textContent = 'En attente de saisie...';
});

// Exercice 4.3 : Salaires aléatoires générés en JS
document.getElementById('btn-random').addEventListener('click', async () => {
    // 1. Générer 9 salaires aléatoires entre 1200 et 5000 €
    const salaires = [];
    for (let i = 0; i < 9; i++) {
        const randomSalary = Math.floor(Math.random() * (5000 - 1200 + 1)) + 1200;
        salaires.push(randomSalary);
    }

    // Affichage des salaires bruts côté JS
    document.getElementById('span-brut').textContent = salaires.join(', ') + ' €';

    try {
        // Envoi à l'API Flask
        const response = await fetch(`/api/tri?t=${salaires.join(',')}`);
        const data = await response.json();

        // Mise à jour de l'interface
        document.getElementById('span-trie').textContent = data.tri.join(', ') + ' €';
        document.getElementById('span-mediane').textContent = data.mediane + ' €';
    } catch (err) {
        alert("Erreur lors de la communication avec Flask : " + err.message);
    }
});

// Exercice 5 : Fusion de tableaux, tri et affichage dynamique dans le DOM
// Cahier des charges vidéo : https://www.youtube.com/watch?v=aGkpJFJ9t4k
document.getElementById('btn-fusion').addEventListener('click', async () => {
    const t1 = document.getElementById('input-t1').value;
    const t2 = document.getElementById('input-t2').value;
    const outputElem = document.getElementById('output-fusion');

    try {
        const url = `/api/fusion?t1=${encodeURIComponent(t1)}&t2=${encodeURIComponent(t2)}`;
        const response = await fetch(url);
        const data = await response.json();

        if (!response.ok) {
            outputElem.textContent = "Erreur : " + (data.erreur || "Erreur lors du traitement");
            return;
        }

        // Affichage dynamique dans le DOM (Cahier des charges vidéo)
        document.getElementById('span-t1').textContent = data.t1 ? data.t1.join(', ') : t1;
        document.getElementById('span-t2').textContent = data.t2 ? data.t2.join(', ') : t2;
        document.getElementById('span-fusion').textContent = data.fusion.join(', ');
        document.getElementById('span-fusion-tri').textContent = data.tri.join(', ');
        document.getElementById('span-fusion-mediane').textContent = data.mediane;

        // Affichage de la réponse JSON brute
        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputElem.textContent = "Erreur réseau : " + err.message;
    }
});

// Exercice 6 : Statistiques BDD
document.getElementById('btn-db-stats').addEventListener('click', async () => {
    const outputElem = document.getElementById('output-db-stats');
    try {
        const response = await fetch('/api/salaires/stats');
        const data = await response.json();
        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputElem.textContent = "Erreur BDD stats : " + err.message;
    }
});

// Exercice 6 : Comparaison employé
document.getElementById('btn-db-emp').addEventListener('click', async () => {
    const empId = document.getElementById('input-emp-id').value;
    const outputElem = document.getElementById('output-db-emp');

    if (!empId) {
        outputElem.textContent = "Veuillez saisir un identifiant d'employé valide.";
        return;
    }

    try {
        const response = await fetch(`/api/employees/${empId}/comparaison`);
        const data = await response.json();
        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputElem.textContent = "Erreur BDD comparaison : " + err.message;
    }
});
