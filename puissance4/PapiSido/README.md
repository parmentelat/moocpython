A mon tour, je vais me lancer sur le sujet.
Mon cahier des charges: initialiser le plateaus de jeu ( Largeur, hauteur ) Le jeu s'arrête lorsque le tableau est plein
* Objectif 1: L'ordinateur arbitre entre deux joueurs
* Objectif 2: le même, mais l'ordinateur décrète la partie nulle lorsqu'aucun  des deux joueurs ne peut plus gagner
* Objectif 3: L'ordinateur joue

Question: ce jeu n'est pas très compliqué et, sans aller chercher Deep Blue, nos ordinateurs doivent pouvoir en faire une analyse complète. Quelqu'un connait-il le résultat?

**version 0.0** : pquatre.0.py : Mise en place de la Mécanique du jeu, sans analyse : les deux joueurs rentrent leur coup à tour de rôle juqu'à ce que le tableau soit rempli ou que l'un des deux joueurs abandonne. La partie est stockée sous forme d'une chaîne contenant les colonnes choisies par chaque joueur ( joueur 1 pour rang pair, 2 pour rang impair) donc facile à rejouer et analyser a posteriori

**version 0.2** : pquatre.2.py : Toujours sans analyse, mais dans une version objet et surtout avec la possibilité d'opposer des joueurs humains ou robots. Je peux maintenant passer aux choses sérieuses: l'analyse d'une partie pour désigner le vainqueur bien sur mais aussi préparer des stratégies pour mes robots (Pour l'instant le seul programmé joue au hasard)
 
