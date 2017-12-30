class Puissance4:
    '''Une partie de Puissance 4'''
    
    SYMBOLES = ('.', '@', 'X', 'O', '+')
    
    _JOUEURS_MIN = 2
    _JOUEURS_MAX = 4
    
    def __init__(self, largeur=7, hauteur=6, nb_joueurs=2):
        '''Initialise une partie avec une grille vide.'''
        if largeur < 7 or hauteur < 6:
            raise ValueError(f'Dimension minimum 6 lignes x 7 colonnes : {hauteur}x{largeur}')
        if nb_joueurs < 2 or nb_joueurs > 4:
            raise ValueError(f'Le nombre de joueurs doit être entre' +
                f' {Puissance4._JOUEURS_MIN} et {Puissance4._JOUEURS_MAX} : {nb_joueurs}')
        self._grille = [[0 for _ in range(largeur)] for _ in range(hauteur)]
        self._largeur = largeur
        self._hauteur = hauteur
        self._nb_joueurs = nb_joueurs
        
        self._joueur_courant = 1
        self._partie_finie = False
        self._gagnant = None
        
        self._nb_coups = 0
        self._pions_par_colonne = [0] * largeur
    
    @property
    def largeur(self):
        '''Retourne la largeur de la grille.'''
        return self._largeur
    
    @property
    def hauteur(self):
        '''Retourne la hauteur de la grille.'''
        return self._hauteur
    
    @property
    def nb_joueurs(self):
        '''Retourne le nombre de joueurs.'''
        return self._nb_joueurs
    
    @property
    def joueur_courant(self):
        '''Retourne le numéro du joueur courant.
        
        Les numéros commencent à 1.'''
        return self._joueur_courant
    
    @property
    def partie_finie(self):
        '''Retourne True si la partie est terminée.
        
        La partie se termine quand un joueur a aligné 4 pions ou si la grille
        est pleine.
        '''
        return self._partie_finie
    
    @property
    def gagnant(self):
        '''Retourne le numéro du joueur gagnant.
        
        Si la partie n'est pas finie ou si personne n'a gagné, retourne None.
        '''
        return self._gagnant
    
    def jouer(self, colonne):
        '''Joue un coup dans la colonne donnée et retourne un booléen.
        
        Si le coup est invalide, retourne False.
        Sinon, place un pion pour le joueur courant et retourne True.
        '''
        if self.partie_finie or colonne <= 0 or colonne > self.largeur:
            return False
        col = colonne - 1
        lgn = self.hauteur - 1 - self._pions_par_colonne[col]
        if lgn < 0: # Colonne pleine
            return False
        
        self._grille[lgn][col] = self.joueur_courant
        self._pions_par_colonne[col] += 1
        self._nb_coups += 1
        if self._coup_gagnant(lgn, col):
            self._partie_finie = True
            self._gagnant = self.joueur_courant
        elif self._nb_coups == self.largeur * self.hauteur:
            self._partie_finie = True
        else:
            self._joueur_courant = self.joueur_courant % self.nb_joueurs + 1
        return True
    
    def _coup_gagnant(self, lgn, col):
        '''Retourne True si le pion aux coordonnées données fait partie d'un alignement de 4.'''
        joueur = self._grille[lgn][col]
        def est_valide(l, c):
            return (0 <= l < self.hauteur) and (0 <= c < self.largeur)
        def compter_pions(dl, dc):
            l, c = lgn + dl, col + dc
            compte = 0
            while est_valide(l, c) and self._grille[l][c] == joueur:
                compte += 1
                l, c = l + dl, c + dc
            return compte
        for dl, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
            if compter_pions(dl,dc) + compter_pions(-dl, -dc) + 1 == 4:
                return True
        return False

    def __str__(self):
        lst = [''.join(f'{str(i):2s}' for i in range(1, self.largeur + 1))]
        for row in self._grille:
            lst.append(''.join(f'{Puissance4.SYMBOLES[value]:2s}' for value in row))
        return '\n'.join(lst)



def jouer(largeur=7, hauteur=6, nb_joueurs=2):
    puiss = Puissance4(largeur, hauteur, nb_joueurs)
    while not puiss.partie_finie:
        print()
        print(puiss)
        print()
        joueur = puiss.joueur_courant
        colonne = int(input(f'Joueur {joueur} ({puiss.SYMBOLES[joueur]}), choisissez une colonne : '))
        puiss.jouer(colonne)
    
    print()
    print('La partie est finie.')
    if puiss.gagnant:
        print(f'Bravo joueur {puiss.gagnant}, vous avez gagné !')
    else:
        print('Match nul.')
