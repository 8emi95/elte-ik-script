#! /usr/bin/python

f=open("bemenet.txt", 'r')
print sum([int(line) for line in f])

f=open("bemenet.txt", 'r')
print reduce(max, [int(line) for line in f])

def myInt(x) :
    try : return int(x);
    except: print "Nem lehet int-re konvertalni:", x, ;

        

f=open("bemenet2.txt", 'r')
szamok = filter(lambda x : x !=None, [myInt(line) for line in f])
print sum(szamok)
print reduce(min, szamok)
