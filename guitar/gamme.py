#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pygame

notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

class gamme:

    def __init__(self, nom, intervalles):
        """
            Nom de la gamme, majeure, mineure, etc. et ces intervalles.
        """
        self.nom = nom
        self.intervalles = intervalles
        self.myScale = () # Va contenir les notes de la gamme en lettre

    def inter(self):
        """
            Affichage des intervalles
        """
        for valeur in self.intervalles:
            if valeur == 2:
                print("1 ton")
            else:
                print("1/2 ton")

    def tone(self, debut):
        """
            Construction de la gamme
        """
        idx = notes.index(debut) # index de la note de début

        for valeur in self.intervalles:

            idx = idx + valeur

            if idx > 11 : # Si j'arrive au bout du tuple je retourne au début
                idx = idx - 12 # Il doit y avoir plus pythonique...

            self.myScale = self.myScale + ( notes[idx],)

        self.myScale = self.myScale[:-1] # Je supprime la huitiéme note

class corde:

    def __init__(self, nom, toneUsed):
        """
            Le nom de la corde, case contiendra le nom des notes,
            caseNumber contiendra le N° des cases
        """
        self.nom = nom
        self.caseNote = ()
        self.caseNumber = ()
        self.startNote = ""
        self.toneUsed = toneUsed

    def cases(self):

        caseInter = self.toneUsed[1:]

        # On met la gamme chromatique dans l'ordre des cases de la corde
        allCases = notes[notes.index(self.nom):] + notes[:notes.index(self.nom)]

        for myItem in allCases:
            if myItem in self.toneUsed:
                self.startNote = myItem
                break

        # On met la gamme diatonique dans l'ordre de la corde
        idx  = self.toneUsed.index(self.startNote)
        self.caseNote = self.toneUsed[idx:] + self.toneUsed[:idx]

        # Liste des cases jouables
        for theNote in self.caseNote:
            self.caseNumber = self.caseNumber + (allCases.index(theNote),)

#--------------- définition de la gamme ------------

gamme1 = gamme('majeure', (0, 2, 2, 1, 2, 2, 2, 1))
gamme1.tone("C")

#--------------- définition des cordes --------------

mi = corde("E", gamme1.myScale)
mi.cases()

la = corde("A", gamme1.myScale)
la.cases()

re = corde("D", gamme1.myScale)
re.cases()

sol = corde("G", gamme1.myScale)
sol.cases()

si = corde("B", gamme1.myScale)
si.cases()

#--------------- Affichage --------------------------

pygame.init()

ecran = pygame.display.set_mode((1200, 200))
pygame.display.set_caption("Ze gamme")

fretboard = pygame.image.load("images/fretboard_12.png").convert_alpha()
dot = pygame.image.load("images/dot.png").convert_alpha()

continuer = True

while continuer:

    ecran.blit(fretboard, (50, 10))

    for c in mi.caseNumber:
        ecran.blit(dot, ((c * 90), 150))

    for c in mi.caseNumber:
        ecran.blit(dot, ((c * 90), 12))

    for c in la.caseNumber:
        ecran.blit(dot, ((c * 90), 120))

    for c in re.caseNumber:
        ecran.blit(dot, ((c * 90), 95))

    for c in sol.caseNumber:
        ecran.blit(dot, ((c * 90), 68))

    for c in si.caseNumber:
        ecran.blit(dot, ((c * 90), 40))



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

    pygame.display.flip()

pygame.quit()

