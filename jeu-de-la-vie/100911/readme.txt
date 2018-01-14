Le jeu de la vie----------------
Url     : http://codes-sources.commentcamarche.net/source/100911-le-jeu-de-la-vieAuteur  : lespinxDate    : 20/05/2015
Licence :
=========

Ce document intitulé « Le jeu de la vie » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Bien que le code &quot;Jeu de la vie&quot; soit dèjà présent plusieurs fois sur 
CCM/Codes-Sources, je poste à mon tour une nouvelle version.
<br />La particula
rité du &quot;Jeu de la vie&quot; est qu'il n'y a pas de joueurs!
<br />L'histo
rique et les règles du jeu sont très bien expliquées sur Wikipedia (automate cel
lulaire, jeu de la vie...)
<br />
<br />Infos:
<br />Compatible Python 2 et 3

<br />Testé avec Python 2.7.3 et Python 3.3.5 dans l'environnement Windows 7 6
4 bits avec un écran 23&quot; 1080x1920
<br />-- Ajout le 11/02/2015
<br />-- 
Modifié le 29/04/2015 : Optimisation du code et ajout de fonctionnalités.
<br /
>-- Modifié le 01/05/2015 : Correction d'un bug.
<br />-- Modifié le 17/05/2015
 : Ajout de fonctionnalité (Accélérer)
<br />
<br />Utilisation:
<br />En fon
ction de la taille et de la résolution de votre écran vous devrez, peut-être, ad
apter les valeurs par défaut qui déterminent la dimension de la grille.
<br />P
our cela, dans la section &quot;__init__&quot; vous interviendrez sur la variabl
e &quot;self.H_appli_diff&quot; (En pixels, estimation de la hauteur de l'écran 
- hauteur de la grille)
<br />La dimension de la grille est fixe, augmenter ou 
diminuer la taille d'une cellule augmentera ou diminuera le nombre de cellules p
ar ligne/colonne.
<br />
<br />Ajouter une cellule = clic gauche
<br />Suppri
mer une cellule = clic droit
<br />
<br />Le contrôle &quot;Ralentir&quot; per
met de temporiser l'affichage des générations successives (en millièmes de secon
de)
<br />L'affichage en mode pas à pas est possible en sélectionnant &quot;Man
uel&quot; dans le contrôle &quot;Ralentir&quot;
<br />
<br />Le contrôle &quot
;Accélérer&quot; permet une pseudo accélération de l'affichage des générations s
uccessives. 
<br />(1 = affichage à chaque génération  / 2 = affichage toutes l
es 2 générations ..... / 10 = affichage toutes les 10 générations)
<br />
<br 
/>Un clic sur un des choix du contrôle &quot;Motifs&quot; affichera le motif dan
s la grille et vous lancerez l'affichage des générations en appuyant sur le bout
on &quot;Démarrer&quot;
<br />Un double clic effacera le motif.
<br />Pour sau
vegarder vos motifs personnels, renseignez la zone de saisie avec le nom du nouv
eau motif et validez par &quot;Entree&quot;
<br />Les motifs sont sauvegardés d
ans 2 fichiers &quot;JDV_Motifs_V2.pickle&quot; et &quot;JDV_Motifs_V3.pickle&qu
ot; selon la version Python utilisée.
<br />
<br />Le bouton &quot;Arreter&quo
t; interrompt l'affichage des générations, un nouvel appui sur &quot;Démarrer&qu
ot; reprend le traitement en cours.
<br />
<br />Le bouton &quot;Import Motifs
&quot; permet d'exécuter des motifs (norme Life 1.05) depuis une bibiothèque ext
érieure et disponible sur Internet.
<br />Le chemin d'accès, par défaut, à cett
e bibliothèque est défini dans la section &quot;__init__&quot; par la variable &
quot;self.chemin_motifs&quot;
<br />Exemple de bibliothèque à télécharger: <a h
ref='http://www.conwaylife.com/wiki/Main_Page' rel='nofollow' target='_blank'>ht
tp://www.conwaylife.com/wiki/Main_Page</a> et clic sur le bouton &quot;Download 
pattern collection&quot;
<br />
<br />Lorsqu'une cellule atteint un des bords 
de la grille, un effet de zoom est appliqué. Cet effet s'arrête lorsque la taill
e de la cellule est inférieure à 1 pixel.
<br />Certains motifs (Puffer_01 ou P
uffer_02 par exemple) nécessitent d'attendre jusqu'à environ 1000 générations et
 1/2 million de cellules pour voir apparaitre des effets intéressants. 
