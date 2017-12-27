# -*- coding: utf-8 -*-
"""
Implémentation du jeu "Puissance 4" en python (pas d'interface graphique, la
sortie se fait directement dans le terminal).

Pour lancer une partie, executer Puissance4(nl,nc),
avec nl et nc le nombre de lignes/colonnes de la grille (6x7 par défaut)

@author: Julien Higuet
"""
import os

class Puissance4():

    def __init__(self, nl=6, nc=7, jeton=('@', 'X')):
        """ Constructeur, crée la grille et lance une nouvelle partie"""
        self.nl = nl
        self.nc = nc
        self.jeton = jeton
        self.board = [['.' for i in range(nc)] for j in range(nl)]
        self.nouvellepartie(self.nl, self.nc, self.jeton)

    def __str__(self):
        """ Affiche la grille de jeu
        La première ligne permet de repérer chaque colonne.
        Les colonnes sont séparées par des espaces pour plus de lisibilité
        """
        board_str = ' '.join([str((i+1) % 10) for i in range(self.nc)]) + '\n'
        for i in range(self.nl):
            board_str += ' '.join(self.board[i]) + '\n'
        return board_str

    def coup(self, joueur, colonne):
        """ Joue le coup du joueur dans la colonne choisie.
        Retourne (False, 0) si le coup n'est pas valide (si la colonne
        est déjà remplie)
        Retourne (True, ligne) si le coup est valide, avec ligne la ligne dans
        laquelle se trouve le jeton jouée. Si le coup est valide,
        la méthode modifie self.board EN PLACE.
        """
        board_colonne = [ligne[colonne] for ligne in self.board]  # on extrait la colonne
        ligne = board_colonne.count('.')
        if ligne == 0:  # plus de '.' dans la ligne, elle est donc remplie
            return False, 0
        else:
            ligne = ligne - 1
            self.board[ligne][colonne] = self.jeton[joueur-1]
            return True, ligne

    def check_victoire(self, ligne, colonne, joueur):
        """ vérifie si le dernier coup joué, qui a placé le jeton
        de joueur en (ligne,colonne) permet de gagner.
        """
        pattern = self.jeton[joueur-1] * 4  # si on trouve jeton qui se suivent, c'est gagné

        if pattern in ''.join([l[colonne] for l in self.board]):  # on teste la colonne
            return True

        if pattern in ''.join(self.board[ligne]):  # on teste la ligne
            return True

        diag1 = []  # on teste une première diagonale ("nord-ouest" -> "sud-est")
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne-ligne+k)]
            except IndexError:
                pass
            else:
                diag1.append(char)
        diag1 = ''.join(diag1)
        if pattern in diag1:
            return True

        diag2 = []  # on teste une deuxième diagonale ("sud-ouest" -> "nord-est")
        for k in range(self.nl):
            try:
                char = self.board[k][(colonne+ligne-k)]
            except IndexError:
                pass
            else:
                diag2.append(char)
        diag2 = ''.join(diag2)
        if pattern in diag2:
            return True

        return False

    def nouvellepartie(self, nl=6, nc=7, jeton=('@', 'X')):
        """
        Fonction principale qui lance la partie.
        Par défaut, on utilise nl = 6 lignes et nc = 7 colonnes
        """
        os.system('clear')  # efface le terminal
        # affichage de la grille initiale
        print(self)

        victoire = False
        compteur = 0

        while not victoire and compteur < nc*nl:
            compteur += 1
            # Attention, pour l'affichage, on pare de joueur 1 et 2, mais pour
            # l'accès aux jetons, c'est jeton[0] et jeton[1]
            joueur = (compteur + 1) % 2 + 1
            while True:
                print(f"Joueur {joueur} ({self.jeton[joueur-1]}), c'est à toi!")
                colonne = input('Colonne jouée: ')
                # on vérifie que le numéro de colonne est valide
                if colonne not in {str(i+1) for i in range(self.nc)}:
                    os.system('clear')
                    print("Coup non valide!")
                    print(f"Il faut entrer un nombre entre 1 et {nc}!")
                    print(self)
                    continue
                # on vérifie que la colonne n'est pas déjà pleine
                colonne = int(colonne) - 1
                coupvalide, ligne = self.coup(joueur, colonne)
                if not coupvalide:
                    print(f"Plus de place en colonne {colonne+1}")
                    print(self)
                    continue
                # si c'est bon, on sort de la boucle
                break

            os.system('clear')
            print(self)

            if compteur > 6:  # on vérifie à partir du 7eme coup
                victoire = self.check_victoire(ligne, colonne, joueur)

        if victoire:
            print(f"Puissance 4, le Joueur {joueur} ({self.jeton[joueur-1]}) a gagné!")
        else:
            print("Match nul!")


if __name__ == '__main__':
    Puissance4()
