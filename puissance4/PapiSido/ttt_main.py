# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:25:50 2018

@author: franc
"""
import tictactoe as ttt

with open("tictactoe.jnl", "w", encoding='utf-8')as journal:
    journal.write("tictactoe par ttt_main\n")
    jeu = ttt.TicTacToe(journal, 3, 3)
    print(jeu.info()+"\n")
    jeu.new_partie((1, 1))
