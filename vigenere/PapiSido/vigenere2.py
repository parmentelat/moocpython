# -*- coding: utf-8 -*-


class Vigenere:
    """codage-décodage selon Vigenere
    La classe s'initialise par Vigenere(mode, cle)
    avec actuellement 4 modes
    0: MAJUSCULE (Majuscules - 26 lettres)
    1: minuscule (minuscules - 26 lettres)
    2: MAJetmin (les 2 - 52 lettres)
    3: кириллица (cyrillique minucule)
    règles: les caractères apartenant à l'alphabet sont modifiés,
    les autres restent inchangées
    la cle doit apartenir à l'alphabet
    Exemple d'utlisation:
    vig Vigenere(1,"musique") #crée l'objet vig, mode minuscule clé musique )
    vig.code("mesesage en clair) renvoie le message crypté
    vig.decode(message_crypté) revient au mesage en clair
    """
    alphabet = ""
    cle = ""
    tcle = ()
    tmode = ("MAJUSCULE", "minuscule", "MAJetmin", "кириллица")
    talphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                 "abcdefghijklmnopqrstuvwxyz",
                 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                 "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

#    def chx_alphabet(self):
#        self.alphabet ="abcdefghijklmnopqrstuvwxyz"
    def valid_cle(self):
        for car in self.cle:
            n = self.nombre(car)
            if n < 0:
                print('ERREUR Mauvaise clé')
                return False
            else:
                self.tcle = self.tcle + (n,)

    def info(self, mode):
        ret = f"Vigenere en mode {self.tmode[mode]} - {len(self.alphabet)}\n"
        return ret + f"cle : {self.cle} ->  {self.tcle}"

    def __init__(self, mode, cle):
        # choisir le mode de crytage
        self.alphabet = self.talphabet[mode]
        self.cle = cle
        self.valid_cle()
        print(self.info(mode))

    def nombre(self, car):
        try:
            return self.alphabet.index(car)
        except ValueError:
            return -1

    def lettre(self, nombre):
        return self.alphabet[nombre]

    def code(self, message, sens=1):
        crypte = ""
        icle = 0
        for car in message:
            n = self.nombre(car)
            if n < 0:
                crypte = crypte + car
            else:
                # print (f"n={n} sens={sens} tcle={self.tcle}, icle={icle}")
                nn = (n + sens*self.tcle[icle])
                nn = nn % len(self.alphabet)
                icle = (icle+1) % len(self.cle)
                crypte = crypte+self.lettre(nn)
        return crypte

    def decode(self, mcrypt):
        return self.code(mcrypt, -1)


mode = 1
cle0 = "musique"
message0 = "j'adore ecouter la radio toute la journee"
message1 = "j'adore écouter la radio toute la journée"
message2 = "J'adore écouter la radio toute la journée"
mode = 2
messagePi1 = "Que j’aime à faire apprendre un nombre utile aux sages !"
cle1 = "PoemePi"
mode = 3
kcle = "таблица"
kirillic = "Некоторые из прежних миссионеров уже пытались "
kirillic += "перевести богослужение на славянский язык"


def test_vigenere(mode, cle, message):
    print(f"-------------------------------")
    vig = Vigenere(mode, cle)
    mcrypt = vig.code(message)
    print(f"message initial: {message}")
    print(f"une fois crypté: {mcrypt}")
    print(f"puis décodé    : {vig.decode(mcrypt)}")


test_vigenere(1, cle0, message0)
test_vigenere(1, cle0, message1)
test_vigenere(1, cle0, message2)
test_vigenere(2, cle1, messagePi1)
test_vigenere(mode, kcle, kirillic.lower())
