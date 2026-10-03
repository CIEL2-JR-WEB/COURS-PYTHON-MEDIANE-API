// BTS CIEL - Client JavaScript (fetch) - CORRIGÉ

// Exercice 4.2 : Appel à /api/tri
document.getElementById('btn-tri').addEventListener('click', async () => {
    const rawInput = document.getElementById('input-tri').value;
    const outputElem = document.getElementById('output-tri');

    try {
        const response = await fetch(`/api/tri?t=${encodeURIComponent(rawInput)}`);
        const data = await response.json();
        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputElem.textContent = "Erreur lors de l'appel API : " + err.message;
    }
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
// Cahier des charges vidéo : https://www.youtubeeducation.com/watch?v=aGkpJFJ9t4k
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
