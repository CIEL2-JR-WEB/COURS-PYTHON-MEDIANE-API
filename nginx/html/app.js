// BTS CIEL - Client JavaScript (fetch)
// Complétez les fonctions ci-dessous pour communiquer avec l'API Flask

// Exercice 4.2 : Appel à /api/tri
document.getElementById('btn-tri').addEventListener('click', async () => {
    const rawInput = document.getElementById('input-tri').value;
    const outputElem = document.getElementById('output-tri');

    // TODO:
    // 1. Nettoyer la chaîne de caractères si nécessaire
    // 2. Émettre une requête GET vers /api/tri?t=... avec fetch()
    // 3. Récupérer le JSON et l'afficher dans outputElem
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/tri";
});

// Exercice 4.3 : Générateur de salaires aléatoires
document.getElementById('btn-random').addEventListener('click', async () => {
    // TODO:
    // 1. Générer une liste de 9 entiers aléatoires entre 1200 et 5000 (représentant des salaires en €)
    // 2. Afficher la liste brute dans l'élément span-brut
    // 3. Envoyer cette série à l'API Flask via /api/tri?t=...
    // 4. Mettre à jour span-trie et span-mediane avec la réponse JSON de Flask
    document.getElementById('span-brut').textContent = "TODO";
    document.getElementById('span-trie').textContent = "TODO";
    document.getElementById('span-mediane').textContent = "TODO";
});

// Exercice 5 : Concaténation et fusion de listes
document.getElementById('btn-fusion').addEventListener('click', async () => {
    const t1 = document.getElementById('input-t1').value;
    const t2 = document.getElementById('input-t2').value;
    const outputElem = document.getElementById('output-fusion');

    // TODO:
    // 1. Émettre un fetch GET vers /api/fusion?t1=...&t2=...
    // 2. Afficher le résultat JSON formatté dans outputElem
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/fusion";
});

// Exercice 6 : Statistiques BDD et comparaison employé
document.getElementById('btn-db-stats').addEventListener('click', async () => {
    const outputElem = document.getElementById('output-db-stats');
    // TODO: Émettre un fetch vers /api/salaires/stats et afficher le JSON
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/salaires/stats";
});

document.getElementById('btn-db-emp').addEventListener('click', async () => {
    const empId = document.getElementById('input-emp-id').value;
    const outputElem = document.getElementById('output-db-emp');
    // TODO: Émettre un fetch vers `/api/employees/${empId}/comparaison` et afficher le JSON
    outputElem.textContent = `TODO: Implémenter l'appel fetch vers /api/employees/${empId}/comparaison`;
});
