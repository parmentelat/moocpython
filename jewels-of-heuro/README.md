Je proposerais volontiers pour occuper nos vacances (Certes nous avons déjà de quoi nous occuper avec Vigenere par exemple mais il faut ausii préparer l'avenir) d’examiner pythoniquement **The Jewels of Heuro**

http://www.open.edu/openlearn/science-maths-technology/computing-and-ict/computing/the-jewels-heuro
C'est en fait le probléme du voyageur de commerce
https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce


Objectif donc trouver le meilleur chemin pour visiter N joyaux en supposant connues les N*(N-1) distances entre chacun d'entre eux, mais avant d'aborder cette recherche il nous faut déja définir comment coder ces distances. Au départ c'est un tableau NxN  symètrique, mais redondant (nous pourrons les supposer entiers quitte à arrondir si nécessaire)
On peut envisager deux possibilités
a/ On connait les coodonnées des points, le calcul des distances est alors facile, mais dans un donjon on progresse rarement en ligne droite !!! donc
b/ on connait directement ces distances. pour les puristes on pourrait même vérifier l'axiome d (A,C) <= d(A,B) + d(B,C) et d'autre part pourquoi supposer d(A,B) = d(B,A) ? dans un donjon, ça monte et ça descend !!! 

Seconde version implantée le 19/01/2018
quelques améliorations de détail et implantation de la méthode closest (plus proche voisin)

Je suggére, si vous voullez vous lancer que nous nous alignons sur ma structure de fichier de données 
très basique, premiére ligne la taile n ( donc n-1 bijoux on part ey on revient à 0 )
ensuite n lignes pour le tableau des distance 

J'ai mis dans le répertoire principal quelques fichiers de données
* d4a.dat pour vous régler
* jd7a.at un exemples de dimension 7, pour lequel la méthode "closest" donne le résultat optimal
* jh9.dat le fichier correspondant au cas de jewels of heuro, soluble par force brute sans douleur

Donc il faut aller au delà pour jouer vraiment, je vous propose http://www.math.uwaterloo.ca/tsp/road/austria.html d'aller randonner en Autriche le fichier des distances est austria101.txt mais n'est pas dans le bon format. A vous de le transformer et pour régler votre code je vous en ai extrait une version de dimension 6. A noter qu'il s'agit du probléme asymètrique( Et si vous avez la flemme, le fichier austria.dat est aussi dans mon répertoire

PapiSido ( aka FSidoroff pour FUN)




