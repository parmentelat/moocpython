#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from pathlib import Path
import shutil


class pile_up_my_file:

    def __init__(self, ext_in, ext_out):
        """Crée la liste des fichiers 'file_list' ayant l'extension 'ext_in'
        la liste 'file_select' du même nombre d'éléments mis à 'none' qui stockera les fichiers sélectionnés.
         Initalise la variable 'ext_out' qui contient l'extension du ficier de sortie sans le point """

        self.p = Path('.')
        self.file_list = list(self.p.glob(ext_in))
        self.file_select = ['none' for element in self.file_list]
        self.ext_out = ext_out

    def list_name(self, file_to_screen):
        """" Affiche la liste des fichiers sans le path"""

        for fichier in file_to_screen:
            print(fichier.name)

    def check_enter(self):
        """Vérifie ce qui est entré par l'utilsateur ( pour le moment s pour sortir ou un N° index valide de 'list_file')"""

        while True:

            try:
                entree = input("\nTaper le numéro du fichier pour le sélectionner. Taper 'S' pour sortir : ")

                if entree in ("Ss") or int(entree) in range(0, len(self.file_list) - 1):
                    break

            except ValueError:

                print(f"Vous devez taper un nombre entre 0 et {len(self.file_list) - 1} ou 's' pour sortir !")

        return entree

    def my_choice(self):
        """Choix des fichiers à assembler"""

        counter = 0 # Index de 'file_select

        while True:

            # Afficahge de l'entête
            titre = "N°".center(3) + " | " + "Disponible".center(20) + " | " + "Sélectionné".center(20)
            print(titre)
            print("-" * len(titre))

            for indx, element in enumerate(self.file_list):

                # Formatage derniere colonne en fonction du contenu
                if self.file_select[indx] == 'none':
                    last_col = self.file_select[indx].ljust(20)
                else:
                    last_col = self.file_select[indx].name.ljust(20)

                # Affichage de la rangée
                print(f"{indx :3} | {element.name.ljust(20)} | {last_col}")

            entree = self.check_enter() # Saisie

            if entree.lower() == "s":

                # Si on sort, supression des none inutiles et compilation du fichier de sortie(prevoir un test si liste vide)
                self.file_select = [fichier for fichier in self.file_select if fichier is not 'none']

                with open('temp_file.' + self.ext_out, 'w', encoding = 'utf8') as sortie:
                    for entree in self.file_select:
                        with open(entree, 'r', encoding = 'utf8') as en_cours:
                            shutil.copyfileobj(en_cours, sortie)
                break

            elif int(entree) in range(0, len(self.file_list) - 1):

                # si le fichier est déjà dans la liste on le supprime
                if self.file_list[int(entree)] in self.file_select:
                    self.file_select.remove(self.file_list[int(entree)])
                    self.file_select.append('none')
                    counter -= 1

                # Sinon, on l'ajoute
                else:
                   self.file_select[counter] = self.file_list[int(entree)]
                   counter += 1

class txt_to_rst:

    def __init__ (self, fichier_in, fichier_out):

        self.fichier_in = fichier_in
        self.fichier_out = fichier_out
        self.chaine =""

    def file_to_string(self):
        """Ouvre le fichier 'fichier' en lecture et le stock dans une chaine"""
        try:
            self.chaine = open(self.fichier_in, 'r', encoding = 'utf8').read()
        except FileNotFoundError:
            print(f"Je ne trouve pas '{self.fichier_in}' !")
        else:
            self.chaine = self.to_rst()
            self.titre()
            self.sauve_fichier()


    def to_rst(self):
        """Traite la chaine créé par 'file_to_string'"""

        temp_list = self.chaine.split("\n")

        for num_ligne, ligne in enumerate(temp_list):

            # Si une ligne contient coding on l'enléve
            if "coding" in ligne:

                temp_list[num_ligne] = ""

            # Si une ligne contient Corrigés faire un titre de niveau 2 et enlever les # de la ligne precedente et suivante
            elif "Corrigés" in ligne:

                temp_list[num_ligne] = ligne[2:] + "\n" + "-" * len(ligne[2:])
                temp_list[num_ligne + 1] = ""
                temp_list[num_ligne - 1] = ""

            # Si une ligne contient Semaine oter les deux premiers carateres et faire un titre de niveau 3
            # les lignes suivante sont du code donc ajouter .. code:: ipython3
            elif "Semaine" in ligne:

                temp_list[num_ligne] = ligne[2:] + "\n" + "~" * len(ligne[2:]) + "\n" + "\n.. code:: ipython3\n"

            # Si une ligne contient plusieurs # mettre une ligne vide
            elif "#######" in ligne:

                temp_list[num_ligne] = ""


            # indenter les autres lignes
            else:

                temp_list[num_ligne] = "    " + ligne

        return "\n".join(temp_list)

    def titre(self):

        titre = "Corrigés\n========\n"
        self.chaine = titre + self.chaine

    def sauve_fichier(self):
        """Sauvegarde du nouveau fichier"""
        with open(self.fichier_out, 'w', encoding = 'utf8') as fichier:
            fichier.write(self.chaine)

#-------------------- Main ------------------------------------

mon_fichier = pile_up_my_file('*.txt', 'txt')

mon_fichier.my_choice()

test = txt_to_rst('temp_file.txt', 'corriges_all.rst')

test.file_to_string()
