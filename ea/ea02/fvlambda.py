# -*- coding: utf-8 -*-	

#ha fv fv-t vár paraméterül akk ez kell, lambda-kifejezés
def mult(x) :
    return lambda n : x * n #fv név nélkül, 1 pm-t vár, megszorozza x-szel
    

double = mult(2) #2-vel szoroz
triple = mult(3)

print double(8)
#16

print triple(8)
#24   
