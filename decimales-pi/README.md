Comme première idée, je vous propose celle-ci : nous avons vu que Python permet avec les entiers et le type fraction, de faire des calculs en multiprécision. Je vous propose donc de calculer les décimales du nombre pi. Personnellement, je me suis amusé à l'écrire en moins de 50 lignes, par la méthode de la [formule de John Machin][1]  (Il s'agit d'un développement en série de la fonction arctangente)

J'avais écrit ce programme en c, il y a des années, et ça m'avait surtout coûté d'écrire moi même toutes les fonctions de calcul en multi précision. Avec les fractions en Python, ça se fait tout seul. Y-a juste un truc un peu technique, c'est l'affichage des décimales à partir des fractions, parce qu'on ne peut pas les convertir en réel sous peine de les perdre. Il faut donc l'approcher par une fraction dont le dénominateur est un exposant de 10.

Ps : Je me suis amusé à tester mon programme avec Python 3.4 et 3.6, et y-a une vache de différence de performance : Python 3.6 va 6-7 fois plus vite que 3.4 sur ce problème.

  [1]: https://fr.wikipedia.org/wiki/Formule_de_Machin

****
Contribution Ritchie:

Pour la multiprécision, le module Decimal semble convenir :

    In [5]: from decimal import *

    In [6]: getcontext().prec = 2000

    In [7]: print(1/Decimal(7))
...

On peut aussi utiliser une autre formule de Machin (parfois orthographié Méchin en France : il avait, parait-il, un ancêtre français).

$\frac{\pi}{4} = \arctan\left(\frac{1}{2}\right) + \arctan\left(\frac{1}{3}\right)$

à la place de la formule utilisée pour le calcul de $\pi$ au XIXe siècle, parce que son deuxième terme converge plus vite :

$\frac{\pi}{4} = 4 \arctan\left(\frac{1}{5}\right) - \arctan\left(\frac{1}{239}\right)$.

Je suis intéressé par ce mini-projet.

*****

pour le calcul de $\arctan\left(\frac{1}{k}\right)$

 Il suffit d'utiliser la formule majorant l'erreur :



$$\left \vert \arctan\left(\frac{1}{k}\right)  - \left( \frac{1}{k} - \frac{1}{3k^{3}}+ \frac{1}{5k^{5}}+ \cdots + \frac{(-1)^n}{(2n+1) k^{2n+1}}  \right)\right \vert \leq \frac{1}{(2n+3) k^{2n+3}}$$

Il n'y a pas besoin d'autre mathématique.
