import optparse

# In version 2.6 or earlier

parser = optparse.OptionParser(description='Argumentumkezelo pelda.', epilog='Echo program.')

parser.add_option('--verbose', dest='verb', action='store_true', 
                      help='Setting verbose mode.')

(options, args) = parser.parse_args()

if options.verb : 
   print "Ez egy echo program!\nA beirt szoveg:\n"

for s in args: print s 


#$ python optparse1.py --v egy ketto harom
#Ez egy echo program!
#A beirt szoveg:
#
#egy
#ketto
#harom

