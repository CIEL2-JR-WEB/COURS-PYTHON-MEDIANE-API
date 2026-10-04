// BTS CIEL - Client JavaScript (fetch)
// Complétez les fonctions ci-dessous pour communiquer avec l'API Flask

// Exercice 4.2 : Saisie dynamique d'entiers (push tant que valeur > 0) puis appel à /api/tri
let tableauSaisieEx4 = [];

// Option 1 : Saisie via champ de texte et bouton 'Ajouter (push)'
document.getElementById('btn-push-tri').addEventListener('click', async () => {
    const input = document.getElementById('input-valeur-tri');
    const outputElem = document.getElementById('output-tri');
    const val = parseInt(input.value.trim(), 10);

    // TODO:
    // 1. Si val > 0 :
    //    - Ajouter au tableau : tableauSaisieEx4.push(val)
    //    - Mettre à jour l'élément HTML : document.getElementById('span-saisie-cours').textContent = `[${tableauSaisieEx4.join(', ')}]`
    //    - Vider le champ de saisie : input.value = ''
    // 2. Si val <= 0 (et tableauSaisieEx4 n'est pas vide) :
    //    - C'est la condition d'arrêt : émettre une requête GET vers /api/tri?t=... avec fetch()
    //      (Astuce Étape 2 : Vous pouvez d'abord tester avec l'URL de votre serveur Mock Postman)
    //    - Récupérer les données retournées en JSON (original, tri, mediane) : const data = await response.json()
    //    - Mettre à jour les balises <span> du DOM dans index.html :
    //        document.getElementById('span-tri-original').textContent = data.original.join(', ')
    //        document.getElementById('span-tri-trie').textContent = data.tri.join(', ')
    //        document.getElementById('span-tri-mediane').textContent = data.mediane
    //        outputElem.textContent = JSON.stringify(data, null, 2)
    //    - Réinitialiser tableauSaisieEx4 = [] pour une nouvelle session
    outputElem.textContent = "TODO: Implémenter la logique push tant que > 0 et l'appel fetch vers /api/tri";
});

