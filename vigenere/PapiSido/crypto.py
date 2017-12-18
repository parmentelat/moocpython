from arithmetique import *

def abCte(l,c):
    ab=[]
    for i in range(0,l):
        ab.append(c)
    return ab

def lettre(nb):
    return chr(65+nb)

def nombre(car):
    return ord(car)-65

def printListe(liste):
    i=0
    while i < len(liste):
        print(liste[i])
        i += 1 

def toString(l):
    #printListe(l)
    s=""
    i=0
    while i<len(l):
        s += str(l[i])+"|"
        i += 1
        #print(i,s)
    return s

def toMessage(s0,l):
    #printListe(l)
    s=""
    i=0
    j=0
    while i<len(l):
        if s0[j]==" ":
            s +=" "
            j += 1
        s += lettre(l[i])
        i += 1
        j += 1
        #print(i,s)
    return s

def toAbyte(s):
    abyte = []
    i=0
    j=0
    while i<len(s):
        if s[i]!=" ":
            abyte.append(nombre(s[i]))
        i=i+1
    return abyte

def permInverse(org):
    des = abCte(len(org),-1)
    for i in range(0,len(org)):
        des[org[i]]=i
    ok= True
    for i in range(0,len(org)):
        if des[i]<0:
            raise NotaPermutation("Not a permutation")
    

    return des

def propVoyelles(ab):
    nbv=0
    for i in range(0,len(ab)):
        if ab[i] in(0,4,8,14,20,24):
            nbv +=1
    return nbv/len(ab)

def pqeVrf(p,q,e):
    print ("rsaCles(>="+str(p)+",>="+str(q)+",>="+str(e)+")")
    p= nextPrime(p)
    q= nextPrime(q)
    phi=(p-1)*(q-1)
    while pgcd(e,phi)>1:
        e += 1;
    print ("===========    p,q,e="+str(p)+","+str(q)+","+str(e))
    return p,q,e
   
    
    

def rsaCles(p,q,e):
    print ("rsaCles("+str(p)+","+str(q)+","+str(e)+")")
    n= p*q
    phi=(p-1)*(q-1)
    d= moduloInverse(e,phi)
    return n,d

def codage_rsa (m , n , e ) :
    return pow (m , e , n)

def decodage_rsa (x , n , d) :
    return pow (x , d , n)

def rsa(p,q,e):
    n,d = rsaCles(p,q,e)
    n,d=rsaCles(p,q,e)

    print( "Clés publiques:\tn = "+str(n)+"\te = "+str(e))
    print( "Clé privee:\td = "+str(d))

    for m in range(0,n):
        mc=codage_rsa(m,n,e)
        mm=decodage_rsa(mc,n,d)
        print ("rsa:\t"+str(m)+" > "+str(mc)+" > "+ str(mm))

if __name__ == "__main__":
    dd= moduloInverse(29,20)
    print( " moduloInverse(29,20) = "+str(dd) )
    print (dd*29%20)
    rsa(3,11,29)

    
    
    
  



        
