#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, re, cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()


print "Content-Type: text/html\n"
print "<html> <head> <title>CGI script </title> </head>"
print "<body>"

if form.getfirst('cim'):
    cim = form.getfirst('cim')
    
    try:
        response = urllib2.urlopen(cim)
    except:
        print "Cannot open URL!"
        print cim
    else:    
        for line in response:
            for m in re.finditer("(<a href=\"http:.+/a>)", line):
                print m.group()
                print "<br>"            
else:
    print "Nem volt cím!"


print "</body></html>"
