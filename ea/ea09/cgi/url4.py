#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, re

try:
    req = urllib2.Request('http://127.0.0.1:8000/python.html')
    response = urllib2.urlopen(req)
except:
    print "cannot open URL"
else:    
    for line in response:
        for m in re.finditer("(?<=href=\")(http:.+?)(?=\")", line):
            print m.group()
        
