Jeu de la vie simple et graphique (tkinter) en python 3-------------------------------------------------------
Url     : http://codes-sources.commentcamarche.net/source/54104-jeu-de-la-vie-simple-et-graphique-tkinter-en-python-3Auteur  : sodawilDate    : 17/08/2013
Licence :
=========

Ce document intitulé « Jeu de la vie simple et graphique (tkinter) en python 3 » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Voici ma version du c&eacute;l&egrave;bre automate cellulaire Jeu De La Vie prog
ramm&eacute; en python dans sa version 3 (3.2.2 pour &ecirc;tre pr&eacute;cis).

<br />C'est une version simple, facile &agrave; comprendre (enfin il me semble^
^) et graphique (tkinter).
<br />Il est possible de modifier la taille de la gr
ille, la taille des cellules et l&#8217;attente entre chaque &eacute;tapes.
<br
 />Le programme poss&egrave;de aussi un bouton pour dessiner automatiquement le 
c&eacute;l&egrave;bre canon &agrave; planeur de Gosper.
<br /><a name='source-e
xemple'></a><h2> Source / Exemple : </h2>
<br /><pre class='code' data-mode='b
asic'>
from tkinter import *

def damier(): #fonction dessinant le tableau
 
   ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    
while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='bla
ck')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != 
height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
       
 c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée
 donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(ev
ent.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c
, fill='black')
    dico_case[x,y]=1

def click_droit(event): #fonction tuant
 la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
 
   x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_recta
ngle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0

def change_vit(event
): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global v
itesse
    vitesse = int(eval(entree.get()))
    print(vitesse)

def canon()
: #fonction dessinant le célèbre canon à planeur de Bill Gosper
    dico_case[0
*c,5*c]=1
    dico_case[0*c,6*c]=1
    dico_case[1*c,5*c]=1
    dico_case[1*c
,6*c]=1
    dico_case[10*c,5*c]=1
    dico_case[10*c,6*c]=1
    dico_case[10*
c,7*c]=1
    dico_case[11*c,4*c]=1
    dico_case[11*c,8*c]=1
    dico_case[12
*c,3*c]=1
    dico_case[12*c,9*c]=1
    dico_case[13*c,3*c]=1
    dico_case[1
3*c,9*c]=1
    dico_case[14*c,6*c]=1
    dico_case[15*c,4*c]=1
    dico_case[
15*c,8*c]=1
    dico_case[16*c,5*c]=1
    dico_case[16*c,6*c]=1
    dico_case
[16*c,7*c]=1
    dico_case[17*c,6*c]=1
    dico_case[20*c,3*c]=1
    dico_cas
e[20*c,4*c]=1
    dico_case[20*c,5*c]=1
    dico_case[21*c,3*c]=1
    dico_ca
se[21*c,4*c]=1
    dico_case[21*c,5*c]=1
    dico_case[22*c,2*c]=1
    dico_c
ase[22*c,6*c]=1
    dico_case[24*c,1*c]=1
    dico_case[24*c,2*c]=1
    dico_
case[24*c,6*c]=1
    dico_case[24*c,7*c]=1
    dico_case[34*c,3*c]=1
    dico
_case[34*c,4*c]=1
    dico_case[35*c,3*c]=1
    dico_case[35*c,4*c]=1    
   
 go()

def go():
    &quot;démarrage de l'animation&quot;
    global flag
 
   if flag ==0:
        flag =1
        play()
        
def stop():
    &qu
ot;arrêt de l'animation&quot;
    global flag    
    flag =0
    
def play(
): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
 
   global flag, vitesse
    v=0
    while v!= width/c:
        w=0
        w
hile w!= height/c:
            x=v*c
            y=w*c
            
        
    # cas spéciaux:
            # les coins
            if x==0 and y==0: #coi
n en haut à gauche
                compt_viv=0
                if dico_case[x,
 y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y
]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]=
=1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            elif x==0 and y==int(height-c): #coin en bas à gauche
           
     compt_viv=0
                if dico_case[x, y-c]==1:
                    
compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    co
mpt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_
viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width
-c) and y==0: #coin en haut à droite
                compt_viv=0
             
   if dico_case[x-c, y]==1:
                    compt_viv+=1
                i
f dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if 
dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_et
at[x, y]=compt_viv
            elif x==int(width-c) and y==int(height-c): #coin
 en bas à droite
                compt_viv=0
                if dico_case[x-c,
 y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y
]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1
:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

                
            # cas spéciaux:
            # les bords du tablea
u (sans les coins)    
            elif x==0 and 0&lt;y&lt;int(height-c): # bor
d de gauche
                compt_viv=0
                if dico_case[x, y-c]==
