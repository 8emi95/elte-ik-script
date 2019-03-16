#!/usr/bin/env python
# -*- coding: utf-8 -*

import cgi

try :
    counter = open("/tmp/counter.txt","r")
except: number = 1
else:
    line = counter.readline()
    counter.close()
    
    if line == "":
        number = 1
    else: 
        number = int(line) + 1

counter = open("/tmp/counter.txt","w")
counter.write(str(number))
counter.close()

print "Content-Type: text/html; charset=utf-8\n"
print "<html> <head> <title>Számláló</title> </head>"
print "<body> <h4>Számláló példa.</h4>"
print "Eddigi látógatószám: ", number
print "</body></html>"
