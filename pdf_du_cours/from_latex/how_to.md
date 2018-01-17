Structure de l'arborescence :
 
 mooc_python ( dossier )  
|__ media( dossier contenant les images )  
|........|__ str-bytes.png  
|........|__ xxx.png  
|__ python3.tex ( Fichier maître )  
|__ w1-s2-c1-installer-python.tex  
|__ wx-sx-cx-xxxx.tex  


### Étape 1
Télécharger les notebooks option LaTeX.
- Les cellules doivent avoir été exécutées.
- Sauf :
   - Celles destinées au code des étudiants.
   - Celles utilisant Python Tutor (pas pris en compte dans LaTex).
  
### Étape 2
#### Création du fichier maître.
- Copier n'importe quel fichier du cours et le renommer python3.tex.
- Tout le début d'un fichier LaTeX concerne  les paramètres du document.
   - Le fichier maître ne va contenir que les paramètres, la page de garde et la liste des fichiers à inclure.
   - On supprime donc tout ce qu'il y a entre **\begin{document}** et **\end{document}**.
- Modifier la ligne **\documentclass[11pt]{article}** => **\documentclass[11pt, a4paper, french]{book}**.
- Ajouter la ligne **\usepackage[francais]{babel}** (Typographie française).
- Dans la section **%Document** parameters mettre en remarque la ligne **\title{titre}** =>**%\title{titre}**.
- Si vous n'avez pas enlevé **\maketitle** sous **\begin{document}**, le mettre en remarque.
- Sous **\begin{document}**, on insère la page de garde. (Voir le modèle que j'utilise: page_garde.tex)
- Insérer la commande **\tableofcontents** pour la table des matières.
- Insérer ensuite la commande **\chapter{blabla}** et les commandes **\include{fichier}**  (voir python3.tex)

Il ne reste plus qu'à compiler le fichier. Je travaille avec MiKTeX qui fournit un éditeur TeXworks et génère un aperçu du résultat. Bien entendu avant la compilation il faut préparer les fichiers à inclure.

###Étape 3
- Pour les fichiers à inclure, il faut supprimer toute l'entête du fichier jusqu'à la ligne {Licence CC BY-NC-ND} {Thierry Parmentelat \& Arnaud Legout} {} incluse. (Cette information ne figurera qu'une seule fois sur la page de garde par exemple)
- Supprimer aussi les deux dernières lignes :
  - % Add a bibliography block to the postdoc
  - \end{document}

Pour que la table des matières soit générer, il faut compiler deux fois.

Avant de supprimer l'entête et la fin des fichiers à inclure, je les compile pour détecter d’éventuels problèmes. C'est plus facile de travailler sur un petit fichier que sur un gros. ;-)
Et on en rencontre certains ( caractères non reconnus, tables non reconnues, etc.)

@parmentelat
- Je ne sais pas si j'ai bien compris ce que tu veut dire par :  

> de savoir comment je peux reproduire moi même, à partir typiquement du contenu du cours qui est donc toujours sur http://github.com/parmentelat/flotpython; 

mais je pense que l'on ne coupe pas au téléchargement des fichiers LaTeX via Jupyter (en local ou par le mooc)

- Je crois aussi que d'avoir un fichier maître et des includes, te permettras :
  - de publier le pdf semaine par semaine afin de ne pas dévoiler la suite du cours.
  - de facilité les corrections.
  - Et enfin si vous êtes plusieurs, chacun peu travailler sur un chapitre différent.

Je mettrais au fur et à mesure de l'avancement du projet tous les fichiers dans un fichier compressé afin que tu puisses les exploiter sans être obligé de tout recommencer. (mooc_python.7z)



