#!/usr/bin/env python3
#!python3

"""
Script adapté à partir d'un modèle mis à dispo sur le Mooc Python 3
Script de départ à compléter et à optimiser...
Commentaires sur le script en cours et toutes suggestions bienvenues ;)
Permet de regrouper les fichiers txt des corrigés par semaine sur un seul fichier rst
Hypothèse de départ : tous les fichiers y compris le script sont dans le même dossier
"""
import os # module suivant platforme
print(os)
import glob
print(glob) # manipuation de fichier ?
import re # formatage des données

# mettre tout les fichiers .txt dans une liste
corriges_list = glob.glob("*.txt")
#corriges_list = [nom for nom in corriges_list]
corriges_list.sort()
print(corriges_list)

# ouvre en lecture et ferme en"context manager" chaque fichier corriges.txt
# récupération des données par fichier, regroupement et mise en forme des données
def read():
    full_contents = ""
    
    for i, titre_semaine in enumerate(corriges_list):      
        with open(titre_semaine, encoding='utf-8') as entree:
            contents = [line for line in entree.readlines()]
            for i, line in enumerate(contents):
                
                #suppression des ### et autres lignes inutiles
                line = re.sub(r"^#*[\n]", "\n", line)
                line = re.sub(r"(\# -\*- coding: utf-8 -\*-)", '', line)
                line = re.sub(r"^(#*\s{1})$", '', line)
                              
                # titre 2
                if re.search(r"\w*(Corrigés de la semaine \d)\n", line):
                    titre2 = re.search(r"\w*(Corrigés de la semaine \d)\n", line)[0]
                    line = "\n\n" + titre2 + ("-" * len(titre2)) + "\n\n"
                    
                # titre 3
                if re.search(r"\w*(Semaine \d Séquence \d\n)", line):
                    titre3 = "\n" + re.search(r"\w*(Semaine \d Séquence \d\n)", line)[0]
                    line = titre3 + ("~" * len(titre3)) + "\n\n" + ".. code:: ipython3" + "\n\n"
                    
                # regroupement de tous les corrges dans un seul objet 
                full_contents += f"{line}"
    
    # lance l'écriture dans le fichier de regroupement rst      
    write(full_contents)
    
# ouvre en écriture et ferme en"context manager" le fichier de regroupement rst 
# regroupant tous les corrigés     
def write(full_contents):
    titre = "Corrigés"
    titre = titre + "\n" + ("=" * len(titre))
    
    with open('corriges-all.rst', "w", encoding='utf-8') as sortie:
        sortie.write(titre)
        sortie.write(f"{full_contents}")
        
# lance la lecture et le regroupement des données
read()
