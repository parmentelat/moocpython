Bonjour,

Une idée de "jeu" (c'est le cas de le dire) qui m'avait amusé: coder un puissance 4! Pas d'interface graphique (pour l'instant), uniquement en ligne de commande, avec une sortie dans le terminal. Quelques contraintes que je m'étais fixées:

 - à chaque tour, le programme demande qq chose du genre "Joueur 1/2, à toi de jouer" et attend la réponse du joueur. Cette réponse correspond à la colonne dans laquelle il fait tomber son jeton.

 - le programme affiche après chaque tour la grille de jeu sous la forme:

![puissance 4][1]

 - 'X' correspond au jeton du joueur 1, '@' à celui du joueur 2 (valeurs
   par défaut, mais qui peuvent être définies par l'utilisateur). La
   première ligne (1 2 3 ...) sert à repérer plus facilement les
   colonnes avant de jouer, et pour plus de lisibilité on insère des
   espaces entre les colonnes.

 - la taille de la grille est 6 lignes x 7 colonnes par défaut, mais on peut modifier ce paramètre pour jouer sur des grilles plus grandes.

 - Après chaque coup, le programme vérifie s'il y a puissance 4 et arrête la partie si c'est le cas, en adressant ses plus sincères félicitations au gagnant!

Moi ça m'avait amusé! (après les goûts et les couleurs...) J'avais fait une première version en utilisant uniquement des fonctions, puis une version plus satisfaisante je pense avec des classes (même si parfois, ça doit rester un peu maladroit dans l'écriture du code). Et puis, après puissance 4, un mastermind?

ArgonCooper

  [1]: map.png

