#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 08:08:35 2018
@author: jg

Le script fonctionne pour regrouper les chapitres par semaine pour pouvoir
générer ensuite des supports en différents formats à partir de Sphinx.
Reste malgré tout en chantier et donc absolument pas finalisé!
Toutes suggestions, corrections, remarques, idées bienvenues...

Important pour la génération des documents par Sphinx
-----------------------------------------------------
Penser à ajouter un dossier "media" dans le dossier "source" du projet
et y mettre les images récupérées à partir de l'export des notebooks originaux.

Pour générer le PDF, il faut penser à supprimer ou déplacer tous 
les fichiers rst des notebooks originaux (à l'extérieur du dossier "source").
Ne garder que les fichiers générés : index et les semaines 1 à 6 (ou plus)
Penser aussi à mettre toutes les images dans le dossier "latex" généré par
Sphinx dans le dossier "racine" du projet (celui du "sphinx-quickstart")
Faire ensuite une 2ème passe le cas échéant.

Pour la génération d'un dossier HTML garder le dossier source" tel quel... 
les fichiers non présents dans le sommaire le seront dans l'index généré par
Sphinx et utilisé "par défaut" pour la recherche apr mots-clés dans le site.
Pas trouvé mieux pour l'instant pour modifier les paramètres par défaut.
"""
from itertools import islice
from pathlib import Path
import re

def read():
# mettre tout les fichiers .rst dans une liste
    path_dir = Path(__file__).parent
    files = [file.name for file in list(path_dir.glob("*.rst")) 
            if re.search(r"(?<=[wW])(\d*)(?=\-)", file.name)]
    files.sort()
    tuples_it = ((makeTitre(file), file) for file in files)
# groupBy from Milind Gokhale => https://stackoverflow.com/questions/45476509/
    group_by_w = dict()
    for tuple in tuples_it:
        if tuple[0] not in group_by_w:
            group_by_w[tuple[0]] = list()
        group_by_w[tuple[0]].append(tuple[1])

    # Création liste vide regroupant le contenu de tous les corriges.txt
    index = []
    # dictionnaire des titres par semaine
    titles_sem = {
    '1': 'Semaine 1 : Introduction au MOOC et aux outils Python',
    '2': 'Semaine 2 : Notions de base pour écrire son premier programme en Python',
    '3': 'Semaine 3 : Renforcement des notions de base, références partagées',
    '4': 'Semaine 4 : Fonctions et portée des variables',
    '5': 'Semaine 5 : Itération, importation et espace de nommage',
    '6': 'Semaine 6 : Conception des classes',
    }
    # récupération des données, regroupement et mise en forme pour Sphinx
    for key, values in group_by_w.items():
        index.append(key[:-4])
        contents_week = []
        for file in values:
            week_num = re.search(r"(?<=[wW])(\d*)(?=\-)", file)[0]
            with open(file, encoding='utf-8') as entree:
                list(islice(entree, 14)) # head
                contents = [line for line in entree]
            contents_week.append(f"{''.join(contents)}") 
            # pour ajouter le titre des fichiers dans l'index... le cas échéant
            # index.append(file[:-4])
        title_sem = titles_sem[week_num]
        title_sem = ("\n"+ ("=" * len(title_sem)) + "\n" + title_sem + "\n" + 
          ("=" * len(title_sem)))
        with open(key, "w", encoding='utf-8') as week:
            week.write(f"{title_sem}\n\n{''.join(contents_week)}")

    index.append("corriges")
    writeIndex(index)
    
def makeTitre(file):
    week = re.search(r"(?<=[wW])(\d*)(?=\-)", file)[0]
    titre1_file = f"Semaine-{week}.rst"
    return titre1_file

def writeIndex(index):
    # Titre du document
    titre = "Python 3 : des fondamentaux aux concepts avancés du langage"
    titre = titre + "\n" + ("=" * len(titre) + "\n" * 2)
    titre = titre + ".. toctree::\n   :maxdepth: 2\n\n"
    toctree_list = index
    # Ouverture du fichier en ecriture et utf-8
    with open("index.rst", "w", encoding='utf-8') as fichier:
        # Ecriture de l'entête
        fichier.write(titre)
        # Ecriture de la liste des fichiers
        for item in toctree_list:
            fichier.write(f"   {item}\n")

read()
