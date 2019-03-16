# -*- coding: utf-8 -*- 
import sys

def lnko(x=10, y=15): #default érték a paraméterekhez (ha nem adnak meg értéket akk ez lesz)
    "Ket szam legnagyobb kozos osztoja."
    print x, "es", y, "legnagyobb kozos osztoja:"
    while not (x == y) :
        if x > y :
            x = x - y
        else :
            y = y - x

    print x 

if len(sys.argv) >= 3 : 
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    lnko(x,y) #két paraméterrel meghívás
elif len(sys.argv)== 2 :
    z = int(sys.argv[1])
    lnko(x=z)
    lnko(y=z)
    lnko(z) #egy paraméterrel meghívás, auto x lesz a z
else:
    lnko() #értékek nélküli meghívás
#5 > 5 és 15, 10 és 15, 15 és 5?
    
    
       
