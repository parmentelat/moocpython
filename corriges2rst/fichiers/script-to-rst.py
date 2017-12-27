#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on Sat Dec 23 05:41:40 2017
@author: jg

Script "artisanal" mais appliqué dont le point de départ est adapté
d'un modèle mis à dispo sur le Mooc Python 3

Objectif : regrouper les fichiers txt des corrigés par semaine sur un seul fichier rst
Hypothèse de départ : tous les fichiers y compris le script sont dans le même dossier
Option choisie : traitement par lignes et regroupement dans un seul objet
avant écriture finale dans le fihcier "corriges.rst"

Le script fonctionne très bien mais doit pouvoir être optimisé
Remarques, suggestions bienvenus...
"""

from pathlib import Path
import re # Opérations à base d’expressions rationnelles
import textwrap # comme indiqué en titre du module ;)

# Vérification préalable pour le dossier et chaque fichier à traiter
def test(arg):
    path_dir = Path(__file__).parent
    if arg == path_dir:    
        response = input(f"dossier => {path_dir} ... à traiter ? (Entrée pour oui) :")
    else:
        if isinstance(arg, list):
            response = input(f"traitement automatique pour ces fichiers ? (Entrée pour oui) :")
        else:
            response = input(f"fichier => {arg} ... à traiter ? (Entrée pour oui) :")

    # validation ou non en réponse
    if len(str(response)):
        print("non")
        return False
    else:
        print("oui")
        return True

def launch_script(ext):
    path_dir = Path(__file__).parent
    # Récupération dans une liste de tous les fichiers.txt du dossier
    if test(path_dir):
        files = [file.name for file in list(path_dir.glob(ext))]
        files.sort()
        print(f"Fichiers txt présents dans le dossier \"{path_dir.name}\": \n{files}")
        if test(files):
            files_list = files
        else:
            files_list = [file for file in files if test(file)]
    
        if len(files_list):
            # lance la lecture des fichiers txt et le regroupement des données
            read(files_list)
        else:
            print("Oups! Apparemment aucun fichier à traiter...")
    else:
        print("Oups! Apparemment ce n'est pas le bon dossier...")

def read(corriges_list):
    # Création liste vide regroupant le contenu de tous les corriges.txt
    txt_fullcontents = []
    # récupération des données, regroupement et mise en forme pour Sphinx
    for titre_semaine in corriges_list:
        # gestionnaire de contexte qui ouvre en lecture
        # et ferme chaque fichier corriges.txt
        with open(titre_semaine, encoding='utf-8') as entree:
            prepareData(entree, txt_fullcontents)

    # lance l'écriture dans le fichier de regroupement rst
    write("".join(txt_fullcontents))

def prepareData(entree, txt_fullcontents):
    for line in entree:
        #suppression de lignes avec #### et autres... à optimiser ?
        line = re.sub(r"^#*[\n]", "\n", line)
        line = re.sub(r"(\# -\*- coding: utf-8 -\*-)", '', line)
        line = re.sub(r"^(#*\s{1})$", '', line)

        # titre 2
        if re.search(r"\w*(Corrigés de la semaine \d)\n", line):
            titre2 = re.search(r"\w*(Corrigés de la semaine \d)\n", line)[0]
            line = "\n\n" + titre2 + ("-" * len(titre2.strip())) + "\n\n"

        # titre 3
        elif re.search(r"\w*(Semaine \d Séquence \d\n)", line):
            titre3 = re.sub(r"^(#{1}\s{1})", '', line)
            line = "\n" + titre3 + ("~" * len(titre3.strip())) + "\n\n" + ".. code:: ipython3" + "\n\n"

        # indentation de 4 espaces les lignes "bloc de code" qui suivent les titres 3
        else:
            line = textwrap.indent(line,'    ')
            
        # regroupement de tous les corrigés dans un seul objet
        txt_fullcontents.append(f"{line}")

    return txt_fullcontents

def write(txt_fullcontents):
    titre = "Corrigés"
    titre = titre + "\n" + ("=" * len(titre))
    # gestionnaire de contexte qui ouvre en écriture
    # et ferme le fichier.rst (regroupement)
    with open('corriges.rst', "w", encoding='utf-8') as sortie:
        sortie.write(titre)
        sortie.write(f"{txt_fullcontents}")
        print('---\nTraitement effectué avec succès dans "corriges.rst" !')

# Lance la procédure pour les fichiers txt du dossier
launch_script("*.txt")
