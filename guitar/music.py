#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Une variation autour de 'gamme.py' initialement écrite par Karduin

J'avais commencé par modifier son code 
mais il y a vraiment beaucoup de différences 
et je préfère créer un nouveau module

"""


class Solfege:

    # a cscale is a chromatic scale; it contains all 12 notes
    cscales = {'en-sharp':
               ["C", "C♯", "D", "D♯", "E", "F",
                "F♯", "G", "G♯", "A", "A♯", "B"],
               'en-flat':
               ["C", "D♭", "D", "E♭", "E", "F",
                "G♭", "G", "A♭", "A", "B♭", "B"],
               'fr-diese':
               ["do", "do♯", "ré", "ré♯", "mi", "fa", "fa♯",
                "sol", "sol♯", "la", "la♯", "si"],
               'fr-bemol':
               ["do", "ré♭", "ré", "mi♭", "mi", "fa", "sol♭",
                "sol", "la♭", "la", "si♭", "si"],
               }

    def __init__(self, lang=None):
        # use english sharp by default
        lang = lang if lang is not None else 'en-sharp'
        self.cscale = self.cscales[lang]

    def index(self, note, cscale=None):
        """
        return an index between 0 and 12 for a note in letter
        also remembers the language where the note was found

        if cscale is specified, then only this cscale is searched

        otherwise returns None
        """
        # search only in cscale if specified
        search_cscales = (cscale,) if cscale is not None \
                         else self.cscales.values()
        for cscale in search_cscales:
            for n in cscale:
                if n == note:
                    search = cscale.index(note)
                    self.cscale = cscale
                    return search
        return None

    def name(self, inote):
        return self.cscale[inote]

    def interval(self, inote, amount):
        """
        Given a note and an amount (may be negative)
        return a tuple (index, name)

        Examples:

        s = Solfege()

        i = s.index('ré') -> 2
        s.interval(i, -4) -> (10, 'la♯')

        i = s.index('si♭') -> 10
        s.interval(i, 3) -> (1, 'ré♭')
        """
        if isinstance(inote, str):
            inote = self.index(inote)
        if inote is None:
            raise ValueError(f"Bad index {inote}")
        inote2 = (inote + amount) % 12
        note2 = self.name(inote2)
        return inote2, note2


class Gamme:

    majeure = (2, 2, 1, 2, 2, 2, 1)
    mineure = (2, 1, 2, 2, 1, 3, 1)

    def __init__(self, start, nom, intervalles=None):
        """
            Nom de la gamme, majeure, mineure, etc. et ces intervalles.
        """
        self.start = start
        self.nom = nom
        if 'maj' in nom:
            self.intervalles = self.majeure
        elif 'min' in nom:
            self.intervalles = self.majeure
        else:
            self.intervalles = intervalles
        ##
        self._scale = []  # Va contenir les notes de la gamme en lettres
        self._iscale = []  # les indices de la gamme par rapport à do
        self.solfege = Solfege()

    def inter(self):
        """
            Affichage des intervalles
        """
        for n in self.intervalles:
            print(("1ton" if n == 2 else "1/2ton") + ' ', end="")
        print()

    def _build(self):
        """
            Construction de la gamme
        """
        s = self.solfege

        i = s.index(self.start)
        self._scale.append(self.start)
        self._iscale.append(0)
        for valeur in self.intervalles:
            i, note = s.interval(i, valeur)
            self._scale.append(note)
            self._iscale.append(i)

    def scale(self):
        if not self._scale:
            self._build()
        return self._scale

    def iscale(self):
        if not self._iscale:
            self._build()
        return self._iscale


class Corde:

    def __init__(self, nom, gamme):
        """
            Le nom de la corde,
            caseNote contiendra le nom des notes,
            caseNumber contiendra le N° des cases
        """
        self.nom = nom
        self.gamme = gamme
        #
        self.solfege = Solfege()
        self.index = self.solfege.index(nom)
        ##
        self.notes = []
        self.indices = []

    def cases(self):

        for iscale in self.gamme.iscale():
            # l'index de la note par rapport à la corde
            self.indices.append((iscale - self.index) % 12)
            self.notes.append(self.solfege.name(iscale))


def main():

    import pygame
    #--------------- définition de la gamme ------------

    doM = Gamme('do', 'majeure')

    #--------------- définition des cordes --------------

    mi = Corde("E", doM)
    mi.cases()

    la = Corde("A", doM)
    la.cases()

    re = Corde("D", doM)
    re.cases()

    sol = Corde("G", doM)
    sol.cases()

    si = Corde("B", doM)
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

        items = ((mi, 150), (la, 120), (re, 95), (sol, 68), (si, 40), (mi, 12))

        for corde, height in items:
            for i in corde.indices:
                ecran.blit(dot, ((i * 90), height))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                continuer = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
