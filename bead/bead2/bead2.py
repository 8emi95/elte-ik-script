#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

be1 = open("data.txt", "r")
be2 = open("update", "r")

ki1 = open("newdata", "w")
ki2 = open("log", "w")

# --------------------------------------- data beolvasás --------------------------------------- 

szamlaData = {}
szamlaDataAdatok = [] #név, utolsó módosítás, aktuális egyenleg

for sorok1 in be1:
	data = sorok1.split()
	szamlaDataAdatok.extend([" ".join(data[0:-3]), data[-2], int(data[-1])])
	szamlaData[data[-3]] = szamlaDataAdatok
	szamlaDataAdatok = []
be1.close()

# --------------------------------------- update beolvasás --------------------------------------- 

szamlaUpdate = []
szamlaUpdateAdatok = []

for sorok2 in be2:
	if len(sorok2) == 12:
		modNap = sorok2[0:11]
	else:
		update = sorok2.split()
		szamlaUpdateAdatok.append(" ".join(update[0:-2])) #modTulaj
		szamlaUpdateAdatok.append(update[-2]) #modSzamlaszam
		szamlaUpdateAdatok.append(int(update[-1])) #modOsszeg
		szamlaUpdate.extend([szamlaUpdateAdatok])
		szamlaUpdateAdatok = []
be2.close()

# --------------------------------------- newdata, log --------------------------------------- 

newData = szamlaData
logNew = {}
logOther = {}

volt = False
for i in range(0, len(szamlaUpdate)):
	volt = False
	for j in range(0, len(newData)):
		if szamlaUpdate[i][1] == newData.keys()[j]:
			volt = True
			ujEgyenleg = newData.values()[j][2] + szamlaUpdate[i][2]
			newData.values()[j][2] = ujEgyenleg
			newData.values()[j][1] = modNap
			logOther[newData.keys()[j]] = newData.values()[j]
	if volt == False:
		newData[szamlaUpdate[i][1]] = [szamlaUpdate[i][0], modNap, szamlaUpdate[i][2]]
		logNew[szamlaUpdate[i][1]] = [szamlaUpdate[i][0], modNap, szamlaUpdate[i][2]]

sortedNewData = sorted(newData.items(), key=lambda (k,v): (v[0], k))
tulaj = [x[1][0] for x in sortedNewData]
szamlaszam = [x[0] for x in sortedNewData]
datum = [x[1][1] for x in sortedNewData]
egyenleg = [x[1][2] for x in sortedNewData]
for i in range(0, len(sortedNewData)):
	nd = str(tulaj[i]) + " " + str(szamlaszam[i]) + " " + str(datum[i]) + " " + str(egyenleg[i]) + "\n"
	ki1.write(nd)
ki1.write("\n")
ki1.close()

ki2.write(modNap)
ki2.write("\n\nnew accounts:\n")
sortedLogNew = sorted(logNew.items(), key=lambda (k,v): (v[0], k))
tulajLogNew = [x[1][0] for x in sortedLogNew]
szamlaszamLogNew = [x[0] for x in sortedLogNew]
for i in range(0, len(sortedLogNew)):
	ln = str(tulajLogNew[i]) + " " + str(szamlaszamLogNew[i]) + "\n"
	ki2.write(ln)

ki2.write("\nother updates:\n")
sortedLogOther = sorted(logOther.items(), key=lambda (k,v): (v[0], k))
tulajLogOther = [x[1][0] for x in sortedLogOther]
szamlaszamLogOther = [x[0] for x in sortedLogOther]
for i in range(0, len(sortedLogOther)):
	lo = str(tulajLogOther[i]) + " " + str(szamlaszamLogOther[i]) + "\n"
	ki2.write(lo)
ki2.close()