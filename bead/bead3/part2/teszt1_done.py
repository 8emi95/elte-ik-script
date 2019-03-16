import sys  

n = int(sys.argv[1])
print "0."

for i in range(1,n) :
    print "1."
    for j in range(1,3) :
        print "2."
        print "2."
    print "1."
    for k in range(1,3) :
        print "2."
        print "2."
    print "1."

if n < 5 :
    for j in range(1,3) :
        print "2."