#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re

for file in os.listdir("./"):
	if file.endswith(".prog"):
		print file
		be = open(file)

		filenev = file.split('.')
		nev = filenev[0] + ".py"
		print nev

		ki = open(nev, "w")

		ce = ("for", "if")
		ceb = (";;for", ";;if", "{for", "{if")

		for sor in be:
			sor = sor.replace("CIKLUS", "for")
			sor = sor.replace("ELAGAZAS", "if")
			if not any(s in sor for s in ce):
				sor = sor.replace(";;", "\n")
			elif not any(s in sor for s in ceb):
				sor = sor.replace("{", ":\n    ")
				sor = sor.replace(";;", "\n    ")
				sor = sor.replace("}", "\n")
			elif any(s in sor for s in ceb):
				sor = sor.replace("{",":\n    ", 1)
				sor = re.sub(":\n    [^{}]*{", lambda x:x.group(0).replace(";;","\n    "), sor)
				sor = re.sub("}[^{}]*{", lambda x:x.group(0).replace(";;","\n    "), sor)
				sor = re.sub("}[^{}]*}", lambda x:x.group(0).replace(";;","\n    "), sor)
				sor = sor.replace("{", ":\n        ")
				sor = sor.replace(";;", "\n        ")
				sor = sor.replace("}", "")
			ki.write(sor)

be.close()
ki.close()