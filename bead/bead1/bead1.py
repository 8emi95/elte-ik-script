#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

try:
	be1 = open(str(sys.argv[1]))
except IndexError: print "Adj meg egy file-t!";
except IOError: print "Nincs ilyen file!";

else:

	ki = open("eredmeny.txt", "w")

	aruk = filter(lambda x: ";" in x, be1.readlines())
	be1.close()
	
	be2 = open(str(sys.argv[1]))
	licitek = filter(lambda y: ":" in y, be2.readlines())
	be2.close()

	max_ar = 0
	nyertes = ""
	result = []
	ism = []
	eredmeny = []

	print type(aruk)

	for line1 in aruk:
		aru = re.split("\. ", line1)
		sorszam = int(aru[0])
		aru_m = re.split("; ", aru[1])
		nev = aru_m[0]
		tul = aru_m[1]
		min_ar = int(aru_m[2])
		for line2 in licitek:
			licit = re.split(": ", line2)
			licitalo = licit[0]
			licit_m = re.split("\. ", licit[1])
			sorszam2 = int(licit_m[0])
			ajanlott_ar = int(licit_m[1])
			if min_ar <= ajanlott_ar and sorszam == sorszam2 and ajanlott_ar > max_ar:
				max_ar = ajanlott_ar
				nyertes = licitalo
				result = str(sorszam) + ". " + str(nev) + ", " + nyertes + " " + str(max_ar)
				eredmeny.append(result)
				
				if int(sorszam) != 0:
					ism.append(int(sorszam))
		max_ar = 0

	for j in eredmeny:
		for i in ism:
			try:
				if ism[i] == ism[i-1]:
					eredmeny.pop(i-1)
					ism.pop(i-1)
			except:
				pass

	for i in eredmeny:
		ki.write(i)
		ki.write("\n")
	ki.close()