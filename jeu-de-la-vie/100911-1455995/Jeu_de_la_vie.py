# -*- coding: ISO-8859-15 -*-
'''
o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
LE JEU DE LA VIE
-- Ajout le 11/02/2015
-- Modifié le 29/04/2015 : Optimisation du code et ajout de fonctionnalités.
-- Modifié le 01/05/2015 : Correction d'un bug.
-- Modifié le 17/05/2015 : Ajout de fonctionnalité (Accélérer)
o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
'''
import sys, os.path, time, pickle

if sys.version_info[0] == 3:        #Si Python V3
    from tkinter import *
    from tkinter.messagebox import showinfo, askyesno
    from tkinter.filedialog import askopenfile
else:
    from Tkinter import *
    from tkMessageBox import showinfo, askyesno
    from tkFileDialog import askopenfile

class Grille:
    def __init__(self):
        self.L_H_cellule = 15           #Largeur/hauteur d'une cellule par défaut
        self.L_H_grille = 0             #Largeur/hauteur de la grille(en fonction de la taille de l'écran)
        self.H_appli_diff = 44          #En pixels = hauteur écran - hauteur de la grille
        self.cpt_gener = 0              #Compteur de générations
        self.traitement_en_cours = False #Témoin traitement générations actif/inactif
        self.frequence_affich = 1       #Temporisation pour la fréquence d'affichage
        self.dic_cell_live = {}         #Dictionnaire des cellules en vie à temps t
        self.dic_cell_live_t1 = {}      #Dictionnaire des cellules en vie à temps t+1
        self.dic_examen = {}            #Dictionnaire des cellules déjà examinées
        self.dic_cell_voisines = {}     #Dictionnaire des cellules voisines de chaque cellule en vie
        self.font1 = "Arial 10 bold"    #Police Titres
        self.font2 = "Arial 8 bold"     #Police Entetes
        self.chemin_motifs = os.environ['HOMEDRIVE'] #Chemin par défaut du fichier Motifs (pour importation)

    def grille_dessin(self):
        '''
        Dessiner la grille et afficher les comptages
        '''
        self.Grille.delete(ALL)
        L_H_ligne = self.L_H_cellule * self.nb_cellules #Longueur exacte de la ligne
        x = 0

        for _ in range(self.nb_cellules + 1):
            self.Grille.create_line(x, 0, x, L_H_ligne, fill = "grey50", tags = "lignes")
            self.Grille.create_line(0, x, L_H_ligne, x, fill = "grey50", tags = "lignes")
            x += self.L_H_cellule

        #Affichage infos de comptage
        self.Var_duree.set("%.3f" % 0)
        self.Var_gener.set(0)
        self.Var_population.set(0)
        self.Var_nb_totcell.set(self.format_milliers(str(self.nb_cellules ** 2)))
        self.Var_Nb_cell_LH.set(self.format_milliers(str(self.nb_cellules)))
        self.Var_Demarrer.set('Démarrer')

    def grille_reinit(self):
        '''
        Après modification de la taille d'une cellule, ré-initialisation de la
        grille et des paramêtres de l'application
        '''
        self.cpt_gener = 0          #Compteur de générations
        self.dic_cell_live = {}     #Dictionnaire des cellules en vie à temps t
        self.dic_cell_live_t1 = {}  #Dictionnaire des cellules en vie à temps t+1
        self.L_H_cellule = self.Var_L_cell.get()
        self.nb_cellules = int(self.L_H_grille / self.L_H_cellule)      #Nombre de cellules par ligne/colonne
        self.frequence_affich = 1
        self.debut = time.time()    #Top début
        self.grille_dessin()

    def coords_lig_col(self, event):
        '''
        Calcul des coordonnées x,y et des numéros de ligne et colonne
        '''
        x = event.x - (event.x % self.L_H_cellule)
        y = event.y - (event.y % self.L_H_cellule)
        lig = int(y / self.L_H_cellule)
        col = int(x / self.L_H_cellule)
        return x, y, lig, col

    def clic_gauche_cell(self, event):
        '''
        - Mettre la cellule à l'état vivant: couleur blanche
        - Enregistrer le numéro de la cellule dans <dic_cell_live>
        '''
        #Création de la cellule et ajout dictionnaire cellules en vie
        x, y, lig, col = self.coords_lig_col(event)

        if lig <= self.nb_cellules and col <= self.nb_cellules:
            if not (lig, col) in self.dic_cell_live:
                self.dic_cell_live.setdefault((lig, col))
                self.Grille.create_rectangle(x, y, x + self.L_H_cellule, y + self.L_H_cellule,
                    fill = "white", tags = ((lig, col), "vie"))

                #Affichage infos de comptage
                self.Var_population.set(len(self.dic_cell_live))

    def clic_droit_cell(self, event):
        '''
        Suppression d'une cellule:
            - Supprimer la cellule de la grille
            - Supprimer la clé de la cellule de <dic_cell_live>
        '''
        #Suppression de la cellule sur la grille
        x, y, lig, col = self.coords_lig_col(event)
        self.Grille.delete((lig, col))

        #Suppression de la cellule du dictionnaire des cellules en vie
        if (lig, col) in self.dic_cell_live:
            del self.dic_cell_live[(lig, col)]

        self.Var_population.set(len(self.dic_cell_live))

    def clic_gauche_listbox(self, event):
        '''
        - Lire le nom du motif sélectionné dans la listbox
        - Initialiser les données dictionnaire correspondantes au motif
        - Re-initialiser la grille et les paramètres
        '''
        index = self.Lstbox.curselection()
        cle = self.Lstbox.get(index)
        self.Var_Saisie.set(cle)

        if cle in self.dic_motifs:
            self.L_H_cellule = self.dic_motifs.get(cle)[0]
            self.Var_L_cell.set(self.L_H_cellule)
            self.grille_reinit()
            self.dic_cell_live = dict(self.dic_motifs.get(cle)[2])
            self.Var_ralentir.set(self.dic_motifs.get(cle)[3])

            for lig, col in self.dic_cell_live.keys():
                x = (col * self.L_H_cellule)
                y = (lig * self.L_H_cellule)
                self.Grille.create_rectangle(x, y, x + self.L_H_cellule, y + self.L_H_cellule,
                    fill = "white", tags = ((lig, col), "vie"))

            self.Var_population.set(len(self.dic_cell_live))
            self.Spin_L_cell.configure(state = DISABLED)
            self.Grille.configure(bg = "black")

            if self.traitement_en_cours:
                self.Grille.itemconfigure("lignes", fill = "black")
            else:
                self.Grille.itemconfigure("lignes", fill = "grey50")

    def double_clic_gauche_listbox(self, event):
        '''
        - Lire le nom du motif sélectionné dans la listbox
        - Supprimer le motif dans le dictonnaire et dans la listbox
        '''
        index = self.Lstbox.curselection()
        cle = self.Lstbox.get(index)
        msg1 = "Attention! vous aller supprimer le motif <" + cle + ">"

        if askyesno("Jeu de la vie - Suppression du motif", msg1, default = "no", icon = "warning"):
            del self.dic_motifs[cle]
            self.Var_Saisie.set("")
            self.Grille.delete("vie")

            if sys.version_info[0] == 3:
                fic_motifs = "JDV_Motifs_V3.pickle"
            else:
                fic_motifs = "JDV_Motifs_V2.pickle"

            fic_JDV = open(fic_motifs, "wb")
            pickle.dump(self.dic_motifs, fic_JDV)
            fic_JDV.close()
            self.Lstbox.delete(index)

    def souris_survol(self, event):
        '''
        Afficher les coordonnées ligne/colonne de la souris
        '''
        x, y, lig, col = self.coords_lig_col(event)

        if lig < self.nb_cellules and col < self.nb_cellules:
            self.Var_coord.set("Lig:%d  Col:%d" %(lig, col))

    def entree_saisie(self, event):
        '''
        - Lire le nom du motif dans la zone de saisie
        - Sauvegarder les paramètres dans le dictionnaire <self.dic_motifs>
        - Sauvegarder le dictionnaire des motifs dans la sauvegarde Pickle
        '''
        nom_motif = self.Var_Saisie.get()

        if nom_motif:
            if nom_motif in self.dic_motifs:
                msg1 = "L'intitulé du motif <" + nom_motif + "> existe déjà\n"
                msg2 = "Voulez vous le remplacer?"

                if not askyesno("Jeu de la vie - Sauvegarde du motif", msg1 + msg2, default = "no", icon = "warning"):
                    self.Var_Saisie.set("")
                    return
                else:
                    del self.dic_motifs[nom_motif]

            #Sauvegarde des motifs
            self.dic_motifs.setdefault(nom_motif, [self.L_H_cellule, self.nb_cellules,
                self.dic_cell_live, self.Var_ralentir.get()])

            if sys.version_info[0] == 3:
                fic_motifs = "JDV_Motifs_V3.pickle"
            else:
                fic_motifs = "JDV_Motifs_V2.pickle"

            fic_JDV = open(fic_motifs, "wb")
            pickle.dump(self.dic_motifs, fic_JDV)
            fic_JDV.close()
            self.Lstbox.delete(0, END)  #RAZ zone Listbox
            self.Var_Saisie.set("")     #RAZ zone de saisie
            cles = sorted(C.dic_motifs.keys())

            for cle in cles:
                C.Lstbox.insert(END, cle)

        else:
            msg1 = "Dans la zone de saisie, veuillez indiquer le titre du motif à sauvegarder."
            showinfo("Jeu de la vie - Sauvegarde du motif", msg1, icon = "warning")

    def spin_ralentir(self):
        '''
        - Restaurer la valeur initiale du widget <spin_accelerer>
        - Si affichage manuel => modification des paramètres
        '''
        self.Var_accelerer.set(1)

        if self.Spin_ralentir.get() == "Manuel":
            self.Var_Demarrer.set('Suite...')
            self.Demarrer.configure(state = NORMAL)

    def spin_accelerer(self):
        '''
        Restaurer la valeur initiale du widget <spin_ralentir>
        '''
        self.Var_ralentir.set(1)

    def bouton_demarrer(self):
        '''
        Lancer le calcul des générations.
        '''
        if self.Spin_ralentir.get() == "Manuel":
            self.traitement_en_cours = False
            self.Var_duree.set("%.3f" % 0)
            self.debut = time.time()    #Top début
            self.Var_Demarrer.set('Suite...')
            self.Demarrer.configure(state = NORMAL)
        else:
            self.traitement_en_cours = True
            self.Demarrer.configure(state = DISABLED)
            self.Spin_L_cell.configure(state = DISABLED)
            self.Var_Demarrer.set('Démarrer')
            self.ImportMotifs.configure(state = DISABLED)

        if self.L_H_cellule > 1 :
            self.Grille.itemconfigure("lignes", fill = "black")

        self.generations()

    def bouton_arreter(self):
        '''
        - Modifier le flag pour arret du traitement
        - Mettre les boutons et widgets actifs
        '''
        self.traitement_en_cours = False
        self.Spin_L_cell.configure(state = "readonly")
        self.Demarrer.configure(state = NORMAL)
        self.ImportMotifs.configure(state = NORMAL)
        self.Var_Demarrer.set('Démarrer')
        self.Grille.itemconfigure("lignes", fill = "grey50")
        self.Grille.configure(bg = "black")

    def bouton_import_motifs(self):
        '''
        Importation des motifs correspondants à la norme "Life 1.05".
         '''
        fic_motif = askopenfile(initialdir = self.chemin_motifs,
            filetypes =[( "Fichiers MOTIFS ", (".LIF", ".lif"))],
            defaultextension = ".LIF", title = "Lire un Motif", mode = "r")

        if fic_motif:
            #Réinitialisation par défaut de la grille
            self.L_H_cellule = 15
            self.Var_L_cell.set(self.L_H_cellule)
            self.Spin_L_cell.configure(state = DISABLED)
            self.grille_reinit()

            #Coordonnées pour centrage du motif
            x_centre = y_centre = int(self.nb_cellules / 2)

            #Initialisation par défaut si la ligne #P":(Position x,y) est absente du fichier
            x = y = x_pos = self.L_H_cellule * 10
            nomfic = os.path.splitext(os.path.split(fic_motif.name)[1])[0]
            infos = "Nom du fichier : " + nomfic + "\n"

            #Traitement Life 1.05
            test = True     #Témoin lecture 1ère ligne

            for ligne in fic_motif:
                ligne = ligne.rstrip("\r\n")

                #Lecture de la 1ère ligne
                if test:
                    if ligne == "#Life 1.05":
                        infos += ligne[1:] + "\n"
                        test = False
                        continue
                    else:
                        msg = "ERREUR : Ce motif n'est pas un fichier <Life 1.05> "
                        showinfo("Jeu de la vie - Importation des motifs", msg, icon = "warning")
                        return

                #Lecture des lignes 2 à n
                #D: Description infos - #N: Nom du motif - #R: #Règle
                if ligne[:2] in("#D", "#N", "#R"):
                    infos += ligne[2:] + "\n"

                elif ligne[:2] == "#P":   #Position x,y (par rapport au centre de la grille)
                    pos = ligne[2:].split(" ")
                    x_pos = (x_centre + int(pos[1])) * self.L_H_cellule
                    x = x_pos
                    y = (y_centre + int(pos[2])) * self.L_H_cellule

                elif ligne[:1] != "#":    #Cellule morte = "."   Cellule en vie = "*"
                    if len(ligne) > 0:
                        for car in ligne:
                            if car == ".":
                                x += self.L_H_cellule
                                continue

                            if car == "*":
                                (lig, col) = (y/self.L_H_cellule, x/self.L_H_cellule)
                                self.dic_cell_live.setdefault((lig, col))
                                self.Grille.create_rectangle(x, y, x + self.L_H_cellule, y + self.L_H_cellule,
                                    fill = "white", tags = ((lig, col), "vie"))
                                x += self.L_H_cellule

                        x = x_pos
                        y += self.L_H_cellule

            #Affichage infos et comptage
            showinfo("Jeu de la vie - Importation des motifs", infos, icon = "info")
            self.Var_population.set(len(self.dic_cell_live))

    def generations(self):
        '''
        - Examen de chaque cellule en vie.
        - Examen et comptage des voisines de chaque cellule en vie.
        - Décision vie/mort et ecriture dans <self.dic_cell_live_t1> selon décision
        '''
        #Si une cellule en vie est sur un bord ==> diminution taille cellule de 1 pixel
        self.zoom()

        #Examen de chaque cellule en vie
        for lig, col in self.dic_cell_live.keys():
            self.dic_examen.setdefault((lig, col))

            #Comptage des cellules voisines de la cellule en vie
            cpt_cell_en_vie = self.scan_cell_voisines(lig, col, True)
            self.decision_vie_mort(cpt_cell_en_vie, lig, col)

        #Examen des cellules voisines de chaque cellule en vie
        for lig, col in self.dic_cell_voisines.keys():
            if not (lig, col) in self.dic_examen:
                self.dic_examen.setdefault((lig, col))
                cpt_cell_en_vie = self.scan_cell_voisines(lig, col, False)
                self.decision_vie_mort(cpt_cell_en_vie, lig, col)

        self.cpt_gener += 1
        self.Var_gener.set(self.cpt_gener)
        self.Var_population.set(len(self.dic_cell_live_t1))
        self.Grille.delete("vie")  #Suppression des cellules en vie au temps "t"

        #Création des cellules en vie au temps "t+1"
        for lig, col in self.dic_cell_live_t1:
            x = (col * self.L_H_cellule)
            y = (lig * self.L_H_cellule)
            self.Grille.create_rectangle(x, y, x + self.L_H_cellule, y + self.L_H_cellule,
                fill = "white", tags = ((lig, col), "vie"))

        #La génération "t+1" devient la génération "t"
        self.dic_cell_live = dict(self.dic_cell_live_t1)
        self.dic_cell_live_t1 = {}
        self.dic_examen = {}
        self.dic_cell_voisines = {}

        #Si aucune cellule en vie: fin du traitement et sortie de boucle
        if not self.dic_cell_live:
            self.bouton_arreter()
            return

        #Si affichage manuel
        if self.Spin_ralentir.get() == "Manuel":
            return

        #Rafraichissement écran et boucle Tk.after
        if self.traitement_en_cours:
            self.Var_duree.set("%.3f" % (time.time() - self.debut))

            if self.frequence_affich >= self.Var_accelerer.get():
                self.frequence_affich = 1
                self.Grille.after(self.Spin_ralentir.get(), self.generations)
            else:
                self.frequence_affich += 1
                self.Grille.after(0, self.generations)

    def scan_cell_voisines(self, lig, col, test):
        '''
        Recherche des cellules voisines et comptage des cellules en vie.
        Les clés des cellules voisines sont stockées dans <self.dic_cell_voisines>
        Paramètre <test>:
            - True si on recherche les voisines des cellules en vie
            - False si on recherche les voisines des voisines des cellules en vie
        '''
        cpt_cell_en_vie = 0   #Compteur cellules voisines et en vie

        for voisine in ((lig - 1, col - 1), #Nord Ouest
                        (lig - 1, col),     #Nord
                        (lig - 1, col + 1), #Nord Est
                        (lig,     col - 1), #Ouest
                        (lig,     col + 1), #Est
                        (lig + 1, col - 1), #Sud Ouest
                        (lig + 1, col),     #Sud
                        (lig + 1, col + 1)):#Sud Est

            if test:
                self.dic_cell_voisines.setdefault(voisine)

            #Si la cellule voisine est en vie
            if voisine in self.dic_cell_live:
                cpt_cell_en_vie += 1

        return cpt_cell_en_vie

    def decision_vie_mort(self, cpt_cell_en_vie, lig, col):
        '''
        Application des règles de vie ou de mort:
        - 0 ou 1 cellule voisine  en vie = mort par isolement
        - 4 à 8 cellules voisines en vie = mort par surpopulation
          Dans ces cas la cellule n'est pas écrite dans <dic_cell_live_t1>
         '''
        #2 cellules voisines en vie = survie (pas de changement)
        if cpt_cell_en_vie == 2:
            #Si la cellule était en vie au temps T
            if (lig, col) in self.dic_cell_live:
                self.dic_cell_live_t1.setdefault((lig, col))

        #3 cellules voisines en vie = survie ou naissance
        elif cpt_cell_en_vie == 3:
            self.dic_cell_live_t1.setdefault((lig, col))

    def zoom(self):
        '''
        Si une cellule atteint un bord :
            - Diminuer taille cellule de 1 pixel pour augmenter le nombre de cellules
            - Les coordonnées de chaque cellule sont recalculées
         '''
        bord = False
        nb_cellules = self.nb_cellules - 1     #Pour comptage de 0 à n

        #Une cellule en vie se trouve-elle sur un bord?
        for lig, col in self.dic_cell_live.keys():

            if lig == 0 or lig == nb_cellules or col == 0 or col == nb_cellules:
                bord = True
                break

        #Zoom
        if bord:
            #Arret si taille de la cellule = 0
            if (self.L_H_cellule - 1) == 0:
                self.bouton_arreter()
                return

            #Diminution de la taille des cellules par pas de -1 pixel
            old_nb_cellules = self.nb_cellules
            increment = 0

            while increment == 0:
                self.L_H_cellule -= 1
                self.nb_cellules = int(self.L_H_grille / self.L_H_cellule)
                increment = int((self.nb_cellules - old_nb_cellules) / 2)
            self.Var_L_cell.set(str(self.L_H_cellule))
            self.grille_dessin()

            #Si taille de la cellule = 1  ==> modif couleurs pour visibilité
            if self.L_H_cellule == 1:
                self.Grille.configure(bg = "grey")
                self.Grille.itemconfigure("vie", fill = "black")
                self.Grille.itemconfigure("lignes", fill = "grey")
            else:
                self.Grille.itemconfigure("lignes", fill = "black")

            #Calcul des nouvelles coordonnées des cellules en vie de la génération "t"
            lst_dic_cell_live_cles = self.dic_cell_live.keys()
            self.dic_cell_live = {} #RAZ

            for cle in lst_dic_cell_live_cles:
                lig = cle[0] + increment
                col = cle[1] + increment
                self.dic_cell_live.setdefault((lig, col))
                x = (col * self.L_H_cellule)
                y = (lig * self.L_H_cellule)
                self.Grille.create_rectangle(x, y, x + self.L_H_cellule, y + self.L_H_cellule,
                    fill = "white", tags = ((lig, col), "vie"))

            #Calcul des nouvelles coordonnées des cellules de la génération "t+1"
            lst_dic_cell_live_t1_cles = self.dic_cell_live_t1.keys()
            self.dic_cell_live_t1 = {}  #RAZ

            for lig, col in lst_dic_cell_live_t1_cles:
                lig += increment
                col += increment
                self.dic_cell_live_t1.setdefault((lig, col))

    def format_milliers(self, nb, sep = " "):
        '''
        Formatage pour séparation par milliers
        '''
        if len(nb) < 4:
            return nb
        else:
            return self.format_milliers(nb[:-3]) + sep + nb[-3:]

    def appli_Tk(self):
        '''
        Créer les objets graphiques Tkinter
        '''
        self.Ecran0 = Tk()
        self.Ecran0.title("Jeu de la vie")
        self.Ecran0.geometry("+0+0")
        self.Ecran0.resizable(0, 0)

