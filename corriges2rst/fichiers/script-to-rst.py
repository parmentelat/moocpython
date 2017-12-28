#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jg

Script "artisanal" mais appliqué dont le point de départ est adapté
d'un modèle mis à dispo sur le Mooc Python 3
Excellent terrain de jeu pour un "apprentissage par tâtonnement expérimental".
Du coup des options, variantes et autres choix de traitement sont possibles...
Le script fonctionne très bien mais doit pouvoir être optimisé
Remarques, suggestions bienvenues...

Objectif, contexte de départ et option d'exécution choisie 
Regrouper les fichiers txt des corrigés par semaine sur un seul fichier rst
Tous les fichiers y compris le script sont dans le même dossier
Le traitement se fait par ligne et le regroupement dans un seul objet
avant écriture finale dans le fichier "corriges.rst"
"""
# *************** voir à la fin du script
import tkinter
from tkinter import filedialog
# ***************
import sys
from pathlib import Path
import re # Opérations à base d’expressions rationnelles
import textwrap # comme indiqué en titre du module ;)

# Vérification préalable pour le dossier et chaque fichier à traiter
def test(arg):
    path_dir = Path(__file__).parent
    
    # si le dossier ne s'affiche pas dans un terminal (c'est mon cas;)
    dirname = sys.path[0] if sys.path[0] else path_dir.name
  
    if arg == path_dir:
        print(f"\ndossier en cours => {dirname}")
        response = input(f"Est-ce le bon dossier à traiter ? (Entrée pour oui)")
    else:
        if isinstance(arg, list):
            response = input(f"traitement automatique pour ces fichiers ? (Entrée pour oui)")
        else:
            response = input(f"fichier => {arg} à traiter ? (Entrée pour oui)")

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
        print(f"Fichiers txt présents dans le dossier : \n{files}")
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
            week = re.search(r"(?<=[wW])(\d*)(?=\.)", titre_semaine)[0]
            prepareData(entree, txt_fullcontents, week)

    # lance l'écriture dans le fichier de regroupement rst
    write("".join(txt_fullcontents))

def prepareData(entree, txt_fullcontents, week):
    #print(week)
    for line in entree:
        #suppression de lignes avec #### et autres... à optimiser ?
        line = re.sub(r"^#*[\n]", "\n", line)
        line = re.sub(r"(\# -\*- coding: utf-8 -\*-)", '', line) 
        line = re.sub(r"^(#*\s{1})$", '', line)

        # titre 2
        if re.search(r"\w*(Corrigés de la semaine \d)\n", line):
            titre2 = re.search(r"\w*(Corrigés de la semaine \d)\n", line)[0]
            line = "\n\n" + titre2 + ("-" * len(titre2.strip())) + "\n\n"
        
        elif re.search(r"(#!/usr/bin/env python3)", line):
            line = re.sub(r"(#!/usr/bin/env python3)", '', line)
            titre2 = f"Corrigés de la semaine {week}\n"
            line = "\n\n" + titre2 + ("-" * len(titre2.strip())) + "\n\n"  + ".. code:: ipython3" + "\n\n"
            #print(line)

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
    # *****************************
    dialog_box = tkinter.Tk()
    dialog_box.filename =  filedialog.askdirectory(title='Choisir le dossier de destination')
    destination_path = dialog_box.filename
    dialog_box .destroy()
    # *****************************
    titre_corriges = "Corrigés"
    titre_corriges = titre_corriges + "\n" + ("=" * len(titre_corriges))
    # gestionnaire de contexte qui ouvre en écriture
    # et ferme le fichier.rst (regroupement)
    with open(destination_path + "/corriges.rst", "w", encoding='utf-8') as corriges:
        corriges.write(titre_corriges)
        corriges.write(f"{txt_fullcontents}")
        with open(destination_path + "/index.rst", "w", encoding='utf-8') as index:
            titre_index = 'MOOC Python 3 - corrigés'
            titre_index = titre_index + "\n" + ("=" * len(titre_index) + "\n" * 2)
            contents_index = titre_index + ".. toctree::\n   :maxdepth: 3\n\n   corriges"
            index.write(contents_index)    
    print(f'''
    Traitement effectué avec succès!
    --- 2 fichiers créés ou mis à jour : corrigés.rst et index.rst
    --- dans le dossier : {destination_path}''')

# Lance la procédure pour les fichiers txt du dossier
launch_script("*.txt")
