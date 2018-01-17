Je proposerais volontiers pour occuper nos vacances (Certes nous avons déjà de quoi nous occuper avec Vigenere par exemple mais il faut ausii préparer l'avenir) d’examiner pythoniquement **The Jewels of Heuro**

http://www.open.edu/openlearn/science-maths-technology/computing-and-ict/computing/the-jewels-heuro

J'imagine qu'il s'agit là d'un problème classique en théorie des graphes, mais la plupart d'entre nous n'étant pas spécialiste ce paut -être un intéressant sujet de réflexion 

Objectif donc trouver le meilleur chemin pour visiter N joyaux en supposant connues les N*(N-1) distances entre chacun d'entre eux, mais avant d'aborder cette recherche il nous faut déja définir comment coder ces distances. Au départ c'est un tableau NxN  symètrique, mais redondant (nous pourrons les supposer entiers quitte à arrondir si nécessaire)
On peut envisager deux possibilités
a/ On connait les coodonnées des points, le calcul des distances est alors facile, mais dans un donjon on progresse rarement en ligne droite !!! donc
b/ on connait directement ces distances. pour les puristes on pourrait même vérifier l'axiome d (A,C) <= d(A,B) + d(B,C) et d'autre part pourquoi supposer d(A,B) = d(B,A) ? dans un donjon, ça monte et ça descend !!! 


Probléme préliminaire dans les exemples proposés dans le lien, on ne nous donne pas directemnt ces distances ( Ou peut-être je n'ai pas su trouver où elles étaient donnés, si quelqu'un est plus malin que moi !!!!)
Par exemple dans le cas N=4, on nous donne seulement le résultat des 6 chemins possibles. Alors question preliminaire au préliminaire comment trouver les 6 distances connaissant le sommes des 6 chemins: systeme linéaire 6 équations à 6 inconnues mais est-il régulier?? 
Nous serons mieux armés après la semaine 7, puisque si j'ai bien compris nous y verrons des outils orientés calcul. 

A suivre donc, vos réflexions sont bienvenues!!

