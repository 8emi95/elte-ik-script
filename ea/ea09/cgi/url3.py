#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, re

try:
    response = urllib2.urlopen('http://127.0.0.1:8000/python.html')
except:
    print "cannot open URL"
else:    
    for line in response:
        for m in re.finditer("(?<=href=\")(http:.+?)(?=\")", line):
            print m.group()
        
