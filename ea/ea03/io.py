#! /usr/bin/python
# -*- coding: utf-8 -*-	

#karakteres állomány....-és

#formázottaBB kiíratás
for x in range(1,5) : #fv stringekre, obj orientált (van fv objektum)
    print str(x).ljust(2),  # a vesszo miatt, ebben a sorban folytatodik	#ha nincs ", akk új sor 	#ljust balra igazít 2 karakternyi helyet
    print str(5*x).center(3), #középre igazít
    print str(x**x).rjust(3) #jobbra igazít
    
# 1   5    1
# 2   10   4
# 3   15  27
# 4   20 256


for x in range(1,5) :
    print "%2d %-2d %3d" %(x, 5*x, x**x) #% után hány karakternek feltételezzük a kiírandó szöveget, d?
	#típus + hány karaktert feltételezünk
	#- balra igazítás, anélkül jobbra
 
#  1 5    1
#  2 10   4
#  3 15  27
#  4 20 256

print "Float:%8.3f" %(6.98767654) # összesen 8 karakterre igazít (ponttal együtt), .3f - 3 tizedesjegyre
# Float:   6.988

tel = {'Peter': 1234, 'Janos': 3456, 'Miklos': 2341}
print "Miklos: %(Miklos)6d, Peter: %(Peter)d, Janos: %(Janos)d" % tel
# Miklos:   2341, Peter: 1234, Janos: 3456

for x in range(1,5) :
    print "{0:2d} {1:<2d} {2:^3d}".format(x, 5*x, x**x)
#rendezés   jobbra  balra   középre
 
#  1 5   1
#  2 10  4
#  3 15 27
#  4 20 256


tel = {'Peter': 1234, 'Janos': 3456, 'Miklos': 2341}
tel2 = {'Peter': 4567, 'Janos': 5634, 'Miklos': 1342}
print "Miklos: {0[Miklos]:d}, Peter: {0[Peter]:d}, Janos: {1[Janos]:d}".format(tel,tel2)
# Miklos: 2341, Peter: 1234, Janos: 5634

print "Miklos: {Miklos:d}, Peter: {Peter:d}, Janos: {Janos:d}".format(**tel) #**-gal is oda lehet adni szótárt fv paramétereként, nevesített paraméter lesz
# Miklos: 2341, Peter: 1234, Janos: 3456

print "Miklos: {Miklos:d}, Peter: {Peter:d}, Janos: {Janos:d}".format(Miklos=2341,Peter=1234,Janos=3456)
# Miklos: 2341, Peter: 1234, Janos: 3456

#beolvasás
#dinamikus típusrendszer: amire használjuk abból kitalálhatja h milyen értéket vár
print "Irj be egy erteket!"
x = input()
print x + 4 #egésszé konvertálja, kiszámolja x+4et, visszaalakítja stringgé és úgy írja ki

print "Irj be egy stringet!"
x = raw_input() #nem alakít át semmit, stringgé alakítja és úgy olvassa (?)
print "A szoveg:", x

#reguláris kifejezések: biztos h szövegként olvassuk be        JÖVŐ ÓRÁN