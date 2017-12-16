#!/usr/bin/env python3
# les caractères alphabetiques en minuscule ou majuscule
from string import ascii_letters


# je profite de cet exercice pour injecter un peu de numpy
# on n'est vraiment pas obligé de faire comme ça...
import numpy as np


def break_vigenere(encoded, key_length):
    """
    Connaissant la longueur de la clé, on calcule 
    la lettre la plus fréquemment citée sur chaque fil 
    correspondant à la même lettre dans la clé
    En admettant que c'est toujours le 'e' on en déduit
    la clé

    cette version fonctionne avec un texte en minuscules
    """

    # pour construire un tableau numpy de charactères
    # il nous faut une liste de ces caractères
    # qui ait la bonne taille, e.i.
    # un multiple de la longueur de la clé

    # on commence par en profiter pour enlever la ponctuation
    chars = [x for x in encoded if x in ascii_letters]

    # combien reste-il si on divise key_length
    extra_length = len(encoded) % key_length
    # on ajoute ce qu'il faut pour tomber sur un multiple de key_length
    pad_length = 0 if (extra_length == 0) else (key_length - extra_length)
    # on ajoute des blancs pour faire le bon compte
    chars += [' ' for i in range(pad_length)]

    # la longueur de la séquence correspondant à chaque
    # caractère dans la clé
    thread_length = len(chars) // key_length

    # on construit un tableau numpy
    # juste pour montrer les manipulations de 'shape'
    array = np.array(chars, dtype='U1')
    # on le transforme en tableau rectangulaire
    # dans lequel chaque colonne correspond à une lettre de la clé
    array = array.reshape((thread_length, key_length))

    # pour chaque lettre dans la clé
    def i_th(i):
        # on extrait sous la forme d'un tableau une colonne,
        # qui contient toutes les lettres encodées avec cette lettre
        col = array[:, i]
        # on compte - il vaut mieux utiliser numpy que collections.Counter
        unique, counts = np.unique(col, return_counts=True)
        # on compte dans un dictionnaire char -> nb_d_apparitions
        occurrences = dict(zip(unique, counts))
        # comme on n'a besoin que du caractère le + cité
        # on construit un dictionnaire: nb_occurrences -> caractère
        reverse_occurrences = {times: char for char,
                               times in occurrences.items()}
        # le plus cité
        most_quoted = reverse_occurrences[max(reverse_occurrences.keys())]
        print(f"key {i} - most-quoted {most_quoted}")
        # for char in sorted(reverse_occurrences):
        #    print(f"quoted {char} times: {reverse_occurrences[char]}")
        # admettant que ça correspond au 'e'
        return chr(ord('a') + ((ord(most_quoted) - ord('e')) % 26))

    return "".join(i_th(i) for i in range(key_length))


# enigme call_me_al

enigme1 = (5, "Cwmjfvz. Ie ifbqolwm zvvd rtbzmisifo unn zoasrldbhoe fb loe tqmgcfbnn gsmeeifa : 'oajt' ms 'Nfom'. Be hvq loeuzd qlf td Zvo Xxtypv dsk uzds gswbhv ec Yee ec Saf: «Uzdnkf zzyfoa boewmqgvob zu dpgdu, dbqr c'vtb ke mjld mveqzn hvq eazu uzrtimq lv dpzr. C'Fbqe upvme ufa oojtqaicjbds,t'fas prs td nfo-msrv rc'nn cfa ttzmqre. (Cbw-Ssvv «Bzo-kp-shnx» Dms ecpod dl wqce df nnuioqs l'fdkzszpv ce ifvcrv iwlmrhm z ue em lej jlnlvt mm mrupdmruqpuvt : Rnhe Iwqtfo Knnnbg, brvbbdui fvsrv bcsrvt lt «Jvv ld lr Wqd» ek emr «Nfnjqej em Boexix», sls tdshvmks a'bq dcijb loe nmlozsm ce UFI , puz dwmskscht «Kpcr lvt vnmssmr, pvuqss vu oqaeea» z prsbhr uf t'dnjfualv wqce. Tfbse dfzuezmtd dv «amqocpohe» r bcrsz girczom tn vuccirob ce Tpvvap : vv beiuihn Upvzlu Lvtty , bcsels ld TvY ms dv mi aismm « Shv Bzs ow Dwlplumq Pipoqadnqmg » . C'iclols «odeb» em Jnlup le gbzzik smkemfz zujtq aivo lt nfo-adnjf yte uf t'gudpcq Zvo lt vvomqe Dbqsrv Min-Tjfc, dt xbodoet yte tfzsazoa cej bcselsa bikfa nnk bcrsz jvrpzsm ke SENK Gljln Vro Znsjvu, zuo dwsej emr Mfobx Ppupnn.Dfzbi gpcq vfuzd akummtzpv z cvubd prsmmtyfad clmbtrvmtd, ue qmt lfoote gpcq ue ftngv ec uiuf !")

from vigenere import Vigenere

if __name__ == '__main__':

    for length, encoded in (enigme1,):
        encoded = encoded.lower()
        print(f"encoded = {encoded}\nlength = {length}")
        key = break_vigenere(encoded, length)
        print(f" key -> {key}")
        codec = Vigenere(key, continuous=False)
        print(f" decoded -> {codec.decode(encoded)}")
