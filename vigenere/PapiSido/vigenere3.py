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
    vig.s_code("message en clair) renvoie le message crypté
    vig.s_decode(message_crypté) revient au mesage en clair
    de la même manière
    vig.f_code("nomf") crypte un fichier nomf.txt en nomf.crypt.txt
    vig.f_decode("crypte") decrypte le fichier crypte.txtx en crypte.clair.txt
    """
    alphabet = ""
    cle = ""
    tcle = ()
    tmode = ("MAJUSCULE", "minuscule", "MAJetmin", "кириллица")
    talphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                 "abcdefghijklmnopqrstuvwxyz",
                 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                 "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    mode = ""

#    def chx_alphabet(self):
#        self.alphabet ="abcdefghijklmnopqrstuvwxyz"
    def valid_cle(self):
        for car in self.cle:
            n = self.nombre(car)
            if n < 0:
                print('ERREUR Mauvaise clé')
                raise MauvaiseCleError(f"{car} inconnu en mode {self.mode}")
            else:
                self.tcle = self.tcle + (n,)

    def info(self, mode):
        ret = f"Vigenere en mode {self.mode} - {len(self.alphabet)}\n"
        return ret + f"cle : {self.cle} ->  {self.tcle}"

    def __init__(self, mode, cle):
        # choisir le mode de crytage
        self.alphabet = self.talphabet[mode]
        self.cle = cle
        self.mode = self.tmode[mode]
        self.valid_cle()
        print(self.info(mode))

    def nombre(self, car):
        try:
            return self.alphabet.index(car)
        except ValueError:
            return -1

    def lettre(self, nombre):
        return self.alphabet[nombre]

    def vigenere(self, message, sens=1, start=0):
        crypte = ""
        icle = start
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
        return (crypte, icle)

    def decode(self, mcrypt, start=0):
        return self.code(mcrypt, -1, start)

    def s_code(self, message):
        return self.vigenere(message)[0]

    def s_decode(self, crypt):
        return self.vigenere(crypt, -1)[0]

    def f_code(self, fname, sens=1):
        if sens == 1:
            fn = fname + '.crypt'
        else:
            fn = fname + '.clair'
        with open(fname+".txt", "r", encoding='utf-8')as entree, \
             open(fn+".txt", "w", encoding='utf-8')as sortie:
            start = 0
            for l in entree:
                ltransf = self.vigenere(l, sens, start)
                sortie.write(ltransf[0])
                start = ltransf[1]

    def f_decode(self, fname):
        self.f_code(fname, -1)


class MauvaiseCleError(Exception):
    pass 


def test_vigenere(mode, cle, message):
    print(f"-------------------------------")
    vig = Vigenere(mode, cle)
    mcrypt = vig.s_code(message)
    print(f"message initial: {message}")
    print(f"une fois crypté: {mcrypt}")
    print(f"puis décodé    : {vig.s_decode(mcrypt)}")


def test_vig_txt(mode, cle, ftxt):
    print(f"-------------------------------")
    vig = Vigenere(mode, cle)
    vig.f_code(ftxt)
    print(f"codage du fichier {ftxt}.txt en {ftxt}.crypt.txt")
    vig.f_decode(ftxt+".crypt")
    print(f"puis decodage en {ftxt}.crypt.clair.txt")


messagePi = "Que j’aime à faire apprendre un nombre utile aux sages !"
cle = "PoemePi"
test_vigenere(2, cle, messagePi)
test_vig_txt(2, cle, "decPi1")
test_vig_txt(2, cle, "decimalesPi")
vig= Vigenere(1,"Andouille")

