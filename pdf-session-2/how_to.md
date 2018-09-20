#### Génération du PDF avec LaTeX

Environnement de travail : [TeXstudio](https://www.texstudio.org/)

Structure de l'arborescence sur Github :

~~~
<pdf-session-2>
|__<python_2018>
|...|__ medias( dossier contenant les images )
|........|__ str-bytes.png
|........|__ xxx.png
|...|__ python.tex ( Fichier maître )
|...|__ w1-s2-c1-installer-python.tex
|...|__ w1-s2-c1-installer-python.aux
|...|__ wx-sx-cx-xxxx.tex
|...|_ python.pdf
~~~

Plus divers fichiers log, toc, out, gz, pdf.

Structure de l'arborescence sur votre pc si l’aventure vous tente :

~~~
<python_2018>
|...|__ medias( dossier contenant les images )
|........|__ str-bytes.png
|........|__ xxx.png
|...|__ python.tex ( Fichier maître )
|...|__ w1-s2-c1-installer-python.tex
|...|__ w1-s2-c1-installer-python.aux
|...|__ wx-sx-cx-xxxx.tex
~~~

Étape 1

Télécharger les notebooks option LaTeX.

    * Les cellules doivent avoir été exécutées. 
    * Sauf : 
        ◦ Celles destinées au code des étudiants. 
        ◦ Celles utilisant Python Tutor (pas pris en compte dans LaTex). 
Étape 2

Création du fichier maître.

    * Copier n'importe quel fichier du cours et le renommer python.tex. 
    * Tout le début d'un fichier LaTeX concerne les paramètres du document. 
        ◦ Le fichier maître ne va contenir que les paramètres, la page de garde et la liste des fichiers à inclure. 
        ◦ On supprime donc tout ce qu'il y a entre \begin{document} et \end{document}. 
    * Modifier la ligne \documentclass[11pt]{article} => \documentclass[11pt, a4paper, french]{book}. 
    * Ajouter la ligne \usepackage[francais]{babel} (Typographie française). 
    * Dans la section %Document parameters mettre en remarque la ligne \title{titre} =>%\title{titre}. 
    * Si vous n'avez pas enlevé \maketitle sous \begin{document}, le mettre en remarque. 
    * Sous \begin{document}, on insère la page de garde. (Voir le modèle que j'utilise: page_garde.tex) 
    * Insérer la commande \tableofcontents pour la table des matières. 
    * Insérer ensuite la commande \chapter{blabla} et les commandes \include{fichier} (voir python.tex) 
Plus simplement utilisez mon fichier python.tex comme base.

Étape 3

    • Pour les fichiers à inclure, il faut supprimer toute l'entête du fichier jusqu’à la ligne:
    {Licence CC BY-NC-ND} {Thierry Parmentelat & Arnaud Legout} {} incluse.
    (Cette information ne figurera qu'une seule fois sur la page de garde par exemple)

    • Supprimer aussi les deux dernières lignes : 
        ◦ % Add a bibliography block to the postdoc 
        ◦ \end{document} 

Il ne reste plus qu’à compiler le fichier. 
Problèmes rencontrés.

    • Parfois des sauts de lignes à ajouter (commande : \\) 

    • URL pas pris en compte faire : \href{https://www.python.org/download}{https://www.python.org/download}
							url				texte

    • Certaines listes ne sont pas mises en forme faire :
    \begin{itemise}
		  \item
		  blablal
    \end{itemise}

    • Justifier un colonne de tableau à droite
    \begin{longtable}[]{@{}lr@{}} Le l justifie à gauche le r à droite

    • Inserer une image :
    \includegraphics{medias/notebook-eval-button.png}

L’essentielle des problèmes rencontrés provient du fait que les fichiers sont générés par Jupyter qui fonctionne comme Sphinx à partir des fichiers rst.
Je n’ai pas fait de script python pour automatiser une partie du travail parce qu’un contrôle visuel du rendu final est indispensable.
