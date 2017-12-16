#!/usr/bin/env python3

#!python3


#----------------------- Fonctions --------------------------

def menu():
   print("1. Encoder un message")
   print("2. Decoder un message")
   print("3. Quitter")

def donnees():
    cle = input('Entrez la cle : => ')
    texte = input('Entrez le texte : => ')
    return (texte, cle)

def encode(texte, cle):
    flag = 0
    temp = ""
    code = ""

    for car in texte:
        if flag == len(cle):
            flag = 0

        if ord(car) not in range(97, 123):
            temp = temp + car

        else:
            temp = temp + cle[flag]
        flag += 1

    for pos, car in enumerate(texte):
        if ord(car) not in range(97, 122):
            code = code + car

        else:
            code = code + chr((((ord(car)-97) + (ord(temp[pos])-97))% 26) + 97)

    return code

def decode(texte, cle):
    flag = 0
    temp = ""
    code = ""

    for car in texte:
        if flag == len(cle):
            flag = 0

        if ord(car) not in range(97, 123):
            temp = temp + car

        else:
            temp = temp + cle[flag]
        flag += 1

    for pos, car in enumerate(texte):
        if ord(car) not in range(97, 122):
            code = code + car

        else:
            code = code + chr((((ord(car)-97) - (ord(temp[pos])-97))% 26) + 97)

    return code

#---------- Main -----------------------


while True:
    menu()
    choix = int(input("Votre choix : => "))

    if choix == 1:
        texte, cle = donnees()
        texte_code = encode(texte, cle)
        print(texte_code)

    elif choix == 2:
        texte, cle = donnees()
        texte_decode = decode(texte, cle)
        print(texte_decode)

    elif choix == 3:
        break
