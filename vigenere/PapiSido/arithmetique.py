def titre(tit):
    print("===================    "+tit+"    =======================")

def strListe(l):
    s="["
    for i in range(0,len(l)):
        if i>0:
            s += ","
        s += str(l[i])
    return s+ "]"
       
def strdiv(a,b):
    return str(a)+" = "+str(b)+" x "+str(a//b)+" + "+str(a%b)

nbprems=[2]
#factPrem=[]

def strFacteurs(facteurs):
    s = "1"
    for i in range(0,len(facteurs)):
        s += "*"+str(facteurs[i])
    return s

def decFactPrem(a):
    i=0
    factPrem=[]
    premiers=[2]
    encore=True
    while encore:
        #print(str(i)+" : " + strListe(factPrem)+str(a))
        nbp=premiers[i-1]
        if a%nbp==0:
            factPrem.append(nbp)
            a = a//nbp
        elif a>nbp^2:
            nextPremier(premiers)
            i +=1
        else:
            if a>1:
                factPrem.append(a)
            encore=False
    return factPrem


def nextPremier(nbprems):
    j=1
    nonPremier = True
    while nonPremier:
        nonPremier = False
        j += 2
        for i in range(0,len(nbprems)):
            if j%nbprems[i]==0:
                nonPremier= True
    nbprems.append(j)            
    return j


def listPremiers(n):
    i=0;
    nbprems=[2]
    while i<n:
        print (str(i)+" : "+str(nbprems[i]))
        nextPremier(nbprems)
        i += 1       
    print (str(i)+" : "+str(nbprems[i]))
        

    

def pgcd ( a,b):
    if a<b:
        c=b
        b=a
        a=c
    while a%b !=0:
        print(strdiv(a,b))
        c=a%b
        a=b
        b=c
    print(strdiv(a,b))   
    return b


def calculCBZ(a,b):
    z=[a,b]
    while a%b>1 :
        print(strdiv(a,b))
        c=a%b
        a=b
        b=c
        z.append(b)
    print(strdiv(a,b))
    n=len(z)
    print("->\tzi = " + strListe(z))
    vu=[1]
    v1= - (z[n-2]//z[n-1])
    vu.append(v1)
    i=2
    while i<n:
        j= n-i
        zg = z[j-1]
        v = vu[i-1]
        u = vu[i-2]
        zd = z[j]
        c=zg//zd
        zr=1
        if j+1<n:
            zr= z[j+1]
        s=  str(zg)+" = " +str(zd) +" x "+str(c)+ " + " + str(zr)
        s += "   &   1 = " +str(u) +" x "+str(zd)+ " + " + str(v) +" x "+str(zr)
        print(s)
        uu= v
        vv= u-c*v
        vu.append(vv)
        print("donc\t" + "1 = "  + str(uu) +" x "+str(zg)+ " + " + str(vv) +" x "+str(zd))
        print("-")
        i +=1
    bz=[vu[n-2],vu[n-1]]   
    print("->\t" + strListe(vu))  
    return bz
    

    

def coeffBezout(a,b):
    bezout=[]
    #zi=[]
    vi=[]
    if a<b:
        c=b
        b=a
        a=c
    bezout.append(a)
    bezout.append(b)
    d=pgcd(a,b)
    a1=a//d
    b1=b//d
    bezout.append(d)
    bezout.append(a1)
    bezout.append(b1)
    titre("coeffBezout("+str(a)+","+str(b)+")")
    s = str(a) +" = " + str(a1)+ "*" +str(d)+"   "
    s += str(b) +" = " + str(b1)+ "*" +str(d)+"          ppcm = "+str(a*b1)
    print(s)
    bz=calculCBZ(a1,b1)
    bezout += calculCBZ(a1,b1)
    titre("coeffBezout fini")
    return bezout

def decBinaire(n):
    decb=[]
    while n>1:
        decb.append(n%2)
        n=n//2
    if n==1:
        decb.append(1)
    return decb

def strBinaire(n):
    s=""
    nbin= decBinaire(n)
    for i in range(0,len(nbin)):
        s= str(nbin[i])+s
    return s



def moduloPuissance(a,q,m):
    # retourne a**q (mod m)
    a= a%m
    ap=a
    aq=1
    qbin= decBinaire(q)
    #print(str(q)+" en binaire = " +strBinaire(q)+" cad "+ strListe(qbin))
    for i in range(0,len(qbin)):
        if qbin[i]==1:
            aq = (aq*ap)%m
        ap= ap*ap
    return aq
            
def puissance(a,q):
    # retourne a**q
    p=1
    while q>0:
        p *= a
        q -= 1
    return p

def moduloInverse(a,m):
    cbz=coeffBezout(m,a)
    if cbz[2]>1:
        return -1
    if pgcd(a,m)>1:
        return -1

    
    inv=cbz[len(cbz)-1]
    if a>m:
        inv=cbz[len(cbz)-2]
    return inv%m

def factorielle(n):
    if n<=1:
        return 1
    else:
        return n*factorielle(n-1)

def diviseur(n):
    if n<2:
        return 0
    if n%2==0:
        return 2
    k=3
    while k*k <= n :
        if n%k==0 :
            return k
        k+=2
    return n    
    
    
def isPrime(n):
    if diviseur(n)==n:
        return True
    else:
        return False

    
def nextPrime(p):
    #renvoie le premier entier >=p
    encore=True
    while encore:
        d= diviseur(p)
        if d==p:
            encore=False
        else:
            print(str(d) +" | " +str(p))
            p+=1
    print(str(p)+" ENTIER ")        
    return p   


# autonomes: test & main
def test1(a,b):
    print ("pgcd("+str(a)+","+str(b)+") = "+str(pgcd(a,b)))


def test2(a,b):   
    cbz=coeffBezout(a,b)
    print("bezout["+str(a)+","+str(b)+") = "+strListe(cbz))    

def test3(a):
    l=decFactPrem(a)
    print (strListe(l))
    print(str(a)+" = "+strFacteurs(l))
    
def test4(a,q,m):
    p= puissance(a,q)
    print (str(p)+ " = " + str(p%m) + " mod "+str(m))
    print(str(a)+"**"+str(q)+" = " +str(moduloPuissance(a,q,m))+ " mod "+str(m))
    print (" ou par pow(a,q,qm): "+str(pow(a,q,m)))

def test5(p):
    encore=True
    s=""
    l=[]
    while encore:
        
        #l= decFactPrem(p)
        s=str(p)#+" = " + strFacteurs(l)
        if isPrime(p):
            encore=False
        else:
            p +=1
            print(s)
    print("ENTIER "+s)        
    return p   
    

if __name__ == "__main__":


    a = 12
    b = 2453

    q = 21
    m = 25
    n=7
    print (nextPrime(10000))


    #test4(a,q,m)




        
    
    
    #test2(a,b)
    #listPremiers(1000)
    #test3(a)




        

        
