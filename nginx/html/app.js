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
    //    - Mettre à jour l'élément span-saisie-cours avec le contenu du tableau
    //    - Vider le champ de saisie
    // 2. Si val <= 0 (et tableauSaisieEx4 n'est pas vide) :
    //    - C'est la condition d'arrêt : émettre une requête GET vers /api/tri?t=... avec fetch()
    //      (Astuce Étape 2 : Vous pouvez d'abord tester avec l'URL de votre serveur Mock Postman)
    //    - Récupérer les données retournées en JSON (original, tri, mediane)
    //    - Mettre à jour span-tri-original, span-tri-trie, span-tri-mediane et outputElem
    //    - Réinitialiser tableauSaisieEx4 pour une nouvelle session
    outputElem.textContent = "TODO: Implémenter la logique push tant que > 0 et l'appel fetch vers /api/tri";
});

// Option 2 : Saisie via boucle prompt() (conforme à la vidéo de démonstration)
document.getElementById('btn-prompt-tri').addEventListener('click', async () => {
    const outputElem = document.getElementById('output-tri');

    // TODO:
    // 1. Réinitialiser un tableau local
    // 2. Utiliser une boucle (while) demandant à l'utilisateur : prompt("saisissez un nombre > 0")
    // 3. Tant que la valeur saisie est > 0, ajouter la valeur au tableau (push)
    // 4. Dès qu'une valeur <= 0 (ou annulation) est rencontrée, arrêter la boucle
    // 5. Envoyer le tableau à l'API Flask (/api/tri?t=...) avec fetch()
    // 6. Afficher les résultats dans le DOM
    outputElem.textContent = "TODO: Implémenter la boucle prompt() et l'appel fetch vers /api/tri";
});

// Réinitialisation
document.getElementById('btn-reset-tri').addEventListener('click', () => {
    tableauSaisieEx4 = [];
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
    // 2. Afficher la liste brute dans l'élément span-brut
    // 3. Envoyer cette série à l'API Flask via /api/tri?t=...
    // 4. Mettre à jour span-trie et span-mediane avec la réponse JSON de Flask
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
    // 1. Récupérer et nettoyer la saisie des deux tableaux t1 et t2
    // 2. Émettre une requête GET vers /api/fusion?t1=...&t2=... avec fetch()
    // 3. Récupérer les données retournées en JSON par Flask
    // 4. Mettre à jour les éléments du DOM :
    //    - span-t1, span-t2
    //    - span-fusion (tableau fusionné brut)
    //    - span-fusion-tri (tableau fusionné et trié)
    //    - span-fusion-mediane (médiane calculée)
    // 5. Afficher la réponse brute dans outputElem
    outputElem.textContent = "TODO: Implémenter l'appel fetch vers /api/fusion et l'affichage dans le DOM";
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
