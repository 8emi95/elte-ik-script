#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('selected'):
   subject = form.getvalue('selected')
else:
   subject = "Nincs megadva!"

print "Content-type:text/html\n\n"
print "<html>"
print "<head>"
print "<title>CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> A kiválasztott ital: %s</h2>" % subject
print "</body>"
print "</html>"
