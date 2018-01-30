# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:08:54 2018

@author: francois.sidoroff
"""

import mastermind as mm
import argparse
parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--alphabet", action='store', default='ABCDEF',
                        help = 'alphabet: the symbols used for colors')
parser.add_argument("-n", "--number", action='store', default=4,
                        help="number of positions in the code")
parser.add_argument("-z", "--nbgames", action='store', default=10,
                        help="number of games to be played")
args = parser.parse_args()
with open("mm_stats.jnl", "w", encoding='utf-8')as journal:
    jeu = mm.Mastermind(journal, args.alphabet, int(args.number))
    nb_coups = ()
    nct = 0
    for i in range(int(args.nbgames)):
        nc = jeu.partie(1, 1)
        nb_coups += (nc,)
        nct += nc
    mean_nbc = nct/int(args.nbgames)
    bilan = f"------ finalement ------\n{nb_coups}, moy = {mean_nbc}"
    journal.write(bilan)
    print(bilan)
