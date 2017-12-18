from crypto import *



def cesar(nb,cle):
    return (nb+cle)%26

#lenCle=3
stat0=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
#cles=[0,1,0]

def vigenere(chaine,lenCle,cles):
    vig =[]
    for i in range(0,len(chaine)):
        vig.append(cesar(chaine[i], cles[i%lenCle]))
    return vig
    
        
#messageChiffre="ZCNUVJ LUYLNQL GXA PFPPJ LV XHKSA UFLPX HXJJ UFPPYL GXAGQSG JZV SHKSL GY ZCNUV XHGSZ CALE XHKSAG JZVJSNJ LUY UCNUG JA UFPPY ZCJUU FCGH"
messageChiffre= "ZCNUVJ LUYLNQL GXA PFPPJ LV XHKSA UFLPX HXJJ UFPPYL GXAGQSG JZV SHKSL GY ZCNUV XHGSZ CALE XHKSAG JZVJSNJ LUY UCNUG JA UFPPY ZCJUU FCGH"

chaineCrypt= toAbyte(messageChiffre)

def testVigenere():
    lcle=5
    cles=[4,1,22,15,2]
    enclair =  "SALUT LES COPAINS"
    print(enclair)
    chaine=toAbyte(enclair)
    chaineCrypt = vigenere(chaine,lcle,cles)                  
    #printListe(chaine)
    print(toString(chaine))
    print(toString(chaineCrypt))
    print(toMessage(enclair,chaineCrypt))
    print(toMessage(enclair,chaine))

def decode():
    decrypte = vigenere(chaineCrypt,lenCle,cles)
    enclair= toMessage(messageChiffre,decrypte)
    print(enclair)

def statistiques(phrase,lcle):
    stats =[]
    for i in range(0,lcle):
        stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        stats.append(stat)
    for i in range(0,len(phrase)):
        cc= phrase[i]
        stats[i%3][cc] += 1
    for i in range (0,26):
        s=lettre(i)+":"+str(i)+"\t"
        for j in range(0,lcle):
            s += str(stats[j][i])+"\t"
        print(s)
        
##### ajout pour l'exercice du MOOC Python ####      
        
    
def code_vigenere(chaine, scle):
    acles =[]
    for c in scle:
        acles.append(nombre(c))
    return toMessage(chaine, vigenere(toAbyte(chaine),len(scle),acles))

def decode_vigenere(chaine, scle):
    acles =[]
    for c in scle:
        acles.append(-nombre(c))
    return toMessage(chaine, vigenere(toAbyte(chaine),len(scle),acles))

  

chaine_test ="j adore ecouter la radio toute la journee".upper()
cle0 = "MUSIQUE"

crypte_test = code_vigenere(chaine_test, cle0).lower()

print (f" chaîne initiale {chaine_test}")
print (f" aprés crytage   {crypte_test.lower()}")
print (f" puis décryptage {decode_vigenere(crypte_test.upper(),cle0)}")

