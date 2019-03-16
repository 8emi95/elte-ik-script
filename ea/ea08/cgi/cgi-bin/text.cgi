#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi,cgitb

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('review'):
   text_content = form.getvalue('review')
else:
   text_content = "Not entered"

print "Content-type:text/html\n"
print "<html>"
print "<head>"
print "<title>CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> A megadott szöveg: %s</h2>" % text_content
print "</body>"

