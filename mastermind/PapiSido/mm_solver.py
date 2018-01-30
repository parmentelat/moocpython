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
args = parser.parse_args()

with open("mastermind.jnl", "w", encoding='utf-8')as journal:
    jeu = mm.Mastermind(journal, args.alphabet, int(args.number))
    jeu.partie(0, 1)

