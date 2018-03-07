Je propose d'élargir le sous-projet pour traiter aussi d'autres jeux de tableau où il faut aligner des pions 

Je pense plus spécifiquement au tictactoe- un peu simplet me direz-vous . Certes, mais

* C'est un jeu facilement analysable et j'ai envie de développer une stratégie pour l'analyse complète d'un jeu, 
voire sur l'apprentissage heuristique (je n'utilise sans doute pas le bon terme, mais c'est je crois la mode )
* Il ya des extensions intéressantes, cf la page wikipedia 
et notamment https://fr.wikipedia.org/wiki/Tic-tac-toe_quantique. 
Je pense aussi à une version périodique. et pourquoi pas du 3-D voire du 4-D ( !!!! )
* ce doit être relativement simple pour démarrer tkinter, gui et graphique

Travail en cours, j'ai pour l'insatnt un tictactoe en état de marche en mode console et mes premiers balbutiements pour un interfaçage graphique: ttt_GUI lance le jeu ( humain ou ordinateur vs humain ou ordinateur) qui ensuie s'éxécute en mode console,
je les ai déposés dans  mon sous-répertoire pour archivage, mais version non documenté et ne perdez pas de temps à aller les voir.
Par contre j'apprécierai vos avis sur ce qui m'arrête en ce moment
* tictactoe.py gère la logique du jeu ( y compris la stratégie de l'ordinateur, mais cela reste à faire, pour l'instant et comme puissance4 il joue au hasard, lol )
* ttt_GUI est l'interface graphique qui pour l'instant se limite au choix de qui joue, et qui passe la main à tictacttoe pour le jeu lui-même

et je tiens à cette logique de séparer le jeu lui-même de son interfaçage, mais comment faire remonter l'info du jeu vers le graphique?

La voie que j'explore est de passer par un objet TTTGUI héritant de tictactoe, mais je pars un peu à l'aveugle.

