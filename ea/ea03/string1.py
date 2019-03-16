#! /usr/bin/python
# -*- coding: utf-8 -*-	

#   String muveletek

print "alMaFA".capitalize() 
# Almafa

print "alMaFA".lower()
# almafa

print "alMaFA".upper()
# ALMAFA

print "alMaFA".swapcase()
# ALmAfa

print "abcd".center(10,"-") #2.: mivel töltsük ki, ha nem mondjunk semmit akk semmivel nem tölti ki
# ---abcd---

print "abcd".center(10)
#    abcd   

print "abcd".ljust(10,"-")
# abcd------

print "abcd".rjust(10,"-")
# ------abcd

print "almafaalatt".count("al",2,10)
# 1

print "almafaalatt".count("al")
# 2

print "almafa".endswith("fa")
# True

print "almafa".endswith(("fa","fu","virag"))
# True

print "almafa".endswith(("fa","fu"),2,5)
# False

"almafa"[2:5]
# 'maf'

print "almafa".startswith(("fa","ma"),2,5)
# True