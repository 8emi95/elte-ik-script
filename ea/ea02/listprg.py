#! /usr/bin/python
# -*- coding: utf-8 -*-	

import sys

print reduce(max, [2, 1, 4, 5, 21, 12, 34, 57, 2, 4, 6, 8]) #maxker

# -----------------------

y = int(sys.argv[1]) #parancssori paraméter

# -----------------------

#kiszedi az x-eket amik osztják y-t, y osztói
print filter(lambda x : y % x == 0, range(1,y+1)) #y+1 h y is benne legyen

# -----------------------

#prímtényezős felbontás
def f((x, pr), z) :
    if x%z == 0 : #pár első tagját osztja-e
        pr.append(z) #pr lista
        return f((x/z, pr), z) #rekurzívan meghívja uezt a fvt
    else:
        return (x,pr)

prim  = [] 
p=reduce(f, range(2,y+1), (y,prim))
print p[1]

#f((10,[]),2) = f((5,[2]),2) = (5,[2])						#2 osztja 10et, 2es listába
#f((20,[]),2) = f((10,[2]),2) = f((5,[2,2]),2) = (5,[2,2]) 	#páros 2. tagjai a prímtényezők