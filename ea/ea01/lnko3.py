# -*- coding: utf-8 -*-	
x = input("Irj be egy szamot: ") #érték bekérése
y = input("Irj be egy ujabb szamot: ")

while not (x == y) :
    if x > y :
        x = x - y
    else :
        y = y - x
        
print "A ket szam legnagyobb kozos osztoja: " #+ str(x) #így : után írja
print x     
