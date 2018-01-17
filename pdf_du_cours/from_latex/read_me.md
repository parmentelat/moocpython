Aprés avoir generé le pdf du cours avec Sphinx à partir des imports en .rst, et puisque dans ce cas, Sphinx utilise LaTeX,
Je tente une nouvelle approche en utilisant directement LaTeX et les imports du cours en .tex.

Je precise qu'avant ce cours je n'utilisai ni l'un ni l'autre, du coup il y aura certainenemnt des maladresses.

#### Pourquoi ?
##### Sphinx
- Je ne maitrise pas vraiment le rst (il est possible donc qu'il y ai une astuce),
mais certaines limitations sont pénalisantes dans le cas du cours.
  - Par exemple : Je ne peux pas imbriquer les enrichissements de texte (mette gras et italique ne marche pas)
  - L'utilisation des niveaux de titre et hierarchisés. Impossible de mettre un niveau trois si le deux nexiste pas.
- Je ne sais pas si cela vient des fichiers Markdown d'origine ou de la generation des rst par ipython, mais les listes ne sont
pas bien gérées.(Visiblement en LaTeX il y a aussi ce problème mais beaucoup moins fréquent).
- Les Tables, Aie gros point noir...
- Bref, autant pour du html ou de l'epub Sphinx et super, autant pour du pdf il faut absolument que les fichiers rst soit parfait.
##### LaTeX
- Je ne maitrise pas plus LaTeX que Sphinx puisque decouvert tout récement...
- Beaucoup de problèmes rencontrés avec les _.rst_ disparaissent avec les _.tex_.
- En structurant les fichiers _.tex_ comme ceci :
  - un fichier maître contenant tout les parametres du fichier à rendre, la page de garde et un include de chaque fichier .tex des notebook(purger des paramètres).
  - On peu travailler en équipe, chacun gérant un chapitre par exemple.
  - Si une modification est necessaire, seul un fichier est concerné.
  - Gestion des TOC, notes, bibliographie, etc.
 - Il y a quand de petits choses à corriger dans certains fichiers .tex, mais le résultat est interessant, assez proche du cours et la coloration syntaxique est plus à mon goût.

### Comment ?
Ca commence à faire long. Je vais faire un how to pour expliquer la demarche.
