#! /usr/bin/python
# -*- coding: utf-8 -*-	

#   String muveletek

print "alma\tfa".expandtabs(4) #tabokat space-ekké alakítja (margó szabály miatt hasznos, nem mindig szerencsés tab helyett space)
# "alma    fa"

print "almafaalatt".find("fa") #részstringet keres, pozíciót megmondja hol kezdődik, első előfordulást
# 4

print "almafaalatt".find("korte") #ha nem talál akk -1, nem 0 mert az létező pozíció
# -1

print "abrakadabra".rfind("ra") #jobbról keres
# 9

print "abrakadabra".rfind("fa")
# -1

print "	  	".isspace() #white space karakterekre ha csak ilyen volt
# True

print "12346756".isdigit()
# True

print "23 45 56".isdigit()
# False

# ------------------

f = open("str_adatok.txt", "r") #r-reading, w-writing, a-appending
lines = f.readlines() 
f.close()

notemptylines = filter(lambda x: not x.isspace(), lines) #nemüres sorokat hagyja meg
newlines = map(lambda x: x.expandtabs(0), notemptylines) #0 paraméterrel meghívva törli a tabokat

f2 = open("str_kimenet.txt", "w")
for line in newlines:
    f2.write(line)
f2.close()

# -------------------

f = open("str_adatok.txt", "r")
f2 = open("str_kimenet2.txt", "w")

for line in [x.expandtabs(0) for x 
                in filter(lambda y: not y.isspace(),f.readlines() )]:
    f2.write(line)

f.close()
f2.close()

# -------------------

f = open("str_kimenet.txt", "r")

szamok = []
for line in f:
    szamok.append(line[line.rfind(" ")+1:-1]) # Windowson -2 (új sor karakter miatt)
f.close()
print szamok
# ['123-45678', '478-2356', '254-6752', '342-8765', '453-9876', '231-9834']