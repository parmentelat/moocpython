# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:42:48 2018

@author: franc
"""

import tkinter as tk
# import random
import tictactoe as ttt

bg_cmd = 'lightblue'


joueurs =[("humain",0),("ordinateur",1)]
coord = lgrid(3, 150, 50)


def go():
    tj1 = vj1.get()
    tj2 = vj2.get()
    print(f"go: {joueurs[tj1][0]} vs {joueurs[tj2][0]}")
    jeu = ttt.TicTacToe(journal, 3, 3)
    jeu.new_partie((tj1,tj2))

    
def lgrid(n,x0,dx):
    return list(range(x0,x0+n*dx,dx))


def paint_pion(g, nj, l, c):
    cx = coord[c]
    cy = coord[l]
    if nj == 0:
        g.create_line(cx+10, cy+10, cx-10, cx-10, width=4, fill='red')
        g.create_line(cx-10, cy+10, cx+10, cx-10, width=4, fill='red')
    else:
        g.create_oval(cx-10, cy-10, cx+10, cy+10, width=4, outline='blue')


def ini_graph(g):
    # print (lgrid(4, 125, 50))
    gx = lgrid(4, 125, 50)
    gy = gx[:]
    for i in gx:
        g.create_line(gx[0],i,gx[3],i)
        g.create_line(i, gx[0],i,gx[3])

    # paint_pion(g,0,1,1)    
    # paint_pion(g,1,1,0)    
        
# Création de la fenêtre principale (main window)
fenetre = tk.Tk()
fenetre.title('TicTacToe')

# inisize = définition de la taille
#sv_h = tk.StringVar()
#sv_h.set("3")
#sv_l = tk.StringVar()
#sv_l.set("3")
#inisize = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE, bg=bg_cmd)
#lbl_h = tk.Label(inisize, text='hauteur', bg=bg_cmd)
#lbl_h.pack(side=tk.LEFT)
#chxh = tk.Spinbox(inisize,from_=3,to=10,increment=1,textvariable=sv_h,width=5)
#chxh.pack(side = tk.LEFT,padx =10)
#lbl_l = tk.Label(inisize, text='largeur', bg=bg_cmd)
#lbl_l.pack(side = tk.LEFT)
#chxl = tk.Spinbox(inisize,from_=3,to=10,increment=1,textvariable=sv_l,width=5)
#chxl.pack(side = tk.LEFT, padx=10, pady=10)
#go1Btn = tk.Button(inisize, text='setsize', command=set_size)
#go1Btn.pack(side = tk.LEFT, padx=10, pady=10)
#inisize.pack(side=tk.TOP, padx=10, pady=10)

# panneau de contrôle
controle = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE, bg=bg_cmd)

lbl_j1 = tk.Label(controle, text='joueur1')
lbl_j1.pack(padx=10, pady=10)

vj1 = tk.IntVar()
vj1.set(0)
for qui, tj in joueurs:
    b = tk.Radiobutton(controle, text=qui, variable = vj1, value = tj)
    b.pack(anchor= tk.W)

lbl_j2 = tk.Label(controle, text='joueur1')
lbl_j2.pack(padx=10, pady=10)

vj2 = tk.IntVar()
vj2.set(0)
for qui, tj in joueurs:
    b = tk.Radiobutton(controle, text=qui, variable = vj2, value = tj)
    b.pack(anchor= tk.W)
    
goBtn = tk.Button(controle, text='Go', command=go)
goBtn.pack(padx=10, pady=10)
closeBtn = tk.Button(controle, text='close', command=fenetre.destroy)
closeBtn.pack(padx=10, pady=10)
controle.pack(side=tk.LEFT, padx=10, pady=10)

graph = tk.Canvas(fenetre, width=400, height=400, bg='white')
graph.pack(side=tk.RIGHT, padx=20, pady=20)
ini_graph(graph)

with open("tictactoe.jnl", "w", encoding='utf-8')as journal:
    journal.write("fenetre.mainloop()\n")
    fenetre.mainloop()
