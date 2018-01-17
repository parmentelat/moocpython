Mon cahier des charges: initialiser le plateaus de jeu ( Largeur, hauteur ) Le jeu s'arrête lorsque le tableau est plein
* Objectif 1: L'ordinateur arbitre entre deux joueurs
* Objectif 2: le même, mais l'ordinateur décrète la partie nulle lorsqu'aucun  des deux joueurs ne peut plus gagner
* Objectif 3: L'ordinateur joue

Question: ce jeu n'est pas très compliqué et, sans aller chercher Deep Blue, nos ordinateurs doivent pouvoir en faire une analyse complète. Quelqu'un connait-il le résultat?

**version 1** : pquatre.v1.py (11/01/2018) : Ma proposition: le programme arbitre une partie entre 2 joueurs (humain ou robot) et annonce une partie nulle.
Mon programme est plus lourd que les votres: c'est la classe Analyse_p4 qui analyse la partie pour décider du vainqueur, mais cela résulte d'une analyse plus complète qui sera mon point de départ pour construire des stratégies pour mes robots.
 
