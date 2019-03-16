#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getlist('szerzo'):
   sz = "; ".join(form.getlist('szerzo'))
else:
   sz = "Nem volt szerző!"


print "Content-type:text/html\n\n"
print "<html>"
print "<head>"
print "<title>CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> A szerzők: %s</h2>" % sz
print "</body>"
print "</html>"

