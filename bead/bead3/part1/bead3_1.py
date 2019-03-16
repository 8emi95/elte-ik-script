#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import os

for file in os.listdir("./"):
	if file.endswith(".prog"):
		print file

		be = open(file)

		filenev = file.split('.')
		nev = filenev[0] + ".py"
		print nev

		ki = open(nev, "w")

		ce = ("CIKLUS","ELAGAZAS")
		for sor in be:
			if '{' in sor:
				sor = sor.replace('{', ":\n    ")
				sor = sor.replace(';;', "\n    ")
				sor = sor.replace('}', "\n")
			else:
				sor = sor[:-1]
				sor = sor.replace(';;', "\n")
			if any(s in sor for s in ce):
				sor = sor.replace("CIKLUS", "for")[:-1]
				sor = sor.replace("ELAGAZAS", "if")[:-1]
			print sor
			ki.write(str(sor+"\n"))

		be.close()
		ki.close()