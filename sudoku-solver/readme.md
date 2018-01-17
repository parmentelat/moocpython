# Solver de sudoku

Dans ce projet, je vous propose de concevoir un solver de sudoku.

Le but est de remplir une grille de valeurs prédéfinies et de laisser le programme essayer de résoudre le sudoku lui-même.

J'ai écrit une version qui m'a permis de valider une solution si cela vous intéresse sous le nom "sudoku_solver_solution_toussaic". Elle reste toutefois améliorable, par exemple en utilisant peut-être numpy/pandas.

Mais le plus intéressant est bien sûr de le faire vous même et je propose plusieurs façons de le résoudre.

La difficulté au départ est de bien définir une structure de données pertinente qui permette de manipuler les données plus facilement par la suite.

La seconde difficulté est de coder les algorithmes de résolution dont certains sont un peu compliqués (et pas toujours nécessaires selon la difficulté de la grille). Je vous recommande donc de commencer par les fonctions qui vous semblent les plus faciles (apparaissent en premier dans les sources).

## Mode hardcore

Débrouillez tout seul sans aucune aide. Cela nécessite de savoir comment résoudre un sudoku avec différentes méthodes.

## Mode difficile avec les algo

Partez du fichier sudoku_solver_hard_algo. Je n'y ai laissé que les prototypes et les aides des fonctions de résolution de l'algo. A vous d'écrire le reste.

## Mode difficile avec la structure

Partez du fichier sudoku_solver_hard_struct. Cette fois, en plus des informations précédentes, j'ai laissé les classes supplémentaires et leur aide.

# Mode intermédiaire avec les prototypes

Partez du fichier sudoku_solver_inter. J'ai laissé cette fois le prototype de toutes des classes et méthodes que j'ai utilisé avec leur aide.

# Mode facile

Partez du fichier sudoku_solver_easy. Deux des fonctions de résolution les plus compliquées sont données, ainsi que la fonction de résolution principale. Il est tout de même intéressant de bien comprendre comment elles fonctionnent pour écrire le reste.