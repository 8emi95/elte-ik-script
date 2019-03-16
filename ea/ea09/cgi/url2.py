#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

try:
    response = urllib2.urlopen('http://127.0.0.1:8000/python.html')
except:
    print "cannot open URL"
else:    
    html = response.read()
    print html
