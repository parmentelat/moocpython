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

########################

class CorrigesToRst:
    """
    Regrouper le contenu de plusieurs fihciers txt en 1 seul fichier rst.
    Le fichier rst pouvant servir à créer un pdf sous SPhinx.
    """
    
    def __init__(self, ext, path_dir = Path(__file__).parent, files = []):
        self.ext = ext
        self.path_dir = Path(__file__).parent
        self.files = sorted([file.name for file in list(path_dir.glob(self.ext))])
        
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

    def _testExt(self): # à optimiser...
        test = re.search(r"\.[a-z]{3}", self.ext[-4:])
        if  test:
            if not re.match(r"\.txt$", self.ext[-4:]):
                raise ExtensionError('Le script ne traite que les .txt ...')
            return True
        else:
            print(f"test : {self.ext[:]}")
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
        # liste vide pour stocker toutes les données avant le fichier rst final
        txt_fullcontents = []
        # lecture, regroupement et mise en forme des données pour Sphinx
        for semaine in files_selected:
            # gestionnaire de contexte en lecture
            with open(semaine, encoding='utf-8') as entree:
                week = re.search(r"(?<=[wW])(\d*)(?=\.)", semaine)[0]
                titre2 = f"Corrigés de la semaine {week}"
                titre2 = "\n\n" + titre2 + "\n" + ("-" * len(titre2)) + "\n"
                
                # lecture par ligne... test économie mémoire à confirmer ?
                txt_contents = ([self._prepareData(line) for line in 
                                 entree.readlines()])
    
            # ajout du titre 2 pour chaque fichier sous condition
            test_re = r"\w*(Semaine \d Séquence \d\n)"
            if re.findall(test_re, "".join(txt_contents)):
                txt_contents.insert(0, titre2)
            else:
                # si aucune séquence signalée dans un fichier (semaine)
                txt_contents.insert(0, titre2 + "\n.. code:: ipython3" + 
                                    "\n\n")
            
            # regroupement de tous les corrigés dans un seul objet
            txt_fullcontents.append("".join(txt_contents))        
        
        # lance l'écriture dans le fichier de regroupement rst
        self._write("".join(txt_fullcontents), files_selected)
        
    def _prepareData(self, line):
        # suppression de lignes contenant certains pattern... à optimiser ou
        # revoir avec une fonction pour gérer les patterns dynamiquement...
        line = re.sub(r"^#*[\n]", '', line)
        line = re.sub(r"(\# -\*- coding: utf-8 -\*-)", '', line) 
        line = re.sub(r"\w*(Corrigés de la semaine \d)\n", '', line)
        line = re.sub(r"(#!/usr/bin/env python3)", '', line)
        line = re.sub(r"^(#*\s{1})$", '', line)
            
        # titre 3
        if re.search(r"\w*(Semaine \d Séquence \d\n)", line):
            titre3 = re.sub(r"^(#{1}\s{1})", '', line)
            line = ("\n" + titre3 + ("~" * len(titre3.strip())) + "\n\n" 
                    + ".. code:: ipython3" + "\n\n")
            
        # indentation de 4 espaces pour les lignes "bloc de code" 
        # qui suivent les titres 3
        else:
            line = textwrap.indent(line,'    ')

        return line
    
    def _write(self, txt_fullcontents, files_selected):
        titre = "Corrigés"
        titre = titre + "\n" + ("=" * len(titre))
        # gestionnaire de contexte en écriture
        with open('corriges.rst', "w", encoding='utf-8') as sortie:
            sortie.write(titre)
            sortie.write(f"{txt_fullcontents}")
            with open("index.rst", "w", encoding='utf-8') as index:
                titre_index = 'MOOC Python 3 - corrigés'
                titre_index = (titre_index + "\n" + ("=" * len(titre_index) + 
                                                     "\n" * 2))
                contents_index = (
                        titre_index +
                        ".. toctree::\n   :maxdepth: 2\n\n   corriges"
                        )
                index.write(contents_index)
                print(f"""
... Fichiers txt traités regroupés avec succès dans "corriges.rst" :
    {files_selected}
... Fichier index.rst créé ou mis à jour
            """)
 
class ExtensionError(Exception):
    pass              

start = CorrigesToRst("txt")

print(f"""
    Infos de démarrage (pour test essentiellement)
--- start instance actuelle de CorrigesToRst("txt")
--- chemin du dossier actif:
    start.path_dir = {start.path_dir}
--- Fichiers {start.ext} présents:
    start.files = {start.files}

--- Méthodes:
    auto(), manual()
--- Attributs:
    ext, path_dir, files
        """)
    
#c.auto()
start.manual()