#-o-o-o-o   Création des Frames conteneurs
        self.Frame_1 = Frame(self.Ecran0)
        self.Frame_2 = Frame(self.Ecran0)
        self.Frame_3 = Frame(self.Ecran0)

        self.Frame_1.grid(row = 1, column = 0, sticky = NW)
        self.Frame_2.grid(row = 1, column = 1, sticky = NW)
        self.Frame_3.grid(row = 1, column = 2, sticky = NW)

#-o-o-o-o   Création des widgets de self.Frame_1
        self.Var_Saisie = StringVar()
        self.Lbl_Motifs = LabelFrame(self.Frame_1, text = "Motifs", font = self.font1)

        #Création Listbox zone de séléction des motifs
        self.Lstbox = Listbox(self.Lbl_Motifs, selectmode = SINGLE, width = 24,
            height = 40)

        #Création Scrollbar Listbox
        self.Bar_Listbox = Scrollbar(self.Lbl_Motifs)
        self.Bar_Listbox.configure(command=self.Lstbox.yview)
        self.Lstbox.configure(yscrollcommand=self.Bar_Listbox.set)
        self.Bar_Listbox.pack(side = RIGHT, fill = Y)

        #Création saisie "nom_motif nouveau motif"
        self.Ent_Saisie = Entry(self.Lbl_Motifs, width = 24,
            textvariable = self.Var_Saisie, takefocus = False)

        self.Lbl_Motifs.pack(padx = 8, pady = 8)
        self.Lstbox.pack()
        self.Ent_Saisie.pack(pady = 4)

