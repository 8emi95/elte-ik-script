#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, urllib2, re

value = {'cim':"http://127.0.0.1/python.html"}

data = urllib.urlencode(value)

try:
    req = urllib2.Request('http://127.0.0.1/cgi-bin/url.cgi', data)
    response = urllib2.urlopen(req)
except:
    print "cannot open URL"
else:    
    page = response.read()
    print "Content-Type: text/html\n"
    print page     