// Option 2 : Saisie via boucle prompt() (conforme à la vidéo de démonstration)
document.getElementById('btn-prompt-tri').addEventListener('click', async () => {
    const outputElem = document.getElementById('output-tri');

    // TODO:
    // 1. Réinitialiser un tableau local : const tableauLocal = []
    // 2. Utiliser une boucle (while) demandant à l'utilisateur : prompt("saisissez un nombre > 0")
    // 3. Tant que la valeur saisie est > 0, ajouter la valeur au tableau (push)
    // 4. Dès qu'une valeur <= 0 (ou annulation) est rencontrée, arrêter la boucle
    // 5. Envoyer le tableau à l'API Flask (/api/tri?t=...) avec fetch()
    // 6. Afficher les résultats dans le DOM (span-tri-original, span-tri-trie, span-tri-mediane)
    outputElem.textContent = "TODO: Implémenter la boucle prompt() et l'appel fetch vers /api/tri";
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

// Exercice 4.3 : Générateur de salaires aléatoires
document.getElementById('btn-random').addEventListener('click', async () => {
    // TODO:
    // 1. Générer une liste de 9 entiers aléatoires entre 1200 et 5000 (représentant des salaires en €)
    // 2. Afficher la liste brute dans la balise <span id="span-brut"> :
    //    document.getElementById('span-brut').textContent = ...
    // 3. Envoyer cette série à l'API Flask via fetch(`/api/tri?t=${...}`)
    // 4. Mettre à jour les balises <span id="span-trie"> et <span id="span-mediane"> avec la réponse JSON de Flask
    document.getElementById('span-brut').textContent = "TODO";
    document.getElementById('span-trie').textContent = "TODO";
    document.getElementById('span-mediane').textContent = "TODO";
});

// Exercice 5 : Concaténation, tri et affichage dynamique dans le DOM
// Cahier des charges vidéo : https://www.youtube.com/watch?v=aGkpJFJ9t4k
document.getElementById('btn-fusion').addEventListener('click', async () => {
    const t1 = document.getElementById('input-t1').value;
    const t2 = document.getElementById('input-t2').value;
    const outputElem = document.getElementById('output-fusion');

    // TODO: Exercice 5 (Conforme à la vidéo)
    // 1. Récupérer la saisie des deux champs <input id="input-t1"> et <input id="input-t2">
    // 2. Émettre une requête GET vers /api/fusion?t1=...&t2=... avec fetch()
    //    (Astuce Étape 2 : Vous pouvez d'abord tester avec l'URL de votre Mock Postman)
    // 3. Récupérer les données retournées en JSON : const data = await response.json()
    // 4. Mettre à jour les balises <span> du DOM dans index.html :
    //    - document.getElementById('span-t1').textContent = ... (Tableau 1 saisi)
    //    - document.getElementById('span-t2').textContent = ... (Tableau 2 saisi)
    //    - document.getElementById('span-fusion').textContent = data.fusion.join(', ') (Tableau brut concaténé)
    //    - document.getElementById('span-fusion-tri').textContent = data.tri.join(', ') (Tableau concaténé trié)
    //    - document.getElementById('span-fusion-mediane').textContent = data.mediane (Médiane globale)
    // 5. Afficher la réponse brute dans la balise <pre id="output-fusion"> :
    //    outputElem.textContent = JSON.stringify(data, null, 2)
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/fusion et l'affichage dans le DOM";
});

// Exercice 6 : Statistiques BDD et comparaison employé
document.getElementById('btn-db-stats').addEventListener('click', async () => {
    const outputElem = document.getElementById('output-db-stats');
    // TODO: Émettre un fetch vers /api/salaires/stats et afficher le JSON formaté dans outputElem
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/salaires/stats";
});

document.getElementById('btn-db-emp').addEventListener('click', async () => {
    const empId = document.getElementById('input-emp-id').value;
    const outputElem = document.getElementById('output-db-emp');
    // TODO: Émettre un fetch vers `/api/employees/${empId}/comparaison` et afficher le JSON formaté dans outputElem
    outputElem.textContent = `TODO: Implémenter l'appel fetch vers /api/employees/${empId}/comparaison`;
});

// Exercice 7 : Jointures SQL & Médiane sur une période (/api/salaires/periode)
document.getElementById('btn-periode').addEventListener('click', async () => {
    const pVal = document.getElementById('input-periode-p').value.trim();
    const d1Val = document.getElementById('input-periode-d1').value.trim();
    const d2Val = document.getElementById('input-periode-d2').value.trim();
    const outputElem = document.getElementById('output-periode');

    // TODO: Exercice 7
    // 1. Construire les paramètres de requête avec URLSearchParams :
    //    const params = new URLSearchParams();
    //    if (pVal !== '') params.append('p', pVal);
    //    if (d1Val !== '') params.append('d1', d1Val);
    //    if (d2Val !== '') params.append('d2', d2Val);
    //
    // 2. Émettre une requête GET vers `/api/salaires/periode?${params.toString()}` avec fetch()
    //    (Astuce Étape 1 : Vous pouvez tester d'abord avec l'URL de votre serveur Mock Postman)
    //
    // 3. Récupérer les données retournées en JSON (const data = await response.json())
    //
    // 4. Mettre à jour les balises du DOM dans index.html :
    //    - document.getElementById('span-periode-cas').textContent = data.cas
    //    - document.getElementById('span-periode-employe').textContent = data.employe_nom ? `${data.employe_nom} (id: ${data.employe_id})` : 'Tous les employés'
    //    - document.getElementById('span-periode-dates').textContent = data.d1 && data.d2 ? `Du ${data.d1} au ${data.d2}` : (data.date_debut ? `À partir du ${data.date_debut}` : 'Toutes dates')
    //    - document.getElementById('span-periode-moyennes').textContent = data.moyennes_individuelles ? data.moyennes_individuelles.map(m => `${m} €`).join(', ') : '-'
    //    - document.getElementById('span-periode-resultat').textContent = (data.salaire_moyen !== undefined ? `${data.salaire_moyen} € (Moyenne)` : `${data.mediane_des_moyennes} € (Médiane)`)
    //    - outputElem.textContent = JSON.stringify(data, null, 2)
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/salaires/periode et la mise à jour du DOM";
});

document.getElementById('btn-periode-reset').addEventListener('click', () => {
    document.getElementById('input-periode-p').value = '';
    document.getElementById('input-periode-d1').value = '';
    document.getElementById('input-periode-d2').value = '';
    document.getElementById('span-periode-cas').textContent = '-';
    document.getElementById('span-periode-employe').textContent = '-';
    document.getElementById('span-periode-dates').textContent = '-';
    document.getElementById('span-periode-moyennes').textContent = '-';
    document.getElementById('span-periode-resultat').textContent = '-';
    document.getElementById('output-periode').textContent = "En attente d'interrogation...";
});

