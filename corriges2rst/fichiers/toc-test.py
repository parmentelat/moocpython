#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 08:08:35 2018
@author: jg
"""

from itertools import islice
from pathlib import Path
import re

"""

Le script fonctionne pour regrouper les chapitres par semaine pour pouvoir
générer ensuite des supports en différents formats à partir de Sphinx.
Tout le reste est à l'essai et en chantier donc absolument finalisé!
Toutes suggestions, corrections, remarques, idées bienvenues...

Important pour la génération des documents par Sphinx :
Penser à ajouter un dossier "media" dans le dossier "source" du projet
et y mettre les images récupérées à partir de l'export des notebooks originaux.

Pour générer le PDF, il faut penser à supprimer ou déplacer tous 
les fichiers RST originaux (en dehors du dossier "source")
pour ne garder que les fichiers générés : index et les semaines 1 à 6 (ou plus)
Penser aussi à mettre toutes les images dans le dossier "latex" généré par Sphinx
dans le dossier "racine" du projet (correspondant au "sphinx-quickstart")
Faire ensuite une 2ème passe le cas échéant.

Par contre pour la génération d'un dossier HTML par Sphinx garder le dossier 
"source" tel quel... les fichiers non présents dans l'index le seront dans
l'index de la page "search.html" ce qui peut s'avérer plus "user-friendly"
Pas trouvé mieux pour l'instant pour modifier les paramètres par déafaut.
"""

def read():
    # mettre tout les fichiers .rst dans une liste
    path_dir = Path(__file__).parent
    files = [file.name for file in list(path_dir.glob("*.rst")) 
            if re.search(r"(?<=[wW])(\d*)(?=\-)", file.name)]
    files.sort()
    tuples_it = ((makeTitre(file),file) for file in files)
# idea group by Milind Gokhale => https://stackoverflow.com/questions/45476509/
    group_by_w = dict()
    for tuple in tuples_it:
        if tuple[0] not in group_by_w:
            group_by_w[tuple[0]] = list()
        group_by_w[tuple[0]].append(tuple[1])

    # récupération des données, mise en forme et regroupement par semaine
    index = []
    for key, values in group_by_w.items():
        titre1 = key[:-4]
        index.append(titre1)
        titre1 = ("\n"+ ("=" * len(titre1)) + "\n" + titre1 + "\n" + 
                  ("=" * len(titre1)))
        contents_week = []
        for file in values:
            with open(file, encoding='utf-8') as entree:        
                head = list(islice(entree, 14))
                contents = checkTitle(entree.read(), file)
            contents_week.append(f"{''.join(contents)}") 
        with open(key, "w", encoding='utf-8') as week:
            week.write(f"{titre1}\n\n{''.join(contents_week)}")
    
    index.append("corriges")
    writeIndex(index)
    
def makeTitre(file): 
    week = re.search(r"(?<=[wW])(\d*)(?=\-)", file)[0]
    titre1_file = f"Semaine-0{week}.rst"
    return titre1_file

def checkTitle(contents, file):
    """
    fonction en chantier pour test essentiellement, sans solution "viable"
    pour le moment
    Objectif : vérifier le motif de chaque titre en fonction de leur "niveau"
    
    1 - vérifier les titres sur 5 niveaux ou plus...
    2 - comparer à un "séquence" donnée correspondant à différents
        niveaux de titres possibles
    3 - pouvoir enfin modifier les "motifs" des titres s'il ne sont pas 
        dans le bon ordre "hiérarchique"
    exemple : Indices négatifs en position 4 dans une séquence (hiérarchie)
              ^^^^^^^^^^^^^^^^
    pouvoir remplacer le motif ^ par ' Indices négatifs (' pour niveau 4)
                                       ''''''''''''''''
    """  
    levels_order = ["===", "---", "~~~", "'''", "^^^"]
    
    # essai sur un niveau 3 repéré
    re_levels3 = re.findall(r"^\={3,}\n|^\-{3,}\n|^\~{3,}\n",
                            contents, re.MULTILINE)  
    levels3  = [reg[0:3] for reg in re_levels3]
    test_3 = re.match(r"^\={3}\-{3}\~{3}", "".join(levels3[0:3]))
    
    re_levels5 = re.findall(r"^\={3,}\n|^\-{3,}\n|^\~{3,}\n|^\'{3,}\n|^\^{3,}\n",
                            contents, re.MULTILINE)  
    levels5  = [reg[0:3] for reg in re_levels5]
    test_5 = re.match(r"^\={3}\-{3}\~{3}\'{3}\^{3}$", "".join(levels5[0:5]))
    
    if test_3:
        print(file, levels5)
        
    return content-tocs

def writeIndex(index):
    # Titre du document
    titre = "Python 3 : des fondamentaux aux concepts avancés du langage"
    titre = titre + "\n" + ("=" * len(titre) + "\n" * 2)
    titre = titre + ".. toctree::\n   :maxdepth: 2\n\n"
    toctree_list = index
    # écriture index.rst
    with open("index.rst", "w", encoding='utf-8') as fichier:
        # Ecriture de l'entête
        fichier.write(titre)
        # Ecriture de la liste des fichiers
        for item in toctree_list:
            fichier.write(f"   {item}\n")

read()
