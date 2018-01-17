Je proposerais volontiers pour occuper nos vacances (Certes nous avons déjà de quoi nous occuper avec Vigenere par exemple mais il faut ausii préparer l'avenir) d’examiner pythoniquement **The Jewels of Heuro**

http://www.open.edu/openlearn/science-maths-technology/computing-and-ict/computing/the-jewels-heuro

J'imagine qu'il s'agit là d'un problème classique en théorie des graphes, mais la plupart d'entre nous n'étant pas spécialiste ce paut -être un intéressant sujet de réflexion 

Objectif donc trouver le meilleur chemin pour visiter N joyaux en supposant connues les N*(N-1) distances entre chacun d'entre eux, mais avant d'aborder cette recherche il nous faut déja définir comment coder ces distances. Au départ c'est un tableau NxN  symètrique, mais redondant (nous pourrons les supposer entiers quitte à arrondir si nécessaire)
On peut envisager deux possibilités
a/ On connait les coodonnées des points, le calcul des distances est alors facile, mais dans un donjon on progresse rarement en ligne droite !!! donc
b/ on connait directement ces distances. pour les puristes on pourrait même vérifier l'axiome d (A,C) <= d(A,B) + d(B,C) et d'autre part pourquoi supposer d(A,B) = d(B,A) ? dans un donjon, ça monte et ça descend !!! 

Première version implantée le 17/01/2018

Je suggére, si vous voullez vous lancer que nous nous alignons sur ma structure de fichier de données 
très basique, premiére ligne la taile n ( donc n-1 bijoux on part ey on revient à 0 )
ensuite n lignes pour le tableau des distance 


