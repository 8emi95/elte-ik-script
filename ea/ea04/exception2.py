#! /usr/bin/python
# -*- coding: utf-8 -*-	

import sys

try:
    y = int(sys.argv[1])
except ValueError: print "Nem egesz szam a parameter!";
except IndexError: print "Kell egy parameter!";
except: print "Varatlan hiba!";
else: 
    print filter(lambda x : y % x == 0, range(1,y+1))


#  az alábbi helyett: 
try:
    y = int(sys.argv[1])
    print filter(lambda x : y % x == 0, range(1,y+1))
except ValueError: print "Nem egesz szam a parameter!";
except IndexError: print "Kell egy parameter!";
except: print "Varatlan hiba!";
    




















