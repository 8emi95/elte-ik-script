#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Ford(object):
	def __init__(self, szt):
		self.szt = szt
		#szt.__init__(self.szt = szt)
	def fordit(self, be, ki):
		try:
			be = open(be, "r")
		except IOError: print "Nincs input file!";
		ki = open(ki, "w")

		ujsor = ""

		for sorok in be:
			sor = sorok.split()
			for szo in sor:
				for en, hu in self.szt.iteritems():
					if en == szo:# or en + "." == szo:
						szo = hu + " "
						ujsor += szo
					if en + "." == szo:
						szo = hu + "."
						ujsor += szo
			ujsor = ujsor + "\n"
		ki.write(ujsor)

# be = open("teszt.txt", "r")

# szotar = {"The" : "A", "sun": "nap", "shining" : "süt", "wind" : "szél", "not" : "nem", "blowing" : "fúj"}

# ujsor = ""

# for sorok in be:
# 	sor = sorok.split()
# 	for szo in sor:
# 		for en, hu in szotar.iteritems():
# 			if en in szo:
# 				szo = hu + " "
# 				ujsor += szo
# 	ujsor = ujsor[:-1] + ".\n"
# print ujsor