1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:

                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
  
                  compt_viv+=1
                if dico_case[x+c, y]==1:
      
              compt_viv+=1
                if dico_case[x+c, y+c]==1:
        
            compt_viv+=1
                dico_etat[x, y]=compt_viv
           
 elif x==int(width-c) and 0&lt;y&lt;int(height-c): # bord de droite
           
     compt_viv=0
                if dico_case[x-c, y-c]==1:
                  
  compt_viv+=1
                if dico_case[x-c, y]==1:
                    co
mpt_viv+=1
                if dico_case[x-c, y+c]==1:
                    comp
t_viv+=1
                if dico_case[x, y-c]==1:
                    compt_vi
v+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1

                dico_etat[x, y]=compt_viv
            elif 0&lt;x&lt;int(widt
h-c) and y==0: # bord du haut
                compt_viv=0
                if d
ico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_
case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_ca
se[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x
+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, 
y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=comp
t_viv
            elif 0&lt;x&lt;int(width-c) and y==int(height-c): # bord du b
as
                compt_viv=0
                if dico_case[x-c, y-c]==1:
   
                 compt_viv+=1
                if dico_case[x-c, y]==1:
       
             compt_viv+=1
                if dico_case[x, y-c]==1:
           
         compt_viv+=1
                if dico_case[x+c, y-c]==1:
             
       compt_viv+=1
                if dico_case[x+c, y]==1:
                 
   compt_viv+=1
                dico_etat[x, y]=compt_viv

            #cas g
énéraux
            #les cellules qui ne sont pas dans les bords du tableau
  
          else:
                compt_viv=0
                if dico_case[x-c, 
y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]
==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==
1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:

                    compt_viv+=1
                if dico_case[x, y+c]==1:
    
                compt_viv+=1
                if dico_case[x+c, y-c]==1:
      
              compt_viv+=1
                if dico_case[x+c, y]==1:
          
          compt_viv+=1
                if dico_case[x+c, y+c]==1:
            
        compt_viv+=1
                dico_etat[x, y]=compt_viv
               
 
            w+=1
        v+=1
    redessiner()
    if flag &gt;0: 
      
  fen1.after(vitesse,play)

        

def redessiner(): #fonction redessinan
t le tableau à partir de dico_etat
    can1.delete(ALL)
    damier()
    t=0

    while t!= width/c:
        u=0
        while u!= height/c:
            x
=t*c
            y=u*c
            if dico_etat[x,y]==3:
                dico
_case[x,y]=1
                can1.create_rectangle(x, y, x+c, y+c, fill='black'
)
            elif dico_etat[x,y]==2:
                if dico_case[x,y]==1:
 
                   can1.create_rectangle(x, y, x+c, y+c, fill='black')
        
        else:
                    can1.create_rectangle(x, y, x+c, y+c, fill='w
hite')
            elif dico_etat[x,y]&lt;2 or dico_etat[x,y]&gt;3:
          
      dico_case[x,y]=0
                can1.create_rectangle(x, y, x+c, y+c, fi
ll='white')
            u+=1
        t+=1
        
    
#les différentes va
riables:

# taille de la grille
height = 400
width = 400

#taille des cell
ules
c = 10

#vitesse de l'animation (en réalité c'est l'attente entre chaque
 étapes en ms)
vitesse=50

flag=0
dico_etat = {} #dictionnaire contenant le 
nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnai
re contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles s
ont respectivement mortes ou vivantes
i=0
while i!= width/c: #assigne une vale
ur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte 
^^)
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dic
o_case[x,y]=0
        j+=1
    i+=1

#programme &quot;principal&quot; 
fen1
 = Tk()

can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.
bind(&quot;&lt;Button-1&gt;&quot;, click_gauche)
can1.bind(&quot;&lt;Button-3&g
t;&quot;, click_droit)
can1.pack(side =TOP, padx =5, pady =5)

damier()

b1
 = Button(fen1, text ='Go!', command =go)
b2 = Button(fen1, text ='Stop', comma
nd =stop)
b1.pack(side =LEFT, padx =3, pady =3)
b2.pack(side =LEFT, padx =3, p
ady =3)
b3 = Button(fen1, text ='Canon planeur', command =canon)
b3.pack(side 
=LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind(&quot;&lt;Return&g
t;&quot;, change_vit)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.co
nfigure(text = &quot;Attente entre chaque étape (ms) :&quot;)
chaine.pack(side 
=RIGHT)

fen1.mainloop()
</pre>
<br /><a name='conclusion'></a><h2> Conclusi
on : </h2>
<br />Merci de laisser des commentaires constructifs
