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

# mettre tout les fichiers .rst dans une liste
corriges_list = glob.glob("*.txt")

# Supprimer l'extension, sphinx n'en veut pas
corriges_list = [nom for nom in corriges_list if nom != 'modele.txt']
corriges_list.sort()
print(corriges_list)

# ouvre et ferme les fichiers corriges.txt en lecture par "context manager"
def read():
    titre_start = "# -*- coding: utf-8 -*-"
    titre_end ="#\n############################################################\n"
    full_contents = ""
    
    for i, titre_semaine in enumerate(corriges_list):
        print(titre_semaine)
        titre = f"Corrigé de la semaine{i+2}"
        titre = titre + "\n" + ("-" * len(titre) + "\n" * 2)
        
        with open(titre_semaine, encoding='utf-8') as entree:
            contents = entree.read()
            print(contents.find(titre_start))
            print(contents.find(titre_end))
            full_contents += f"{titre}{contents}\n\n"
            
    write(full_contents)
    
# ouvre et ferme le fichier.rst e regroupement en écriture par "context manager"           
def write(full_contents):
    titre = "Corrigés"
    titre = titre + "\n" + ("=" * len(titre) + "\n" * 2)
    
    with open('corriges-all.rst', "w", encoding='utf-8') as sortie:
        sortie.write(titre)
        sortie.write(f"{full_contents}")

read()
