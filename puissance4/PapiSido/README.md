A mon tour, je vais me lancer sur le sujet.
Mon cahier des charges: initialiser le plateaus de jeu ( Largeur, hauteur ) Le jeu s'arrête lorsque le tableau est plein
* Objectif 1: L'ordinateur arbitre entre deux joueurs
* Objectif 2: le même, mais l'ordinateur décrète la partie nulle lorsqu'aucun  des deux joueurs ne peut plus gagner
* Objectif 3: L'ordinateur joue

Question: ce jeu n'est pas très compliqué et, sans aller chercher Deep Blue, nos ordinateurs doivent pouvoir en faire une analyse complète. Quelqu'un connait-il le résultat?

**version 0** : pquatre.0.py : Mise en place de la Mécanique du jeu, sans analyse : les deux joueurs rentrent leur coup à tour de rôle juqu'à ce que le tableau soit rempli ou que l'un des deux joueurs abandonne. La partie est stockée sous forme d'une chaîne contenant les colonnes choisies par chaque joueur ( joueur 1 pour rang pair, 2 pour rang impair) donc facile à rejouer et analyser a posteriori

Je m'interroge sur ce que sera ma seconde étape
* Analyser la position pour reconnaître une ligne et donc le vainqueur
* Créer un objet Partie
* Créer un Robot opposant pour jouer contre la machine
Mais auparavant je vais aller voir vos propositions sur la mise ne place du jeu. L'idéal serait que nos programmes s'accordent sur un minimum de choses pour pouvoir communiquer 
 
