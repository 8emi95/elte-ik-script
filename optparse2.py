import optparse

# In version 2.6 or earlier

parser = optparse.OptionParser(description='Argumentumkezelo pelda.', epilog='Echo program.')

parser.add_option('--verbose', dest='verb', action='store_true', 
                      help='Setting verbose mode.')

parser.add_option('-c', dest='value', action='store', 
                      help='Adding value.')


(options, args) = parser.parse_args()

if options.verb : 
   print "Ez egy echo program!\nA beirt szoveg:\n"

print options.value

for s in args: print s 

#$ python optparse2.py --v egy ketto harom -c 54
#Ez egy echo program!
#A beirt szoveg:
#
#54
#egy
#ketto
#harom
