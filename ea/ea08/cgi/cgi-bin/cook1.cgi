#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi, Cookie

form = cgi.FieldStorage()

name = form.getvalue("name")
text = form.getvalue("comment")

cook = Cookie.SimpleCookie()
cook["cookie_name"] = name
cook["cookie_text"] = text
print cook

print "Content-Type: text/html; charset=utf-8\n"
print "<html> <head> <title>CGI script </title> </head>"
print "<body> <h4>CGI script!</h4>"
print "<form action = '/cgi-bin/cook2.cgi' method='post'>"
print "Hello " + name + "! Az átküldött szöveg:" + text
print "<p>Biztos ez legyen?</p>"
print "<input type='submit' value='Igen'>"
print "</form>"
print "</body></html>"

