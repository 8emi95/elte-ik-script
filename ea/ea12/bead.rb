 
Adott egy adatfájl, ami lottóhúzás eredményeket tartalmaz a következő alakban (az első sor is benne van, az egyes elemeket SPACE-ek és TAB-ok választják el):

~~~~
Év Hét Húzásdátum 5 találat (db) 5 találat (Ft) 4 találat (db) 4 találat (Ft) 3 találat (db) 3 találat (Ft) 2 találat (db) 2 találat (Ft) Számok
2014 	38 	2014.09.20. 	0 0 Ft 	100 	529215 Ft 	5748 	9750 Ft 	116451 	935 Ft  2 7 12 25 76
2014 	37 	2014.09.13. 	0 0 Ft 	22 	2428080 Ft 	2394 	23625 Ft 	76973 	1430 Ft  7 39 40 58 68
2014 	36 	2014.09.06. 	1 387392635 Ft 	70 	793275 Ft 	4717 	12465 Ft 	104031 	1100 Ft  3 16 27 45 81
2014 	35 	2014.08.30. 	0 0 Ft 	21 	2599165 Ft 	3000 	19265 Ft 	90999 	1310 Ft  19 53 60 66 67
~~~~ 

Készítsünk egy olyan fájlt, amely megadja, hogy melyik héten volt 50 darabnál több négytalálatos és ezeknek mennyi volt a nyereménye, valamint, hogy az összes hetet tekintve, melyik héten fizettek a legtöbbet egy 4 találatosért:

~~~~
2014, 38:: 529215 Ft
2014, 36:: 793275 Ft
max 4-es:: 2014, 35
~~~~

Az inputfájl neve legyen a program parancssori paramétere, az elkészített fájl neve pedig legyen "eredmeny.txt". További követelmény, hogy a program hianyzó paraméter esetén: "Adj meg egy file-t!", míg rosszul megadott paraméter esetén: "Nincs ilyen file!" hibaüzenetet adjon.
