# -*- coding: utf-8 -*-	

#akárhány paraméter, nevesítve is meg lehet csinálni
def tizenot() :
    return 15

print "tizenöt:", tizenot()

t15 = tizenot #fv-objektumot jelöli () nélkül
print "t15:", t15() #()-kel meghívja tizenot fv-t

# tizenöt: 15
# t15: 15

# -----------------------

x = 10
def fv(arg=x) : #ha nem konstant hanem változó a default, megpiszkáljuk akk formális paraméterhez hozzáköti a változó értékét, eredeti érték lesz
    print "arg:", arg    

x = 20
fv()

#arg: 10

# ----------------------

list = [1,2,3] #lista objektum default értékként fvnek
def fv2(arg2=list) :
    print "arg2:", arg2    

list[1] = 4 #változó által tartalmazott objektum értékét változtatjuk, 1-es indexűt cseréli
fv2() #fv-t meghívom, változás látszik

#arg2: [1, 4, 3]

# ----------------------

list = [1,2,3]
list2 = list #változón keresztül a megpiszkált változót érjük el
list[1] = 4

print list, list2

# [1, 4, 3] [1, 4, 3]

# ----------------------

def fv3(x,y) : #ha lista ugyanannyi elemű mint ahány paraméter kell nekünk
    print "osszeg:", x+y    

list = [5,8] 
fv3(*list) #*

#osszeg: 13