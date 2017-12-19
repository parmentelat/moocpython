

modes = ("majuscule", "minuscule") #, "mixed", "ot[her") pour extension ultérieure
mode = 1;

def casse():
    print (f"code de Vigenere en mode {modes[mode]}")
    

def lettre(nb):
    if mode==0:
        return chr(65+nb)
    if mode==1:
        return chr(97+nb)
    return 

def nombre(car):
    if mode==0:
        return ord(car)-65
    if mode==1:
        return ord(car)-97
    return -1

def cesar(nb,cle):
    return (nb+cle)%26

def str2tuple(s):
    t = ()
    for c in s:
        t = t + (nombre(c),)
    return t 

def code(message, cle, sens=1):
    tuple_cle = str2tuple(cle)
    icle = 0
    crypt =""
    for l in message:
        c = nombre(l)
        if c in range(0,26):
            crypt = crypt + lettre((c + sens*tuple_cle[icle])%26)
            icle = (icle+1)%len(cle)
        else:
            crypt = crypt + l
    return crypt

def decode (crypte,cle):
    return code(crypte,cle,-1) 

       
        
        
casse()
cle ="musique"
message0 = "j'adore ecouter la radio toute la journee"
message1 = "j'adore écouter la radio toute la journée"
message2 = "J'adore écouter la radio toute la journée"


def test_vigenere(message,cle):
    print (f"-----     vigenere en {modes[mode]}, cle = {cle} -----")
    mcrypt= code(message,cle)
    print (f"message initial: {message}")
    print (f"une fois crypté: {mcrypt}")
    # print(len(mcrypt))
    print (f"puis décodé    : {decode(mcrypt,cle)}")
    
test_vigenere(message0,cle)    
test_vigenere(message1,cle)  
test_vigenere(message2,cle)      



