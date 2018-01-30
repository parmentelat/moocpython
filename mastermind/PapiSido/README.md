Une version en évolution (30/01/2018): paramètrage du programme par la ligne de commande
 options disponibles ( en fonction du programme )
 *  -c l'ordinateur est le codeur: choisit le code ( sinon l'utilisateur )
 *  -s l'ordinateur est le solveur: il cherche ( et trouve plutôt plus vite que vous)  la solution, sinon l'utilisateur
 *  -a choisit l'alphabet ABCDEF par défaut( sans guillemets , le paramètres sont si je comprends bien toujours interpretés comme des string
 *  -n le nombre de pions (4 par défaut), string donc à transformer en int avant utilisation (petite erreur dans la proposition de Thierry, je crois )
 *  -z nombre de parties à jouer ( pour mm_stat, 10 par défaut )
 *  -j pour le nom du fichier journal( mm.jnl par défaut, - pour stdout )

Toutes les options sauf -z sont disponibles lorsque l'on lance mastermind.py. Donc par défaut sans les options -c et/ou -s le programme est seulemnt spectateur, il deviendra bientôt arbitre en vérifiant la cohérence des réponses. De même si les deux options sont actives le programme joue contre lui-même, Regardez le à l'oeuvre, c'est impressionnant et pourtant ce n'est vraiment pas de l'"intelligence artificielle". Un exemple de plus de l'adage "un ordinateur, c'est bête mais ça va vite et ça n'oublie rien"
Les autres programmes importent mastermind.py
* mm_coder.py choisit un code et répond à vos essais ( jeu standard: 4 pions, 6 couleurs ). les options -a et -n sont disponibles mais ne soyez pas trop gourmant, cela devient vite très lent ( petite déception, en java il me semble que cela allait nettement plus vite )
* mm_solver.py trouve un code choisi par vous ( idem)
* mm_tester.py sorte de bac à sable ( cf le docstring de mastermind.py )
* mm_stats.py joue plusieurs parties ( le paramètre -z ) contre lui-même, -a et -n disponibles

Attention le programe bugge si le codeur humain entre une réponse incohérente avec les précédentes ( boucle infinie je pense) Normalemnt j'avais réglé ce problème mais il revient; ce doit être assez bête mais à corriger. Ce sera, avec quelques améliorations cosmétiques la prochaine version avant d'aborder gui et graphique
