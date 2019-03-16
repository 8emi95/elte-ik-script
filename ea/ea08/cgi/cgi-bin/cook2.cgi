#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi, Cookie, os

cook = Cookie.SimpleCookie()
cook.load(os.environ["HTTP_COOKIE"])

name = cook["cookie_name"].value
text = cook["cookie_text"].value

print "Content-Type: text/html; charset=utf-8\n"
print "<html> <head> <title>Second CGI script </title> </head>"
print "<body> <h4>CGI script.</h4>"
print "Kösz " + name + ". A szöveg:" + text
print "</body></html>"
