#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 07:38:06 2017
@author: jg

Script "artisanal" faisant suite aux cours et supports du Mooc Python 3.
Excellent terrain de jeu pour un "apprentissage par tâtonnement expérimental".
Du coup des options, variantes et autres choix de traitement sont possibles...

Objectif : regrouper les fichiers.txt des corrigés/semaine dans un fichier.rst
Hypothèse de départ : les fichiers sont dans le même dossier que le script

Option choisie : éxécution à partir d'une instance "start" de la classe
CorrigesToRst() 

Le script fonctionne bien mais son code est-il suffisamement "pythonique" ?
Signalement de bugs, remarques ou suggestions d'optimisation bienvenus !
"""

from pathlib import Path
import re
import textwrap

class CorrigesToRst:
    """
    Regrouper le contenu de plusieurs fihciers txt en 1 seul fichier rst.
    Le fichier rst pouvant servir à créer un pdf sous SPhinx.
    """
    
    def __init__(self, ext, path_dir = Path(__file__).parent, files = []):
        self.ext = ext
        self.path_dir = Path(__file__).parent
        self.files = sorted([file.name for file in list(path_dir.glob(self.ext))])
        print(f"""
    Infos de démarrage (pour test essentiellement;)
--- chemin du dossier actif:
    {self.path_dir}
--- Fichiers {self.ext} présents:
    {self.files}

--- Méthodes:
    start.auto(), start.manual()
--- Attributs:
    ext, path_dir, files
        """)
        
    def _get_ext(self):
        return self._ext
    
    def _set_ext(self, ext):
        # ne lit et sélectionne que les fichiers correspondants au "pattern"
        # à optimiser le cas échéant
        self._ext = "corriges-w*." + ext
        
    ext = property(_get_ext, _set_ext)

    def auto(self):
        """
        Lance la procédure automatique de regroupement sur tous les fichiers
        présents dans le dossier actif
        """
        if self._testExt():
            self._launch(self.files)

    def manual(self):
        """
        Lance une procédure de selection préalable sur les fichiers présents
        dans le dossier actif avant regroupement dans le fichier final rst
        
        """
        if self._testExt():
            files_selected = [file for file in self.files if self._test(file)]
            self._launch(files_selected)
        
    def _testExt(self):
        test = re.match(r"[a-z]{3}", self.ext[-3:])
        if  test:
            return True
        else:
            print(f"test : {self.ext[-3:]}")
            print(f"Oups ! L'extension doit avoir 3 caractères minuscules...")
            return False
            
    def _test(self, arg):
        """
        Sélection manuelle des fichiers présents dans le dossier actif
        """
        response = input(f"fichier => {arg} ... à traiter ? (Entrée pour oui)")            
        if not response:
            print("oui")
            return True
        else:
            print("non")
            return False

    def _launch(self, files_selected):
        # test si la liste est vide
        if not files_selected or files_selected is None:
            # lance la lecture des fichiers txt et le regroupement des données
            print("Oups! Apparemment aucun fichier à traiter...")
        else:
            self._read(files_selected)

    def _read(self, files_selected):
        # le liste vide qui va servir à regrouper les données des fichiers txt
        txt_fullcontents = []
        # lecture, regroupement et mise en forme des données pour Sphinx
        for titre_semaine in files_selected:
            # gestionnaire de contexte en lecture
            with open(titre_semaine, encoding='utf-8') as entree:
                week = re.search(r"(?<=[wW])(\d*)(?=\.)", titre_semaine)[0]
                self._prepareData(entree, txt_fullcontents, week)
    
        # lance l'écriture dans le fichier de regroupement rst
        self._write("".join(txt_fullcontents), files_selected)
        
    def _prepareData(self, entree, txt_fullcontents, week):
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
                line = ("\n\n" + titre2 + ("-" * len(titre2.strip())) + "\n\n"
                        + ".. code:: ipython3" + "\n\n")
                #print(line)
    
            # titre 3
            elif re.search(r"\w*(Semaine \d Séquence \d\n)", line):
                titre3 = re.sub(r"^(#{1}\s{1})", '', line)
                line = ("\n" + titre3 + ("~" * len(titre3.strip())) + "\n\n" 
                        + ".. code:: ipython3" + "\n\n")
    
            # indentation de 4 espaces pour les lignes "bloc de code" 
            # qui suivent les titres 3
            else:
                line = textwrap.indent(line,'    ')
                
            # regroupement de tous les corrigés dans un seul objet
            txt_fullcontents.append(f"{line}")
    
        return txt_fullcontents
    
    def _write(self, txt_fullcontents, files_selected):
        titre = "Corrigés"
        titre = titre + "\n" + ("=" * len(titre))
        # gestionnaire de contexte en écriture
        with open('corriges.rst', "w", encoding='utf-8') as sortie:
            sortie.write(titre)
            sortie.write(f"{txt_fullcontents}")
            with open("index.rst", "w", encoding='utf-8') as index:
                titre_index = 'MOOC Python 3 - corrigés'
                titre_index = titre_index + "\n" + ("=" * len(titre_index) + "\n" * 2)
                contents_index = titre_index + ".. toctree::\n   :maxdepth: 2\n\n   corriges"
                index.write(contents_index)
                print(f"""
... Fichiers txt traités regroupés avec succès dans "corriges.rst" :
    {files_selected}
... Fichier index.rst créé ou mis à jour
            """)
                
start = CorrigesToRst("txt")

#start.auto()
start.manual()
