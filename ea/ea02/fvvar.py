# -*- coding: utf-8 -*-    #trükk, ékezetet nem szereti az interprteter alapból, beadnál készítette-hez kell
#! /usr/bin/env python    #lefuttatható scriptként így, ./neve.py?

#fv def-re vonatkozó... lokális változók lesznek

#globális változók
x = "global_x" #blokkon belül elérhető
y = "global_y"


def localfv() :
    global x
    
    print "A függvény elején x:", x
    #print "A függvény elején y:", y
    x = "changed_x" #ugyanolyan nevűt használhatok, belső lokális x
    y = "changed_y"
    print "A függvényben x:", x, "y:", y

print "Kezdetben x:", x, "y:", y
localfv()
print "A függvényhívás után x:", x, "y:", y

#Kezdetben x: global_x y: global_y
#A függvény elején x: global_x
#A függvényben x: changed_x y: changed_y
#A függvényhívás után x: changed_x y: global_y