#-o-o-o-o   Création des widgets de self.Frame_2
        self.Grille = Canvas(self.Frame_2, width = 0, height = 0, bg = "black")
        self.Grille.pack(pady = 4)

#-o-o-o-o   Création des widgets de self.Frame_3
        self.Var_duree      = StringVar()
        self.Var_gener      = IntVar()
        self.Var_population = IntVar()
        self.Var_Nb_cell_LH = IntVar()
        self.Var_nb_totcell = IntVar()
        self.Var_coord      = IntVar()
        self.Var_L_cell     = IntVar()
        self.Var_ralentir   = StringVar()
        self.Var_accelerer  = IntVar()
        self.Var_L_cell.set(self.L_H_cellule)

        #Création du label "Durée"
        self.Lbl_Duree = Label(self.Frame_3, textvariable = self.Var_duree,
            width = 8, anchor = E, relief = "groove", fg = "green", bg = "black",
            font = "Arial 16 bold")

        self.LbF_infos      = LabelFrame(self.Frame_3, text = " Infos ", font = self.font1)
        self.LbF_Gener      = LabelFrame(self.LbF_infos, text = "Générations", font = self.font2)
        self.LbF_Population = LabelFrame(self.LbF_infos, text = "Population", font = self.font2)
        self.LbF_Nb_cell_LH = LabelFrame(self.LbF_infos, text = "Nb cellules L/H", font = self.font2)
        self.LbF_Nb_totcell = LabelFrame(self.LbF_infos, text = "Nb Total cellules", font = self.font2)
        self.LbF_Coord      = LabelFrame(self.LbF_infos, text = "Coordonnées", font = self.font2)
        self.Lbl_sep1       = Label(self.Frame_3)
        self.LbF_actions    = LabelFrame(self.Frame_3, text = " Actions ", font = self.font1)
        self.LbF_L_cell     = LabelFrame(self.LbF_actions, text = "Largeur cellule", font = self.font2)
        self.LbF_ralentir   = LabelFrame(self.LbF_actions, text = "Ralentir", font = self.font2)
        self.LbF_accelerer  = LabelFrame(self.LbF_actions, text = "Accélérer", font = self.font2)
        self.Lbl_sep2       = Label(self.LbF_actions)

        #Création du label "Générations"
        self.Lbl_Gener = Label(self.LbF_Gener, textvariable = self.Var_gener)
        #Création du label "Population"
        self.Lbl_Population = Label(self.LbF_Population, textvariable = self.Var_population)
        #Création du label "Nb cellules L/H"
        self.Lbl_Nb_cell_LH = Label(self.LbF_Nb_cell_LH, textvariable = self.Var_Nb_cell_LH)
        #Création du label "Nb total de cellules"
        self.Lbl_Nb_totcell = Label(self.LbF_Nb_totcell, textvariable = self.Var_nb_totcell)
        #Création du label "Coordonnées"
        self.Lbl_Coord = Label(self.LbF_Coord, textvariable = self.Var_coord)

        #Création du Spinbox largeur cellule
        self.Spin_L_cell = Spinbox(self.LbF_L_cell, from_ = 1, to_ = 40,
            increment = 1, textvariable = self.Var_L_cell, width = 10,
            relief = "groove", state = "readonly", command = self.grille_reinit)
        #Création du Spinbox Ralentir
        valeurs = ("1","10","30","50","100","200","300","400","500","1000","2000", "Manuel")
        self.Spin_ralentir = Spinbox(self.LbF_ralentir, values = valeurs,
            width = 10, textvariable = self.Var_ralentir, relief = "groove",
            wrap = "true", state = "readonly", command = self.spin_ralentir)
        #Création du Spinbox Accelerer
        self.Spin_accelerer = Spinbox(self.LbF_accelerer, from_ = 1, to_ = 10,
            width = 10, textvariable = self.Var_accelerer, relief = "groove",
            wrap = "true", state = "readonly", command = self.spin_accelerer)

        #Création des boutons
        self.Var_Demarrer = StringVar()
        self.Demarrer = Button(self.LbF_actions, textvariable = self.Var_Demarrer,
            bg = "light yellow", width = 14, takefocus = False,
            command = self.bouton_demarrer)
        self.Arreter = Button(self.LbF_actions, text = 'Arreter',
            bg = "light yellow", width = 14, takefocus = False,
            command = self.bouton_arreter)
        self.ImportMotifs = Button(self.LbF_actions, text = 'Import Motifs',
            bg = "light yellow", width = 14, takefocus = False,
            command = self.bouton_import_motifs)
        self.Quitter = Button(self.LbF_actions, text = 'Quitter', bg = "#993366",
            fg = "white", width = 14, takefocus = False,
            command = self.Ecran0.destroy)

        self.Lbl_Duree.pack(padx = 4, pady = 8)
        self.LbF_infos.pack()
        self.LbF_Gener.pack(padx = 4, expand = YES, fill = X)
        self.Lbl_Gener.pack(padx = 4, expand = YES, fill = X)
        self.LbF_Population.pack(padx = 4, expand = YES, fill = X)
        self.Lbl_Population.pack(padx = 4, expand = YES, fill = X)
        self.LbF_Nb_cell_LH.pack(padx = 4, expand = YES, fill = X)
        self.Lbl_Nb_cell_LH.pack(padx = 4, expand = YES, fill = X)
        self.LbF_Nb_totcell.pack(padx = 4, expand = YES, fill = X)
        self.Lbl_Nb_totcell.pack(padx = 4, expand = YES, fill = X)
        self.LbF_Coord.pack(padx = 4, pady = 4,expand = YES, fill = X)
        self.Lbl_Coord.pack(padx = 4, expand = YES, fill = X)
        self.Lbl_sep1.pack(pady = 8)
        self.LbF_actions.pack()
        self.LbF_L_cell.pack(padx = 4, expand = YES, fill = X)
        self.Spin_L_cell.pack(padx = 4, pady = 4, expand = YES, fill = X)
        self.LbF_ralentir.pack(padx = 4, expand = YES, fill = X)
        self.Spin_ralentir.pack(padx = 4, pady = 4, expand = YES, fill = X)
        self.LbF_accelerer.pack(padx = 4, expand = YES, fill = X)
        self.Spin_accelerer.pack(padx = 4, pady = 4, expand = YES, fill = X)
        self.Lbl_sep2.pack()
        self.Demarrer.pack(pady = 4)
        self.Arreter.pack(pady = 4)
        self.ImportMotifs.pack(pady = 4)
        self.Quitter.pack(padx = 4, pady = 20)

