# Génération du PDF avec LaTeX

### Environnement de travail : [TeXstudio](https://www.texstudio.org/)

## Structure de l'arborescence sur Github :

~~~
<pdf-session-2>
|__<python_2018>
|...|__ medias( dossier contenant les images )
|........|__ str-bytes.png
|........|__ xxx.png
|...|__ Python.tex ( Fichier maître )
|...|__ w1-s2-c1-installer-python.tex
|...|__ wx-sx-cx-xxxx.tex
|...|__ Python.pdf
~~~

## Structure de l'arborescence sur votre pc si l’aventure vous tente :

Idem, plus divers fichiers log, toc, out, gz, pdf.


## Étape 1

Télécharger les notebooks option LaTeX.

* Les cellules doivent avoir été exécutées.
* Sauf :
    ◦ Celles destinées au code des étudiants.
    ◦ Celles utilisant Python Tutor (pas pris en compte dans LaTex).

## Étape 2

Création du fichier maître. **`Python.tex` est inclus dans le repo git** il n'y a en principe pas besoin d'y retoucher.

Pour mémoire, voici la logique pour le construire:

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

## Étape 3

Pour chaque notebook:

* évaluer les cellules qui vont bien,
* transformer en .tex
* supprimer toute l'entête du fichier jusqu’à la ligne:
{Licence CC BY-NC-ND} {Thierry Parmentelat & Arnaud Legout} {} incluse.
(Cette information ne figurera qu'une seule fois sur la page de garde par exemple)

* Supprimer aussi la dernière ligne qui contient
 ◦ \end{document}
 On peut aussi si on veut enlever la ligne
 `% Add a bibliography block to the postdoc`
 mais c'est un commentaire

## Étape 4

Sélectionnez la plage de semaines qui vous intéresse. Pour cela utilisez

   `./contenu.py --help`

Par exemple si vous voulez des semaines 2 à 4 incluses:

   `./contenu.py --from 2 --to 4`
   ou bien, c'est pareil
   `./contenu.py -f 2 -t 4`

Cela va créer un fichier `contenu.tex` qui aura les chapitres et sections qui vont bien, en fonction de:

* les .tex qui sont présents dans le répertoire
* le fichier `00-chapter-names.txt`

## Étape 5

Il ne reste plus qu’à compiler le fichier; pour cela faire **trois fois (3 fois)**

    pdflatex Python



## Problèmes rencontrés.

• Parfois des sauts de lignes à ajouter (commande : \\)

• URL pas pris en compte faire : \href{https://www.python.org/download}{https://www.python.org/download}
							url				texte

• Justifier un colonne de tableau à droite
    \begin{longtable}[]{@{}lr@{}} Le l justifie à gauche le r à droite

• Inserer une image :
\includegraphics{medias/notebook-eval-button.png}

L’essentiel des problèmes rencontrés provient du fait que les fichiers sont générés par Jupyter qui fonctionne comme Sphinx à partir des fichiers rst.

• Certaines listes ne sont pas mises en forme; *(en principe ce cas ne devrait plus se présenter)*. Dans ce cas faire :

    \begin{itemize}
        \item
        blablal
    \end{itemize}


Je n’ai pas fait de script python pour automatiser une partie du travail parce qu’un contrôle visuel du rendu final est indispensable.
