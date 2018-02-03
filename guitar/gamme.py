#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

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

    def __init__(self, nom):
        """
            Le nom de la corde, case contiendra le nom des notes,
            caseNumber contiendra le N° des cases
        """
        self.nom = nom
        self.caseNote = ()
        self.caseNumber = ()

    def cases(self):

        caseInter = gamme1.intervalles[1:]

        # On met la gamme chromatique dans l'ordre des cases de la corde
        allCases = notes[notes.index(self.nom):] + notes[:notes.index(self.nom)]

        # On met la gamme diatonique dans l'ordre de la corde
        if self.nom in gamme1.myScale:

            idx  = gamme1.myScale.index(self.nom)

            self.caseNote = gamme1.myScale[idx:] + gamme1.myScale[:idx]

#            caseInter = caseInter[idx:] + caseInter[:idx]
#            print(caseInter)
#            print(allCases)

        # Liste des cases jouables
        for theNote in self.caseNote:

            self.caseNumber = self.caseNumber + (allCases.index(theNote),)






gamme1 = gamme('majeure', (0, 2, 2, 1, 2, 2, 2, 1))

print(gamme1.nom)
gamme1.inter()

gamme1.tone("C")
print(gamme1.myScale)
mi = corde("E")
mi.cases()
print(mi.caseNote)
print(mi.caseNumber)


