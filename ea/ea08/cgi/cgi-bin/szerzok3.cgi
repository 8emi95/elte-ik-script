#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getfirst('szerzo'):
   sz = form.getfirst('szerzo')
else:
   sz = "Nem volt szerző!"


print "Content-type:text/html\n\n"
print "<html>"
print "<head>"
print "<title>CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Az egyik szerző: %s</h2>" % sz
print "</body>"
print "</html>"

