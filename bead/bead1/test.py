#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

try:
	be1 = open(str(sys.argv[1]))
except IndexError: print "Adj meg egy file-t!";
except IOError: print "Nincs ilyen file!";

else:

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
		print i

	# if len(eredmeny) > 0:
	# 	for j in eredmeny:
	# 		for i in ism:
	# 			try:
	# 				if ism[i] == ism[i-1]:
	# 					eredmeny.pop(i-1)
	# 					ism.pop(i-1)
	# 			except:
	# 				pass

	# 	for i in eredmeny:
	# 		print i
	# else:
	# 	print "nem jo"





#-----------------------------------


szoveg = "elso1;\nelso2;\nelso3;\n\n\nmasodik1:\nmasodik2:\nmasodik3:"
#print re.split("\n\n+", szoveg) #string kell, nem lista
#print szoveg.split("\n\n+") #nincs általánosítás, + nem jó
#print filter(";" in szoveg, szoveg)
#print ";" in szoveg

#-----------------------------------

#áru
line1 = "111. grillsuto; jo allapotu; 5000"
aru = re.split("\. ", line1)
sorszam = aru[0]
aru_m = re.split("; ", aru[1])
nev = aru_m[0]
tul = aru_m[1]
min_ar = aru_m[2]
#print sorszam, "+", nev, "+", tul, "+", min_ar #sorszám pont nélkül

#licit
line2 = "Kis Peter: 111. 4000"
licit = re.split(": ", line2)
licitalo = licit[0]
licit_m = re.split("\. ", licit[1])
sorszam2 = licit_m[0]
ajanlott_ar = licit_m[1]
#print licitalo, "+", sorszam2, "+", ajanlott_ar #sorszám pont nélkül

#-----------------------------------

# print re.split(" ","Kis Peter: 1. 4000")

# s = re.search("\d*\.", "111. grillsuto; jo allapotu; 5000")
# print s.group(), " x", "nah"

# s = re.search("[a-zA-z\ ]*:", "Kis Peter: 1. 4000")
# print s.group()

# print re.split(":\ ", "Kis Peter: 1. 4000")

# szoveg = "Kis Peter: 1. 4000"
# print szoveg.split(": ")

# szoveg = " 1. 4000"
# print szoveg.split(" ")

#sor = "111. grillsuto; jo allapotu; 5000"
#e = sor.rsplit("; ",2)
#print e[2]