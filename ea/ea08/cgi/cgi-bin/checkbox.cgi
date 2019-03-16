#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
import cgi

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('Kávé'):
   kv_flag = "Igen"
else:
   kv_flag = "Nem"

if form.getvalue('Tea'):
   tea_flag = "Igen"
else:
   tea_flag = "Nem"

if form.getvalue('Kakaó'):
   kakao_flag = "Igen"
else:
   kakao_flag = "Nem"


print "Content-type:text/html\n\n"
print "<html>"
print "<head>"
print "<title>CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Kakaó kiválasztva: %s</h2>" % kakao_flag
print "<h2> Tea kiválasztva: %s</h2>" % tea_flag
print "<h2> Kávé kiválasztva: %s</h2>" % kv_flag
print "</body>"
print "</html>"
