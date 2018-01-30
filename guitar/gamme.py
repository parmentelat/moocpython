#!/usr/bin/env python
# -*- coding: utf-8 -*-
#



class gamme:

    def __init__(self, nom, intervalles):

        self.nom = nom
        self.intervalles = intervalles
        self.notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

    def inter(self):

        for valeur in self.intervalles:
            if valeur == 2:
                print("1 ton")
            else:
                print("1/2 ton")

    def tone(self, debut):

        idx = self.notes.index(debut)

        for valeur in self.intervalles:

            idx = idx + valeur
            if idx > 11 :
                idx = idx - 12

            print(self.notes[idx])


gamme1 = gamme('majeure', (0, 2, 2, 1, 2, 2, 2, 1))

print(gamme1.nom)
gamme1.inter()

gamme1.tone("C#")