#-o-o-o-o   Activation des évenements
        self.Grille.bind("<Button-1>", self.clic_gauche_cell)
        self.Grille.bind("<Button-3>", self.clic_droit_cell)
        self.Grille.bind("<Motion>", self.souris_survol)
        self.Lstbox.bind("<ButtonRelease-1>", self.clic_gauche_listbox)
        self.Lstbox.bind("<Double-Button-1>", self.double_clic_gauche_listbox)
        self.Ent_Saisie.bind("<Return>", self.entree_saisie)

if __name__ == '__main__':
    C = Grille()
    C.appli_Tk()

    #Ajustement dimension de la grille en fonction de la taille et résolution de l'écran
    C.L_H_grille = C.Ecran0.winfo_screenheight() - C.H_appli_diff
    C.Grille.configure(width = C.L_H_grille, height = C.L_H_grille)
    C.nb_cellules = int(C.L_H_grille / C.L_H_cellule)      #Nombre de cellules par ligne/colonne

    #Dessin de la grille
    C.grille_dessin()

    #Chargement du dictionnaire des motifs
    if sys.version_info[0] == 3:
        fic_motifs = "JDV_Motifs_V3.pickle"
    else:
        fic_motifs = "JDV_Motifs_V2.pickle"

    if os.path.exists(fic_motifs):
        fic_JDV = open(fic_motifs, "rb")
        C.dic_motifs = pickle.load(fic_JDV)
        fic_JDV.close()
        cles = sorted(C.dic_motifs.keys())

        for cle in cles:
            C.Lstbox.insert(END, cle)
    else:
        C.dic_motifs = {}

    #Boucle de traitement des évenements
    C.Ecran0.mainloop()

